from __future__ import annotations

from dataclasses import dataclass
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "markdown" / "content" / "chapter-2"
CODE = ROOT / "markdown" / "assets" / "codefordiagrams"


@dataclass(frozen=True)
class Context:
    number: int
    name: str
    slug: str
    folder: str
    module: str
    purpose: str
    existing_domain: tuple[str, ...]
    proposed_domain: tuple[str, ...]
    controllers: tuple[str, ...]
    resources: tuple[str, ...]
    app_services: tuple[str, ...]
    commands_queries: tuple[str, ...]
    repository: str
    aggregate: str
    capability: str
    integration: str
    externals: tuple[str, ...]
    puml_body: str
    server_erd: str
    local_entities: tuple[tuple[str, tuple[tuple[str, str], ...]], ...]


CONTEXTS = (
    Context(
        1,
        "Identity and Access Management",
        "identity-and-access-management",
        "2.6.1. Bounded Context Identity and Access Management",
        "Iam",
        "Administrar identidades, credenciales, roles y sesiones para que cada operación de AniTec se ejecute con una identidad autenticada y autorizada.",
        ("User", "IamError", "IUserRepository"),
        ("UserRole", "CredentialPolicy", "AuthenticatedSession"),
        ("AuthenticationController", "UsersController"),
        ("SignInResource", "SignUpResource", "AuthenticatedUserResource", "UserResource"),
        ("UserCommandService", "UserQueryService", "IamContextFacade"),
        ("SignInCommand", "SignUpCommand", "GetUserByIdQuery", "GetUserByUsernameQuery"),
        "UserRepository",
        "User",
        "registro, inicio de sesión, emisión y validación de JWT",
        "BCrypt, JWT y almacenamiento seguro del dispositivo",
        ("Profiles Context",),
        r'''
class User <<Aggregate Root>> {
  -id: int
  -username: string
  -passwordHash: string
  -fullName: string
  -role: UserRole
  +UpdateUsername(username: string): User
  +UpdatePasswordHash(hash: string): User
  +UpdateProfile(fullName: string, role: UserRole): User
}
enum UserRole {
  Rancher
  Veterinarian
  Administrator
}
class AuthenticatedSession <<Entity - target>> {
  -userId: int
  -tokenReference: string
  -expiresAt: DateTime
  +IsExpired(now: DateTime): bool
  +Revoke(): void
}
class CredentialPolicy <<Domain Service - target>> {
  +ValidateUsername(username: string): bool
  +ValidatePassword(password: string): bool
}
interface IUserRepository {
  +FindById(id: int): User?
  +FindByUsername(username: string): User?
  +Add(user: User): void
}
User --> UserRole : has
AuthenticatedSession --> User : belongs to
CredentialPolicy ..> User : validates
IUserRepository ..> User : persists
''',
        r'''
erDiagram
    USERS {
        int id PK
        varchar username "required, max 80; target unique"
        varchar password_hash "required"
        varchar full_name "required, max 120"
        varchar role "required, max 40"
        datetime created_at "audit"
        datetime updated_at "audit"
    }
''',
        (("CACHED_IDENTITY", (("int", "user_id PK"), ("text", "username"), ("text", "full_name"), ("text", "role"), ("datetime", "expires_at"), ("text", "sync_state"))),),
    ),
    Context(
        2,
        "Profile Management",
        "profile-management",
        "2.6.2. Bounded Context Profile Management",
        "Profiles",
        "Mantener la información personal y de contacto asociada con una identidad sin mezclarla con credenciales o reglas de autenticación.",
        ("Profile", "PersonName", "EmailAddress", "StreetAddress", "IProfileRepository"),
        ("ProfileOwnerId", "ProfileUpdated"),
        ("ProfilesController",),
        ("CreateProfileResource", "ProfileResource"),
        ("ProfileCommandService", "ProfileQueryService", "ProfilesContextFacade"),
        ("CreateProfileCommand", "GetProfileByIdQuery", "GetProfileByEmailQuery"),
        "ProfileRepository",
        "Profile",
        "creación, consulta y actualización del perfil",
        "IAM Context Facade y almacenamiento local de perfiles",
        ("IAM Context",),
        r'''
class Profile <<Aggregate Root>> {
  -id: int
  -ownerId: int
  -name: PersonName
  -email: EmailAddress
  -address: StreetAddress
  +FullName(): string
  +ChangeEmail(email: EmailAddress): void
  +ChangeAddress(address: StreetAddress): void
}
class PersonName <<Value Object>> {
  -firstName: string
  -lastName: string
  +FullName(): string
}
class EmailAddress <<Value Object>> {
  -address: string
  +IsValid(): bool
}
class StreetAddress <<Value Object>> {
  -street: string
  -number: string
  -city: string
  -postalCode: string
  -country: string
  +FullAddress(): string
}
interface IProfileRepository {
  +FindById(id: int): Profile?
  +FindByOwnerId(ownerId: int): Profile?
  +Add(profile: Profile): void
  +Update(profile: Profile): void
}
Profile *-- PersonName
Profile *-- EmailAddress
Profile *-- StreetAddress
IProfileRepository ..> Profile : persists
''',
        r'''
erDiagram
    USERS ||--o| PROFILES : owns
    USERS {
        int id PK
    }
    PROFILES {
        int id PK
        int user_id FK,UK "target traceability"
        varchar first_name "required"
        varchar last_name "required"
        varchar email_address UK "required"
        varchar address_street
        varchar address_number
        varchar address_city
        varchar address_postal_code
        varchar address_country
        datetime created_at "audit"
        datetime updated_at "audit"
    }
''',
        (("CACHED_PROFILES", (("int", "profile_id PK"), ("int", "user_id UK"), ("text", "first_name"), ("text", "last_name"), ("text", "email"), ("text", "address_json"), ("datetime", "updated_at"), ("text", "sync_state"))),),
    ),
    Context(
        3,
        "Livestock Management",
        "livestock-management",
        "2.6.3. Bounded Context Livestock Management",
        "Livestock",
        "Gestionar fincas, hatos, animales e identificadores QR como fuente de referencia para los demás procesos ganaderos.",
        ("Herd", "Animal", "IHerdRepository", "IAnimalRepository"),
        ("Farm", "AnimalTag", "QrIdentifier", "AnimalOwnershipPolicy"),
        ("HerdsController", "AnimalsController"),
        ("HerdResource", "AnimalResource", "CreateHerdResource", "CreateAnimalResource"),
        ("HerdCommandService", "HerdQueryService", "AnimalCommandService", "AnimalQueryService"),
        ("CreateHerdCommand", "UpdateHerdCommand", "CreateAnimalCommand", "UpdateAnimalCommand", "GetAnimalByIdQuery"),
        "HerdRepository / AnimalRepository",
        "Farm, Herd y Animal",
        "registro de fincas, hatos, animales y resolución de códigos QR",
        "Profiles, cámara, Google ML Kit, Room y SQLite",
        ("Profiles Context", "Google ML Kit"),
        r'''
class Farm <<Aggregate Root - target>> {
  -id: int
  -ownerId: int
  -name: string
  -location: string
  +RegisterHerd(herd: Herd): void
  +BelongsTo(ownerId: int): bool
}
class Herd <<Entity>> {
  -id: int
  -farmId: int
  -name: string
  -mainType: string
  -veterinarianId: int?
  +AssignVeterinarian(id: int): void
  +AddAnimal(animal: Animal): void
}
class Animal <<Entity>> {
  -id: int
  -herdId: int
  -tag: AnimalTag
  -qrIdentifier: QrIdentifier
  -name: string
  -species: string
  -breed: string
  -status: AnimalStatus
  +UpdateWeight(weight: decimal): void
  +ChangeStatus(status: AnimalStatus): void
}
class AnimalTag <<Value Object>> {
  -value: string
  +IsValid(): bool
}
class QrIdentifier <<Value Object - target>> {
  -value: string
  +AsPayload(): string
}
enum AnimalStatus {
  Active
  Sold
  Deceased
}
interface IAnimalRepository {
  +FindById(id: int): Animal?
  +FindByQr(code: string): Animal?
  +Add(animal: Animal): void
}
interface IHerdRepository {
  +FindById(id: int): Herd?
  +Add(herd: Herd): void
}
Farm "1" *-- "0..*" Herd
Herd "1" *-- "0..*" Animal
Animal *-- AnimalTag
Animal *-- QrIdentifier
Animal --> AnimalStatus
IAnimalRepository ..> Animal
IHerdRepository ..> Herd
''',
        r'''
erDiagram
    USERS ||--o{ FARMS : owns
    FARMS ||--o{ HERDS : contains
    HERDS ||--o{ ANIMALS : contains
    USERS {
        int id PK
    }
    FARMS {
        int id PK "target addition"
        int owner_id FK
        varchar name "required"
        varchar location "required"
    }
    HERDS {
        int id PK
        int farm_id FK "target addition"
        int owner_id FK
        int veterinarian_id FK "nullable"
        varchar name "required, max 80"
        varchar location "legacy field"
        varchar owner "legacy display field"
        varchar main_type "required, max 40"
    }
    ANIMALS {
        int id PK
        int herd_id FK
        varchar tag "required, max 30; target unique"
        varchar qr_identifier "target addition; target unique"
        varchar name "required, max 80"
        varchar species "required, max 40"
        varchar breed "required, max 60"
        varchar gender "required, max 20"
        date birth_date "nullable"
        decimal weight "required"
        varchar status "required, max 30"
    }
''',
        (
            ("CACHED_HERDS", (("int", "herd_id PK"), ("int", "farm_id"), ("text", "name"), ("text", "location"), ("text", "main_type"), ("datetime", "updated_at"))),
            ("CACHED_ANIMALS", (("int", "animal_id PK"), ("int", "herd_id FK"), ("text", "tag UK"), ("text", "qr_identifier UK"), ("text", "name"), ("text", "species"), ("text", "status"), ("datetime", "updated_at"))),
        ),
    ),
    Context(
        4,
        "Sanitary Management",
        "sanitary-management",
        "2.6.4. Bounded Context Sanitary Management",
        "Sanitary",
        "Conservar la historia sanitaria del animal y controlar el registro de diagnósticos, tratamientos, prescripciones y seguimientos autorizados.",
        ("HealthEvent", "IHealthEventRepository"),
        ("MedicalVisit", "Diagnosis", "Treatment", "Prescription", "SanitaryAlert", "SanitaryAuthorizationPolicy"),
        ("HealthEventsController",),
        ("CreateHealthEventResource", "HealthEventResource"),
        ("HealthEventCommandService", "HealthEventQueryService"),
        ("CreateHealthEventCommand", "UpdateHealthEventCommand", "DeleteHealthEventCommand", "GetHealthEventByIdQuery"),
        "HealthEventRepository",
        "HealthEvent",
        "registro sanitario, seguimiento clínico y generación de alertas",
        "Livestock, Veterinary Collaboration y Activity Management",
        ("Livestock Context", "Veterinary Collaboration Context", "Activity Context"),
        r'''
class HealthEvent <<Aggregate Root>> {
  -id: int
  -animalId: int
  -type: HealthEventType
  -date: Date
  -veterinarianId: int?
  -description: string
  -diagnosis: Diagnosis
  -treatment: Treatment
  -prescription: Prescription
  -nextDueDate: Date?
  +RescheduleFollowUp(date: Date): void
  +UpdateClinicalData(diagnosis: Diagnosis, treatment: Treatment): void
}
class Diagnosis <<Value Object - target>> {
  -description: string
  +IsEmpty(): bool
}
class Treatment <<Value Object - target>> {
  -instructions: string
  +IsValid(): bool
}
class Prescription <<Value Object - target>> {
  -details: string
  +IsRequired(): bool
}
enum HealthEventType {
  MedicalVisit
  Vaccination
  Treatment
  SanitaryControl
}
class SanitaryAuthorizationPolicy <<Domain Service - target>> {
  +CanRegister(actorId: int, animalId: int): bool
}
interface IHealthEventRepository {
  +FindById(id: int): HealthEvent?
  +FindByAnimal(animalId: int): List~HealthEvent~
  +Add(event: HealthEvent): void
  +Update(event: HealthEvent): void
}
HealthEvent *-- Diagnosis
HealthEvent *-- Treatment
HealthEvent *-- Prescription
HealthEvent --> HealthEventType
SanitaryAuthorizationPolicy ..> HealthEvent
IHealthEventRepository ..> HealthEvent
''',
        r'''
erDiagram
    ANIMALS ||--o{ HEALTH_EVENTS : has
    ANIMALS {
        int id PK
    }
    HEALTH_EVENTS {
        int id PK
        int animal_id FK
        int veterinarian_id FK "target traceability, nullable"
        varchar type "required, max 40"
        date event_date "required"
        varchar description "required, max 500"
        varchar veterinarian "legacy display field"
        varchar diagnosis
        varchar treatment
        varchar prescription
        varchar follow_up
        date next_due_date "nullable"
    }
''',
        (("CACHED_HEALTH_EVENTS", (("int", "health_event_id PK"), ("int", "animal_id"), ("int", "veterinarian_id"), ("text", "type"), ("date", "event_date"), ("text", "clinical_data_json"), ("date", "next_due_date"), ("datetime", "updated_at"))),),
    ),
    Context(
        5,
        "Veterinary Collaboration",
        "veterinary-collaboration",
        "2.6.5. Bounded Context Veterinary Collaboration",
        "Clients",
        "Administrar solicitudes y autorizaciones entre ganaderos y veterinarios, delimitando clientes, pacientes y alcance de acceso.",
        ("VeterinarianClient", "IVeterinarianClientRepository"),
        ("CollaborationRequest", "AccessGrant", "CollaborationStatus", "AuthorizationScope"),
        ("VeterinarianClientsController",),
        ("AvailableRancherResource", "VeterinarianClientResource"),
        ("VeterinarianClientCommandService", "VeterinarianClientQueryService"),
        ("CreateVeterinarianClientCommand", "DeleteVeterinarianClientCommand", "GetVeterinarianClientsByVeterinarianIdQuery"),
        "VeterinarianClientRepository",
        "VeterinarianClient",
        "solicitud, aceptación, revocación y consulta de clientes y pacientes",
        "IAM, Profiles y Livestock",
        ("IAM Context", "Profiles Context", "Livestock Context"),
        r'''
class VeterinarianClient <<Aggregate Root>> {
  -id: int
  -veterinarianId: int
  -rancherId: int
  -status: CollaborationStatus
  -requestedAt: DateTime
  -acceptedAt: DateTime?
  -revokedAt: DateTime?
  -scope: AuthorizationScope
  +Accept(at: DateTime): void
  +Reject(): void
  +Revoke(at: DateTime): void
  +IsActive(): bool
}
enum CollaborationStatus {
  Pending
  Accepted
  Rejected
  Revoked
}
class AuthorizationScope <<Value Object - target>> {
  -farmIds: Set~int~
  -animalIds: Set~int~
  -canWriteHealthRecords: bool
  +AllowsAnimal(animalId: int): bool
}
class CollaborationPolicy <<Domain Service - target>> {
  +CanAccept(rancherId: int, relation: VeterinarianClient): bool
  +CanAccess(veterinarianId: int, animalId: int): bool
}
interface IVeterinarianClientRepository {
  +Find(veterinarianId: int, rancherId: int): VeterinarianClient?
  +FindByVeterinarian(id: int): List~VeterinarianClient~
  +Add(relation: VeterinarianClient): void
  +Update(relation: VeterinarianClient): void
}
VeterinarianClient --> CollaborationStatus
VeterinarianClient *-- AuthorizationScope
CollaborationPolicy ..> VeterinarianClient
IVeterinarianClientRepository ..> VeterinarianClient
''',
        r'''
erDiagram
    USERS ||--o{ VETERINARIAN_CLIENTS : veterinarian
    USERS ||--o{ VETERINARIAN_CLIENTS : rancher
    VETERINARIAN_CLIENTS {
        int id PK
        int veterinarian_id FK
        int rancher_id FK
        varchar status "required, max 30"
        datetime requested_at "required"
        datetime accepted_at "nullable"
        datetime revoked_at "target addition"
        json authorization_scope "target addition"
    }
    USERS {
        int id PK
    }
    %% Existing composite unique index: (veterinarian_id, rancher_id)
''',
        (("CACHED_COLLABORATIONS", (("int", "collaboration_id PK"), ("int", "veterinarian_id"), ("int", "rancher_id"), ("text", "status"), ("text", "authorization_scope_json"), ("datetime", "updated_at"))),),
    ),
    Context(
        6,
        "Activity Management",
        "activity-management",
        "2.6.6. Bounded Context Activity Management",
        "Activities",
        "Planificar actividades ganaderas y sanitarias, controlar su estado y decidir cuándo corresponde generar un recordatorio.",
        ("FarmActivity", "IFarmActivityRepository"),
        ("ActivitySchedule", "ActivityPriority", "ActivityStatus", "ReminderPolicy"),
        ("FarmActivitiesController",),
        ("CreateFarmActivityResource", "FarmActivityResource"),
        ("FarmActivityCommandService", "FarmActivityQueryService"),
        ("CreateFarmActivityCommand", "UpdateFarmActivityCommand", "DeleteFarmActivityCommand", "GetFarmActivityByIdQuery"),
        "FarmActivityRepository",
        "FarmActivity",
        "programación, reprogramación, finalización y recordatorios",
        "Livestock, Sanitary y Firebase Cloud Messaging",
        ("Livestock Context", "Sanitary Context", "Firebase Cloud Messaging"),
        r'''
class FarmActivity <<Aggregate Root>> {
  -id: int
  -ownerId: int?
  -veterinarianId: int?
  -animalId: int?
  -title: string
  -type: string
  -schedule: ActivitySchedule
  -priority: ActivityPriority
  -status: ActivityStatus
  +Reschedule(schedule: ActivitySchedule): void
  +Complete(): void
  +Cancel(): void
}
class ActivitySchedule <<Value Object - target>> {
  -scheduledAt: DateTime
  -reminderAt: DateTime?
  +IsUpcoming(now: DateTime): bool
}
enum ActivityPriority {
  Low
  Medium
  High
}
enum ActivityStatus {
  Pending
  InProgress
  Completed
  Cancelled
}
class ReminderPolicy <<Domain Service - target>> {
  +ShouldNotify(activity: FarmActivity, now: DateTime): bool
}
interface IFarmActivityRepository {
  +FindById(id: int): FarmActivity?
  +FindUpcoming(userId: int): List~FarmActivity~
  +Add(activity: FarmActivity): void
  +Update(activity: FarmActivity): void
}
FarmActivity *-- ActivitySchedule
FarmActivity --> ActivityPriority
FarmActivity --> ActivityStatus
ReminderPolicy ..> FarmActivity
IFarmActivityRepository ..> FarmActivity
''',
        r'''
erDiagram
    USERS ||--o{ FARM_ACTIVITIES : owns
    ANIMALS ||--o{ FARM_ACTIVITIES : concerns
    USERS {
        int id PK
    }
    ANIMALS {
        int id PK
    }
    FARM_ACTIVITIES {
        int id PK
        int owner_id FK "nullable"
        int veterinarian_id FK "nullable"
        int animal_id FK "target addition, nullable"
        varchar title "required, max 120"
        varchar type "required, max 40"
        datetime scheduled_at "date in legacy model"
        datetime reminder_at "target addition, nullable"
        varchar priority "required, max 20"
        varchar status "required, max 30"
    }
''',
        (("CACHED_ACTIVITIES", (("int", "activity_id PK"), ("int", "owner_id"), ("int", "veterinarian_id"), ("int", "animal_id"), ("text", "title"), ("datetime", "scheduled_at"), ("datetime", "reminder_at"), ("text", "priority"), ("text", "status"), ("datetime", "updated_at"))),),
    ),
    Context(
        7,
        "Financial Management",
        "financial-management",
        "2.6.7. Bounded Context Financial Management",
        "Financial",
        "Registrar ingresos y egresos operativos y producir resúmenes económicos básicos para apoyar decisiones del ganadero.",
        ("FinancialRecord", "IFinancialRecordRepository"),
        ("Money", "FinancialRecordType", "FinancialCategory", "FinancialSummary"),
        ("FinancialRecordsController",),
        ("CreateFinancialRecordResource", "FinancialRecordResource"),
        ("FinancialRecordCommandService", "FinancialRecordQueryService"),
        ("CreateFinancialRecordCommand", "UpdateFinancialRecordCommand", "DeleteFinancialRecordCommand", "GetFinancialRecordByIdQuery"),
        "FinancialRecordRepository",
        "FinancialRecord",
        "registro de movimientos y cálculo de resúmenes",
        "Profiles, MySQL y almacenamiento offline",
        ("Profiles Context", "Analytics Context"),
        r'''
class FinancialRecord <<Aggregate Root>> {
  -id: int
  -ownerId: int
  -type: FinancialRecordType
  -category: FinancialCategory
  -amount: Money
  -date: Date
  -description: string
  +ChangeAmount(amount: Money): void
  +ChangeCategory(category: FinancialCategory): void
}
class Money <<Value Object - target>> {
  -amount: decimal
  -currency: string
  +Add(other: Money): Money
  +IsPositive(): bool
}
enum FinancialRecordType {
  Income
  Expense
}
class FinancialCategory <<Value Object - target>> {
  -name: string
  +IsValid(): bool
}
class FinancialSummary <<Domain Service - target>> {
  +Calculate(records: List~FinancialRecord~): Money
}
interface IFinancialRecordRepository {
  +FindById(id: int): FinancialRecord?
  +FindByOwner(ownerId: int): List~FinancialRecord~
  +Add(record: FinancialRecord): void
  +Update(record: FinancialRecord): void
}
FinancialRecord *-- Money
FinancialRecord --> FinancialRecordType
FinancialRecord *-- FinancialCategory
FinancialSummary ..> FinancialRecord
IFinancialRecordRepository ..> FinancialRecord
''',
        r'''
erDiagram
    USERS ||--o{ FINANCIAL_RECORDS : owns
    USERS {
        int id PK
    }
    FINANCIAL_RECORDS {
        int id PK
        int owner_id FK
        varchar type "required, max 20"
        varchar category "required, max 80"
        decimal amount "precision 10,2"
        varchar currency "target addition, default PEN"
        date record_date "required"
        varchar description
    }
''',
        (("CACHED_FINANCIAL_RECORDS", (("int", "record_id PK"), ("int", "owner_id"), ("text", "type"), ("text", "category"), ("decimal", "amount"), ("text", "currency"), ("date", "record_date"), ("text", "description"), ("datetime", "updated_at"))),),
    ),
    Context(
        8,
        "Subscription Management",
        "subscription-management",
        "2.6.8. Bounded Context Subscription Management",
        "Subscriptions",
        "Administrar planes, vigencia de suscripciones y pagos confirmados sin introducir conceptos propios de Stripe en el dominio.",
        ("SubscriptionPlan", "Subscription", "Payment", "ISubscriptionPlanRepository", "ISubscriptionRepository", "IPaymentRepository"),
        ("Money", "SubscriptionStatus", "PaymentStatus", "PaymentGateway"),
        ("SubscriptionPlansController", "SubscriptionsController"),
        ("SubscriptionPlanResource", "SubscriptionResource", "PaymentResource", "StripeCheckoutResource"),
        ("SubscriptionPlanCommandService", "SubscriptionCommandService", "PaymentCommandService", "SubscriptionQueryService"),
        ("CreateSubscriptionCommand", "CreatePaymentCommand", "GetSubscriptionByIdQuery", "GetAllSubscriptionPlansQuery"),
        "SubscriptionPlanRepository / SubscriptionRepository / PaymentRepository",
        "Subscription",
        "consulta de planes, checkout, confirmación de pago y vigencia",
        "IAM y Stripe mediante Anti-Corruption Layer",
        ("IAM Context", "Stripe"),
        r'''
class SubscriptionPlan <<Entity>> {
  -id: int
  -name: string
  -price: Money
  -providerPriceId: string
  -maxAnimals: int
  -isActive: bool
  +Deactivate(): void
  +ChangePrice(price: Money): void
}
class Subscription <<Aggregate Root>> {
  -id: int
  -userId: int
  -planId: int
  -status: SubscriptionStatus
  -startedAt: Date
  -endsAt: Date?
  +Activate(start: Date, end: Date?): void
  +Cancel(end: Date): void
  +IsActive(on: Date): bool
}
class Payment <<Entity>> {
  -id: int
  -subscriptionId: int
  -userId: int
  -amount: Money
  -providerPaymentId: string
  -status: PaymentStatus
  -paidAt: DateTime
  +Confirm(providerId: string, paidAt: DateTime): void
  +Reject(): void
}
class Money <<Value Object - target>> {
  -amount: decimal
  -currency: string
  +IsPositive(): bool
}
enum SubscriptionStatus {
  Pending
  Active
  Cancelled
  Expired
}
enum PaymentStatus {
  Pending
  Paid
  Failed
}
interface ISubscriptionRepository {
  +FindById(id: int): Subscription?
  +FindActiveByUser(userId: int): Subscription?
  +Add(subscription: Subscription): void
  +Update(subscription: Subscription): void
}
SubscriptionPlan "1" <-- "0..*" Subscription
Subscription "1" *-- "0..*" Payment
Subscription --> SubscriptionStatus
Payment --> PaymentStatus
Payment *-- Money
SubscriptionPlan *-- Money
ISubscriptionRepository ..> Subscription
''',
        r'''
erDiagram
    USERS ||--o{ SUBSCRIPTIONS : owns
    SUBSCRIPTION_PLANS ||--o{ SUBSCRIPTIONS : selects
    SUBSCRIPTIONS ||--o{ PAYMENTS : receives
    USERS {
        int id PK
    }
    SUBSCRIPTION_PLANS {
        int id PK
        varchar name "required, max 80"
        decimal price "precision 10,2"
        varchar stripe_price_id "max 120"
        int max_animals
        boolean is_active
    }
    SUBSCRIPTIONS {
        int id PK
        int user_id FK
        int plan_id FK
        varchar stripe_customer_id "max 120"
        varchar stripe_subscription_id "max 120"
        varchar status "required, max 40"
        date started_at
        date ends_at "nullable"
    }
    PAYMENTS {
        int id PK
        int user_id FK
        int subscription_id FK
        decimal amount "precision 10,2"
        varchar currency "required, max 10"
        varchar provider "required, max 40"
        varchar provider_payment_id "required, max 120; target unique"
        varchar status "required, max 40"
        datetime paid_at
    }
''',
        (
            ("CACHED_SUBSCRIPTION_PLANS", (("int", "plan_id PK"), ("text", "name"), ("decimal", "price"), ("text", "currency"), ("int", "max_animals"), ("boolean", "is_active"), ("datetime", "updated_at"))),
            ("CACHED_SUBSCRIPTIONS", (("int", "subscription_id PK"), ("int", "user_id"), ("int", "plan_id FK"), ("text", "status"), ("date", "started_at"), ("date", "ends_at"), ("datetime", "updated_at"))),
        ),
    ),
    Context(
        9,
        "Analytics and Reporting",
        "analytics-and-reporting",
        "2.6.9. Bounded Context Analytics and Reporting",
        "Analytics",
        "Construir proyecciones y métricas de consulta para los dashboards sin adquirir propiedad sobre los registros de los contextos fuente.",
        ("ReportMetric", "IReportMetricRepository"),
        ("DashboardProjection", "MetricSlice", "MetricPeriod", "ProjectionBuilder"),
        ("DashboardAnalyticsController", "ReportMetricsController"),
        ("RancherDashboardResource", "VeterinarianDashboardResource", "FinancialSummaryResource", "HealthSummaryResource"),
        ("ReportMetricCommandService", "ReportMetricQueryService"),
        ("CreateReportMetricCommand", "UpdateReportMetricCommand", "GetAllReportMetricsQuery", "GetReportMetricByIdQuery"),
        "ReportMetricRepository",
        "DashboardProjection",
        "construcción y consulta de dashboards por rol y periodo",
        "Livestock, Sanitary, Activities y Financial como fuentes",
        ("Livestock Context", "Sanitary Context", "Activities Context", "Financial Context"),
        r'''
class DashboardProjection <<Aggregate Root - target>> {
  -id: int
  -ownerId: int
  -audience: string
  -period: MetricPeriod
  -generatedAt: DateTime
  -metrics: List~ReportMetric~
  +ReplaceMetrics(metrics: List~ReportMetric~): void
  +IsStale(now: DateTime): bool
}
class ReportMetric <<Entity>> {
  -id: int
  -label: string
  -slice: MetricSlice
  -trend: string
  -sourceContext: string
  +Update(slice: MetricSlice, trend: string): void
}
class MetricSlice <<Value Object - target>> {
  -label: string
  -value: decimal
  -unit: string
  +IsComparableTo(other: MetricSlice): bool
}
class MetricPeriod <<Value Object - target>> {
  -from: Date
  -to: Date
  +Contains(date: Date): bool
}
class ProjectionBuilder <<Domain Service - target>> {
  +BuildRancher(ownerId: int, period: MetricPeriod): DashboardProjection
  +BuildVeterinarian(id: int, period: MetricPeriod): DashboardProjection
}
interface IReportMetricRepository {
  +FindProjection(ownerId: int, period: MetricPeriod): DashboardProjection?
  +Save(projection: DashboardProjection): void
}
DashboardProjection "1" *-- "1..*" ReportMetric
DashboardProjection *-- MetricPeriod
ReportMetric *-- MetricSlice
ProjectionBuilder ..> DashboardProjection
IReportMetricRepository ..> DashboardProjection
''',
        r'''
erDiagram
    DASHBOARD_PROJECTIONS ||--o{ REPORT_METRICS : contains
    DASHBOARD_PROJECTIONS {
        int id PK "target read model"
        int owner_id
        varchar audience
        date period_from
        date period_to
        datetime generated_at
        string owner_audience_period UK
    }
    REPORT_METRICS {
        int id PK
        int projection_id FK "target addition"
        varchar label "required, max 80"
        varchar value "required, max 40"
        varchar trend "max 80"
        varchar source_context "target traceability"
    }
''',
        (
            ("CACHED_DASHBOARDS", (("int", "dashboard_id PK"), ("int", "owner_id"), ("text", "audience"), ("date", "period_from"), ("date", "period_to"), ("datetime", "generated_at"), ("text", "sync_state"))),
            ("CACHED_REPORT_METRICS", (("int", "metric_id PK"), ("int", "dashboard_id FK"), ("text", "label"), ("text", "value"), ("text", "trend"), ("text", "source_context"))),
        ),
    ),
)


