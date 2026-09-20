<a id="toc-2-6-5-bounded-context-veterinary-collaboration"></a>

# 2.6.5. Bounded Context: Veterinary Collaboration

Administrar solicitudes y autorizaciones entre ganaderos y veterinarios, delimitando clientes, pacientes y alcance de acceso.

La base implementada se encuentra en el módulo `Clients` de la API ASP.NET Core. El diseño móvil de Android y Flutter se presenta como **diseño objetivo** porque esos clientes todavía no existen en el workspace. Los tres productos comparten contratos REST y lenguaje ubicuo, mientras la API conserva las reglas autoritativas.

<a id="toc-2-6-5-1-domain-layer"></a>

## 2.6.5.1. Domain Layer

**Responsabilidad estable.** Esta capa documenta el modelo que representa el núcleo de **Veterinary Collaboration**. Las reglas autoritativas se ejecutan en la API; Android y Flutter mantienen modelos equivalentes para presentación, validación inmediata y trabajo offline. La columna de estado distingue el código heredado de la arquitectura objetivo.

### Aggregate Root: VeterinarianClient

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend; modelo equivalente en Android y Flutter — **Implementado en el backend** |
| **Propósito** | Controlar la relación y autorización entre veterinario y ganadero. |
| **Relaciones** | VeterinarianClient se relaciona con CollaborationStatus; VeterinarianClient compone AuthorizationScope; CollaborationPolicy depende de VeterinarianClient; IVeterinarianClientRepository depende de VeterinarianClient |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `id` | `int` |
| `veterinarianId` | `int` |
| `rancherId` | `int` |
| `status` | `CollaborationStatus` |
| `requestedAt` | `DateTime` |
| `acceptedAt` | `DateTime?` |
| `revokedAt` | `DateTime?` |
| `scope` | `AuthorizationScope` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Accept(at: DateTime)` | `void` |
| `Reject()` | `void` |
| `Revoke(at: DateTime)` | `void` |
| `IsActive()` | `bool` |

### Enumeration: CollaborationStatus

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend, Android y Flutter (modelo canónico) — **Diseño objetivo** |
| **Propósito** | Definir los valores válidos de CollaborationStatus. |
| **Relaciones** | VeterinarianClient se relaciona con CollaborationStatus |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `Pending` | `No especificado` |
| `Accepted` | `No especificado` |
| `Rejected` | `No especificado` |
| `Revoked` | `No especificado` |

**Métodos u operaciones**

No aplica.

### Value Object: AuthorizationScope

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend, Android y Flutter (modelo canónico) — **Diseño objetivo** |
| **Propósito** | Delimitar fincas, animales y operaciones autorizadas. |
| **Relaciones** | VeterinarianClient compone AuthorizationScope |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `farmIds` | `Set~int~` |
| `animalIds` | `Set~int~` |
| `canWriteHealthRecords` | `bool` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `AllowsAnimal(animalId: int)` | `bool` |

### Domain Service: CollaborationPolicy

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend y modelos equivalentes Android/Flutter — **Diseño objetivo** |
| **Propósito** | Evaluar aceptación y acceso dentro de una colaboración. |
| **Relaciones** | CollaborationPolicy depende de VeterinarianClient |

**Atributos o dependencias**

No aplica.

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `CanAccept(rancherId: int, relation: VeterinarianClient)` | `bool` |
| `CanAccess(veterinarianId: int, animalId: int)` | `bool` |

### Repository Interface: IVeterinarianClientRepository

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend; modelo equivalente en Android y Flutter — **Implementado en el backend** |
| **Propósito** | Abstraer la persistencia de VeterinarianClient. |
| **Relaciones** | IVeterinarianClientRepository depende de VeterinarianClient |

**Atributos o dependencias**

No aplica.

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Find(veterinarianId: int, rancherId: int)` | `VeterinarianClient?` |
| `FindByVeterinarian(id: int)` | `List~VeterinarianClient~` |
| `Add(relation: VeterinarianClient)` | `void` |
| `Update(relation: VeterinarianClient)` | `void` |



<a id="toc-2-6-5-2-interface-layer"></a>

## 2.6.5.2. Interface Layer

