<a id="toc-2-6-4-bounded-context-sanitary-management"></a>

# 2.6.4. Bounded Context: Sanitary Management

Conservar la historia sanitaria del animal y controlar el registro de diagnósticos, tratamientos, prescripciones y seguimientos autorizados.

La base implementada se encuentra en el módulo `Sanitary` de la API ASP.NET Core. El diseño móvil de Android y Flutter se presenta como **diseño objetivo** porque esos clientes todavía no existen en el workspace. Los tres productos comparten contratos REST y lenguaje ubicuo, mientras la API conserva las reglas autoritativas.

<a id="toc-2-6-4-1-domain-layer"></a>

## 2.6.4.1. Domain Layer

**Responsabilidad estable.** Esta capa documenta el modelo que representa el núcleo de **Sanitary Management**. Las reglas autoritativas se ejecutan en la API; Android y Flutter mantienen modelos equivalentes para presentación, validación inmediata y trabajo offline. La columna de estado distingue el código heredado de la arquitectura objetivo.

**Detalle técnico evolutivo.** El siguiente diccionario identifica las clases, sus responsabilidades, atributos, métodos y relaciones. Los campos **Producto** y **Estado** distinguen los elementos comprobados en el código de aquellos que aún pertenecen al diseño objetivo.

### Aggregate Root: HealthEvent

| Campo | Detalle |
|---|---|
| **Producto** | Backend; modelo equivalente en Android y Flutter |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Mantener un acontecimiento clínico dentro de la historia sanitaria. |
| **Relaciones** | HealthEvent compone Diagnosis; HealthEvent compone Treatment; HealthEvent compone Prescription; HealthEvent se relaciona con HealthEventType; SanitaryAuthorizationPolicy depende de HealthEvent; IHealthEventRepository depende de HealthEvent |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `id` | `int` |
| `animalId` | `int` |
| `type` | `HealthEventType` |
| `date` | `Date` |
| `veterinarianId` | `int?` |
| `description` | `string` |
| `diagnosis` | `Diagnosis` |
| `treatment` | `Treatment` |
| `prescription` | `Prescription` |
| `nextDueDate` | `Date?` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `RescheduleFollowUp(date: Date)` | `void` |
| `UpdateClinicalData(diagnosis: Diagnosis, treatment: Treatment)` | `void` |

---

### Value Object: Diagnosis

| Campo | Detalle |
|---|---|
| **Producto** | Backend, Android y Flutter (modelo canónico) |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Representar el diagnóstico clínico. |
| **Relaciones** | HealthEvent compone Diagnosis |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `description` | `string` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `IsEmpty()` | `bool` |

---

### Value Object: Treatment

| Campo | Detalle |
|---|---|
| **Producto** | Backend, Android y Flutter (modelo canónico) |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Representar instrucciones de tratamiento. |
| **Relaciones** | HealthEvent compone Treatment |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `instructions` | `string` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `IsValid()` | `bool` |

---

### Value Object: Prescription

| Campo | Detalle |
|---|---|
| **Producto** | Backend, Android y Flutter (modelo canónico) |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Representar la prescripción asociada a un evento sanitario. |
| **Relaciones** | HealthEvent compone Prescription |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `details` | `string` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `IsRequired()` | `bool` |

---

### Enumeration: HealthEventType

| Campo | Detalle |
|---|---|
| **Producto** | Backend y modelos equivalentes Android/Flutter |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Definir los valores válidos de HealthEventType. |
| **Relaciones** | HealthEvent se relaciona con HealthEventType |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `MedicalVisit` | `No especificado` |
| `Vaccination` | `No especificado` |
| `Treatment` | `No especificado` |
| `SanitaryControl` | `No especificado` |

**Métodos u operaciones**

No aplica.

---

### Domain Service: SanitaryAuthorizationPolicy

| Campo | Detalle |
|---|---|
| **Producto** | Backend, Android y Flutter (modelo canónico) |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Decidir si un actor puede registrar información sanitaria. |
| **Relaciones** | SanitaryAuthorizationPolicy depende de HealthEvent |

**Atributos o dependencias**

No aplica.

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `CanRegister(actorId: int, animalId: int)` | `bool` |

---

### Repository Interface: IHealthEventRepository

