from __future__ import annotations

from html import escape
from pathlib import Path
from textwrap import wrap


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "markdown" / "assets" / "chapter-2" / "strategic-ddd"
OUTPUT.mkdir(parents=True, exist_ok=True)

COLORS = {
    "navy": "#17365D",
    "blue": "#5B9BD5",
    "blue_light": "#DDEBF7",
    "orange": "#F4B183",
    "orange_light": "#FCE4D6",
    "green": "#70AD47",
    "green_light": "#E2F0D9",
    "purple": "#A64D79",
    "purple_light": "#E4DFEC",
    "yellow": "#FFD966",
    "yellow_light": "#FFF2CC",
    "pink": "#FF99CC",
    "gray": "#E7E6E6",
    "gray_dark": "#595959",
    "red": "#C00000",
    "white": "#FFFFFF",
}


def lines(text: str, width: int) -> list[str]:
    result: list[str] = []
    for paragraph in text.split("\n"):
        result.extend(wrap(paragraph, width=width, break_long_words=False) or [""])
    return result


class Svg:
    def __init__(self, width: int, height: int, title: str):
        self.width = width
        self.height = height
        self.parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
            f"<title>{escape(title)}</title>",
            "<defs>",
            '<filter id="shadow" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="3" stdDeviation="4" flood-opacity="0.18"/></filter>',
            '<marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L0,6 L9,3 z" fill="#595959"/></marker>',
            "</defs>",
            f'<rect width="{width}" height="{height}" fill="#FAFAFA"/>',
        ]

    def rect(self, x, y, w, h, fill, stroke="#BFBFBF", radius=12, shadow=False, sw=2):
        filt = ' filter="url(#shadow)"' if shadow else ""
        self.parts.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{filt}/>'
        )

    def text(self, x, y, value, size=18, weight="normal", fill="#1F1F1F", anchor="start", italic=False):
        style = "italic" if italic else "normal"
        self.parts.append(
            f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" font-weight="{weight}" font-style="{style}" fill="{fill}" text-anchor="{anchor}">{escape(value)}</text>'
        )

    def multiline(self, x, y, value, width=28, size=17, weight="normal", fill="#1F1F1F", anchor="start", line_height=None):
        line_height = line_height or int(size * 1.28)
        for index, line in enumerate(lines(value, width)):
            self.text(x, y + index * line_height, line, size=size, weight=weight, fill=fill, anchor=anchor)

    def path(self, d, stroke="#595959", sw=2, dash=None, arrow=True):
        dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
        marker = ' marker-end="url(#arrow)"' if arrow else ""
        self.parts.append(f'<path d="{d}" fill="none" stroke="{stroke}" stroke-width="{sw}"{dash_attr}{marker}/>' )

    def line(self, x1, y1, x2, y2, stroke="#595959", sw=2, dash=None, arrow=True):
        self.path(f"M{x1},{y1} L{x2},{y2}", stroke=stroke, sw=sw, dash=dash, arrow=arrow)

    def save(self, name: str):
        self.parts.append("</svg>")
        (OUTPUT / name).write_text("\n".join(self.parts), encoding="utf-8")


def title(svg: Svg, heading: str, subtitle: str):
    svg.text(50, 48, heading, size=30, weight="bold", fill=COLORS["navy"])
    svg.text(50, 78, subtitle, size=16, fill=COLORS["gray_dark"])


def draw_eventstorming_overview():
    svg = Svg(1800, 760, "EventStorming móvil actualizado de AniTec")
    title(svg, "EventStorming móvil actualizado — AniTec", "Síntesis del flujo principal validado contra el Product Backlog móvil")
    phases = [
        ("Acceso", "Usuario registrado\nSesión iniciada", "Registrar usuario\nIniciar sesión", "Ganadero / Veterinario"),
        ("Gestión del hato", "Finca registrada\nAnimal registrado\nAnimal identificado", "Registrar finca\nRegistrar animal\nEscanear QR", "Ganadero"),
        ("Sanidad y colaboración", "Acceso veterinario concedido\nIncidencia registrada\nAtención registrada", "Autorizar veterinario\nRegistrar incidencia\nRegistrar atención", "Ganadero / Veterinario"),
        ("Trabajo de campo", "Actividad programada\nOperación guardada localmente\nDatos sincronizados", "Programar control\nGuardar sin conexión\nSincronizar cambios", "Ganadero / Veterinario"),
        ("Valor y sostenibilidad", "Indicadores generados\nCheckout iniciado\nSuscripción activada", "Consultar indicadores\nSeleccionar plan\nConfirmar pago", "Usuario autenticado"),
    ]
    card_w, gap, start_x = 310, 30, 50
    centers = []
    for i, (phase, events, commands, actors) in enumerate(phases):
        x = start_x + i * (card_w + gap)
        centers.append(x + card_w / 2)
        svg.rect(x, 110, card_w, 46, COLORS["navy"], stroke=COLORS["navy"], radius=8)
        svg.text(x + card_w / 2, 140, phase, size=19, weight="bold", fill=COLORS["white"], anchor="middle")
        svg.rect(x, 180, card_w, 120, COLORS["blue_light"], stroke=COLORS["blue"], radius=8)
        svg.text(x + 15, 207, "COMMANDS", size=15, weight="bold", fill=COLORS["navy"])
        svg.multiline(x + 15, 234, commands, width=31, size=16)
        svg.rect(x, 325, card_w, 120, COLORS["orange_light"], stroke=COLORS["orange"], radius=8)
        svg.text(x + 15, 352, "DOMAIN EVENTS", size=15, weight="bold", fill="#8A3B12")
        svg.multiline(x + 15, 379, events, width=31, size=16)
        svg.rect(x, 470, card_w, 78, COLORS["yellow_light"], stroke=COLORS["yellow"], radius=8)
        svg.text(x + 15, 497, "ACTOR", size=15, weight="bold", fill="#7F6000")
        svg.multiline(x + 15, 523, actors, width=31, size=16)
        if i < len(phases) - 1:
            svg.line(x + card_w, 385, x + card_w + gap - 5, 385, stroke=COLORS["gray_dark"], sw=3)
    svg.rect(50, 585, 1660, 115, COLORS["purple_light"], stroke=COLORS["purple"], radius=8)
    svg.text(70, 616, "POLICIES AND HOTSPOTS", size=16, weight="bold", fill=COLORS["purple"])
    svg.multiline(70, 645, "Cuando se programa un control, se genera un recordatorio. Cuando no existe conexión, la operación queda pendiente y se sincroniza después. Cuando Stripe confirma el pago, se activa la suscripción. Hotspots: códigos duplicados, acceso veterinario vencido, conflictos de sincronización y pagos no confirmados.", width=155, size=17)
    svg.save("eventstorming-mobile-overview.svg")