**Responsabilidad estable.** Esta capa recibe las acciones relacionadas con **solicitud, aceptación, revocación y consulta de colaboraciones veterinarias** y las traduce a casos de uso. Los controllers y resources corresponden a la API; las pantallas y controladores de estado representan la presentación objetivo en Android y Flutter. Ninguna de estas clases implementa reglas de negocio.

### REST Controller: VeterinarianClientsController

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend ASP.NET Core — **Implementado en el backend** |
| **Propósito** | Publicar por HTTP las capacidades de Veterinary Collaboration. |
| **Relaciones** | Recibe resources, invoca servicios de aplicación y devuelve resources HTTP. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `commandService` | `IVeterinarianClientCommandService` |
| `queryService` | `IVeterinarianClientQueryService` |
| `userQueryService` | `IUserQueryService` |
| `herdQueryService` | `IHerdQueryService` |
| `animalQueryService` | `IAnimalQueryService` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `GetClients(int veterinarianId, CancellationToken cancellationToken)` | `No especificado` |
| `GetAvailableRanchers(int veterinarianId, CancellationToken cancellationToken)` | `No especificado` |
| `AddClient(int veterinarianId, int rancherId, CancellationToken cancellationToken)` | `No especificado` |
| `RemoveClient(int veterinarianId, int rancherId, CancellationToken cancellationToken)` | `No especificado` |




### Presentation Model: VeterinarianClientViewModel

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


### State Controller: VeterinarianClientController

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

<a id="toc-2-6-5-3-application-layer"></a>

## 2.6.5.3. Application Layer

**Responsabilidad estable.** Esta capa coordina las capacidades de **solicitud, aceptación, revocación y consulta de colaboraciones veterinarias**. Los commands y queries expresan intenciones; los handlers cargan aggregates, aplican reglas, persisten cambios y reaccionan a eventos. Los casos de uso móviles coordinan lectura local, actualización remota y sincronización idempotente.