| Campo | Detalle |
|---|---|
| **Producto** | Backend; modelo equivalente en Android y Flutter |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Abstraer la persistencia de HealthEvent. |
| **Relaciones** | IHealthEventRepository depende de HealthEvent |

**Atributos o dependencias**

No aplica.

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `FindById(id: int)` | `HealthEvent?` |
| `FindByAnimal(animalId: int)` | `List~HealthEvent~` |
| `Add(event: HealthEvent)` | `void` |
| `Update(event: HealthEvent)` | `void` |

---

### Entity: MedicalVisit

| Campo | Detalle |
|---|---|
| **Producto** | Backend; modelo equivalente en Android y Flutter |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Representar una visita veterinaria asociada con el historial sanitario. |
| **Relaciones** | Pertenece a HealthEvent y referencia al veterinario autorizado. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `id` | `int` |
| `healthEventId` | `int` |
| `veterinarianId` | `int` |
| `scheduledAt` | `DateTime` |
| `status` | `string` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Reschedule(date)` | `No especificado` |
| `Complete()` | `No especificado` |

---

### Entity: SanitaryAlert

| Campo | Detalle |
|---|---|
| **Producto** | Backend; modelo equivalente en Android y Flutter |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Representar una alerta por vacunación, tratamiento o seguimiento pendiente. |
| **Relaciones** | Se origina desde HealthEvent y puede generar una actividad. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `id` | `int` |
| `animalId` | `int` |
| `dueDate` | `Date` |
| `severity` | `string` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `IsDue(on: Date)` | `bool` |
| `Dismiss()` | `No especificado` |

---

<a id="toc-2-6-4-2-interface-layer"></a>

## 2.6.4.2. Interface Layer

**Responsabilidad estable.** Esta capa recibe las acciones relacionadas con **registro y seguimiento de eventos sanitarios, diagnósticos y tratamientos** y las traduce a casos de uso. Los controllers y resources corresponden a la API; las pantallas y controladores de estado representan la presentación objetivo en Android y Flutter. Ninguna de estas clases implementa reglas de negocio.

**Detalle técnico evolutivo.** El siguiente diccionario identifica las clases, sus responsabilidades, atributos, métodos y relaciones. Los campos **Producto** y **Estado** distinguen los elementos comprobados en el código de aquellos que aún pertenecen al diseño objetivo.

### REST Controller: HealthEventsController

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Publicar por HTTP las capacidades de Sanitary Management. |
| **Relaciones** | Recibe resources, invoca servicios de aplicación y devuelve resources HTTP. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `commandService` | `IHealthEventCommandService` |
| `queryService` | `IHealthEventQueryService` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `GetAll(CancellationToken cancellationToken)` | `No especificado` |
| `GetById(int id, CancellationToken cancellationToken)` | `No especificado` |
| `Create(CreateHealthEventResource resource, CancellationToken cancellationToken)` | `No especificado` |
| `Update(int id, CreateHealthEventResource resource, CancellationToken cancellationToken)` | `No especificado` |
| `Delete(int id, CancellationToken cancellationToken)` | `No especificado` |

---

### Resource/Assembler: CreateHealthEventResource

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Definir un contrato estable de entrada o salida para la API REST. |
| **Relaciones** | Es construido o traducido por assemblers y consumido por el controller y los clientes móviles. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `AnimalId` | `int` |
| `Type` | `string` |
| `Date` | `DateOnly` |
| `Description` | `string` |
| `Veterinarian` | `string` |
| `Diagnosis` | `string` |
| `Treatment` | `string` |
| `Prescription` | `string` |
| `FollowUp` | `string` |
| `NextDueDate` | `DateOnly?` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Create(...)` | `No especificado` |
| `Deconstruct(...)` | `No especificado` |

---