def html_table(rows: list[tuple[str, str, str, str, str]]) -> str:
    body = "\n".join(
        "    <tr>" + "".join(f"<td>{escape(value)}</td>" for value in row) + "</tr>"
        for row in rows
    )
    return f'''<table>
  <thead>
    <tr><th>Clase o componente</th><th>Tipo</th><th>Producto</th><th>Propósito</th><th>Responsabilidades</th></tr>
  </thead>
  <tbody>
{body}
  </tbody>
</table>'''


def symbol_name(value: str) -> str:
    words = "".join(character if character.isalnum() else " " for character in value).split()
    return "".join(word[:1].upper() + word[1:] for word in words)


def layer_rows(context: Context, layer: str) -> list[tuple[str, str, str, str, str]]:
    if layer == "domain":
        rows = []
        for name in context.existing_domain:
            if name.startswith("I") and name.endswith("Repository"):
                item_type = "Repository Interface existente"
            elif name.endswith("Error"):
                item_type = "Enumeración existente"
            else:
                item_type = "Clase de dominio existente"
            rows.append((name, item_type, f"Backend / módulo {context.module}", f"Representar {name} dentro de {context.name}.", "Conservar las invariantes actualmente implementadas y servir como evidencia trazable."))
        rows.extend(
            (name, "Diseño objetivo", "Modelo canónico compartido", f"Completar el lenguaje ubicuo de {context.name}.", "Expresar reglas o conceptos requeridos por el alcance móvil que aún no están implementados en el backend heredado.")
            for name in context.proposed_domain
        )
        return rows
    if layer == "interface":
        rows = [
            (name, "REST Controller existente", "Backend ASP.NET Core", f"Exponer {context.capability}.", "Validar el contrato HTTP, traducir resources y delegar el caso de uso.")
            for name in context.controllers
        ]
        rows.extend(
            (name, "Resource/Assembler existente", "Backend ASP.NET Core", "Definir el contrato público de entrada o salida.", "Evitar exponer directamente entidades del dominio.")
            for name in context.resources
        )
        feature = symbol_name(context.aggregate)
        rows.extend([
            (f"{feature}Screen", "Composable objetivo", "Android / Jetpack Compose", f"Presentar {context.capability}.", "Renderizar estado, recibir acciones y mostrar errores recuperables."),
            (f"{feature}ViewModel", "Presentation Model objetivo", "Android / Kotlin", "Coordinar el estado observable de la pantalla.", "Invocar casos de uso y convertir resultados en UI state."),
            (f"{feature}Page", "Widget objetivo", "Flutter / Dart", f"Presentar {context.capability}.", "Renderizar estado y enviar intenciones del usuario."),
            (f"{feature}Controller", "State Controller objetivo", "Flutter / Dart", "Coordinar el estado de presentación.", "Invocar casos de uso y publicar estados de carga, éxito y error."),
        ])
        return rows
    if layer == "application":
        rows = [
            (name, "Application Service existente", "Backend ASP.NET Core", f"Orquestar {context.capability}.", "Coordinar repositorios, reglas del dominio y Unit of Work.")
            for name in context.app_services
        ]
        rows.extend(
            (name, "Command/Query existente", "Backend ASP.NET Core", "Representar una intención o consulta explícita.", "Transportar datos tipados hacia el servicio de aplicación correspondiente.")
            for name in context.commands_queries
        )
        rows.extend([
            (f"{symbol_name(context.aggregate)}CommandHandler", "Command Handler objetivo", "Backend ASP.NET Core", "Ejecutar comandos mediante una unidad de aplicación explícita.", "Cargar el agregado, aplicar sus reglas, persistirlo y publicar el resultado."),
            (f"{symbol_name(context.aggregate)}EventHandler", "Event Handler objetivo", "Backend ASP.NET Core", "Reaccionar a cambios confirmados en el contexto.", "Actualizar proyecciones o solicitar integraciones sin acoplarlas al agregado."),
            (f"Observe{symbol_name(context.aggregate)}UseCase", "Use Case objetivo", "Android y Flutter", "Consultar el read model local y actualizar la UI.", "Combinar caché local con actualización remota."),
            (f"Sync{symbol_name(context.aggregate)}UseCase", "Use Case objetivo", "Android y Flutter", "Sincronizar cambios pendientes.", "Procesar el outbox de forma idempotente y resolver resultados del servidor."),
        ])
        return rows
    return [
        (context.repository, "Repository Adapter existente", "Backend / Entity Framework Core", "Implementar los puertos de persistencia del dominio.", "Consultar y guardar las entidades mediante AppDbContext y MySQL."),
        ("ModelBuilderExtensions", "Persistence Configuration existente", "Backend / Entity Framework Core", "Configurar tablas, columnas, constraints y conversiones.", "Mantener el modelo relacional alineado con las entidades."),
        (f"{symbol_name(context.aggregate)}ApiDataSource", "Remote Adapter objetivo", "Android / Kotlin", "Consumir los endpoints REST del contexto.", "Enviar JWT, serializar JSON y normalizar errores HTTP."),
        (f"{symbol_name(context.aggregate)}Dao", "Room Adapter objetivo", "Android / Room", "Acceder al almacenamiento local.", "Mantener caché, estado de sincronización y operaciones pendientes."),
        (f"{symbol_name(context.aggregate)}RemoteDataSource", "Remote Adapter objetivo", "Flutter / Dart", "Consumir los mismos contratos REST.", "Serializar DTOs y traducir errores de red."),
        (f"{symbol_name(context.aggregate)}LocalDataSource", "SQLite Adapter objetivo", "Flutter / Dart", "Acceder a la persistencia local equivalente.", "Mantener el mismo comportamiento offline que Android."),
        (context.integration, "Integración/ACL", "Infraestructura compartida", "Conectar el contexto con capacidades externas.", "Traducir contratos técnicos sin contaminar el modelo del dominio."),
    ]