def draw_candidate_contexts():
    svg = Svg(1500, 900, "Candidate Context Discovery de AniTec")
    title(svg, "Candidate Context Discovery — AniTec", "Resultado de Start-with-Value y búsqueda de pivotal events")
    columns = [
        ("CORE DOMAIN", COLORS["green"], [
            ("Livestock Management", "Animal registered · Animal identified"),
            ("Sanitary Management", "Health event recorded · Care registered"),
            ("Veterinary Collaboration", "Veterinary access granted · Access revoked"),
        ]),
        ("SUPPORTING SUBDOMAINS", COLORS["blue"], [
            ("Profile Management", "Profile created · Role details updated"),
            ("Activity Management", "Activity scheduled · Reminder handled"),
            ("Financial Management", "Financial movement recorded"),
            ("Subscription Management", "Payment confirmed · Subscription activated"),
            ("Analytics and Reporting", "Indicators generated"),
        ]),
        ("GENERIC SUBDOMAIN", COLORS["purple"], [
            ("Identity and Access Management", "User registered · Session issued"),
        ]),
    ]
    col_w, gap, start_x = 440, 40, 50
    for col_i, (name, color, contexts) in enumerate(columns):
        x = start_x + col_i * (col_w + gap)
        svg.rect(x, 110, col_w, 55, color, stroke=color, radius=8)
        svg.text(x + col_w / 2, 145, name, size=18, weight="bold", fill=COLORS["white"], anchor="middle")
        y = 190
        for context, events in contexts:
            svg.rect(x, y, col_w, 108, COLORS["white"], stroke=color, radius=10, shadow=True)
            svg.text(x + 20, y + 32, context, size=18, weight="bold", fill=COLORS["navy"])
            svg.multiline(x + 20, y + 62, events, width=48, size=15, fill=COLORS["gray_dark"])
            y += 125
    svg.rect(50, 825, 1400, 48, COLORS["gray"], stroke="#BFBFBF", radius=6)
    svg.text(750, 856, "Capacidades técnicas transversales: almacenamiento offline, sincronización, QR/ML Kit, notificaciones y distribución móvil.", size=16, anchor="middle")
    svg.save("candidate-context-discovery.svg")


FLOW_COLORS = {"actor": COLORS["yellow_light"], "command": COLORS["blue_light"], "context": COLORS["green_light"], "event": COLORS["orange_light"], "external": "#F4CCCC", "local": COLORS["purple_light"]}


def draw_flow(filename: str, heading: str, subtitle: str, steps: list[tuple[str, str, str]], messages: list[str]):
    width = max(1500, 80 + len(steps) * 215)
    svg = Svg(width, 500, heading)
    title(svg, heading, subtitle)
    x_positions = []
    for i, (kind, name, detail) in enumerate(steps):
        x = 45 + i * 215
        x_positions.append(x)
        fill = FLOW_COLORS[kind]
        stroke = {"actor": COLORS["yellow"], "command": COLORS["blue"], "context": COLORS["green"], "event": COLORS["orange"], "external": COLORS["red"], "local": COLORS["purple"]}[kind]
        svg.rect(x, 145, 175, 165, fill, stroke=stroke, radius=12, shadow=True)
        svg.text(x + 87.5, 174, kind.upper(), size=13, weight="bold", fill=stroke, anchor="middle")
        svg.multiline(x + 87.5, 207, name, width=18, size=17, weight="bold", fill=COLORS["navy"], anchor="middle")
        svg.multiline(x + 87.5, 265, detail, width=22, size=14, fill=COLORS["gray_dark"], anchor="middle")
        if i:
            previous_x = x_positions[i - 1]
            svg.line(previous_x + 175, 226, x - 6, 226, sw=2.5)
            if i - 1 < len(messages):
                svg.multiline((previous_x + 175 + x) / 2, 122, messages[i - 1], width=22, size=13, weight="bold", fill=COLORS["gray_dark"], anchor="middle")
    svg.rect(45, 350, width - 90, 95, COLORS["white"], stroke="#BFBFBF", radius=8)
    svg.text(65, 380, "LECTURA DEL FLUJO", size=14, weight="bold", fill=COLORS["navy"])
    svg.multiline(65, 408, subtitle, width=max(100, int((width - 140) / 9)), size=16)
    svg.save(filename)