### Resource/Assembler: HealthEventResource

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Definir un contrato estable de entrada o salida para la API REST. |
| **Relaciones** | Es construido o traducido por assemblers y consumido por el controller y los clientes móviles. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `Id` | `int` |
| `AnimalId` | `int` |
| `Type` | `string` |
| `Date` | `DateOnly` |
| `Description` | `string` |
| `Veterinarian` | `string` |
| `Diagnosis` | `string` |
| `Treatment` | `string` |
| `Prescription` | `string` |
| `FollowUp` | `string` |
| `NextDueDate` | `DateOnly?` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Create(...)` | `No especificado` |
| `Deconstruct(...)` | `No especificado` |

---

### Composable: HealthEventScreen

| Campo | Detalle |
|---|---|
| **Producto** | Android / Jetpack Compose |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Presentar registro y seguimiento de eventos sanitarios, diagnósticos y tratamientos en Android. |
| **Relaciones** | Observa HealthEventViewModel y emite acciones de interfaz. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `uiState` | `No especificado` |
| `onAction` | `No especificado` |
| `navigation` | `No especificado` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Render()` | `No especificado` |
| `Submit()` | `No especificado` |
| `Retry()` | `No especificado` |

---

### Presentation Model: HealthEventViewModel

| Campo | Detalle |
|---|---|
| **Producto** | Android / Kotlin |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Mantener el estado observable y traducir acciones de Android a casos de uso. |
| **Relaciones** | Invoca casos de uso de Application Layer y publica un UI State inmutable. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `state` | `No especificado` |
| `observeUseCase` | `No especificado` |
| `syncUseCase` | `No especificado` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Load()` | `No especificado` |
| `Submit(action)` | `No especificado` |
| `RetrySync()` | `No especificado` |

---

### Widget: HealthEventPage

| Campo | Detalle |
|---|---|
| **Producto** | Flutter / Dart |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Presentar registro y seguimiento de eventos sanitarios, diagnósticos y tratamientos en Flutter. |
| **Relaciones** | Observa HealthEventController y emite intenciones del usuario. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `state` | `No especificado` |
| `onAction` | `No especificado` |
| `router` | `No especificado` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `build(context)` | `No especificado` |
| `submit()` | `No especificado` |
| `retry()` | `No especificado` |

---

### State Controller: HealthEventController

| Campo | Detalle |
|---|---|
| **Producto** | Flutter / Dart |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Mantener el estado de presentación de Flutter y coordinar casos de uso. |
| **Relaciones** | Invoca Application Layer y publica estados de carga, éxito y error. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `state` | `No especificado` |
| `observeUseCase` | `No especificado` |
| `syncUseCase` | `No especificado` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `load()` | `No especificado` |
| `submit(action)` | `No especificado` |
| `retrySync()` | `No especificado` |

---

<a id="toc-2-6-4-3-application-layer"></a>

## 2.6.4.3. Application Layer

**Responsabilidad estable.** Esta capa coordina las capacidades de **registro y seguimiento de eventos sanitarios, diagnósticos y tratamientos**. Los commands y queries expresan intenciones; los handlers cargan aggregates, aplican reglas, persisten cambios y reaccionan a eventos. Los casos de uso móviles coordinan lectura local, actualización remota y sincronización idempotente.

**Detalle técnico evolutivo.** El siguiente diccionario identifica las clases, sus responsabilidades, atributos, métodos y relaciones. Los campos **Producto** y **Estado** distinguen los elementos comprobados en el código de aquellos que aún pertenecen al diseño objetivo.

### Application Service: HealthEventCommandService

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Orquestar registro y seguimiento de eventos sanitarios, diagnósticos y tratamientos sin contener reglas del dominio. |
| **Relaciones** | Invoca agregados y repositories; confirma la transacción mediante Unit of Work. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `repository` | `IHealthEventRepository` |
| `unitOfWork` | `IUnitOfWork` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Handle(CreateHealthEventCommand command, CancellationToken cancellationToken)` | `No especificado` |
| `Handle(UpdateHealthEventCommand command, CancellationToken cancellationToken)` | `No especificado` |
| `Handle(DeleteHealthEventCommand command, CancellationToken cancellationToken)` | `No especificado` |

---