def dsl_for(context: Context) -> str:
    key = f"BC{context.number}"
    external_defs = "\n".join(
        f'        external{i} = softwareSystem "{name}" "Dependencia externa de {context.name}."'
        for i, name in enumerate(context.externals, 1)
    )
    external_rels = "\n".join(
        f'        apiApplication -> external{i} "Consulta o publica información mediante un contrato explícito"'
        for i, _ in enumerate(context.externals, 1)
    )
    controllers = ", ".join(context.controllers)
    services = ", ".join(context.app_services)
    return f'''workspace "AniTec - {context.name} Components" "Vistas C4 de componentes del bounded context {context.name}." {{
    model {{
        user = person "Authenticated Mobile User" "Ganadero o veterinario autorizado para usar las capacidades del contexto."
{external_defs}

        anitec = softwareSystem "AniTec" "Solución móvil para gestión ganadera." {{
            api = container "AniTec REST API" "Backend y fuente autoritativa de reglas de negocio." "C# y ASP.NET Core" {{
                apiController = component "REST Interface" "Controladores: {controllers}." "ASP.NET Core Controllers"
                apiAssembler = component "Resource Assemblers" "Traduce resources y comandos sin exponer entidades." "C#"
                apiApplication = component "Application Services and Handlers" "Servicios existentes: {services}. Incluye command handlers y event handlers como diseño objetivo." "C# Application Services"
                apiDomain = component "{context.name} Domain Model" "{context.aggregate}; reglas, value objects y puertos del contexto." "C# Domain Model"
                repositoryPort = component "Repository Ports" "Interfaces de repositorio definidas desde el dominio." "C# Interfaces"
                repositoryAdapter = component "Persistence Adapters" "{context.repository}." "Entity Framework Core"
            }}
            android = container "Native Android Application" "Cliente Android nativo." "Kotlin y Jetpack Compose" {{
                androidUi = component "{context.name} Compose UI" "Pantallas y componentes visuales del contexto." "Jetpack Compose"
                androidViewModel = component "ViewModel and UI State" "Mantiene estado de presentación y procesa intenciones." "Kotlin ViewModel"
                androidUseCases = component "Mobile Use Cases" "Casos de uso de {context.capability}." "Kotlin"
                androidRepository = component "Repository Implementation" "Coordina fuentes remota y local." "Kotlin"
                androidRemote = component "REST Data Source" "Consume los endpoints del contexto." "Retrofit/OkHttp"
                androidLocal = component "Room Data Source" "Mantiene caché y outbox local." "Room"
                androidSync = component "Synchronization Worker" "Reintenta operaciones pendientes de forma idempotente." "WorkManager"
            }}
            flutter = container "Cross-Platform Mobile Application" "Cliente móvil multiplataforma." "Flutter y Dart" {{
                flutterUi = component "{context.name} Widgets" "Páginas y widgets del contexto." "Flutter"
                flutterState = component "State Controller" "Mantiene estado de presentación y procesa intenciones." "Dart"
                flutterUseCases = component "Mobile Use Cases" "Casos de uso equivalentes a Android." "Dart"
                flutterRepository = component "Repository Implementation" "Coordina fuentes remota y local." "Dart"
                flutterRemote = component "REST Data Source" "Consume los endpoints del contexto." "Dio"
                flutterLocal = component "SQLite Data Source" "Mantiene caché y outbox local." "SQLite"
                flutterSync = component "Synchronization Coordinator" "Reintenta operaciones pendientes de forma idempotente." "Dart"
            }}
            mysql = container "AniTec Database" "Persistencia autoritativa del contexto." "MySQL" "Database"
            room = container "Android Local Database" "Caché y outbox del contexto en Android." "Room/SQLite" "Database"
            flutterDb = container "Flutter Local Database" "Caché y outbox del contexto en Flutter." "SQLite" "Database"
        }}

        user -> androidUi "Usa"
        user -> flutterUi "Usa"
        androidUi -> androidViewModel "Envía intenciones y observa estado"
        androidViewModel -> androidUseCases "Invoca"
        androidUseCases -> androidRepository "Usa el puerto"
        androidRepository -> androidRemote "Consulta o sincroniza"
        androidRepository -> androidLocal "Lee y escribe"
        androidSync -> androidRepository "Procesa operaciones pendientes"
        androidRemote -> apiController "Consume" "JSON/HTTPS + JWT"
        androidLocal -> room "Persiste" "Room"

        flutterUi -> flutterState "Envía intenciones y observa estado"
        flutterState -> flutterUseCases "Invoca"
        flutterUseCases -> flutterRepository "Usa el puerto"
        flutterRepository -> flutterRemote "Consulta o sincroniza"
        flutterRepository -> flutterLocal "Lee y escribe"
        flutterSync -> flutterRepository "Procesa operaciones pendientes"
        flutterRemote -> apiController "Consume" "JSON/HTTPS + JWT"
        flutterLocal -> flutterDb "Persiste" "SQLite"

        apiController -> apiAssembler "Traduce requests y responses"
        apiAssembler -> apiApplication "Entrega comandos y consultas"
        apiApplication -> apiDomain "Ejecuta reglas"
        apiApplication -> repositoryPort "Depende del puerto"
        repositoryAdapter -> repositoryPort "Implementa"
        repositoryAdapter -> mysql "Lee y escribe" "Entity Framework Core / SQL"
{external_rels}
    }}

    views {{
        component api "{key}-ApiComponents" "Componentes backend de {context.name}." {{
            include *
            autoLayout lr
        }}
        component android "{key}-AndroidComponents" "Componentes Android de {context.name}." {{
            include *
            autoLayout lr
        }}
        component flutter "{key}-FlutterComponents" "Componentes Flutter de {context.name}." {{
            include *
            autoLayout lr
        }}
        styles {{
            element "Person" {{
                shape person
                background #084C61
                color #FFFFFF
            }}
            element "Software System" {{
                background #177E89
                color #FFFFFF
            }}
            element "Container" {{
                background #2A9D8F
                color #FFFFFF
            }}
            element "Component" {{
                background #457B9D
                color #FFFFFF
            }}
            element "Database" {{
                shape cylinder
                background #5C6B73
                color #FFFFFF
            }}
            relationship "Relationship" {{
                color #52616B
                routing orthogonal
            }}
        }}
    }}
    configuration {{
        scope softwaresystem
    }}
}}
'''


