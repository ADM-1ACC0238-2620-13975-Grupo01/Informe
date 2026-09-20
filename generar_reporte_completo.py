"""Reúne el informe en un Markdown con enlaces internos y recursos locales válidos."""

from __future__ import annotations

import os
import re
import unicodedata
from pathlib import Path
from urllib.parse import quote, unquote


ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / "markdown" / "content"
OUTPUT = (
    Path(os.environ["ANITEC_REPORT_OUTPUT"]).resolve()
    if os.environ.get("ANITEC_REPORT_OUTPUT")
    else ROOT / "upc-pre-202620-1acc0238-13975-ADM-report.md"
)
SECTIONS = [
    (None, ["registro-versiones.md", "report-collaboration.md", "student-outcome.md", "objetivos-smart.md"]),
    ("Capítulo I: Presentación", [
        "chapter-1/1-1-startup-profile.md",
        "chapter-1/1-2-solution-profile.md",
        "chapter-1/1-3-segmentos-objetivo.md",
    ]),
    ("Capítulo II: Requirements Development and Software Solution Design", [
        "chapter-2/2-1-competidores.md",
        "chapter-2/2-2-entrevistas.md",
        "chapter-2/2-3-needfinding.md",
        "chapter-2/2-4-Requirements-specification.md",
        "chapter-2/2-5-Strategic-Level-Domain-Driven-Design.md",
        "chapter-2/2-6-Tactical-Level-Domain-Driven-Design.md",
        *[f"chapter-2/2-6-{number}-Bounded-Context-{name}.md" for number, name in [
            (1, "Identity-and-Access-Management"),
            (2, "Profile-Management"),
            (3, "Livestock-Management"),
            (4, "Sanitary-Management"),
            (5, "Veterinary-Collaboration"),
            (6, "Activity-Management"),
            (7, "Financial-Management"),
            (8, "Subscription-Management"),
            (9, "Analytics-and-Reporting"),
        ]],
    ]),
    ("Capítulo III: Solution UI/UX Design", ["chapter-3/3-1-product-design.md"]),
    ("Capítulo IV: Product Implementation & Validation", [
        "chapter-4/4-0-Product-Implementation-and-Validation.md",
        "chapter-4/4-1-Software-Configuration-Management.md",
        "chapter-4/4-2-Landing-Page-and-Mobile-Application-Implementation.md",
        "chapter-4/4-3-validation-interviews.md",
    ]),
    (None, ["conclusiones.md", "bibliografia.md", "anexos.md"]),
]


def numeric_key(label: str) -> str | None:
    match = re.match(r"^(\d+(?:\.\d+)*)(?:\.)?(?:\s|$)", label)
    return match.group(1) if match else None


def normalise(label: str) -> str:
    value = unicodedata.normalize("NFKD", label.casefold())
    return "".join(char for char in value if char.isalnum())


caratula = (ROOT / "caratula.md").read_text(encoding="utf-8-sig")
cover, toc_source = caratula.split('<div style="font-size: 18px; line-height: 1.65;">', 1)
toc_source = toc_source.split("## Índice general", 1)[1]
toc_source = toc_source.split('<div style="page-break-before: always;">', 1)[0]
toc_lines = [line for line in toc_source.splitlines() if "[Glosario]" not in line]
while toc_lines and (not toc_lines[0].strip() or toc_lines[0].strip() == "</div>"):
    toc_lines.pop(0)
while toc_lines and (not toc_lines[-1].strip() or toc_lines[-1].strip() == "</div>"):
    toc_lines.pop()

toc_pairs = re.findall(r"\[([^]]+)\]\(#([^)]+)\)", "\n".join(toc_lines))
allowed_unnumbered = {
    "Registro de Versiones del Informe",
    "Project Report Collaboration Insights",
    "Student Outcome",
    "Objetivos SMART",
    "Conclusiones",
    "Bibliografía",
    "Anexos",
}
unexpected_toc_entries = [label for label, _ in toc_pairs if not numeric_key(label) and label not in allowed_unnumbered]
numbered_entries = [numeric_key(label) for label, _ in toc_pairs if numeric_key(label)]
duplicate_numbers = sorted({number for number in numbered_entries if numbered_entries.count(number) > 1})
if unexpected_toc_entries or duplicate_numbers:
    details = []
    if unexpected_toc_entries:
        details.append("entradas sin numeración: " + ", ".join(unexpected_toc_entries))
    if duplicate_numbers:
        details.append("numeraciones duplicadas: " + ", ".join(duplicate_numbers))
    raise ValueError("El índice de caratula.md no es el índice curado: " + "; ".join(details))