def draw_domain_message_flows():
    draw_flow(
        "domain-flow-01-register-animal.svg",
        "Domain Story 1 — Registro móvil de un animal",
        "El registro se confirma en el dominio cuando existe conexión; si la red falla, la aplicación conserva el comando con un identificador idempotente y lo envía posteriormente.",
        [("actor", "Ganadero", "Trabaja desde el campo"), ("command", "Registrar animal", "Datos y finca"), ("local", "Mobile Sync Queue", "Guarda operación pendiente"), ("context", "Livestock Management", "Valida propiedad y código"), ("event", "Animal registered", "AnimalId asignado"), ("context", "Analytics", "Actualiza indicadores")],
        ["solicita", "persistLocal(commandId)", "POST /animals", "publica", "consume evento"],
    )
    draw_flow(
        "domain-flow-02-identify-qr.svg",
        "Domain Story 2 — Identificación de un animal mediante QR",
        "La cámara y ML Kit interpretan el QR en el dispositivo. Livestock Management resuelve el identificador y aplica autorización; la búsqueda manual mantiene el flujo disponible si el escaneo falla.",
        [("actor", "Usuario autorizado", "Ganadero o veterinario"), ("command", "Escanear QR", "Solicita usar cámara"), ("local", "ML Kit Barcode Scanning", "Decodifica en el dispositivo"), ("context", "Livestock Management", "Resuelve AnimalId"), ("event", "Animal identified", "Acceso autorizado"), ("command", "Consultar ficha", "Muestra datos permitidos")],
        ["inicia", "envía imagen", "resolve(animalCode)", "publica", "habilita"],
    )
    draw_flow(
        "domain-flow-03-health-follow-up.svg",
        "Domain Story 3 — Incidencia y seguimiento sanitario",
        "El ganadero registra la incidencia, Sanitary Management incorpora el evento al historial y Activity Management programa el seguimiento y la notificación correspondiente.",
        [("actor", "Ganadero", "Detecta una incidencia"), ("command", "Registrar incidencia", "Animal y observación"), ("context", "Sanitary Management", "Valida animal y autoría"), ("event", "Health event recorded", "Historial actualizado"), ("context", "Activity Management", "Programa próximo control"), ("event", "Reminder scheduled", "Notificación pendiente")],
        ["solicita", "envía comando", "publica", "consume evento", "publica"],
    )
    draw_flow(
        "domain-flow-04-veterinary-care.svg",
        "Domain Story 4 — Autorización y atención veterinaria",
        "Veterinary Collaboration decide el alcance del acceso. Sanitary Management solo entrega antecedentes y acepta la atención cuando la autorización permanece vigente.",
        [("actor", "Ganadero", "Controla el acceso"), ("command", "Autorizar veterinario", "Solicitud aceptada"), ("context", "Veterinary Collaboration", "Crea autorización vigente"), ("event", "Veterinary access granted", "Cliente disponible"), ("actor", "Veterinario", "Consulta antecedentes"), ("context", "Sanitary Management", "Valida permiso y registra atención"), ("event", "Veterinary care recorded", "Autoría trazable")],
        ["decide", "envía comando", "publica", "habilita", "consulta/crea", "publica"],
    )
    draw_flow(
        "domain-flow-05-offline-sync.svg",
        "Domain Story 5 — Sincronización y resolución de conflictos",
        "La sincronización es una responsabilidad de infraestructura móvil. Cada comando conserva identidad, versión y fecha; el contexto propietario decide si aplica, rechaza o devuelve un conflicto para resolución.",
        [("actor", "Usuario móvil", "Trabaja sin conexión"), ("command", "Guardar operación", "CommandId y versión"), ("local", "Local Database", "Estado Pending"), ("local", "Sync Worker", "Detecta conexión"), ("context", "Contexto propietario", "Valida idempotencia y versión"), ("event", "Data synchronized", "Estado Synced o Conflict"), ("actor", "Usuario móvil", "Revisa el resultado")],
        ["solicita", "persiste", "entrega pendientes", "HTTPS/JSON", "responde", "notifica estado"],
    )
    draw_flow(
        "domain-flow-06-subscription.svg",
        "Domain Story 6 — Suscripción y pago con Stripe",
        "Subscription Management traduce el modelo interno a Stripe mediante una Anti-Corruption Layer. La suscripción se activa únicamente después de validar la sesión de pago en el backend.",
        [("actor", "Usuario autenticado", "Selecciona un plan"), ("command", "Iniciar checkout", "PlanId y UserId"), ("context", "Subscription Management", "Crea intención de pago"), ("external", "Stripe Checkout", "Procesa el pago"), ("context", "Stripe ACL", "Valida resultado externo"), ("event", "Subscription activated", "Pago confirmado"), ("actor", "Usuario", "Consulta el estado")],
        ["solicita", "crea sesión", "redirect/checkout", "retorno/webhook", "publica", "informa"],
    )