def puml_for(context: Context) -> str:
    return f'''@startuml
title AniTec - {context.name} - Domain Layer
hide circle
skinparam classAttributeIconSize 0
skinparam shadowing false
skinparam linetype ortho
skinparam class {{
  BackgroundColor #F7FAFC
  BorderColor #2A9D8F
  ArrowColor #52616B
}}

package "{context.name}" {{
{context.puml_body.strip()}
}}

note bottom
  Existing elements preserve the backend vocabulary.
  Elements marked as target complete the mobile course design.
end note
@enduml
'''


def local_erd(context: Context, product: str) -> str:
    names = [name for name, _ in context.local_entities]
    relations = []
    if len(names) > 1:
        for child in names[1:]:
            relations.append(f"    {names[0]} ||--o{{ {child} : contains")
    entity_blocks = []
    for name, fields in context.local_entities:
        field_lines = "\n".join(f"        {field_type} {field_name}" for field_type, field_name in fields)
        entity_blocks.append(f"    {name} {{\n{field_lines}\n    }}")
    outbox = f'''    PENDING_OPERATIONS {{
        text operation_id PK
        text aggregate_type
        text aggregate_id
        text operation_type
        text payload_json
        datetime created_at
        int retry_count
        text status
    }}'''
    return "\n".join([
        f"%% {product} local persistence for {context.name}",
        "erDiagram",
        *relations,
        *entity_blocks,
        outbox,
        "",
    ])