### Application Service: VeterinarianClientCommandService

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend ASP.NET Core — **Implementado en el backend** |
| **Propósito** | Orquestar solicitud, aceptación, revocación y consulta de colaboraciones veterinarias sin contener reglas del dominio. |
| **Relaciones** | Invoca agregados y repositories; confirma la transacción mediante Unit of Work. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `repository` | `IVeterinarianClientRepository` |
| `unitOfWork` | `IUnitOfWork` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Handle(CreateVeterinarianClientCommand command, CancellationToken cancellationToken)` | `No especificado` |
| `Handle(DeleteVeterinarianClientCommand command, CancellationToken cancellationToken)` | `No especificado` |





### Use Case: ObserveVeterinarianClientUseCase

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


### Command Handler: RequestCollaborationCommandHandler

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


### Event Handler: CollaborationAcceptedEventHandler

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

<a id="toc-2-6-5-4-infrastructure-layer"></a>

## 2.6.5.4. Infrastructure Layer

**Responsabilidad estable.** Esta capa implementa los puertos definidos hacia el interior de **Veterinary Collaboration** y concentra acceso a base de datos, red, almacenamiento local e integraciones externas. Las clases de infraestructura traducen errores y contratos técnicos antes de devolver resultados a Application Layer.

### Repository Adapter: VeterinarianClientRepository

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend / Entity Framework Core — **Implementado en el backend** |
| **Propósito** | Implementar el puerto de persistencia definido por Domain Layer. |
| **Relaciones** | Implementa IVeterinarianClientRepository; utiliza AppDbContext/MySQL y reconstruye el aggregate. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `context` | `AppDbContext` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `FindByVeterinarianIdAsync(int veterinarianId, CancellationToken cancellationToken)` | `No especificado` |
| `FindByVeterinarianIdAndRancherIdAsync(int veterinarianId, int rancherId, CancellationToken cancellationToken)` | `No especificado` |
| `ExistsByVeterinarianIdAndRancherIdAsync(int veterinarianId, int rancherId, CancellationToken cancellationToken)` | `No especificado` |



### Room Adapter: VeterinarianClientDao

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


### SQLite Adapter: VeterinarianClientLocalDataSource

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


### Context Adapter: ProfilesDirectoryAdapter

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend ASP.NET Core — **Diseño objetivo** |
| **Propósito** | Aislar una dependencia externa detrás de un puerto explícito. |
| **Relaciones** | Implementa el puerto de directorio y consume Profile Management. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `profilesFacade` | `No especificado` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `GetDisplayName(userId)` | `No especificado` |
| `FindRanchers()` | `No especificado` |


<a id="toc-2-6-5-5-bounded-context-software-architecture-component-level-diagrams"></a>

## 2.6.5.5. Bounded Context Software Architecture Component Level Diagrams

El archivo [`component-level.dsl`](<../../assets/codefordiagrams/2.6.5. Bounded Context Veterinary Collaboration/component-level.dsl>) contiene las vistas `BC5-ApiComponents`, `BC5-AndroidComponents` y `BC5-FlutterComponents`. Las tres parten del mismo modelo C4 y muestran la separación entre presentación, aplicación, dominio y adaptadores.

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-5-Bounded-Context-Veterinary-Collaboration/2-6-5-BC5-ApiComponents.svg" alt="Componentes API de Veterinary Collaboration" width="900">
  <p><i>Figura 2.6.5.1. Componentes de la API para Veterinary Collaboration. Fuente: elaboración propia con Structurizr DSL.</i></p>
</div>

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-5-Bounded-Context-Veterinary-Collaboration/2-6-5-BC5-AndroidComponents.svg" alt="Componentes Android de Veterinary Collaboration" width="900">
  <p><i>Figura 2.6.5.2. Componentes Android para Veterinary Collaboration. Fuente: elaboración propia con Structurizr DSL.</i></p>
</div>

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-5-Bounded-Context-Veterinary-Collaboration/2-6-5-BC5-FlutterComponents.svg" alt="Componentes Flutter de Veterinary Collaboration" width="900">
  <p><i>Figura 2.6.5.3. Componentes Flutter para Veterinary Collaboration. Fuente: elaboración propia con Structurizr DSL.</i></p>
</div>

<a id="toc-2-6-5-6-bounded-context-software-architecture-code-level-diagrams"></a>

## 2.6.5.6. Bounded Context Software Architecture Code Level Diagrams

Los diagramas de código detallan el modelo del dominio y los objetos de persistencia. El UML diferencia los elementos existentes de las incorporaciones objetivo, mientras los esquemas SQL señalan mediante comentarios las columnas propuestas. Los archivos ERD quedan disponibles para completar la importación manual.

<a id="toc-2-6-5-6-1-bounded-context-domain-layer-class-diagrams"></a>

### 2.6.5.6.1. Bounded Context Domain Layer Class Diagrams

El Class Diagram incluye agregados, entidades, value objects, enumeraciones, servicios de dominio e interfaces de repositorio con atributos, operaciones, visibilidad y multiplicidades.

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-5-Bounded-Context-Veterinary-Collaboration/2-6-5-domain-layer-class-diagram.svg" alt="Class Diagram de Veterinary Collaboration" width="900">
  <p><i>Figura 2.6.5.4. Domain Layer Class Diagram de Veterinary Collaboration. Fuente: elaboración propia con PlantUML.</i></p>
</div>

<a id="toc-2-6-5-6-2-bounded-context-database-design-diagram"></a>

### 2.6.5.6.2. Bounded Context Database Design Diagram

MySQL mantiene la persistencia autoritativa. Room y SQLite contienen únicamente caché, metadatos de sincronización y operaciones pendientes; no sustituyen las reglas ni la fuente de verdad del backend. En IAM, las credenciales y tokens permanecen fuera de las tablas locales y se almacenan mediante mecanismos seguros del sistema operativo.

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-5-Bounded-Context-Veterinary-Collaboration/2-6-5-mysql-database-design.png" alt="MySQL Database Diagram de Veterinary Collaboration" width="900">
  <p><i>Figura 2.6.5.5. MySQL Database Design de Veterinary Collaboration. Fuente: elaboración propia a partir del esquema SQL.</i></p>
</div>

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-5-Bounded-Context-Veterinary-Collaboration/2-6-5-android-room-database-design.png" alt="Room Database Diagram de Veterinary Collaboration" width="900">
  <p><i>Figura 2.6.5.6. Android Room Database Design de Veterinary Collaboration. Fuente: elaboración propia a partir del esquema SQL.</i></p>
</div>


