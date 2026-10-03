const fs = require('fs');
const path = require('path');
const { pathToFileURL } = require('url');
const { marked } = require('marked');
const { chromium } = require('playwright');

const root = path.resolve(__dirname, '..', '..');
const source = path.join(root, 'upc-pre-202620-1acc0238-13975-ADM-report.md');
const htmlPath = path.join(__dirname, 'updated-report.html');
const pdfPath = path.join(__dirname, 'updated-report.pdf');

marked.setOptions({ gfm: true, breaks: false, headerIds: false, mangle: false });
const content = marked.parse(fs.readFileSync(source, 'utf8'));
const base = pathToFileURL(root + path.sep).href;
const html = `<!doctype html><html lang="es"><head><meta charset="utf-8"><base href="${base}"><style>
@page{size:A4;margin:13mm 13mm 17mm}*{box-sizing:border-box}html,body{background:#fff}body{margin:0;color:#111;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Arial,sans-serif;font-size:14px;line-height:1.6}h1,h2{font-weight:400;border-bottom:1px solid #222;padding-bottom:.16em}h1{font-size:2em;margin:.67em 0}h2{font-size:1.5em;margin:.83em 0}h3{font-size:1.17em;margin:1em 0}h4{font-size:1em;margin:1.15em 0 .55em}h5{font-size:.9em;margin:1.1em 0 .5em}p{margin:.65em 0;orphans:3;widows:3}a{color:#0645ad;text-decoration:none}img{max-width:100%;height:auto}table{border-collapse:collapse;margin:1em auto;max-width:100%;page-break-inside:auto}thead{display:table-header-group}tr{page-break-inside:avoid}th,td{border:1px solid #c8c8c8;padding:5px 8px;vertical-align:top}th{background:#f3f3f3;font-weight:600}blockquote{margin:1em 0;padding:.2em 1em;border-left:4px solid #d0d7de;color:#555}pre,code{font-family:Consolas,"Courier New",monospace}pre{white-space:pre-wrap;overflow-wrap:anywhere;padding:.8em;background:#f6f8fa}div[align="center"]{text-align:center}div[align="center"]>p{margin-top:.25em}
</style></head><body>${content}</body></html>`;
fs.writeFileSync(htmlPath, html, 'utf8');

(async()=>{
  const browser=await chromium.launch({headless:true});
  const page=await browser.newPage();
  await page.goto(pathToFileURL(htmlPath).href,{waitUntil:'networkidle',timeout:120000});
  await page.evaluate(async()=>{await Promise.all(Array.from(document.images,img=>img.complete?Promise.resolve():new Promise(resolve=>{img.onload=img.onerror=resolve})));if(document.fonts&&document.fonts.ready)await document.fonts.ready});
  const missing=await page.evaluate(()=>Array.from(document.images).filter(img=>!img.naturalWidth).map(img=>img.getAttribute('src')));
  if(missing.length)throw new Error(`Images failed to load: ${missing.join(', ')}`);
  await page.pdf({path:pdfPath,format:'A4',printBackground:true,displayHeaderFooter:true,headerTemplate:'<div style="width:100%;font-size:8px;padding:0 13mm;color:#222;display:flex;justify-content:space-between"><span>upc-pre-202620-1acc0238-13975-ADM-report.md</span><span>2026-10-03</span></div>',footerTemplate:'<div style="width:100%;font-size:8px;text-align:center;color:#222"><span class="pageNumber"></span> / <span class="totalPages"></span></div>',margin:{top:'13mm',right:'13mm',bottom:'17mm',left:'13mm'},preferCSSPageSize:true});
  await browser.close();
  console.log(pdfPath);
})().catch(error=>{console.error(error);process.exit(1)});
