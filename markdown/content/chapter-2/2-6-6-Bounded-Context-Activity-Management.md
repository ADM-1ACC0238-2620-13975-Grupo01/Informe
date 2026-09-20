<a id="toc-2-6-6-bounded-context-activity-management"></a>

# 2.6.6. Bounded Context: Activity Management

Planificar actividades ganaderas y sanitarias, controlar su estado y decidir cuándo corresponde generar un recordatorio.

La base implementada se encuentra en el módulo `Activities` de la API ASP.NET Core. El diseño móvil de Android y Flutter se documenta como **no implementado** porque esos clientes todavía no existen en el workspace. Los tres productos comparten contratos REST y lenguaje ubicuo, mientras la API conserva las reglas autoritativas.

<a id="toc-2-6-6-1-domain-layer"></a>

## 2.6.6.1. Domain Layer

**Responsabilidad estable.** Esta capa documenta el modelo que representa el núcleo de **Activity Management**. Las reglas autoritativas se ejecutan en la API; Android y Flutter mantienen modelos equivalentes para presentación, validación inmediata y trabajo offline. La columna de estado distingue el código heredado de la arquitectura objetivo.

### Aggregate Root: FarmActivity

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend; modelo equivalente en Android y Flutter — **Implementado** |
| **Propósito** | Controlar el ciclo de vida de una actividad programada. |
| **Relaciones** | FarmActivity compone ActivitySchedule; FarmActivity se relaciona con ActivityPriority; FarmActivity se relaciona con ActivityStatus; ReminderPolicy depende de FarmActivity; IFarmActivityRepository depende de FarmActivity |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `id` | `int` |
| `ownerId` | `int?` |
| `veterinarianId` | `int?` |
| `animalId` | `int?` |
| `title` | `string` |
| `type` | `string` |
| `schedule` | `ActivitySchedule` |
| `priority` | `ActivityPriority` |
| `status` | `ActivityStatus` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Reschedule(schedule: ActivitySchedule)` | `void` |
| `Complete()` | `void` |
| `Cancel()` | `void` |

### Value Object: ActivitySchedule

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend, Android y Flutter (modelo canónico) — **No implementado** |
| **Propósito** | Representar fecha programada y recordatorio. |
| **Relaciones** | FarmActivity compone ActivitySchedule |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `scheduledAt` | `DateTime` |
| `reminderAt` | `DateTime?` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `IsUpcoming(now: DateTime)` | `bool` |


### Enumeration: ActivityStatus

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend, Android y Flutter (modelo canónico) — **No implementado** |
| **Propósito** | Definir los valores válidos de ActivityStatus. |
| **Relaciones** | FarmActivity se relaciona con ActivityStatus |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `Pending` | `No especificado` |
| `InProgress` | `No especificado` |
| `Completed` | `No especificado` |
| `Cancelled` | `No especificado` |

**Métodos u operaciones**

No aplica.

### Domain Service: ReminderPolicy

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend, Android y Flutter (modelo canónico) — **No implementado** |
| **Propósito** | Decidir cuándo debe emitirse una notificación. |
| **Relaciones** | ReminderPolicy depende de FarmActivity |

**Atributos o dependencias**

No aplica.

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `ShouldNotify(activity: FarmActivity, now: DateTime)` | `bool` |

### Repository Interface: IFarmActivityRepository

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend; modelo equivalente en Android y Flutter — **Implementado** |
| **Propósito** | Abstraer la persistencia de FarmActivity. |
| **Relaciones** | IFarmActivityRepository depende de FarmActivity |

**Atributos o dependencias**

No aplica.

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `FindById(id: int)` | `FarmActivity?` |
| `FindUpcoming(userId: int)` | `List~FarmActivity~` |
| `Add(activity: FarmActivity)` | `void` |
| `Update(activity: FarmActivity)` | `void` |

<a id="toc-2-6-6-2-interface-layer"></a>

## 2.6.6.2. Interface Layer

**Responsabilidad estable.** Esta capa recibe las acciones relacionadas con **programación, reprogramación, finalización y recordatorio de actividades** y las traduce a casos de uso. Los controllers y resources corresponden a la API; las pantallas y controladores de estado representan la presentación objetivo en Android y Flutter. Ninguna de estas clases implementa reglas de negocio.

### REST Controller: FarmActivitiesController

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend ASP.NET Core — **Implementado** |
| **Propósito** | Publicar por HTTP las capacidades de Activity Management. |
| **Relaciones** | Recibe resources, invoca servicios de aplicación y devuelve resources HTTP. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `commandService` | `IFarmActivityCommandService` |
| `queryService` | `IFarmActivityQueryService` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `GetAll(CancellationToken cancellationToken)` | `No especificado` |
| `GetById(int id, CancellationToken cancellationToken)` | `No especificado` |
| `Create(CreateFarmActivityResource resource, CancellationToken cancellationToken)` | `No especificado` |
| `Update(int id, CreateFarmActivityResource resource, CancellationToken cancellationToken)` | `No especificado` |
| `Delete(int id, CancellationToken cancellationToken)` | `No especificado` |




### Presentation Model: FarmActivityViewModel

| Campo | Detalle |
|---|---|
| **Producto y estado** | Android / Kotlin — **No implementado** |
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


### State Controller: FarmActivityController

| Campo | Detalle |
|---|---|
| **Producto y estado** | Flutter / Dart — **No implementado** |
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

<a id="toc-2-6-6-3-application-layer"></a>

## 2.6.6.3. Application Layer

**Responsabilidad estable.** Esta capa coordina las capacidades de **programación, reprogramación, finalización y recordatorio de actividades**. Los commands y queries expresan intenciones; los handlers cargan aggregates, aplican reglas, persisten cambios y reaccionan a eventos. Los casos de uso móviles coordinan lectura local, actualización remota y sincronización idempotente.

### Application Service: FarmActivityCommandService

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend ASP.NET Core — **Implementado** |
| **Propósito** | Orquestar programación, reprogramación, finalización y recordatorio de actividades sin contener reglas del dominio. |
| **Relaciones** | Invoca agregados y repositories; confirma la transacción mediante Unit of Work. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `repository` | `IFarmActivityRepository` |
| `unitOfWork` | `IUnitOfWork` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Handle(CreateFarmActivityCommand command, CancellationToken cancellationToken)` | `No especificado` |
| `Handle(UpdateFarmActivityCommand command, CancellationToken cancellationToken)` | `No especificado` |
| `Handle(DeleteFarmActivityCommand command, CancellationToken cancellationToken)` | `No especificado` |






