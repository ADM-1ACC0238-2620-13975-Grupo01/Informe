"""Genera seis User Flow Diagrams estandar a partir de los mock-ups de AniTec.

Cada diagrama representa un user goal independientemente de la implementacion en
Flutter o Android. Las pantallas se usan como referencias visuales y los detalles
de recuperacion se explican en el texto del informe para mantener la legibilidad.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "markdown" / "assets" / "chapter-3"
OUTPUT = ASSETS / "user-flow-diagrams"
OUTPUT.mkdir(parents=True, exist_ok=True)

CANVAS = (2200, 1080)
GREEN = "#3F7F2A"
GREEN_LIGHT = "#EAF5E5"
RED = "#B42318"
RED_LIGHT = "#FDECEA"
AMBER = "#9A5B00"
AMBER_LIGHT = "#FFF3D6"
INK = "#17313F"
MUTED = "#52636D"
BORDER = "#AEBCC2"
SHADOW = "#DDE5E8"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        Path("C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
    ]
    for candidate in candidates:
        if candidate.is_file():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default()


F_TITLE = font(46, True)
F_SUBTITLE = font(25)
F_NODE = font(28, True)
F_ACTION = font(22, True)
F_DECISION = font(26, True)
F_BRANCH = font(24, True)
F_BRANCH_BODY = font(21)
F_SMALL = font(18)


@dataclass(frozen=True)
class ScreenNode:
    label: str
    image: Path


@dataclass(frozen=True)
class Branch:
    title: str
    response: str
    alternative: bool = False


@dataclass(frozen=True)
class Flow:
    slug: str
    title: str
    personas: str
    nodes: tuple[ScreenNode, ScreenNode, ScreenNode]
    actions: tuple[str, str, str]
    decision: str
    branches: tuple[Branch, Branch, Branch]


def mockup(platform: str, role: str, filename: str) -> Path:
    platform_folder = {
        "flutter": "mock-upsMobileFlutter",
        "android": "mock-upsMobileAndroid",
    }[platform]
    role_folder = {"iam": "iam", "rancher": "rancher", "vet": "vets"}[role]
    path = ASSETS / platform_folder / role_folder / filename
    if not path.is_file():
        raise FileNotFoundError(path)
    return path


def flutter_screen(role: str, number: int) -> Path:
    return mockup("flutter", role, f"iPhone 17 - {number}.png")


def android_screen(role: str, number: int) -> Path:
    return mockup("android", role, f"Android Compact - {number}.png")


def named(platform: str, filename: str) -> Path:
    return mockup(platform, "rancher", filename)


def wrap(draw: ImageDraw.ImageDraw, text: str, selected_font: ImageFont.ImageFont, width: int) -> list[str]:
    lines: list[str] = []
    current = ""
    for word in text.split():
        candidate = f"{current} {word}".strip()
        if draw.textlength(candidate, font=selected_font) <= width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def centered_text(
    draw: ImageDraw.ImageDraw,
    text: str,
    box: tuple[int, int, int, int],
    selected_font: ImageFont.ImageFont,
    fill: str,
    gap: int = 4,
) -> None:
    x1, y1, x2, y2 = box
    lines = wrap(draw, text, selected_font, x2 - x1)
    line_box = draw.textbbox((0, 0), "Ag", font=selected_font)
    line_height = line_box[3] - line_box[1]
    total = len(lines) * line_height + max(0, len(lines) - 1) * gap
    y = y1 + max(0, (y2 - y1 - total) // 2)
    for line in lines:
        length = draw.textlength(line, font=selected_font)
        draw.text(((x1 + x2 - length) / 2, y), line, font=selected_font, fill=fill)
        y += line_height + gap


def arrow(
    draw: ImageDraw.ImageDraw,
    start: tuple[int, int],
    end: tuple[int, int],
    color: str,
    width: int = 6,
    dashed: bool = False,
) -> None:
    import math

    x1, y1 = start
    x2, y2 = end
    if dashed:
        distance = max(abs(x2 - x1), abs(y2 - y1))
        segments = max(1, distance // 18)
        for index in range(segments):
            if index % 2:
                continue
            t1 = index / segments
            t2 = min(1, (index + 1) / segments)
            draw.line(
                (
                    x1 + (x2 - x1) * t1,
                    y1 + (y2 - y1) * t1,
                    x1 + (x2 - x1) * t2,
                    y1 + (y2 - y1) * t2,
                ),
                fill=color,
                width=width,
            )
    else:
        draw.line((x1, y1, x2, y2), fill=color, width=width)
    angle = math.atan2(y2 - y1, x2 - x1)
    size = 18
    left = (x2 - size * math.cos(angle - 0.55), y2 - size * math.sin(angle - 0.55))
    right = (x2 - size * math.cos(angle + 0.55), y2 - size * math.sin(angle + 0.55))
    draw.polygon([(x2, y2), left, right], fill=color)


def paste_phone(canvas: Image.Image, source_path: Path, box: tuple[int, int, int, int]) -> None:
    x1, y1, x2, y2 = box
    with Image.open(source_path) as source:
        phone = source.convert("RGB")
        phone.thumbnail((x2 - x1, y2 - y1), Image.Resampling.LANCZOS)
        px = x1 + (x2 - x1 - phone.width) // 2
        py = y1 + (y2 - y1 - phone.height) // 2
        canvas.paste(phone, (px, py))


def draw_screen_card(
    canvas: Image.Image,
    draw: ImageDraw.ImageDraw,
    node: ScreenNode,
    x: int,
    y: int,
) -> tuple[int, int, int, int]:
    width, height = 330, 610
    draw.rounded_rectangle((x + 9, y + 10, x + width + 9, y + height + 10), radius=24, fill=SHADOW)
    draw.rounded_rectangle((x, y, x + width, y + height), radius=24, fill="white", outline=BORDER, width=3)
    draw.rounded_rectangle((x, y, x + width, y + 64), radius=24, fill=GREEN_LIGHT, outline=GREEN, width=3)
    draw.rectangle((x, y + 35, x + width, y + 64), fill=GREEN_LIGHT)
    centered_text(draw, node.label, (x + 18, y + 8, x + width - 18, y + 58), F_NODE, INK)
    paste_phone(canvas, node.image, (x + 24, y + 82, x + width - 24, y + height - 20))
    return (x, y, x + width, y + height)


def draw_decision(draw: ImageDraw.ImageDraw, center: tuple[int, int], label: str) -> tuple[int, int, int, int]:
    cx, cy = center
    points = [(cx, cy - 110), (cx + 150, cy), (cx, cy + 110), (cx - 150, cy)]
    draw.polygon(points, fill="#F2F7EF", outline=GREEN)
    draw.line(points + [points[0]], fill=GREEN, width=4, joint="curve")
    centered_text(draw, label, (cx - 105, cy - 60, cx + 105, cy + 60), F_DECISION, INK)
    return (cx - 150, cy - 110, cx + 150, cy + 110)


def build(flow: Flow) -> None:
    image = Image.new("RGB", CANVAS, "white")
    draw = ImageDraw.Draw(image)

    draw.text((70, 34), flow.title, font=F_TITLE, fill=INK)
    draw.text((72, 92), f"User Persona: {flow.personas}", font=F_SUBTITLE, fill=MUTED)
    draw.text((72, 126), "Flujo estándar para Android y Flutter · Mock-ups representativos", font=F_SUBTITLE, fill=MUTED)

    # El color se acompana de linea y etiqueta para no depender solo del color.
    draw.line((1625, 72, 1740, 72), fill=GREEN, width=7)
    draw.text((1755, 55), "Happy path", font=F_ACTION, fill=GREEN)
    arrow(draw, (1625, 118), (1740, 118), RED, width=5, dashed=True)
    draw.text((1755, 101), "Unhappy / alternativa", font=F_ACTION, fill=RED)

    y = 190
    card1 = draw_screen_card(image, draw, flow.nodes[0], 70, y)
    card2 = draw_screen_card(image, draw, flow.nodes[1], 550, y)
    decision = draw_decision(draw, (1120, 495), flow.decision)
    card3 = draw_screen_card(image, draw, flow.nodes[2], 1390, y)

    mid_y = 495
    draw.ellipse((8, mid_y - 17, 42, mid_y + 17), fill=GREEN)
    arrow(draw, (42, mid_y), (card1[0] - 10, mid_y), GREEN)
    arrow(draw, (card1[2] + 10, mid_y), (card2[0] - 10, mid_y), GREEN)
    arrow(draw, (card2[2] + 10, mid_y), (decision[0] - 10, mid_y), GREEN)
    arrow(draw, (decision[2] + 10, mid_y), (card3[0] - 10, mid_y), GREEN)
    arrow(draw, (card3[2] + 10, mid_y), (1900, mid_y), GREEN)
    draw.ellipse((1900, mid_y - 19, 1938, mid_y + 19), outline=GREEN, width=5)
    draw.ellipse((1908, mid_y - 11, 1930, mid_y + 11), fill=GREEN)

    centered_text(draw, flow.actions[0], (card1[2] + 8, mid_y - 74, card2[0] - 8, mid_y - 24), F_ACTION, GREEN)
    centered_text(draw, flow.actions[1], (card2[2] + 8, mid_y - 74, decision[0] - 8, mid_y - 24), F_ACTION, GREEN)
    centered_text(draw, "Sí", (decision[2] + 10, mid_y - 70, card3[0] - 10, mid_y - 25), F_ACTION, GREEN)
    centered_text(draw, flow.actions[2], (card3[2] + 8, mid_y - 74, 1900, mid_y - 24), F_ACTION, GREEN)

    branch_y = 855
    branch_w = 620
    branch_h = 155
    branch_xs = (70, 790, 1510)
    for index, (branch, bx) in enumerate(zip(flow.branches, branch_xs)):
        color = AMBER if branch.alternative else RED
        fill = AMBER_LIGHT if branch.alternative else RED_LIGHT
        tag = "RUTA ALTERNATIVA" if branch.alternative else "UNHAPPY PATH"
        target_x = bx + branch_w // 2
        lane_y = 820 + index * 8
        arrow(draw, (1120, decision[3] + 8), (1120, lane_y), color, width=4, dashed=True)
        arrow(draw, (1120, lane_y), (target_x, lane_y), color, width=4, dashed=True)
        arrow(draw, (target_x, lane_y), (target_x, branch_y - 8), color, width=4, dashed=True)
        draw.rounded_rectangle((bx, branch_y, bx + branch_w, branch_y + branch_h), radius=20, fill=fill, outline=color, width=3)
        draw.text((bx + 22, branch_y + 15), tag, font=F_SMALL, fill=color)
        draw.text((bx + 22, branch_y + 47), branch.title, font=F_BRANCH, fill=color)
        centered_text(draw, branch.response, (bx + 22, branch_y + 78, bx + branch_w - 22, branch_y + branch_h - 12), F_BRANCH_BODY, INK)

    draw.text((70, 1038), "Fuente: elaboración propia a partir de los mock-ups de AniTec.", font=F_SMALL, fill=MUTED)
    image.save(OUTPUT / f"{flow.slug}.png", optimize=True)


def flows() -> list[Flow]:
    return [
        Flow(
            "user-flow-01-registro-inicio-sesion",
            "User Flow 1 - Registrarse e iniciar sesión",
            "Jorge Luis Rivas y Valeria Mendoza",
            (
                ScreenNode("Conocer AniTec", flutter_screen("iam", 1)),
                ScreenNode("Crear cuenta o ingresar", flutter_screen("iam", 4)),
                ScreenNode("Llegar al dashboard", named("flutter", "01 Dashboard.png")),
            ),
            ("Continuar", "Enviar datos", "Acceso correcto"),
            "¿Acceso válido?",
            (
                Branch("Datos o credenciales inválidos", "Corregir y volver a enviar."),
                Branch("Cuenta existente", "Cambiar a Sign in.", True),
                Branch("Sin conexión", "Conservar los datos y reintentar."),
            ),
        ),
        Flow(
            "user-flow-02-consultar-dashboard",
            "User Flow 2 - Consultar dashboard",
            "Jorge Luis Rivas y Valeria Mendoza",
            (
                ScreenNode("Iniciar sesión", android_screen("iam", 9)),
                ScreenNode("Consultar resumen", named("android", "01 Dashboard.png")),
                ScreenNode("Abrir un módulo", named("android", "02 Animals.png")),
            ),
            ("Ingresar", "Cargar resumen", "Elegir módulo"),
            "¿Resumen disponible?",
            (
                Branch("Sin datos o cargando", "Mostrar estado inicial o de carga."),
                Branch("Sesión vencida", "Volver a iniciar sesión."),
                Branch("Servicio o acceso no disponible", "Reintentar o recuperar acceso."),
            ),
        ),
        Flow(
            "user-flow-03-registrar-animal",
            "User Flow 3 - Registrar animal",
            "Jorge Luis Rivas (ganadero)",
            (
                ScreenNode("Abrir Animals", named("flutter", "02 Animals.png")),
                ScreenNode("Completar registro", named("flutter", "08 New animal.png")),
                ScreenNode("Revisar animal", named("flutter", "07 Animal detail.png")),
            ),
            ("Tocar +", "Guardar", "Registro creado"),
            "¿Registro válido?",
            (
                Branch("Campos o tag inválidos", "Corregir sin perder la información."),
                Branch("Sin conexión", "Guardar como pendiente de sincronización."),
                Branch("Varios animales", "Usar el registro masivo.", True),
            ),
        ),
        Flow(
            "user-flow-04-consultar-actualizar-animal",
            "User Flow 4 - Consultar o actualizar animal",
            "Jorge Luis Rivas (ganadero)",
            (
                ScreenNode("Buscar animal", named("android", "02 Animals.png")),
                ScreenNode("Revisar detalle", named("android", "07 Animal detail.png")),
                ScreenNode("Editar y guardar", named("android", "19 Edit animal.png")),
            ),
            ("Seleccionar", "Tocar Edit", "Cambios guardados"),
            "¿Cambios válidos?",
            (
                Branch("Sin resultados", "Limpiar o ajustar la búsqueda."),
                Branch("Solo lectura", "Consultar sin modificar."),
                Branch("Conflicto de sincronización", "Elegir la versión que se conservará."),
            ),
        ),
        Flow(
            "user-flow-05-historial-sanitario",
            "User Flow 5 - Consultar historial sanitario",
            "Jorge Luis Rivas y Valeria Mendoza",
            (
                ScreenNode("Seleccionar paciente", named("flutter", "07 Animal detail.png")),
                ScreenNode("Abrir Health history", flutter_screen("rancher", 17)),
                ScreenNode("Revisar registro", flutter_screen("vet", 60)),
            ),
            ("Abrir detalle", "Ver historial", "Elegir registro"),
            "¿Historial accesible?",
            (
                Branch("Sin registros", "Mostrar estado vacío y acción disponible."),
                Branch("Sin permiso", "Solicitar o restablecer el acceso."),
                Branch("Modo offline", "Mostrar la copia local identificada."),
            ),
        ),
        Flow(
            "user-flow-06-registrar-evento-sanitario",
            "User Flow 6 - Registrar evento sanitario",
            "Jorge Luis Rivas y Valeria Mendoza",
            (
                ScreenNode("Abrir paciente", named("android", "07 Animal detail.png")),
                ScreenNode("Registrar evento", android_screen("vet", 61)),
                ScreenNode("Confirmar en historial", android_screen("vet", 63)),
            ),
            ("Elegir acción", "Guardar", "Evento registrado"),
            "¿Evento válido?",
            (
                Branch("Datos incompletos", "Corregir sin cerrar el formulario."),
                Branch("Sin conexión o permiso", "Guardar pendiente o recuperar acceso."),
                Branch("Programar seguimiento", "Crear una actividad posterior.", True),
            ),
        ),
    ]


def main() -> None:
    all_flows = flows()
    for flow in all_flows:
        build(flow)
        print(OUTPUT / f"{flow.slug}.png")
    print(f"Diagramas generados: {len(all_flows)}")


if __name__ == "__main__":
    main()