### Application Service: HealthEventQueryService

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Orquestar registro y seguimiento de eventos sanitarios, diagnósticos y tratamientos sin contener reglas del dominio. |
| **Relaciones** | Invoca agregados y repositories; confirma la transacción mediante Unit of Work. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `repository` | `IHealthEventRepository` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Handle(GetHealthEventByIdQuery query, CancellationToken cancellationToken)` | `No especificado` |
| `Handle(GetAllHealthEventsQuery query, CancellationToken cancellationToken)` | `No especificado` |

---

### Command/Query: CreateHealthEventCommand

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Transportar una intención o consulta tipada hacia su handler. |
| **Relaciones** | Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `AnimalId` | `int` |
| `Type` | `string` |
| `Date` | `DateOnly` |
| `Description` | `string` |
| `Veterinarian` | `string` |
| `Diagnosis` | `string` |
| `Treatment` | `string` |
| `Prescription` | `string` |
| `FollowUp` | `string` |
| `NextDueDate` | `DateOnly?` |

**Métodos u operaciones**

No aplica.

---

### Command/Query: UpdateHealthEventCommand

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Transportar una intención o consulta tipada hacia su handler. |
| **Relaciones** | Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `Id` | `int` |
| `AnimalId` | `int` |
| `Type` | `string` |
| `Date` | `DateOnly` |
| `Description` | `string` |
| `Veterinarian` | `string` |
| `Diagnosis` | `string` |
| `Treatment` | `string` |
| `Prescription` | `string` |
| `FollowUp` | `string` |
| `NextDueDate` | `DateOnly?` |

**Métodos u operaciones**

No aplica.

---

### Command/Query: DeleteHealthEventCommand

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Transportar una intención o consulta tipada hacia su handler. |
| **Relaciones** | Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `Id` | `int` |

**Métodos u operaciones**

No aplica.

---

### Command/Query: GetHealthEventByIdQuery

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Transportar una intención o consulta tipada hacia su handler. |
| **Relaciones** | Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `Id` | `int` |

**Métodos u operaciones**

No aplica.

---

### Use Case: ObserveHealthEventUseCase

| Campo | Detalle |
|---|---|
| **Producto** | Android y Flutter |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Entregar primero datos locales y actualizar la consulta cuando exista conectividad. |
| **Relaciones** | Es invocado por ViewModel/Controller y coordina repositorios móviles. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `localRepository` | `No especificado` |
| `remoteRepository` | `No especificado` |
| `connectivityMonitor` | `No especificado` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Execute(criteria)` | `Stream<Result>` |

---

### Use Case: SyncHealthEventUseCase

| Campo | Detalle |
|---|---|
| **Producto** | Android y Flutter |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Procesar operaciones móviles pendientes de manera idempotente. |
| **Relaciones** | Lee el outbox local, consume la API y actualiza el estado de sincronización. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `outboxRepository` | `No especificado` |
| `remoteRepository` | `No especificado` |
| `conflictResolver` | `No especificado` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Execute()` | `SyncResult` |

---

### Command Handler: CreateHealthEventCommandHandler

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Ejecutar una intención concreta, aplicar reglas del agregado y confirmar la transacción. |
| **Relaciones** | Consume un Command, carga el aggregate mediante su repository y puede publicar un Domain Event. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `repository` | `No especificado` |
| `unitOfWork` | `No especificado` |
| `domainPolicy` | `No especificado` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Handle(command)` | `Result` |

---

### Command Handler: UpdateHealthEventCommandHandler

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Ejecutar una intención concreta, aplicar reglas del agregado y confirmar la transacción. |
| **Relaciones** | Consume un Command, carga el aggregate mediante su repository y puede publicar un Domain Event. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `repository` | `No especificado` |
| `unitOfWork` | `No especificado` |
| `domainPolicy` | `No especificado` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Handle(command)` | `Result` |

---

### Event Handler: HealthEventRegisteredEventHandler

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Reaccionar al evento confirmado y actualizar proyecciones o integraciones. |
| **Relaciones** | Consume un Domain Event y utiliza puertos de infraestructura sin modificar directamente el agregado. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `projectionRepository` | `No especificado` |
| `notificationPort` | `No especificado` |
| `unitOfWork` | `No especificado` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Handle(domainEvent)` | `Task` |

---

<a id="toc-2-6-4-4-infrastructure-layer"></a>

## 2.6.4.4. Infrastructure Layer

**Responsabilidad estable.** Esta capa implementa los puertos definidos hacia el interior de **Sanitary Management** y concentra acceso a base de datos, red, almacenamiento local e integraciones externas. Las clases de infraestructura traducen errores y contratos técnicos antes de devolver resultados a Application Layer.