CANVASES = {
    "iam": {
        "name": "Identity and Access Management", "classification": "Generic subdomain · Custom built", "purpose": "Autenticar usuarios, emitir sesiones y aplicar autorización por rol.", "roles": "Identity provider · Policy and execution context",
        "language": "User, Role, Credentials, Session, Access Token", "rules": "Correo único; contraseña protegida; sesión expirable; autorización por rol y relación.",
        "inbound": "SignUp, SignIn, SignOut, ValidateAccess", "outbound": "UserRegistered, SessionIssued, SessionExpired, AccessDenied", "dependencies": "No depende de modelos internos de otros contextos.",
        "assumptions": "Los usuarios disponen de un correo válido y protegen sus credenciales.", "metrics": "Registro exitoso; tasa de login; accesos rechazados; expiración correcta.", "questions": "¿Se requerirá recuperación de contraseña o autenticación multifactor?",
    },
    "profiles": {
        "name": "Profile Management", "classification": "Supporting subdomain · Custom built", "purpose": "Mantener datos personales y profesionales asociados con una identidad.", "roles": "Master data and execution context",
        "language": "Profile, Rancher, Veterinarian, Contact Information", "rules": "Una identidad posee un perfil; el rol no cambia sin validación; datos de contacto normalizados.",
        "inbound": "CreateProfile, UpdateProfile, GetProfile", "outbound": "ProfileCreated, ProfileUpdated, ProfileSummary", "dependencies": "IAM publica UserId y Role mediante un contrato estable.",
        "assumptions": "Los datos mínimos difieren entre ganadero y veterinario.", "metrics": "Perfiles completos; actualizaciones válidas; consistencia UserId/ProfileId.", "questions": "¿Qué credencial profesional será obligatoria para veterinarios?",
    },
    "livestock": {
        "name": "Livestock Management", "classification": "Core domain · Revenue · Custom built", "purpose": "Gestionar fincas, hatos, animales e identificación individual desde el campo.", "roles": "Core execution context",
        "language": "Farm, Herd, Animal, Animal Code, QR Identifier, Traceability", "rules": "Código único por propietario; animal asociado con una finca; archivado conserva historial.",
        "inbound": "RegisterFarm, RegisterAnimal, UpdateAnimal, IdentifyAnimal", "outbound": "FarmRegistered, AnimalRegistered, AnimalUpdated, AnimalIdentified", "dependencies": "Profiles identifica al propietario; publica AnimalId a Sanitary, Activities y Analytics.",
        "assumptions": "El usuario puede operar con conectividad intermitente y utilizar QR o búsqueda manual.", "metrics": "Animales registrados; tiempo de identificación; duplicados rechazados; sincronizaciones.", "questions": "¿Qué formato físico y esquema de códigos QR se adoptará?",
    },
    "sanitary": {
        "name": "Sanitary Management", "classification": "Core domain · Custom built", "purpose": "Mantener un historial sanitario trazable de incidencias, diagnósticos, tratamientos y controles.", "roles": "Core execution and record context",
        "language": "Health Event, Diagnosis, Treatment, Veterinary Care, Health History", "rules": "No elimina historia; correcciones trazables; atención veterinaria exige autorización vigente.",
        "inbound": "RecordIncident, RecordCare, CorrectHealthEvent, GetHealthHistory", "outbound": "HealthEventRecorded, CareRecorded, FollowUpRequired", "dependencies": "Livestock valida AnimalId; Veterinary Collaboration confirma autorización.",
        "assumptions": "Ganaderos y veterinarios registran información durante o inmediatamente después de la atención.", "metrics": "Eventos completos; seguimientos programados; tiempo de registro; conflictos resueltos.", "questions": "¿Qué campos clínicos serán obligatorios por tipo de atención?",
    },
    "collaboration": {
        "name": "Veterinary Collaboration", "classification": "Core domain · Custom built", "purpose": "Controlar la relación autorizada entre ganaderos, veterinarios, clientes y pacientes.", "roles": "Coordination and policy context",
        "language": "Access Request, Veterinary Authorization, Client, Patient, Access Scope", "rules": "El ganadero concede y revoca; acceso limitado a animales autorizados; revocación inmediata.",
        "inbound": "RequestAccess, GrantAccess, RejectAccess, RevokeAccess, GetAuthorizedPatients", "outbound": "AccessRequested, AccessGranted, AccessRejected, AccessRevoked", "dependencies": "Profiles valida roles; Livestock publica propietario y animales.",
        "assumptions": "El ganadero conoce al veterinario antes de conceder acceso.", "metrics": "Solicitudes resueltas; accesos vigentes; consultas rechazadas; revocaciones efectivas.", "questions": "¿La autorización será global por finca o granular por animal?",
    },
    "activities": {
        "name": "Activity Management", "classification": "Supporting subdomain · Custom built", "purpose": "Planificar actividades, controles y recordatorios y registrar su atención.", "roles": "Planning and execution context",
        "language": "Farm Activity, Due Date, Reminder, Activity Status, Reschedule", "rules": "Actividad con responsable y fecha; estados válidos; reprogramación conserva trazabilidad.",
        "inbound": "ScheduleActivity, CompleteActivity, RescheduleActivity, ListPendingActivities", "outbound": "ActivityScheduled, ActivityCompleted, ActivityRescheduled, ReminderDue", "dependencies": "Recibe referencias de Livestock y eventos de seguimiento desde Sanitary.",
        "assumptions": "Los usuarios autorizan notificaciones o consultan su lista de pendientes.", "metrics": "Actividades atendidas a tiempo; recordatorios entregados; reprogramaciones.", "questions": "¿Se usarán notificaciones locales, push o una combinación?",
    },
    "financial": {
        "name": "Financial Management", "classification": "Supporting subdomain · Custom built", "purpose": "Registrar ingresos y egresos operativos para ofrecer visibilidad económica básica.", "roles": "Supporting execution context",
        "language": "Financial Movement, Income, Expense, Category, Balance", "rules": "Monto positivo; tipo ingreso/egreso; propietario autorizado; correcciones auditables.",
        "inbound": "RecordIncome, RecordExpense, UpdateMovement, GetFinancialSummary", "outbound": "FinancialMovementRecorded, FinancialMovementUpdated", "dependencies": "Profiles identifica al propietario; Analytics consume resúmenes publicados.",
        "assumptions": "El alcance inicial no reemplaza un sistema contable formal.", "metrics": "Movimientos mensuales; registros completos; conciliaciones de balance.", "questions": "¿Se requerirán monedas, comprobantes o exportación tributaria?",
    },
    "subscriptions": {
        "name": "Subscription Management", "classification": "Supporting subdomain · Stripe integration", "purpose": "Administrar planes, checkout, pagos confirmados y estado de suscripción.", "roles": "Gateway and policy context",
        "language": "Subscription Plan, Checkout Session, Payment, Active Subscription", "rules": "El backend verifica Stripe; no almacena tarjeta; pago confirmado activa la suscripción.",
        "inbound": "SelectPlan, StartCheckout, ConfirmCheckout, GetSubscription", "outbound": "CheckoutStarted, PaymentConfirmed, SubscriptionActivated, PaymentFailed", "dependencies": "IAM aporta UserId; Stripe se integra mediante Anti-Corruption Layer.",
        "assumptions": "Stripe opera inicialmente en modo de prueba y retorna un identificador verificable.", "metrics": "Checkouts iniciados; pagos confirmados; fallos; activaciones consistentes.", "questions": "¿La renovación será automática y qué política de cancelación se aplicará?",
    },
    "analytics": {
        "name": "Analytics and Reporting", "classification": "Supporting subdomain · Engagement", "purpose": "Construir indicadores operativos, sanitarios y financieros para cada rol.", "roles": "Analysis and read-model context",
        "language": "Indicator, Dashboard, Health Summary, Financial Summary, Time Range", "rules": "Solo datos autorizados; indicadores reproducibles; periodo explícito; fuentes trazables.",
        "inbound": "GetRancherIndicators, GetVeterinarianIndicators, RefreshReadModel", "outbound": "IndicatorsGenerated, DashboardReadModelUpdated", "dependencies": "Consume contratos publicados por Livestock, Sanitary, Activities y Financial.",
        "assumptions": "Los contextos fuente mantienen identificadores y fechas consistentes.", "metrics": "Tiempo de respuesta; consistencia con fuentes; consultas por rol.", "questions": "¿Se calcularán indicadores bajo demanda o mediante proyecciones asíncronas?",
    },
}