def placeholder(path: str, alt: str, caption: str, note: str) -> str:
    return f'''<div align="center">
  <!-- Placeholder: {note} -->
  <img src="{path}" alt="{alt}" width="900">
  <p><i>{caption}</i></p>
</div>'''


def markdown_for(context: Context) -> str:
    prefix = f"2.6.{context.number}"
    asset = f"../../assets/chapter-2/tactical-ddd/{context.slug}"
    code_link = f"../../assets/codefordiagrams/{context.folder}"
    database_asset = f"../../assets/codefordiagrams/{context.folder}"
    api_key = f"BC{context.number}-ApiComponents"
    android_key = f"BC{context.number}-AndroidComponents"
    flutter_key = f"BC{context.number}-FlutterComponents"
    figure = lambda index: f"Figura {prefix}.{index}."
    sections = [
        f"# {prefix}. Bounded Context: {context.name}",
        "",
        context.purpose,
        "",
        f"La base implementada se encuentra en el módulo `{context.module}` de la API ASP.NET Core. El diseño móvil de Android y Flutter se presenta como **diseño objetivo** porque esos clientes todavía no existen en el workspace. Los tres productos comparten contratos REST y lenguaje ubicuo, mientras la API conserva las reglas autoritativas.",
        "",
        f"## {prefix}.1. Domain Layer",
        "",
        f"Esta capa representa el núcleo de {context.name}. Los elementos existentes se conservarán como punto de partida; los elementos objetivo completan las invariantes identificadas en EventStorming y en el Bounded Context Canvas.",
        "",
        html_table(layer_rows(context, "domain")),
        "",
        f"## {prefix}.2. Interface Layer",
        "",
        "La Interface Layer traduce acciones de usuarios y contratos externos. En el backend utiliza controllers, resources y assemblers; en los clientes móviles utiliza pantallas y controladores de estado específicos de cada plataforma.",
        "",
        html_table(layer_rows(context, "interface")),
        "",
        f"## {prefix}.3. Application Layer",
        "",
        "La Application Layer orquesta comandos, consultas y sincronización. Los casos de uso móviles consultan primero el read model local, solicitan actualización remota cuando existe conectividad y procesan operaciones pendientes mediante un outbox idempotente.",
        "",
        html_table(layer_rows(context, "application")),
        "",
        f"## {prefix}.4. Infrastructure Layer",
        "",
        f"La Infrastructure Layer conecta el dominio con {context.integration}. Los adapters implementan interfaces definidas hacia el interior y traducen errores técnicos a resultados comprendidos por los casos de uso.",
        "",
        html_table(layer_rows(context, "infrastructure")),
        "",
        f"## {prefix}.5. Bounded Context Software Architecture Component Level Diagrams",
        "",
        f"El archivo [`component-level.dsl`](<{code_link}/component-level.dsl>) contiene las vistas `{api_key}`, `{android_key}` y `{flutter_key}`. Las tres parten del mismo modelo C4 y muestran la separación entre presentación, aplicación, dominio y adaptadores.",
        "",
        placeholder(f"{asset}/{context.slug}-api-components.png", f"Componentes API de {context.name}", f"{figure(1)} Componentes de la API para {context.name}. Fuente: elaboración propia con Structurizr DSL.", f"exportar la vista {api_key}."),
        "",
        placeholder(f"{asset}/{context.slug}-android-components.png", f"Componentes Android de {context.name}", f"{figure(2)} Componentes Android para {context.name}. Fuente: elaboración propia con Structurizr DSL.", f"exportar la vista {android_key}."),
        "",
        placeholder(f"{asset}/{context.slug}-flutter-components.png", f"Componentes Flutter de {context.name}", f"{figure(3)} Componentes Flutter para {context.name}. Fuente: elaboración propia con Structurizr DSL.", f"exportar la vista {flutter_key}."),
        "",
        f"## {prefix}.6. Bounded Context Software Architecture Code Level Diagrams",
        "",
        "Los diagramas de código detallan el modelo del dominio y los objetos de persistencia. El UML diferencia los elementos existentes de las incorporaciones objetivo, mientras los ERD señalan mediante comentarios o descripciones las columnas propuestas.",
        "",
        f"### {prefix}.6.1. Bounded Context Domain Layer Class Diagrams",
        "",
        "El Class Diagram incluye agregados, entidades, value objects, enumeraciones, servicios de dominio e interfaces de repositorio con atributos, operaciones, visibilidad y multiplicidades.",
        "",
        placeholder(f"{asset}/{context.slug}-domain-class-diagram.png", f"Class Diagram de {context.name}", f"{figure(4)} Domain Layer Class Diagram de {context.name}. Fuente: elaboración propia con PlantUML.", "renderizar domain-layer-class-diagram.puml."),
        "",
        f"### {prefix}.6.2. Bounded Context Database Design Diagram",
        "",
        "MySQL mantiene la persistencia autoritativa. Room y SQLite contienen únicamente caché, metadatos de sincronización y operaciones pendientes; no sustituyen las reglas ni la fuente de verdad del backend. En IAM, las credenciales y tokens permanecen fuera de las tablas locales y se almacenan mediante mecanismos seguros del sistema operativo.",
        "",
        placeholder(f"{database_asset}/mysql-database-design.png", f"MySQL Database Diagram de {context.name}", f"{figure(5)} MySQL Database Design de {context.name}. Fuente: elaboración propia con Mermaid ER.", "imagen generada desde mysql-database-design.erd."),
        "",
        placeholder(f"{database_asset}/android-room-database-design.png", f"Room Database Diagram de {context.name}", f"{figure(6)} Android Room Database Design de {context.name}. Fuente: elaboración propia con Mermaid ER.", "imagen generada desde android-room-database-design.erd."),
        "",
        placeholder(f"{database_asset}/flutter-sqlite-database-design.png", f"Flutter SQLite Database Diagram de {context.name}", f"{figure(7)} Flutter SQLite Database Design de {context.name}. Fuente: elaboración propia con Mermaid ER.", "imagen generada desde flutter-sqlite-database-design.erd."),
        "",
    ]
    return "\n".join(sections)


