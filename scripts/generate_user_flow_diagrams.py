"""Genera seis User Flow Diagrams directos a partir de los mock-ups de AniTec.

Cada lámina contiene solo las pantallas, acciones y condiciones necesarias para
comprender la interacción principal y sus rutas secundarias.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


# Los mock-ups se leen del capítulo 3 y los diagramas se guardan en user-flow-diagrams.
ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "markdown" / "assets" / "chapter-3"
OUTPUT = ASSETS / "user-flow-diagrams"
OUTPUT.mkdir(parents=True, exist_ok=True)

# Tamaño en píxeles de cada diagrama y colores de nodos, ramas, texto y bordes.
CANVAS = (2200, 1200)
GREEN = "#3F7F2A"
GREEN_LIGHT = "#EAF5E5"
RED = "#B42318"
AMBER = "#9A5B00"
INK = "#17313F"
BORDER = "#AEBCC2"
SHADOW = "#DDE5E8"

# Carga la fuente Arial o DejaVu Sans en el tamaño indicado; si no existen, usa la fuente por defecto.
def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    """Carga Arial o DejaVu Sans en el tamaño indicado; si no existen, usa la fuente por defecto."""
    candidates = [
        Path("C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
    ]
    for candidate in candidates:
        if candidate.is_file():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default()


# Fuentes cargadas una sola vez y reutilizadas en todos los diagramas.
F_NODE = font(27, True)
F_ACTION = font(22, True)
F_BRANCH = font(25, True)

# Pantalla del flujo con su etiqueta y la ruta de la imagen del mock-up.
@dataclass(frozen=True)
class ScreenNode:
    """Pantalla del flujo con su etiqueta y la imagen del mock-up."""
    label: str
    image: Path

# Resultado posible después de la decisión del flujo, indicando su título, respuesta y si es una alternativa.
@dataclass(frozen=True)
class Branch:
    """Desvío del flujo con la condición y la acción que permite continuar."""
    condition: str
    next_action: str
    source_index: int
    image: Path
    alternative: bool = False

# User flow completo que agrupa las pantallas, acciones, decisiones y ramas del proceso de negocio.
@dataclass(frozen=True)
class Flow:
    slug: str
    nodes: tuple[ScreenNode, ScreenNode, ScreenNode]
    actions: tuple[str, str, str, str]
    branches: tuple[Branch, Branch, Branch]

# Devuelve la ruta de un mock-up de Flutter o Android y genera un error si el archivo no existe.
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

# Devuelve la ruta del archivo de mock-up "iPhone 17 - N" de Flutter para el rol indicado.
def flutter_screen(role: str, number: int) -> Path:
    return mockup("flutter", role, f"iPhone 17 - {number}.png")

# Devuelve la ruta del archivo de mock-up "Android Compact - N" de Android para el rol indicado.
def android_screen(role: str, number: int) -> Path:
    """Devuelve el mock-up "Android Compact - N" de Android para el rol indicado."""
    return mockup("android", role, f"Android Compact - {number}.png")

# Devuelve la ruta del mock-up correspondiente al rol de ganadero utilizando su nombre de archivo específico.
def named(platform: str, filename: str) -> Path:
    """Devuelve un mock-up del ganadero por su nombre de archivo."""
    return mockup(platform, "rancher", filename)


def wrap(draw: ImageDraw.ImageDraw, text: str, selected_font: ImageFont.ImageFont, width: int) -> list[str]:
    """Divide un texto en líneas que caben en el ancho indicado con la fuente elegida."""
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

# Dibuja texto centrado vertical y horizontalmente dentro de una caja delimitadora específica.
def centered_text(
    draw: ImageDraw.ImageDraw,
    text: str,
    box: tuple[int, int, int, int],
    selected_font: ImageFont.ImageFont,
    fill: str,
    gap: int = 4,
) -> None:
    """Escribe un texto ajustado y centrado dentro de una caja."""
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


# Dibuja una flecha entre dos puntos, con soporte opcional para líneas discontinuas y grosor personalizado.
def dashed_line(
    draw: ImageDraw.ImageDraw,
    start: tuple[int, int],
    end: tuple[int, int],
    color: str,
    width: int = 4,
) -> None:
    """Dibuja una línea discontinua sin punta de flecha."""
    x1, y1 = start
    x2, y2 = end
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


def arrow(
    draw: ImageDraw.ImageDraw,
    start: tuple[int, int],
    end: tuple[int, int],
    color: str,
    width: int = 6,
    dashed: bool = False,
) -> None:
    """Dibuja una flecha entre dos puntos, continua o discontinua."""
    import math

    x1, y1 = start
    x2, y2 = end
    if dashed:
        dashed_line(draw, start, end, color, width)
    else:
        draw.line((x1, y1, x2, y2), fill=color, width=width)
    angle = math.atan2(y2 - y1, x2 - x1)
    size = 18
    left = (x2 - size * math.cos(angle - 0.55), y2 - size * math.sin(angle - 0.55))
    right = (x2 - size * math.cos(angle + 0.55), y2 - size * math.sin(angle + 0.55))
    draw.polygon([(x2, y2), left, right], fill=color)


def paste_phone(canvas: Image.Image, source_path: Path, box: tuple[int, int, int, int]) -> None:
    """Pega la captura de una pantalla escalada y centrada dentro de la caja."""
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
    """Dibuja la tarjeta de una pantalla con su sombra, captura y etiqueta, y devuelve su caja."""
    width, height = 330, 590
    draw.rounded_rectangle((x + 9, y + 10, x + width + 9, y + height + 10), radius=24, fill=SHADOW)
    draw.rounded_rectangle((x, y, x + width, y + height), radius=24, fill="white", outline=BORDER, width=3)
    draw.rounded_rectangle((x, y, x + width, y + 64), radius=24, fill=GREEN_LIGHT, outline=GREEN, width=3)
    draw.rectangle((x, y + 35, x + width, y + 64), fill=GREEN_LIGHT)
    centered_text(draw, node.label, (x + 18, y + 8, x + width - 18, y + 58), F_NODE, INK)
    paste_phone(canvas, node.image, (x + 24, y + 82, x + width - 24, y + height - 20))
    return (x, y, x + width, y + height)


def draw_branch_screen(
    canvas: Image.Image,
    draw: ImageDraw.ImageDraw,
    branch: Branch,
    center_x: int,
    y: int,
) -> None:
    """Dibuja la pantalla y las etiquetas mínimas de una ruta secundaria."""
    color = AMBER if branch.alternative else RED
    centered_text(draw, branch.condition, (center_x - 300, y - 78, center_x + 300, y - 20), F_BRANCH, color)

    image_box = (center_x - 110, y, center_x + 110, y + 300)
    draw.rounded_rectangle((image_box[0] + 7, image_box[1] + 8, image_box[2] + 7, image_box[3] + 8), radius=18, fill=SHADOW)
    draw.rounded_rectangle(image_box, radius=18, fill="white", outline=color, width=3)
    paste_phone(canvas, branch.image, (image_box[0] + 10, image_box[1] + 10, image_box[2] - 10, image_box[3] - 10))

    centered_text(draw, branch.next_action, (center_x - 300, y + 320, center_x + 300, y + 380), F_ACTION, INK)


def build(flow: Flow) -> None:
    """Dibuja un user flow completo y lo guarda como PNG."""
    image = Image.new("RGB", CANVAS, "white")
    draw = ImageDraw.Draw(image)

    y = 70
    card_xs = (140, 935, 1730)
    cards = tuple(draw_screen_card(image, draw, node, x, y) for node, x in zip(flow.nodes, card_xs))

    mid_y = 365
    draw.ellipse((24, mid_y - 17, 58, mid_y + 17), fill=GREEN)
    arrow(draw, (58, mid_y), (cards[0][0] - 10, mid_y), GREEN)
    arrow(draw, (cards[0][2] + 10, mid_y), (cards[1][0] - 10, mid_y), GREEN)
    arrow(draw, (cards[1][2] + 10, mid_y), (cards[2][0] - 10, mid_y), GREEN)
    arrow(draw, (cards[2][2] + 10, mid_y), (2142, mid_y), GREEN)
    draw.ellipse((2140, mid_y - 19, 2178, mid_y + 19), outline=GREEN, width=5)
    draw.ellipse((2148, mid_y - 11, 2170, mid_y + 11), fill=GREEN)

    action_boxes = (
        (5, mid_y - 82, cards[0][0] - 10, mid_y - 28),
        (cards[0][2] + 14, mid_y - 82, cards[1][0] - 14, mid_y - 28),
        (cards[1][2] + 14, mid_y - 82, cards[2][0] - 14, mid_y - 28),
        (cards[2][2] + 14, mid_y - 82, 2195, mid_y - 28),
    )
    for label, box in zip(flow.actions, action_boxes):
        centered_text(draw, label, box, F_ACTION, GREEN)

    branch_y = 820
    branch_centers = (300, 1100, 1900)
    source_counts = {
        source_index: sum(branch.source_index == source_index for branch in flow.branches)
        for source_index in range(len(cards))
    }
    source_positions: dict[int, int] = {}
    for index, (branch, target_x) in enumerate(zip(flow.branches, branch_centers)):
        color = AMBER if branch.alternative else RED
        source = cards[branch.source_index]
        position = source_positions.get(branch.source_index, 0)
        source_positions[branch.source_index] = position + 1
        total_from_source = source_counts[branch.source_index]
        offset = int((position - (total_from_source - 1) / 2) * 48)
        anchor_x = (source[0] + source[2]) // 2 + offset
        decision_y = 682 + index * 12
        draw.line((anchor_x, source[3] + 8, anchor_x, decision_y - 13), fill=color, width=4)
        diamond = [(anchor_x, decision_y - 13), (anchor_x + 13, decision_y), (anchor_x, decision_y + 13), (anchor_x - 13, decision_y)]
        draw.polygon(diamond, fill="white", outline=color)
        draw.line(diamond + [diamond[0]], fill=color, width=3)

        if abs(anchor_x - target_x) < 24:
            # Si origen y destino están alineados, evita una flecha horizontal de pocos píxeles.
            arrow(draw, (anchor_x, decision_y + 13), (target_x, branch_y - 86), color, width=4, dashed=True)
        else:
            # El tramo horizontal solo enruta; la dirección se indica al descender al destino.
            dashed_line(draw, (anchor_x, decision_y + 13), (target_x, decision_y + 13), color, width=4)
            arrow(draw, (target_x, decision_y + 13), (target_x, branch_y - 86), color, width=4, dashed=True)
        arrow(draw, (target_x, branch_y - 16), (target_x, branch_y - 5), color, width=4, dashed=True)
        draw_branch_screen(image, draw, branch, target_x, branch_y)

    image.save(OUTPUT / f"{flow.slug}.png", optimize=True)


def flows() -> list[Flow]:
    """Devuelve los seis user flows del informe."""
    return [
        Flow(
            "user-flow-01-registro-inicio-sesion",
            (
                ScreenNode("Conocer AniTec", flutter_screen("iam", 1)),
                ScreenNode("Crear una cuenta", flutter_screen("iam", 3)),
                ScreenNode("Llegar al dashboard", named("flutter", "01 Dashboard.png")),
            ),
            ("Abrir AniTec", "Tocar Get Started", "Enviar datos de acceso", "Sesión iniciada"),
            (
                Branch(
                    "Si los datos son inválidos",
                    "Corregir y volver a enviar",
                    1,
                    flutter_screen("iam", 3),
                ),
                Branch(
                    "Si la cuenta ya existe",
                    "Ingresar las credenciales existentes",
                    1,
                    flutter_screen("iam", 4),
                    True,
                ),
                Branch(
                    "Si no hay conexión",
                    "Reintentar al recuperar la red",
                    1,
                    flutter_screen("iam", 3),
                ),
            ),
        ),
        Flow(
            "user-flow-02-consultar-dashboard",
            (
                ScreenNode("Iniciar sesión", android_screen("iam", 9)),
                ScreenNode("Consultar resumen", named("android", "01 Dashboard.png")),
                ScreenNode("Abrir un módulo", named("android", "02 Animals.png")),
            ),
            ("Autenticarse", "Cargar datos del rol", "Elegir módulo", "Módulo disponible"),
            (
                Branch(
                    "Si aún no existen datos",
                    "Agregar la primera finca o cliente",
                    1,
                    android_screen("rancher", 10),
                    True,
                ),
                Branch(
                    "Si la sesión venció",
                    "Iniciar sesión nuevamente",
                    1,
                    android_screen("vet", 43),
                ),
                Branch(
                    "Si el servicio no responde",
                    "Reintentar o abrir datos guardados",
                    1,
                    android_screen("vet", 42),
                ),
            ),
        ),
        Flow(
            "user-flow-03-registrar-animal",
            (
                ScreenNode("Abrir Animals", named("flutter", "02 Animals.png")),
                ScreenNode("Completar registro", named("flutter", "08 New animal.png")),
                ScreenNode("Revisar animal", named("flutter", "07 Animal detail.png")),
            ),
            ("Entrar a Animals", "Tocar +", "Guardar ficha del animal", "Registro creado"),
            (
                Branch(
                    "Si faltan datos o el tag es inválido",
                    "Corregir los campos",
                    1,
                    android_screen("rancher", 15),
                ),
                Branch(
                    "Si no hay conexión",
                    "Sincronizar al recuperar la red",
                    1,
                    named("android", "11 Sync status.png"),
                ),
                Branch(
                    "Si se registrarán varios animales",
                    "Completar y registrar el grupo",
                    0,
                    named("android", "20 Bulk registration.png"),
                    True,
                ),
            ),
        ),
        Flow(
            "user-flow-04-consultar-actualizar-animal",
            (
                ScreenNode("Buscar animal", named("android", "02 Animals.png")),
                ScreenNode("Revisar detalle", named("android", "07 Animal detail.png")),
                ScreenNode("Editar y guardar", named("android", "19 Edit animal.png")),
            ),
            ("Abrir Animals", "Seleccionar resultado", "Editar y guardar datos", "Cambios guardados"),
            (
                Branch(
                    "Si la búsqueda no devuelve resultados",
                    "Ajustar o limpiar la búsqueda",
                    0,
                    android_screen("rancher", 12),
                ),
                Branch(
                    "Si el recurso es de solo lectura",
                    "Consultar o recuperar el permiso",
                    1,
                    named("android", "07 Animal detail.png"),
                ),
                Branch(
                    "Si existe un conflicto de sincronización",
                    "Elegir la versión que se conservará",
                    2,
                    named("android", "11 Sync status.png"),
                ),
            ),
        ),
        Flow(
            "user-flow-05-historial-sanitario",
            (
                ScreenNode("Seleccionar paciente", named("flutter", "07 Animal detail.png")),
                ScreenNode("Abrir Health history", flutter_screen("rancher", 17)),
                ScreenNode("Revisar registro", flutter_screen("vet", 60)),
            ),
            ("Abrir paciente", "Ver historial", "Elegir registro sanitario", "Detalle consultado"),
            (
                Branch(
                    "Si el animal no tiene registros",
                    "Registrar el primer evento sanitario",
                    1,
                    android_screen("rancher", 14),
                ),
                Branch(
                    "Si el acceso fue revocado",
                    "Solicitar acceso nuevamente",
                    0,
                    android_screen("vet", 60),
                ),
                Branch(
                    "Si se consulta sin conexión",
                    "Consultar la copia local",
                    1,
                    android_screen("vet", 59),
                    True,
                ),
            ),
        ),
        Flow(
            "user-flow-06-registrar-evento-sanitario",
            (
                ScreenNode("Abrir paciente", named("android", "07 Animal detail.png")),
                ScreenNode("Registrar evento", android_screen("vet", 61)),
                ScreenNode("Confirmar en historial", android_screen("vet", 63)),
            ),
            ("Abrir paciente", "Elegir acción sanitaria", "Guardar datos del evento", "Evento registrado"),
            (
                Branch(
                    "Si los datos están incompletos",
                    "Corregir y volver a guardar",
                    1,
                    android_screen("vet", 62),
                ),
                Branch(
                    "Si no hay conexión o se pierde el permiso",
                    "Sincronizar o restablecer el acceso",
                    1,
                    android_screen("vet", 82),
                ),
                Branch(
                    "Si se requiere seguimiento",
                    "Programar la actividad posterior",
                    2,
                    android_screen("vet", 67),
                    True,
                ),
            ),
        ),
    ]


def main() -> None:
    """Genera todos los user flows e imprime la ruta de cada PNG."""
    all_flows = flows()
    for flow in all_flows:
        build(flow)
        print(OUTPUT / f"{flow.slug}.png")
    print(f"Diagramas generados: {len(all_flows)}")


if __name__ == "__main__":
    main()