CANVAS_VISUALS = {
    "iam": {"domain": "Generic", "business": "Enabler", "evolution": "Custom built", "actor": "Mobile User", "downstream": "Profiles / Subscriptions", "reads": ["Account Status", "Role Catalog"], "incoming": ["Access Requested"]},
    "profiles": {"domain": "Supporting", "business": "Engagement", "evolution": "Custom built", "actor": "Authenticated User", "downstream": "Livestock / Collaboration", "reads": ["Current Profile", "Role Details"], "incoming": ["User Registered"]},
    "livestock": {"domain": "Core", "business": "Revenue", "evolution": "Custom built", "actor": "Rancher / Authorized Veterinarian", "downstream": "Sanitary / Activities / Analytics", "reads": ["Farm List", "Animal List", "Animal Detail"], "incoming": ["Profile Created"]},
    "sanitary": {"domain": "Core", "business": "Revenue / Retention", "evolution": "Custom built", "actor": "Rancher / Authorized Veterinarian", "downstream": "Activities / Analytics", "reads": ["Health History", "Authorized Patients", "Pending Follow-ups"], "incoming": ["Animal Registered", "Access Granted"]},
    "collaboration": {"domain": "Core", "business": "Differentiation", "evolution": "Custom built", "actor": "Rancher / Veterinarian", "downstream": "Sanitary Management", "reads": ["Veterinarian Directory", "Access Requests", "Authorized Clients"], "incoming": ["Profile Updated", "Animal Registered"]},
    "activities": {"domain": "Supporting", "business": "Engagement", "evolution": "Custom built", "actor": "Rancher / Veterinarian", "downstream": "Analytics / Notification Provider", "reads": ["Pending Activities", "Calendar", "Reminder Status"], "incoming": ["Follow-up Required"]},
    "financial": {"domain": "Supporting", "business": "Engagement", "evolution": "Custom built", "actor": "Rancher", "downstream": "Analytics and Reporting", "reads": ["Financial Summary", "Movement List", "Category Catalog"], "incoming": ["Profile Created"]},
    "subscriptions": {"domain": "Supporting", "business": "Revenue", "evolution": "Buy and integrate", "actor": "Authenticated User", "downstream": "IAM / Mobile Applications", "reads": ["Plan Catalog", "Subscription Status", "Payment Status"], "incoming": ["User Registered", "Stripe Result"]},
    "analytics": {"domain": "Supporting", "business": "Engagement", "evolution": "Custom built", "actor": "Rancher / Veterinarian", "downstream": "Rancher / Veterinarian", "reads": ["Dashboard", "Date Range", "Authorized Scope"], "incoming": ["Livestock Updated", "Health Event Recorded", "Financial Movement Recorded"]},
}