def write_context(context: Context) -> None:
    folder = CODE / context.folder
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "component-level.dsl").write_text(dsl_for(context), encoding="utf-8")
    (folder / "domain-layer-class-diagram.puml").write_text(puml_for(context), encoding="utf-8")
    (folder / "mysql-database-design.erd").write_text(context.server_erd.strip() + "\n", encoding="utf-8")
    (folder / "android-room-database-design.erd").write_text(local_erd(context, "Android Room"), encoding="utf-8")
    (folder / "flutter-sqlite-database-design.erd").write_text(local_erd(context, "Flutter SQLite"), encoding="utf-8")
    filename = f"2-6-{context.number}-Bounded-Context-{context.name.replace(' ', '-')}.md"
    (CONTENT / filename).write_text(markdown_for(context), encoding="utf-8")


def write_main_markdown() -> None:
    rows = "\n".join(
        f"    <tr><td>2.6.{c.number}</td><td><a href=\"./2-6-{c.number}-Bounded-Context-{c.name.replace(' ', '-')}.md\">{escape(c.name)}</a></td><td>{escape(c.module)}</td><td>{escape(c.purpose)}</td></tr>"
        for c in CONTEXTS
    )
    content = f'''# 2.6. Tactical-Level Domain-Driven Design

Esta sección describe cómo los nueve bounded contexts identificados en el diseño estratégico se materializan en clases, capas, componentes y estructuras de persistencia. La propuesta utiliza un enfoque híbrido trazable: conserva nombres y responsabilidades del backend heredado y presenta como diseño objetivo los elementos requeridos para Android, Flutter y la evolución del dominio.

Para todos los contextos se aplican las siguientes convenciones:

- La **Domain Layer** mantiene entidades, aggregates, value objects, servicios de dominio e interfaces de repositorio.
- La **Application Layer** orquesta comandos, consultas, eventos y casos de uso sin depender de frameworks de presentación.
- La **Interface Layer** traduce HTTP o acciones de la interfaz móvil hacia los casos de uso.
- La **Infrastructure Layer** implementa persistencia, red, seguridad, sincronización e integraciones externas.
- MySQL es la fuente autoritativa; Room y SQLite mantienen caché y un outbox idempotente.
- Las reglas de negocio permanecen en la API y el dominio; Android y Flutter reutilizan los mismos contratos y lenguaje ubicuo.

<table>
  <thead>
    <tr><th>Sección</th><th>Bounded Context</th><th>Módulo heredado</th><th>Propósito</th></tr>
  </thead>
  <tbody>
{rows}
  </tbody>
</table>
'''
    (CONTENT / "2-6-Tactical-Level-Domain-Driven-Design.md").write_text(content, encoding="utf-8")