### Use Case: ObserveFarmActivityUseCase

| Campo | Detalle |
|---|---|
| **Producto y estado** | Android y Flutter — **No implementado** |
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


### Command Handler: CreateFarmActivityCommandHandler

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend ASP.NET Core — **No implementado** |
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


### Event Handler: ActivityScheduledEventHandler

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend ASP.NET Core — **No implementado** |
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

<a id="toc-2-6-6-4-infrastructure-layer"></a>

## 2.6.6.4. Infrastructure Layer

**Responsabilidad estable.** Esta capa implementa los puertos definidos hacia el interior de **Activity Management** y concentra acceso a base de datos, red, almacenamiento local e integraciones externas. Las clases de infraestructura traducen errores y contratos técnicos antes de devolver resultados a Application Layer.

### Repository Adapter: FarmActivityRepository

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend / Entity Framework Core — **Implementado** |
| **Propósito** | Implementar el puerto de persistencia definido por Domain Layer. |
| **Relaciones** | Implementa IFarmActivityRepository; utiliza AppDbContext/MySQL y reconstruye el aggregate. |

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



### Room Adapter: FarmActivityDao

| Campo | Detalle |
|---|---|
| **Producto y estado** | Android / Room — **No implementado** |
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


### SQLite Adapter: FarmActivityLocalDataSource

| Campo | Detalle |
|---|---|
| **Producto y estado** | Flutter / Dart — **No implementado** |
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