def sticky(svg: Svg, x: int, y: int, w: int, h: int, value: str, fill: str, stroke: str, chars: int = 18, size: int = 12):
    svg.rect(x, y, w, h, fill, stroke=stroke, radius=1, shadow=True, sw=1)
    wrapped = lines(value, chars)
    start_y = y + h / 2 - ((len(wrapped) - 1) * size * 0.62) + 4
    for index, line in enumerate(wrapped):
        svg.text(x + w / 2, start_y + index * int(size * 1.22), line, size=size, fill="#404040", anchor="middle")


def bullet_text(svg: Svg, x: int, y: int, value: str, chars: int, size: int = 13):
    items = [item.strip().rstrip(".") for item in value.replace(". ", "; ").split(";") if item.strip()]
    cursor = y
    for item in items:
        wrapped = lines(item, chars)
        for index, line in enumerate(wrapped):
            prefix = "• " if index == 0 else "  "
            svg.text(x, cursor, prefix + line, size=size, fill="#333333")
            cursor += int(size * 1.28)
        cursor += 5


def draw_canvas(key: str, data: dict[str, str]):
    visual = CANVAS_VISUALS[key]
    svg = Svg(1600, 1300, f"Bounded Context Canvas — {data['name']}")
    svg.parts[-1] = '<rect width="1600" height="1300" fill="#C9C9C9"/>'
    svg.rect(22, 22, 1556, 1238, COLORS["white"], stroke="#555555", radius=0, sw=2)

    # Header: name and template version.
    svg.line(22, 112, 1578, 112, stroke="#555555", sw=2, arrow=False)
    svg.line(1060, 22, 1060, 112, stroke="#555555", sw=2, arrow=False)
    svg.text(38, 77, "Name", size=27, weight="bold")
    svg.text(145, 77, data["name"], size=27, fill="#666666")
    svg.multiline(1078, 56, "Version based on:\nDDD Crew Bounded Context Canvas v5", width=40, size=15, fill="#404040")

    # Purpose, strategic classification, and domain roles.
    svg.line(22, 350, 1578, 350, stroke="#555555", sw=2, arrow=False)
    svg.line(495, 112, 495, 350, stroke="#555555", sw=2, arrow=False)
    svg.line(1060, 112, 1060, 350, stroke="#555555", sw=2, arrow=False)
    svg.text(38, 152, "Purpose", size=26, weight="bold")
    svg.multiline(50, 205, data["purpose"], width=48, size=16, fill="#6A6A6A", line_height=22)
    svg.text(515, 152, "Strategic Classification", size=26, weight="bold")
    for x, label, value in [(530, "Domain:", visual["domain"]), (700, "Business Model:", visual["business"]), (890, "Evolution:", visual["evolution"])]:
        svg.text(x, 232, label, size=16, weight="bold", fill="#777777")
        svg.multiline(x, 258, "- " + value, width=20, size=15, fill="#777777")
    svg.text(1080, 152, "Domain Roles", size=26, weight="bold")
    svg.text(1090, 232, "Role types:", size=16, weight="bold", fill="#777777")
    svg.multiline(1090, 258, "- " + data["roles"], width=45, size=15, fill="#777777")

    # Communication canvas.
    svg.line(22, 925, 1578, 925, stroke="#555555", sw=2, arrow=False)
    svg.text(35, 390, "Inbound Communication", size=25, weight="bold")
    svg.text(1120, 390, "Outbound Communication", size=25, weight="bold")

    commands = [item.strip() for item in data["inbound"].split(",")]
    for index, value in enumerate(visual["reads"][:3]):
        sticky(svg, 70, 455 + index * 105, 125, 82, value, "#B7E66B", "#9BBB59")
    for index, value in enumerate(commands[:4]):
        sticky(svg, 225, 425 + index * 105, 135, 82, value, "#A9C9F5", "#7EA6D8")
    for index, value in enumerate(visual["incoming"][:3]):
        sticky(svg, 400, 485 + index * 115, 125, 82, value, COLORS["orange_light"], COLORS["orange"])

    outbound = [item.strip() for item in data["outbound"].split(",")]
    for index, value in enumerate(outbound[:4]):
        sticky(svg, 1290, 425 + index * 105, 135, 82, value, COLORS["orange_light"], COLORS["orange"])

    # Center: ubiquitous language and business decisions.
    svg.rect(565, 375, 470, 510, "#FCFCFC", stroke="#777777", radius=0, sw=2)
    svg.text(800, 420, "Ubiquitous Language", size=25, weight="bold", anchor="middle")
    svg.text(800, 445, "Context-specific terminology", size=13, fill="#777777", anchor="middle")
    language = [item.strip() for item in data["language"].split(",")]
    for index, value in enumerate(language[:6]):
        col, row = index % 2, index // 2
        sticky(svg, 605 + col * 205, 470 + row * 72, 185, 54, value, "#F2F2F2", "#999999", chars=23, size=11)
    svg.text(800, 700, "Business Decisions", size=25, weight="bold", anchor="middle")
    svg.text(800, 725, "Key business rules, policies, and decisions", size=13, fill="#777777", anchor="middle")
    decisions = [item.strip() for item in data["rules"].split(";") if item.strip()]
    for index, value in enumerate(decisions[:4]):
        col, row = index % 2, index // 2
        sticky(svg, 605 + col * 205, 750 + row * 72, 185, 58, value, "#C9B5F4", "#A58AD8", chars=24, size=10)

    # Actor and downstream arrows.
    svg.parts.append('<polygon points="70,840 350,840 350,812 510,865 350,918 350,890 70,890" fill="#F7F7F7" stroke="#BFBFBF" stroke-width="2"/>')
    svg.text(270, 871, visual["actor"], size=14, fill="#777777", anchor="middle")
    svg.parts.append('<polygon points="1090,840 1370,840 1370,812 1530,865 1370,918 1370,890 1090,890" fill="#F7F7F7" stroke="#BFBFBF" stroke-width="2"/>')
    svg.text(1290, 871, visual["downstream"], size=14, fill="#777777", anchor="middle")

    # Assumptions, metrics, and open questions.
    svg.line(510, 925, 510, 1215, stroke="#555555", sw=2, arrow=False)
    svg.line(1050, 925, 1050, 1215, stroke="#555555", sw=2, arrow=False)
    svg.text(38, 968, "Assumptions", size=25, weight="bold")
    svg.text(530, 968, "Verification Metrics", size=25, weight="bold")
    svg.text(1070, 968, "Open Questions", size=25, weight="bold")
    bullet_text(svg, 42, 1010, data["assumptions"], chars=58, size=13)
    bullet_text(svg, 530, 1010, data["metrics"], chars=59, size=13)
    bullet_text(svg, 1070, 1010, data["questions"], chars=58, size=13)

    svg.line(22, 1215, 1578, 1215, stroke="#555555", sw=2, arrow=False)
    svg.text(1560, 1244, "Template Bounded Context Canvas after DDD Crew Version 1", size=11, fill="#666666", anchor="end")
    svg.save(f"bounded-context-canvas-{key}.svg")