def update_report_readme() -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    start = text.index("- [2.6. Tactical-Level Domain-Driven Design]")
    end_marker = "## Capítulo III: Solution UI/UX Design"
    end = text.index(end_marker, start)
    lines = [
        "- [2.6. Tactical-Level Domain-Driven Design](./markdown/content/chapter-2/2-6-Tactical-Level-Domain-Driven-Design.md)"
    ]
    for c in CONTEXTS:
        filename = f"2-6-{c.number}-Bounded-Context-{c.name.replace(' ', '-')}.md"
        base = f"  - [2.6.{c.number}. Bounded Context: {c.name}](./markdown/content/chapter-2/{filename})"
        lines.extend([
            base,
            f"    - [2.6.{c.number}.1. Domain Layer](./markdown/content/chapter-2/{filename})",
            f"    - [2.6.{c.number}.2. Interface Layer](./markdown/content/chapter-2/{filename})",
            f"    - [2.6.{c.number}.3. Application Layer](./markdown/content/chapter-2/{filename})",
            f"    - [2.6.{c.number}.4. Infrastructure Layer](./markdown/content/chapter-2/{filename})",
            f"    - [2.6.{c.number}.5. Bounded Context Software Architecture Component Level Diagrams](./markdown/content/chapter-2/{filename})",
            f"    - [2.6.{c.number}.6. Bounded Context Software Architecture Code Level Diagrams](./markdown/content/chapter-2/{filename})",
            f"      - [2.6.{c.number}.6.1. Bounded Context Domain Layer Class Diagrams](./markdown/content/chapter-2/{filename})",
            f"      - [2.6.{c.number}.6.2. Bounded Context Database Design Diagram](./markdown/content/chapter-2/{filename})",
        ])
    updated = text[:start] + "\n".join(lines) + "\n\n" + text[end:]
    path.write_text(updated, encoding="utf-8")


