<a id="toc-2-6-2-bounded-context-profile-management"></a>

# 2.6.2. Bounded Context: Profile Management

Mantener la información personal y de contacto asociada con una identidad sin mezclarla con credenciales o reglas de autenticación.

La base implementada se encuentra en el módulo `Profiles` de la API ASP.NET Core. El diseño móvil de Android y Flutter se presenta como **diseño objetivo** porque esos clientes todavía no existen en el workspace. Los tres productos comparten contratos REST y lenguaje ubicuo, mientras la API conserva las reglas autoritativas.

<a id="toc-2-6-2-1-domain-layer"></a>

## 2.6.2.1. Domain Layer

**Responsabilidad estable.** Esta capa documenta el modelo que representa el núcleo de **Profile Management**. Las reglas autoritativas se ejecutan en la API; Android y Flutter mantienen modelos equivalentes para presentación, validación inmediata y trabajo offline. La columna de estado distingue el código heredado de la arquitectura objetivo.

### Aggregate Root: Profile

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend; modelo equivalente en Android y Flutter — **Implementado en el backend** |
| **Propósito** | Mantener la información personal y de contacto de un propietario. |
| **Relaciones** | Profile compone PersonName; Profile compone EmailAddress; Profile compone StreetAddress; IProfileRepository depende de Profile : persists |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `id` | `int` |
| `ownerId` | `int` |
| `name` | `PersonName` |
| `email` | `EmailAddress` |
| `address` | `StreetAddress` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `FullName()` | `string` |
| `ChangeEmail(email: EmailAddress)` | `void` |
| `ChangeAddress(address: StreetAddress)` | `void` |

### Value Object: PersonName

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend; modelo equivalente en Android y Flutter — **Implementado en el backend** |
| **Propósito** | Representar un nombre personal válido. |
| **Relaciones** | Profile compone PersonName |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `firstName` | `string` |
| `lastName` | `string` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `FullName()` | `string` |

### Value Object: EmailAddress

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend; modelo equivalente en Android y Flutter — **Implementado en el backend** |
| **Propósito** | Representar y validar un correo electrónico. |
| **Relaciones** | Profile compone EmailAddress |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `address` | `string` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `IsValid()` | `bool` |

### Value Object: StreetAddress

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend; modelo equivalente en Android y Flutter — **Implementado en el backend** |
| **Propósito** | Representar una dirección postal completa. |
| **Relaciones** | Profile compone StreetAddress |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `street` | `string` |
| `number` | `string` |
| `city` | `string` |
| `postalCode` | `string` |
| `country` | `string` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `FullAddress()` | `string` |

### Repository Interface: IProfileRepository

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend; modelo equivalente en Android y Flutter — **Implementado en el backend** |
| **Propósito** | Abstraer la persistencia de Profile. |
| **Relaciones** | IProfileRepository depende de Profile : persists |

**Atributos o dependencias**

No aplica.

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `FindById(id: int)` | `Profile?` |
| `FindByOwnerId(ownerId: int)` | `Profile?` |
| `Add(profile: Profile)` | `void` |
| `Update(profile: Profile)` | `void` |



<a id="toc-2-6-2-2-interface-layer"></a>

## 2.6.2.2. Interface Layer

**Responsabilidad estable.** Esta capa recibe las acciones relacionadas con **creación, actualización y consulta de perfiles** y las traduce a casos de uso. Los controllers y resources corresponden a la API; las pantallas y controladores de estado representan la presentación objetivo en Android y Flutter. Ninguna de estas clases implementa reglas de negocio.

### REST Controller: ProfilesController

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend ASP.NET Core — **Implementado en el backend** |
| **Propósito** | Publicar por HTTP las capacidades de Profile Management. |
| **Relaciones** | Recibe resources, invoca servicios de aplicación y devuelve resources HTTP. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `profileCommandService` | `IProfileCommandService` |
| `profileQueryService` | `IProfileQueryService` |
| `errorLocalizer` | `IStringLocalizer<ErrorMessages>` |
| `problemDetailsFactory` | `ProblemDetailsFactory` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `GetProfileById(int profileId, CancellationToken cancellationToken)` | `No especificado` |
| `CreateProfile(CreateProfileResource resource, CancellationToken cancellationToken)` | `No especificado` |
| `GetAllProfiles(CancellationToken cancellationToken)` | `No especificado` |




### Presentation Model: ProfileViewModel

| Campo | Detalle |
|---|---|
| **Producto y estado** | Android / Kotlin — **Diseño objetivo** |
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


### State Controller: ProfileController

| Campo | Detalle |
|---|---|
| **Producto y estado** | Flutter / Dart — **Diseño objetivo** |
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

<a id="toc-2-6-2-3-application-layer"></a>

## 2.6.2.3. Application Layer

**Responsabilidad estable.** Esta capa coordina las capacidades de **creación, actualización y consulta de perfiles**. Los commands y queries expresan intenciones; los handlers cargan aggregates, aplican reglas, persisten cambios y reaccionan a eventos. Los casos de uso móviles coordinan lectura local, actualización remota y sincronización idempotente.