**Detalle técnico evolutivo.** El siguiente diccionario identifica las clases, sus responsabilidades, atributos, métodos y relaciones. Los campos **Producto** y **Estado** distinguen los elementos comprobados en el código de aquellos que aún pertenecen al diseño objetivo.

### Repository Adapter: HealthEventRepository

| Campo | Detalle |
|---|---|
| **Producto** | Backend / Entity Framework Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Implementar el puerto de persistencia definido por Domain Layer. |
| **Relaciones** | Implementa IHealthEventRepository; utiliza AppDbContext/MySQL y reconstruye el aggregate. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `context` | `AppDbContext` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `FindById(id)` | `No especificado` |
| `Add(entity)` | `No especificado` |
| `Update(entity)` | `No especificado` |
| `Delete(entity)` | `No especificado` |

---

### Persistence Configuration: ModelBuilderExtensions

| Campo | Detalle |
|---|---|
| **Producto** | Backend / Entity Framework Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Mapear entidades y value objects del contexto al modelo relacional. |
| **Relaciones** | Configura tablas, claves, relaciones, restricciones y conversiones de Entity Framework Core. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `configuration` | `EntityTypeBuilder` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `ApplyConfiguration(modelBuilder)` | `No especificado` |

---

### Remote Adapter: HealthEventApiDataSource

| Campo | Detalle |
|---|---|
| **Producto** | Android / Kotlin |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Implementar el acceso remoto del cliente móvil a la API. |
| **Relaciones** | Consume controllers REST por HTTPS/JSON y traduce errores HTTP al modelo de aplicación. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `httpClient` | `No especificado` |
| `tokenProvider` | `No especificado` |
| `serializer` | `No especificado` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Get(criteria)` | `No especificado` |
| `Create(dto)` | `No especificado` |
| `Update(dto)` | `No especificado` |
| `Delete(id)` | `No especificado` |

---

### Room Adapter: HealthEventDao

| Campo | Detalle |
|---|---|
| **Producto** | Android / Room |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Implementar persistencia local y observación reactiva en Android. |
| **Relaciones** | Implementa el puerto local mediante Room y participa en la estrategia de caché/outbox. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `roomDatabase` | `No especificado` |
| `entityMapper` | `No especificado` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Observe(criteria)` | `No especificado` |
| `Upsert(entity)` | `No especificado` |
| `Delete(id)` | `No especificado` |
| `Pending()` | `No especificado` |

---

### Remote Adapter: HealthEventRemoteDataSource

| Campo | Detalle |
|---|---|
| **Producto** | Flutter / Dart |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Implementar el acceso remoto del cliente móvil a la API. |
| **Relaciones** | Consume controllers REST por HTTPS/JSON y traduce errores HTTP al modelo de aplicación. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `httpClient` | `No especificado` |
| `tokenProvider` | `No especificado` |
| `serializer` | `No especificado` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Get(criteria)` | `No especificado` |
| `Create(dto)` | `No especificado` |
| `Update(dto)` | `No especificado` |
| `Delete(id)` | `No especificado` |

---

### SQLite Adapter: HealthEventLocalDataSource

| Campo | Detalle |
|---|---|
| **Producto** | Flutter / Dart |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Implementar persistencia local equivalente en Flutter. |
| **Relaciones** | Implementa el puerto local mediante SQLite y participa en la estrategia de caché/outbox. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `sqliteDatabase` | `No especificado` |
| `entityMapper` | `No especificado` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `watch(criteria)` | `No especificado` |
| `upsert(entity)` | `No especificado` |
| `delete(id)` | `No especificado` |
| `pending()` | `No especificado` |

---

### Context Adapter: LivestockAnimalAdapter

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Aislar una dependencia externa detrás de un puerto explícito. |
| **Relaciones** | Implementa el puerto de consulta de animales y consume Livestock Management. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `livestockFacade` | `No especificado` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `GetAnimal(animalId)` | `No especificado` |
| `Exists(animalId)` | `bool` |

---

### Context Adapter: VeterinaryAuthorizationAdapter

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Aislar una dependencia externa detrás de un puerto explícito. |
| **Relaciones** | Implementa el puerto de autorización y consume Veterinary Collaboration. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `collaborationFacade` | `No especificado` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `CanWrite(veterinarianId, animalId)` | `bool` |

---

### Offline Adapter: SanitaryOutboxStore

| Campo | Detalle |
|---|---|
| **Producto** | Android y Flutter |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Aislar una dependencia externa detrás de un puerto explícito. |
| **Relaciones** | Implementa el puerto de sincronización sanitaria sobre Room o SQLite. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `serializer` | `database,` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Enqueue(event)` | `No especificado` |
| `Pending()` | `No especificado` |
| `MarkSynced(id)` | `No especificado` |