def update_diagram_readme() -> None:
    path = CODE / "README.md"
    current = path.read_text(encoding="utf-8") if path.exists() else "# Diagramas de AniTec\n"
    marker = "\n## Diagramas tácticos de bounded contexts"
    if marker in current:
        current = current[: current.index(marker)]
    rows = "\n".join(
        f"| 2.6.{c.number} {c.name} | `{c.folder}/component-level.dsl` | `{c.folder}/domain-layer-class-diagram.puml` | Tres archivos `.erd` |"
        for c in CONTEXTS
    )
    addition = f'''

## Diagramas tácticos de bounded contexts

Cada carpeta contiene un workspace C4 con tres vistas, un UML del dominio y los modelos de persistencia de MySQL, Android Room y Flutter SQLite.

| Bounded Context | C4 Components | Domain UML | Database Designs |
|---|---|---|---|
{rows}

### Convenciones de exportación

- Los `.dsl` se validan y exportan con Structurizr; cada archivo declara vistas para API, Android y Flutter.
- Los `.puml` se renderizan con PlantUML.
- Los `.erd` contienen sintaxis Mermaid `erDiagram`; cada PNG renderizado se guarda junto a su archivo fuente.
- Los nombres exactos de los PNG esperados aparecen en los placeholders de cada Markdown de 2.6.
'''
    path.write_text(current.rstrip() + addition, encoding="utf-8")


def main() -> None:
    for context in CONTEXTS:
        write_context(context)
    write_main_markdown()
    update_report_readme()
    update_diagram_readme()
    print(f"Generated {len(CONTEXTS)} contexts, {len(CONTEXTS) * 5} diagram sources and 9 report chapters.")


if __name__ == "__main__":
    main()