number_to_id = {numeric_key(label): anchor for label, anchor in toc_pairs if numeric_key(label)}
title_to_id = {normalise(label): anchor for label, anchor in toc_pairs if not numeric_key(label)}
all_sources = [(CONTENT / name).resolve() for _, names in SECTIONS for name in names]
source_set = set(all_sources)
unlisted_sources = set(CONTENT.rglob("*.md")) - source_set
if unlisted_sources:
    raise ValueError("Markdown de content sin incluir: " + ", ".join(str(path) for path in sorted(unlisted_sources)))


def first_anchor(path: Path) -> str:
    contents = path.read_text(encoding="utf-8-sig")
    heading = re.search(r"^#{1,6}\s+(.+?)\s*$", contents, re.MULTILINE)
    if not heading:
        raise ValueError(f"Sin encabezado: {path}")
    title = heading.group(1)
    anchor = number_to_id.get(numeric_key(title)) or title_to_id.get(normalise(title))
    if not anchor:
        explicit_anchor = re.search(r'<a\s+(?:id|name)="([^"]+)"', contents, flags=re.IGNORECASE)
        if explicit_anchor:
            return explicit_anchor.group(1)
        anchor = "toc-" + re.sub(r"[^a-z0-9]+", "-", unicodedata.normalize("NFKD", title.casefold()).encode("ascii", "ignore").decode()).strip("-")
    return anchor


source_anchors = {path: first_anchor(path) for path in all_sources}
missing_resources: list[tuple[str, str]] = []


def rewrite_target(target: str, source: Path, *, image: bool = False) -> str:
    if target.startswith(("#", "http://", "https://", "mailto:", "data:", "javascript:")):
        return target
    path_text, separator, fragment = target.partition("#")
    path_text = unquote(path_text)
    resolved = (source.parent / path_text).resolve()
    if resolved in source_set:
        return "#" + (fragment if separator else source_anchors[resolved])
    if not resolved.exists() and resolved.name == "component-level.dsl":
        old_folder = re.fullmatch(r"2\.6\.(\d+)\. Bounded Context (.+)", resolved.parent.name)
        if old_folder:
            number, context_name = old_folder.groups()
            current_folder = f"2-6-{number}-Bounded-Context-{context_name.replace(' ', '-')}"
            candidate = resolved.parent.parent / current_folder / resolved.name
            if candidate.is_file():
                resolved = candidate
    if image and (not resolved.is_file()):
        missing_resources.append((source.relative_to(ROOT).as_posix(), target))
    relative = Path(os.path.relpath(resolved, ROOT)).as_posix()
    return relative + ("#" + fragment if separator else "")


def rewrite_refs(contents: str, source: Path) -> str:
    def html_attribute(match: re.Match[str]) -> str:
        prefix, target, suffix = match.groups()
        is_image = prefix.lower().lstrip().startswith("src")
        rewritten = rewrite_target(target, source, image=is_image)
        if is_image and not rewritten.startswith(("http://", "https://", "data:")):
            rewritten = quote(rewritten, safe="/:#%?=&")
        return prefix + rewritten + suffix

    contents = re.sub(r'((?:src|href)\s*=\s*")([^"]+)(")', html_attribute, contents, flags=re.IGNORECASE)

    def markdown_link(match: re.Match[str]) -> str:
        prefix, raw, suffix = match.groups()
        angled = raw.startswith("<") and raw.endswith(">")
        target = raw[1:-1] if angled else raw
        is_image = prefix.startswith("!")
        new_target = rewrite_target(target, source, image=is_image)
        if angled or " " in new_target:
            new_target = f"<{new_target}>"
        return prefix + new_target + suffix

    return re.sub(r"(!?\[[^]\n]*\]\()(<[^>\n]+>|[^)\n]+)(\))", markdown_link, contents)


def add_toc_anchors(contents: str) -> str:
    existing = set(re.findall(r'<a\s+(?:id|name)="([^"]+)"', contents, flags=re.IGNORECASE))
    lines = contents.splitlines()
    result = []
    for line in lines:
        match = re.match(r"^#{1,6}\s+(.+?)\s*$", line)
        if match:
            heading = match.group(1)
            anchor = number_to_id.get(numeric_key(heading)) or title_to_id.get(normalise(heading))
            if anchor and anchor not in existing:
                result.extend([f'<a id="{anchor}"></a>', ""])
                existing.add(anchor)
        result.append(line)
    return "\n".join(result).strip() + "\n"