def draw_context_map():
    svg = Svg(1800, 1430, "Context Mapping de AniTec")
    title(svg, "Context Mapping — AniTec", "Mapa seleccionado después de comparar alternativas de descomposición")
    nodes = {
        "iam": (70, 120, "IAM", "Generic"),
        "profiles": (380, 120, "Profile Management", "Supporting"),
        "subscriptions": (720, 120, "Subscription Management", "Supporting"),
        "stripe": (1120, 120, "Stripe", "External system"),
        "livestock": (220, 390, "Livestock Management", "Core"),
        "collaboration": (620, 390, "Veterinary Collaboration", "Core"),
        "sanitary": (1050, 390, "Sanitary Management", "Core"),
        "financial": (90, 720, "Financial Management", "Supporting"),
        "activities": (520, 720, "Activity Management", "Supporting"),
        "analytics": (1000, 720, "Analytics and Reporting", "Supporting"),
        "notification": (1440, 720, "Notification Provider", "External/technical"),
    }
    boxes = {}
    for key, (x, y, label, kind) in nodes.items():
        external = "External" in kind
        fill = "#F4CCCC" if external else (COLORS["green_light"] if kind == "Core" else COLORS["blue_light"] if kind == "Supporting" else COLORS["purple_light"])
        stroke = COLORS["red"] if external else (COLORS["green"] if kind == "Core" else COLORS["blue"] if kind == "Supporting" else COLORS["purple"])
        w = 280 if key not in {"stripe", "notification"} else 260
        h = 115
        svg.rect(x, y, w, h, fill, stroke=stroke, radius=12, shadow=True, sw=3)
        svg.multiline(x + w / 2, y + 40, label, width=25, size=18, weight="bold", fill=COLORS["navy"], anchor="middle")
        svg.text(x + w / 2, y + 91, kind, size=14, fill=COLORS["gray_dark"], anchor="middle")
        boxes[key] = (x, y, w, h)

    def badge(x, y, number):
        svg.rect(x - 17, y - 15, 34, 30, COLORS["white"], stroke=COLORS["navy"], radius=15, sw=2)
        svg.text(x, y + 6, str(number), size=14, weight="bold", fill=COLORS["navy"], anchor="middle")

    def connect(a, b, number, y_offset=0, dash=None, route_y=None):
        ax, ay, aw, ah = boxes[a]
        bx, by, bw, bh = boxes[b]
        if route_y is not None:
            x1, y1 = ax + aw / 2, ay + ah
            x2, y2 = bx + bw / 2, by + bh
            svg.path(f"M{x1},{y1} L{x1},{route_y} L{x2},{route_y} L{x2},{y2}", sw=2.2, dash=dash)
            badge((x1 + x2) / 2, route_y, number)
            return
        if abs(ay - by) < 30:
            if bx > ax:
                x1, x2 = ax + aw, bx
            else:
                x1, x2 = ax, bx + bw
            y1 = y2 = ay + ah / 2 + y_offset
        else:
            x1, y1 = ax + aw / 2 + y_offset, ay + ah
            x2, y2 = bx + bw / 2 + y_offset, by
        mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
        svg.path(f"M{x1},{y1} C{mid_x},{y1} {mid_x},{y2} {x2},{y2}", sw=2.2, dash=dash)
        badge(mid_x, mid_y, number)

    connect("iam", "profiles", 1)
    connect("profiles", "livestock", 2, y_offset=-45)
    connect("profiles", "collaboration", 3, y_offset=45)
    connect("iam", "subscriptions", 4, y_offset=-30, route_y=300)
    connect("stripe", "subscriptions", 5)
    connect("livestock", "collaboration", 6, y_offset=-24)
    connect("livestock", "sanitary", 7, y_offset=28, route_y=630)
    connect("collaboration", "sanitary", 8, y_offset=-24)
    connect("livestock", "activities", 9, y_offset=-55)
    connect("sanitary", "activities", 10, y_offset=55)
    connect("financial", "analytics", 11, dash="8 5", route_y=930)
    connect("activities", "analytics", 12, y_offset=-18, dash="8 5")
    connect("sanitary", "analytics", 13, y_offset=35, dash="8 5")
    connect("activities", "notification", 14, y_offset=22, route_y=955)
    connect("livestock", "analytics", 15, dash="8 5", route_y=985)

    relationships = [
        "1. IAM → Profiles: Customer/Supplier + Published Language (UserId, Role).",
        "2. Profiles → Livestock: Open Host Service + Published Language.",
        "3. Profiles → Veterinary Collaboration: Open Host Service + Published Language.",
        "4. IAM → Subscriptions: Open Host Service (UserId y sesión).",
        "5. Stripe ↔ Subscriptions: Anti-Corruption Layer.",
        "6. Livestock → Veterinary Collaboration: Customer/Supplier + Published Language.",
        "7. Livestock → Sanitary: Customer/Supplier + Published Language (AnimalId).",
        "8. Veterinary Collaboration → Sanitary: Customer/Supplier (autorización).",
        "9. Livestock → Activities: Published Language.",
        "10. Sanitary → Activities: Published Language (FollowUpRequired).",
        "11. Financial → Analytics: Conformist read model.",
        "12. Activities → Analytics: Conformist read model.",
        "13. Sanitary → Analytics: Conformist read model.",
        "14. Activities ↔ Notification Provider: Anti-Corruption Layer.",
        "15. Livestock → Analytics: Conformist read model.",
    ]
    svg.rect(70, 1040, 1660, 310, COLORS["white"], stroke="#BFBFBF", radius=8)
    svg.text(95, 1072, "RELACIONES Y PATRONES", size=15, weight="bold", fill=COLORS["navy"])
    for index, relation in enumerate(relationships):
        col = 0 if index < 8 else 1
        row = index if index < 8 else index - 8
        svg.text(95 + col * 810, 1105 + row * 29, relation, size=14, fill=COLORS["gray_dark"])
    svg.text(95, 1392, "Las capacidades offline, sincronización, QR y almacenamiento local pertenecen a la infraestructura móvil y no constituyen bounded contexts.", size=14, weight="bold", fill=COLORS["navy"])
    svg.save("context-map-anitec.svg")


def main():
    draw_eventstorming_overview()
    draw_candidate_contexts()
    draw_domain_message_flows()
    for key, data in CANVASES.items():
        draw_canvas(key, data)
    draw_context_map()
    print(f"Generated {len(list(OUTPUT.glob('*.svg')))} SVG diagrams in {OUTPUT}")


if __name__ == "__main__":
    main()