### Messaging Adapter: FirebaseReminderPublisher

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend y Android — **No implementado** |
| **Propósito** | Aislar una dependencia externa detrás de un puerto explícito. |
| **Relaciones** | Implementa el puerto de notificaciones mediante FCM y notificaciones locales. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `localNotifier` | `fcmClient,` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Publish(reminder)` | `No especificado` |
| `ScheduleLocal(reminder)` | `No especificado` |

<a id="toc-2-6-6-5-bounded-context-software-architecture-component-level-diagrams"></a>

## 2.6.6.5. Bounded Context Software Architecture Component Level Diagrams

El archivo [`component-level.dsl`](<../../assets/codefordiagrams/2.6.6. Bounded Context Activity Management/component-level.dsl>) contiene las vistas `BC6-ApiComponents`, `BC6-AndroidComponents` y `BC6-FlutterComponents`. Las tres parten del mismo modelo C4 y muestran la separación entre presentación, aplicación, dominio y adaptadores.

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-6-Bounded-Context-Activity-Management/2-6-6-BC6-ApiComponents.svg" alt="Componentes API de Activity Management" width="900">
  <p><i>Figura 2.6.6.1. Componentes de la API para Activity Management. Fuente: elaboración propia con Structurizr DSL.</i></p>
</div>

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-6-Bounded-Context-Activity-Management/2-6-6-BC6-AndroidComponents.svg" alt="Componentes Android de Activity Management" width="900">
  <p><i>Figura 2.6.6.2. Componentes Android para Activity Management. Fuente: elaboración propia con Structurizr DSL.</i></p>
</div>

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-6-Bounded-Context-Activity-Management/2-6-6-BC6-FlutterComponents.svg" alt="Componentes Flutter de Activity Management" width="900">
  <p><i>Figura 2.6.6.3. Componentes Flutter para Activity Management. Fuente: elaboración propia con Structurizr DSL.</i></p>
</div>

<a id="toc-2-6-6-6-bounded-context-software-architecture-code-level-diagrams"></a>

## 2.6.6.6. Bounded Context Software Architecture Code Level Diagrams

Los diagramas de código detallan el modelo del dominio y los objetos de persistencia. El UML diferencia los elementos existentes de las incorporaciones objetivo, mientras los esquemas SQL señalan mediante comentarios las columnas propuestas. Los archivos ERD quedan disponibles para completar la importación manual.

<a id="toc-2-6-6-6-1-bounded-context-domain-layer-class-diagrams"></a>

### 2.6.6.6.1. Bounded Context Domain Layer Class Diagrams

El Class Diagram incluye agregados, entidades, value objects, enumeraciones, servicios de dominio e interfaces de repositorio con atributos, operaciones, visibilidad y multiplicidades.

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-6-Bounded-Context-Activity-Management/2-6-6-domain-layer-class-diagram.svg" alt="Class Diagram de Activity Management" width="900">
  <p><i>Figura 2.6.6.4. Domain Layer Class Diagram de Activity Management. Fuente: elaboración propia con PlantUML.</i></p>
</div>

<a id="toc-2-6-6-6-2-bounded-context-database-design-diagram"></a>

### 2.6.6.6.2. Bounded Context Database Design Diagram

MySQL mantiene la persistencia autoritativa. Room y SQLite contienen únicamente caché, metadatos de sincronización y operaciones pendientes; no sustituyen las reglas ni la fuente de verdad del backend. En IAM, las credenciales y tokens permanecen fuera de las tablas locales y se almacenan mediante mecanismos seguros del sistema operativo.

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-6-Bounded-Context-Activity-Management/2-6-6-mysql-database-design.png" alt="MySQL Database Diagram de Activity Management" width="900">
  <p><i>Figura 2.6.6.5. MySQL Database Design de Activity Management. Fuente: elaboración propia a partir del esquema SQL.</i></p>
</div>

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-6-Bounded-Context-Activity-Management/2-6-6-android-room-database-design.png" alt="Room Database Diagram de Activity Management" width="900">
  <p><i>Figura 2.6.6.6. Android Room Database Design de Activity Management. Fuente: elaboración propia a partir del esquema SQL.</i></p>
</div>