### Application Service: ProfileCommandService

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend ASP.NET Core — **Implementado en el backend** |
| **Propósito** | Orquestar creación, actualización y consulta de perfiles sin contener reglas del dominio. |
| **Relaciones** | Invoca agregados y repositories; confirma la transacción mediante Unit of Work. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `profileRepository` | `IProfileRepository` |
| `unitOfWork` | `IUnitOfWork` |
| `localizer` | `IStringLocalizer<ErrorMessages>` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Handle(CreateProfileCommand command, CancellationToken cancellationToken)` | `No especificado` |






### Use Case: ObserveProfileUseCase

| Campo | Detalle |
|---|---|
| **Producto y estado** | Android y Flutter — **Diseño objetivo** |
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


### Command Handler: CreateProfileCommandHandler

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend ASP.NET Core — **Diseño objetivo** |
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


### Event Handler: ProfileUpdatedEventHandler

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend ASP.NET Core — **Diseño objetivo** |
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

<a id="toc-2-6-2-4-infrastructure-layer"></a>

## 2.6.2.4. Infrastructure Layer

**Responsabilidad estable.** Esta capa implementa los puertos definidos hacia el interior de **Profile Management** y concentra acceso a base de datos, red, almacenamiento local e integraciones externas. Las clases de infraestructura traducen errores y contratos técnicos antes de devolver resultados a Application Layer.

### Repository Adapter: ProfileRepository

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend / Entity Framework Core — **Implementado en el backend** |
| **Propósito** | Implementar el puerto de persistencia definido por Domain Layer. |
| **Relaciones** | Implementa IProfileRepository; utiliza AppDbContext/MySQL y reconstruye el aggregate. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `context` | `AppDbContext` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `FindProfileByEmailAsync(EmailAddress email, CancellationToken cancellationToken)` | `No especificado` |



### Room Adapter: ProfileDao

| Campo | Detalle |
|---|---|
| **Producto y estado** | Android / Room — **Diseño objetivo** |
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


### SQLite Adapter: ProfileLocalDataSource

| Campo | Detalle |
|---|---|
| **Producto y estado** | Flutter / Dart — **Diseño objetivo** |
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

### Context Adapter: IamProfileOwnerAdapter

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend ASP.NET Core — **Diseño objetivo** |
| **Propósito** | Aislar una dependencia externa detrás de un puerto explícito. |
| **Relaciones** | Implementa el puerto de verificación del propietario y consume IAM Context Facade. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `iamFacade` | `No especificado` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Exists(ownerId)` | `bool` |


<a id="toc-2-6-2-5-bounded-context-software-architecture-component-level-diagrams"></a>

## 2.6.2.5. Bounded Context Software Architecture Component Level Diagrams

El archivo [`component-level.dsl`](<../../assets/codefordiagrams/2.6.2. Bounded Context Profile Management/component-level.dsl>) contiene las vistas `BC2-ApiComponents`, `BC2-AndroidComponents` y `BC2-FlutterComponents`. Las tres parten del mismo modelo C4 y muestran la separación entre presentación, aplicación, dominio y adaptadores.

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-2-Bounded-Context-Profile-Management/2-6-2-BC2-ApiComponents.svg" alt="Componentes API de Profile Management" width="900">
  <p><i>Figura 2.6.2.1. Componentes de la API para Profile Management. Fuente: elaboración propia con Structurizr DSL.</i></p>
</div>

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-2-Bounded-Context-Profile-Management/2-6-2-BC2-AndroidComponents.svg" alt="Componentes Android de Profile Management" width="900">
  <p><i>Figura 2.6.2.2. Componentes Android para Profile Management. Fuente: elaboración propia con Structurizr DSL.</i></p>
</div>

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-2-Bounded-Context-Profile-Management/2-6-2-BC2-FlutterComponents.svg" alt="Componentes Flutter de Profile Management" width="900">
  <p><i>Figura 2.6.2.3. Componentes Flutter para Profile Management. Fuente: elaboración propia con Structurizr DSL.</i></p>
</div>

<a id="toc-2-6-2-6-bounded-context-software-architecture-code-level-diagrams"></a>

## 2.6.2.6. Bounded Context Software Architecture Code Level Diagrams

Los diagramas de código detallan el modelo del dominio y los objetos de persistencia. El UML diferencia los elementos existentes de las incorporaciones objetivo, mientras los esquemas SQL señalan mediante comentarios las columnas propuestas. Los archivos ERD quedan disponibles para completar la importación manual.

<a id="toc-2-6-2-6-1-bounded-context-domain-layer-class-diagrams"></a>

### 2.6.2.6.1. Bounded Context Domain Layer Class Diagrams

El Class Diagram incluye agregados, entidades, value objects, enumeraciones, servicios de dominio e interfaces de repositorio con atributos, operaciones, visibilidad y multiplicidades.

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-2-Bounded-Context-Profile-Management/2-6-2-domain-layer-class-diagram.svg" alt="Class Diagram de Profile Management" width="900">
  <p><i>Figura 2.6.2.4. Domain Layer Class Diagram de Profile Management. Fuente: elaboración propia con PlantUML.</i></p>
</div>

<a id="toc-2-6-2-6-2-bounded-context-database-design-diagram"></a>

### 2.6.2.6.2. Bounded Context Database Design Diagram

MySQL mantiene la persistencia autoritativa. Room y SQLite contienen únicamente caché, metadatos de sincronización y operaciones pendientes; no sustituyen las reglas ni la fuente de verdad del backend. En IAM, las credenciales y tokens permanecen fuera de las tablas locales y se almacenan mediante mecanismos seguros del sistema operativo.

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-2-Bounded-Context-Profile-Management/2-6-2-mysql-database-design.png" alt="MySQL Database Diagram de Profile Management" width="900">
  <p><i>Figura 2.6.2.5. MySQL Database Design de Profile Management. Fuente: elaboración propia a partir del esquema SQL.</i></p>
</div>

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-2-Bounded-Context-Profile-Management/2-6-2-android-room-database-design.png" alt="Room Database Diagram de Profile Management" width="900">
  <p><i>Figura 2.6.2.6. Android Room Database Design de Profile Management. Fuente: elaboración propia a partir del esquema SQL.</i></p>
</div>