def table_font_size(match: re.Match[str]) -> str:
    attributes = match.group(1)
    if re.search(r"\balign\s*=", attributes, flags=re.IGNORECASE):
        return match.group(0)  # Conserva la tabla de integrantes de la carátula.
    style = re.search(r'\bstyle="([^"]*)"', attributes, flags=re.IGNORECASE)
    if style:
        current = style.group(1).rstrip().rstrip(";")
        updated = f'{current}; font-size: 11px; line-height: 1.8;'
        attributes = attributes[:style.start(1)] + updated + attributes[style.end(1):]
    else:
        attributes += ' style="font-size: 11px; line-height: 1.8;"'
    return f"<table{attributes}>"


parts = [
    cover.strip(),
    '<div style="font-size: 20px; line-height: 1.8;">',
    '<div style="page-break-before: always;"></div>',
    '<h1 align="center">Índice general</h1>',
    "\n".join(toc_lines).strip(),
]
parts.append('<div style="page-break-before: always;"></div>')
for chapter, names in SECTIONS:
    if chapter:
        chapter_anchor = title_to_id.get(normalise(chapter))
        chapter_heading = f'<a id="{chapter_anchor}"></a>\n\n# {chapter}' if chapter_anchor else f"# {chapter}"
        parts.extend(['<div style="page-break-before: always;"></div>', chapter_heading])
    for name in names:
        source = (CONTENT / name).resolve()
        contents = source.read_text(encoding="utf-8-sig")
        if name == "conclusiones.md":
            # El origen deja una carpeta como src de una captura futura; no es una imagen exportable.
            contents = re.sub(
                r'<div align="center">\s*<img src="\.\./assets/chapter-5/"[^>]*>\s*<p>.*?</p>\s*</div>',
                '<!-- Captura del video About The Team pendiente de incorporación. -->',
                contents,
                flags=re.DOTALL,
            )
        contents = rewrite_refs(contents, source)
        contents = add_toc_anchors(contents)
        if re.fullmatch(r"chapter-2/2-6-[1-9]-Bounded-Context-.*\.md", name):
            contents = re.sub(r"<table\b([^>]*)>", table_font_size, contents, flags=re.IGNORECASE)
        parts.append(contents)

parts.append("</div>")

report = "\n\n".join(parts).rstrip() + "\n"
# En la versión destinada a PDF, nombres y firmas se leen como texto normal.
report = report.replace("<code>", "").replace("</code>", "").replace("`", "")
OUTPUT.write_text(report, encoding="utf-8")

defined_anchors = set(re.findall(r'<a\s+(?:id|name)="([^"]+)"', report, flags=re.IGNORECASE))
missing_anchors = sorted({anchor for _, anchor in toc_pairs if anchor not in defined_anchors})
print(f"Generado: {OUTPUT}")
print(f"Archivos de contenido: {len(all_sources)}")
print(f"Enlaces del índice: {len(toc_pairs)}; destinos faltantes: {len(missing_anchors)}")
for anchor in missing_anchors:
    print(f"  Ancla ausente: {anchor}")
print(f"Imágenes locales ausentes: {len(missing_resources)}")
for source, target in missing_resources:
    print(f"  {source}: {target}")

# La validación final usa las rutas del archivo combinado, no las de los archivos fuente.
html_refs = re.findall(r'(?:src|href)="([^"]+)"', report, flags=re.IGNORECASE)
markdown_refs = re.findall(r'!?\[[^]\n]*\]\((<[^>\n]+>|[^)\n]+)\)', report)
local_refs = [ref[1:-1] if ref.startswith("<") and ref.endswith(">") else ref
              for ref in html_refs + markdown_refs]
missing_files = sorted({ref for ref in local_refs
                        if not ref.startswith(("#", "http://", "https://", "mailto:", "data:"))
                        and not (ROOT / unquote(ref.split("#", 1)[0])).is_file()})
missing_internal = sorted({ref for ref in local_refs if ref.startswith("#") and ref[1:] not in defined_anchors})
print(f"Referencias a archivos locales inexistentes: {len(missing_files)}")
for ref in missing_files:
    print(f"  Archivo ausente: {ref}")
print(f"Enlaces internos sin destino: {len(missing_internal)}")
for ref in missing_internal:
    print(f"  Destino ausente: {ref}")
if missing_anchors or missing_resources or missing_files or missing_internal:
    raise SystemExit(1)