---

<a id="toc-2-6-4-5-bounded-context-software-architecture-component-level-diagrams"></a>

## 2.6.4.5. Bounded Context Software Architecture Component Level Diagrams

El archivo [`component-level.dsl`](<../../assets/codefordiagrams/2.6.4. Bounded Context Sanitary Management/component-level.dsl>) contiene las vistas `BC4-ApiComponents`, `BC4-AndroidComponents` y `BC4-FlutterComponents`. Las tres parten del mismo modelo C4 y muestran la separación entre presentación, aplicación, dominio y adaptadores.

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-4-Bounded-Context-Sanitary-Management/2-6-4-BC4-ApiComponents.svg" alt="Componentes API de Sanitary Management" width="900">
  <p><i>Figura 2.6.4.1. Componentes de la API para Sanitary Management. Fuente: elaboración propia con Structurizr DSL.</i></p>
</div>

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-4-Bounded-Context-Sanitary-Management/2-6-4-BC4-AndroidComponents.svg" alt="Componentes Android de Sanitary Management" width="900">
  <p><i>Figura 2.6.4.2. Componentes Android para Sanitary Management. Fuente: elaboración propia con Structurizr DSL.</i></p>
</div>

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-4-Bounded-Context-Sanitary-Management/2-6-4-BC4-FlutterComponents.svg" alt="Componentes Flutter de Sanitary Management" width="900">
  <p><i>Figura 2.6.4.3. Componentes Flutter para Sanitary Management. Fuente: elaboración propia con Structurizr DSL.</i></p>
</div>

<a id="toc-2-6-4-6-bounded-context-software-architecture-code-level-diagrams"></a>

## 2.6.4.6. Bounded Context Software Architecture Code Level Diagrams

Los diagramas de código detallan el modelo del dominio y los objetos de persistencia. El UML diferencia los elementos existentes de las incorporaciones objetivo, mientras los esquemas SQL señalan mediante comentarios las columnas propuestas. Los archivos ERD quedan disponibles para completar la importación manual.

<a id="toc-2-6-4-6-1-bounded-context-domain-layer-class-diagrams"></a>

### 2.6.4.6.1. Bounded Context Domain Layer Class Diagrams

El Class Diagram incluye agregados, entidades, value objects, enumeraciones, servicios de dominio e interfaces de repositorio con atributos, operaciones, visibilidad y multiplicidades.

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-4-Bounded-Context-Sanitary-Management/2-6-4-domain-layer-class-diagram.svg" alt="Class Diagram de Sanitary Management" width="900">
  <p><i>Figura 2.6.4.4. Domain Layer Class Diagram de Sanitary Management. Fuente: elaboración propia con PlantUML.</i></p>
</div>

<a id="toc-2-6-4-6-2-bounded-context-database-design-diagram"></a>

### 2.6.4.6.2. Bounded Context Database Design Diagram

MySQL mantiene la persistencia autoritativa. Room y SQLite contienen únicamente caché, metadatos de sincronización y operaciones pendientes; no sustituyen las reglas ni la fuente de verdad del backend. En IAM, las credenciales y tokens permanecen fuera de las tablas locales y se almacenan mediante mecanismos seguros del sistema operativo.

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-4-Bounded-Context-Sanitary-Management/2-6-4-mysql-database-design.png" alt="MySQL Database Diagram de Sanitary Management" width="900">
  <p><i>Figura 2.6.4.5. MySQL Database Design de Sanitary Management. Fuente: elaboración propia a partir del esquema SQL.</i></p>
</div>

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-4-Bounded-Context-Sanitary-Management/2-6-4-android-room-database-design.png" alt="Room Database Diagram de Sanitary Management" width="900">
  <p><i>Figura 2.6.4.6. Android Room Database Design de Sanitary Management. Fuente: elaboración propia a partir del esquema SQL.</i></p>
</div>


