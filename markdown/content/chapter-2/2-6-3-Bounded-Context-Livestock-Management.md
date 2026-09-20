<a id="toc-2-6-3-bounded-context-livestock-management"></a>

# 2.6.3. Bounded Context: Livestock Management

Gestionar fincas, hatos, animales e identificadores QR como fuente de referencia para los demás procesos ganaderos.

La base implementada se encuentra en el módulo `Livestock` de la API ASP.NET Core. El diseño móvil de Android y Flutter se presenta como **diseño objetivo** porque esos clientes todavía no existen en el workspace. Los tres productos comparten contratos REST y lenguaje ubicuo, mientras la API conserva las reglas autoritativas.

<a id="toc-2-6-3-1-domain-layer"></a>

## 2.6.3.1. Domain Layer

**Responsabilidad estable.** Esta capa documenta el modelo que representa el núcleo de **Livestock Management**. Las reglas autoritativas se ejecutan en la API; Android y Flutter mantienen modelos equivalentes para presentación, validación inmediata y trabajo offline. La columna de estado distingue el código heredado de la arquitectura objetivo.

**Detalle técnico evolutivo.** El siguiente diccionario identifica las clases, sus responsabilidades, atributos, métodos y relaciones. Los campos **Producto** y **Estado** distinguen los elementos comprobados en el código de aquellos que aún pertenecen al diseño objetivo.

### Aggregate Root: Farm

| Campo | Detalle |
|---|---|
| **Producto** | Backend, Android y Flutter (modelo canónico) |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Agrupar los hatos de un propietario. |
| **Relaciones** | Farm compone Herd |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `id` | `int` |
| `ownerId` | `int` |
| `name` | `string` |
| `location` | `string` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `RegisterHerd(herd: Herd)` | `void` |
| `BelongsTo(ownerId: int)` | `bool` |

---

### Entity: Herd

| Campo | Detalle |
|---|---|
| **Producto** | Backend; modelo equivalente en Android y Flutter |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Administrar un conjunto de animales dentro de una finca. |
| **Relaciones** | Farm compone Herd; Herd compone Animal; IHerdRepository depende de Herd |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `id` | `int` |
| `farmId` | `int` |
| `name` | `string` |
| `mainType` | `string` |
| `veterinarianId` | `int?` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `AssignVeterinarian(id: int)` | `void` |
| `AddAnimal(animal: Animal)` | `void` |

---

### Entity: Animal

| Campo | Detalle |
|---|---|
| **Producto** | Backend; modelo equivalente en Android y Flutter |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Mantener identificación y estado productivo de un animal. |
| **Relaciones** | Herd compone Animal; Animal compone AnimalTag; Animal compone QrIdentifier; Animal se relaciona con AnimalStatus; IAnimalRepository depende de Animal |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `id` | `int` |
| `herdId` | `int` |
| `tag` | `AnimalTag` |
| `qrIdentifier` | `QrIdentifier` |
| `name` | `string` |
| `species` | `string` |
| `breed` | `string` |
| `status` | `AnimalStatus` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `UpdateWeight(weight: decimal)` | `void` |
| `ChangeStatus(status: AnimalStatus)` | `void` |

---

### Value Object: AnimalTag

| Campo | Detalle |
|---|---|
| **Producto** | Backend, Android y Flutter (modelo canónico) |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Representar el identificador visible del animal. |
| **Relaciones** | Animal compone AnimalTag |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `value` | `string` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `IsValid()` | `bool` |

---

### Value Object: QrIdentifier

| Campo | Detalle |
|---|---|
| **Producto** | Backend, Android y Flutter (modelo canónico) |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Representar la carga QR que identifica un animal. |
| **Relaciones** | Animal compone QrIdentifier |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `value` | `string` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `AsPayload()` | `string` |

---

### Enumeration: AnimalStatus

| Campo | Detalle |
|---|---|
| **Producto** | Backend y modelos equivalentes Android/Flutter |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Definir los valores válidos de AnimalStatus. |
| **Relaciones** | Animal se relaciona con AnimalStatus |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `Active` | `No especificado` |
| `Sold` | `No especificado` |
| `Deceased` | `No especificado` |

**Métodos u operaciones**

No aplica.

---

### Repository Interface: IAnimalRepository

| Campo | Detalle |
|---|---|
| **Producto** | Backend; modelo equivalente en Android y Flutter |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Abstraer la persistencia de Animal. |
| **Relaciones** | IAnimalRepository depende de Animal |

**Atributos o dependencias**

No aplica.

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `FindById(id: int)` | `Animal?` |
| `FindByQr(code: string)` | `Animal?` |
| `Add(animal: Animal)` | `void` |

---

### Repository Interface: IHerdRepository

| Campo | Detalle |
|---|---|
| **Producto** | Backend; modelo equivalente en Android y Flutter |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Abstraer la persistencia de Herd. |
| **Relaciones** | IHerdRepository depende de Herd |

**Atributos o dependencias**

No aplica.

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `FindById(id: int)` | `Herd?` |
| `Add(herd: Herd)` | `void` |

---

### Domain Service: AnimalOwnershipPolicy

| Campo | Detalle |
|---|---|
| **Producto** | Backend; modelo equivalente en Android y Flutter |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Decidir si un actor puede administrar un animal. |
| **Relaciones** | Consulta Farm, Herd y Animal sin asumir persistencia. |

**Atributos o dependencias**

No aplica.

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `CanManage(actorId: int, animalId: int)` | `bool` |

---

<a id="toc-2-6-3-2-interface-layer"></a>

## 2.6.3.2. Interface Layer

**Responsabilidad estable.** Esta capa recibe las acciones relacionadas con **gestión de fincas, hatos, animales e identificación QR** y las traduce a casos de uso. Los controllers y resources corresponden a la API; las pantallas y controladores de estado representan la presentación objetivo en Android y Flutter. Ninguna de estas clases implementa reglas de negocio.

**Detalle técnico evolutivo.** El siguiente diccionario identifica las clases, sus responsabilidades, atributos, métodos y relaciones. Los campos **Producto** y **Estado** distinguen los elementos comprobados en el código de aquellos que aún pertenecen al diseño objetivo.

### REST Controller: HerdsController

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Publicar por HTTP las capacidades de Livestock Management. |
| **Relaciones** | Recibe resources, invoca servicios de aplicación y devuelve resources HTTP. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `commandService` | `IHerdCommandService` |
| `queryService` | `IHerdQueryService` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `GetAll(CancellationToken cancellationToken)` | `No especificado` |
| `GetById(int id, CancellationToken cancellationToken)` | `No especificado` |
| `Create(CreateHerdResource resource, CancellationToken cancellationToken)` | `No especificado` |
| `Update(int id, CreateHerdResource resource, CancellationToken cancellationToken)` | `No especificado` |
| `Delete(int id, CancellationToken cancellationToken)` | `No especificado` |

---

### REST Controller: AnimalsController

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Publicar por HTTP las capacidades de Livestock Management. |
| **Relaciones** | Recibe resources, invoca servicios de aplicación y devuelve resources HTTP. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `commandService` | `IAnimalCommandService` |
| `queryService` | `IAnimalQueryService` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `GetAll(CancellationToken cancellationToken)` | `No especificado` |
| `GetById(int id, CancellationToken cancellationToken)` | `No especificado` |
| `Create(CreateAnimalResource resource, CancellationToken cancellationToken)` | `No especificado` |
| `Update(int id, CreateAnimalResource resource, CancellationToken cancellationToken)` | `No especificado` |
| `Delete(int id, CancellationToken cancellationToken)` | `No especificado` |

---

### Resource/Assembler: HerdResource

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
| `Name` | `string` |
| `Location` | `string` |
| `Owner` | `string` |
| `OwnerId` | `int` |
| `VeterinarianId` | `int?` |
| `MainType` | `string` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Create(...)` | `No especificado` |
| `Deconstruct(...)` | `No especificado` |

---

### Resource/Assembler: AnimalResource

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
| `Tag` | `string` |
| `Name` | `string` |
| `Species` | `string` |
| `Breed` | `string` |
| `Gender` | `string` |
| `BirthDate` | `DateOnly?` |
| `Weight` | `decimal` |
| `Status` | `string` |
| `HerdId` | `int` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Create(...)` | `No especificado` |
| `Deconstruct(...)` | `No especificado` |

---

### Resource/Assembler: CreateHerdResource

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Definir un contrato estable de entrada o salida para la API REST. |
| **Relaciones** | Es construido o traducido por assemblers y consumido por el controller y los clientes móviles. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `Name` | `string` |
| `Location` | `string` |
| `Owner` | `string` |
| `OwnerId` | `int` |
| `VeterinarianId` | `int?` |
| `MainType` | `string` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Create(...)` | `No especificado` |
| `Deconstruct(...)` | `No especificado` |

---

### Resource/Assembler: CreateAnimalResource

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Definir un contrato estable de entrada o salida para la API REST. |
| **Relaciones** | Es construido o traducido por assemblers y consumido por el controller y los clientes móviles. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `Tag` | `string` |
| `Name` | `string` |
| `Species` | `string` |
| `Breed` | `string` |
| `Gender` | `string` |
| `BirthDate` | `DateOnly?` |
| `Weight` | `decimal` |
| `Status` | `string` |
| `HerdId` | `int` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Create(...)` | `No especificado` |
| `Deconstruct(...)` | `No especificado` |

---

### Composable: FarmHerdYAnimalScreen

| Campo | Detalle |
|---|---|
| **Producto** | Android / Jetpack Compose |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Presentar gestión de fincas, hatos, animales e identificación QR en Android. |
| **Relaciones** | Observa FarmHerdYAnimalViewModel y emite acciones de interfaz. |

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

### Presentation Model: FarmHerdYAnimalViewModel

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

### Widget: FarmHerdYAnimalPage

| Campo | Detalle |
|---|---|
| **Producto** | Flutter / Dart |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Presentar gestión de fincas, hatos, animales e identificación QR en Flutter. |
| **Relaciones** | Observa FarmHerdYAnimalController y emite intenciones del usuario. |

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

### State Controller: FarmHerdYAnimalController

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

<a id="toc-2-6-3-3-application-layer"></a>

## 2.6.3.3. Application Layer

**Responsabilidad estable.** Esta capa coordina las capacidades de **gestión de fincas, hatos, animales e identificación QR**. Los commands y queries expresan intenciones; los handlers cargan aggregates, aplican reglas, persisten cambios y reaccionan a eventos. Los casos de uso móviles coordinan lectura local, actualización remota y sincronización idempotente.

**Detalle técnico evolutivo.** El siguiente diccionario identifica las clases, sus responsabilidades, atributos, métodos y relaciones. Los campos **Producto** y **Estado** distinguen los elementos comprobados en el código de aquellos que aún pertenecen al diseño objetivo.

### Application Service: HerdCommandService

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Orquestar gestión de fincas, hatos, animales e identificación QR sin contener reglas del dominio. |
| **Relaciones** | Invoca agregados y repositories; confirma la transacción mediante Unit of Work. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `repository` | `IHerdRepository` |
| `unitOfWork` | `IUnitOfWork` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Handle(CreateHerdCommand command, CancellationToken cancellationToken)` | `No especificado` |
| `Handle(UpdateHerdCommand command, CancellationToken cancellationToken)` | `No especificado` |
| `Handle(DeleteHerdCommand command, CancellationToken cancellationToken)` | `No especificado` |

---

### Application Service: HerdQueryService

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Orquestar gestión de fincas, hatos, animales e identificación QR sin contener reglas del dominio. |
| **Relaciones** | Invoca agregados y repositories; confirma la transacción mediante Unit of Work. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `repository` | `IHerdRepository` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Handle(GetHerdByIdQuery query, CancellationToken cancellationToken)` | `No especificado` |
| `Handle(GetAllHerdsQuery query, CancellationToken cancellationToken)` | `No especificado` |

---

### Application Service: AnimalCommandService

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Orquestar gestión de fincas, hatos, animales e identificación QR sin contener reglas del dominio. |
| **Relaciones** | Invoca agregados y repositories; confirma la transacción mediante Unit of Work. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `repository` | `IAnimalRepository` |
| `unitOfWork` | `IUnitOfWork` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Handle(CreateAnimalCommand command, CancellationToken cancellationToken)` | `No especificado` |
| `Handle(UpdateAnimalCommand command, CancellationToken cancellationToken)` | `No especificado` |
| `Handle(DeleteAnimalCommand command, CancellationToken cancellationToken)` | `No especificado` |

---

### Application Service: AnimalQueryService

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Orquestar gestión de fincas, hatos, animales e identificación QR sin contener reglas del dominio. |
| **Relaciones** | Invoca agregados y repositories; confirma la transacción mediante Unit of Work. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `repository` | `IAnimalRepository` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Handle(GetAnimalByIdQuery query, CancellationToken cancellationToken)` | `No especificado` |
| `Handle(GetAllAnimalsQuery query, CancellationToken cancellationToken)` | `No especificado` |

---

### Command/Query: CreateHerdCommand

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Transportar una intención o consulta tipada hacia su handler. |
| **Relaciones** | Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `Name` | `string` |
| `Location` | `string` |
| `Owner` | `string` |
| `OwnerId` | `int` |
| `VeterinarianId` | `int?` |
| `MainType` | `string` |

**Métodos u operaciones**

No aplica.

---

### Command/Query: UpdateHerdCommand

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
| `Name` | `string` |
| `Location` | `string` |
| `Owner` | `string` |
| `OwnerId` | `int` |
| `VeterinarianId` | `int?` |
| `MainType` | `string` |

**Métodos u operaciones**

No aplica.

---

### Command/Query: CreateAnimalCommand

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Transportar una intención o consulta tipada hacia su handler. |
| **Relaciones** | Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `Tag` | `string` |
| `Name` | `string` |
| `Species` | `string` |
| `Breed` | `string` |
| `Gender` | `string` |
| `BirthDate` | `DateOnly?` |
| `Weight` | `decimal` |
| `Status` | `string` |
| `HerdId` | `int` |

**Métodos u operaciones**

No aplica.

---

### Command/Query: UpdateAnimalCommand

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
| `Tag` | `string` |
| `Name` | `string` |
| `Species` | `string` |
| `Breed` | `string` |
| `Gender` | `string` |
| `BirthDate` | `DateOnly?` |
| `Weight` | `decimal` |
| `Status` | `string` |
| `HerdId` | `int` |

**Métodos u operaciones**

No aplica.

---

### Command/Query: GetAnimalByIdQuery

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

### Use Case: ObserveFarmHerdYAnimalUseCase

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

### Use Case: SyncFarmHerdYAnimalUseCase

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

### Command Handler: CreateHerdCommandHandler

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

### Command Handler: CreateAnimalCommandHandler

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

### Event Handler: AnimalRegisteredEventHandler

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

<a id="toc-2-6-3-4-infrastructure-layer"></a>

## 2.6.3.4. Infrastructure Layer

**Responsabilidad estable.** Esta capa implementa los puertos definidos hacia el interior de **Livestock Management** y concentra acceso a base de datos, red, almacenamiento local e integraciones externas. Las clases de infraestructura traducen errores y contratos técnicos antes de devolver resultados a Application Layer.

**Detalle técnico evolutivo.** El siguiente diccionario identifica las clases, sus responsabilidades, atributos, métodos y relaciones. Los campos **Producto** y **Estado** distinguen los elementos comprobados en el código de aquellos que aún pertenecen al diseño objetivo.

### Repository Adapter: HerdRepository / AnimalRepository

| Campo | Detalle |
|---|---|
| **Producto** | Backend / Entity Framework Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Implementar el puerto de persistencia definido por Domain Layer. |
| **Relaciones** | Implementa IHerdRepository / IAnimalRepository; utiliza AppDbContext/MySQL y reconstruye el aggregate. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `HerdRepository` | `AppDbContext context` |
| `AnimalRepository` | `AppDbContext context` |

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

### Remote Adapter: FarmHerdYAnimalApiDataSource

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

### Room Adapter: FarmHerdYAnimalDao

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

### Remote Adapter: FarmHerdYAnimalRemoteDataSource

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

### SQLite Adapter: FarmHerdYAnimalLocalDataSource

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

### Context Adapter: ProfilesOwnerAdapter

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Aislar una dependencia externa detrás de un puerto explícito. |
| **Relaciones** | Implementa el puerto de propietarios y consume Profile Management. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `profilesFacade` | `No especificado` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `ValidateOwner(ownerId)` | `bool` |

---

### Device Adapter: MlKitQrScanner

| Campo | Detalle |
|---|---|
| **Producto** | Android / ML Kit |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Aislar una dependencia externa detrás de un puerto explícito. |
| **Relaciones** | Implementa el puerto de lectura QR mediante la cámara y Google ML Kit. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `scannerClient` | `No especificado` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Scan(image)` | `QrIdentifier` |

---

### Offline Adapter: LivestockOutboxStore

| Campo | Detalle |
|---|---|
| **Producto** | Android y Flutter |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Aislar una dependencia externa detrás de un puerto explícito. |
| **Relaciones** | Implementa el puerto de sincronización local sobre Room o SQLite. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `serializer` | `database,` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Enqueue(operation)` | `No especificado` |
| `Pending()` | `No especificado` |
| `MarkSynced(id)` | `No especificado` |

---

<a id="toc-2-6-3-5-bounded-context-software-architecture-component-level-diagrams"></a>

## 2.6.3.5. Bounded Context Software Architecture Component Level Diagrams

El archivo [`component-level.dsl`](<../../assets/codefordiagrams/2.6.3. Bounded Context Livestock Management/component-level.dsl>) contiene las vistas `BC3-ApiComponents`, `BC3-AndroidComponents` y `BC3-FlutterComponents`. Las tres parten del mismo modelo C4 y muestran la separación entre presentación, aplicación, dominio y adaptadores.

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-3-Bounded-Context-Livestock-Management/2-6-3-BC3-ApiComponents.svg" alt="Componentes API de Livestock Management" width="900">
  <p><i>Figura 2.6.3.1. Componentes de la API para Livestock Management. Fuente: elaboración propia con Structurizr DSL.</i></p>
</div>

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-3-Bounded-Context-Livestock-Management/2-6-3-BC3-AndroidComponents.svg" alt="Componentes Android de Livestock Management" width="900">
  <p><i>Figura 2.6.3.2. Componentes Android para Livestock Management. Fuente: elaboración propia con Structurizr DSL.</i></p>
</div>

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-3-Bounded-Context-Livestock-Management/2-6-3-BC3-FlutterComponents.svg" alt="Componentes Flutter de Livestock Management" width="900">
  <p><i>Figura 2.6.3.3. Componentes Flutter para Livestock Management. Fuente: elaboración propia con Structurizr DSL.</i></p>
</div>

<a id="toc-2-6-3-6-bounded-context-software-architecture-code-level-diagrams"></a>

## 2.6.3.6. Bounded Context Software Architecture Code Level Diagrams

Los diagramas de código detallan el modelo del dominio y los objetos de persistencia. El UML diferencia los elementos existentes de las incorporaciones objetivo, mientras los esquemas SQL señalan mediante comentarios las columnas propuestas. Los archivos ERD quedan disponibles para completar la importación manual.

<a id="toc-2-6-3-6-1-bounded-context-domain-layer-class-diagrams"></a>

### 2.6.3.6.1. Bounded Context Domain Layer Class Diagrams

El Class Diagram incluye agregados, entidades, value objects, enumeraciones, servicios de dominio e interfaces de repositorio con atributos, operaciones, visibilidad y multiplicidades.

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-3-Bounded-Context-Livestock-Management/2-6-3-domain-layer-class-diagram.svg" alt="Class Diagram de Livestock Management" width="900">
  <p><i>Figura 2.6.3.4. Domain Layer Class Diagram de Livestock Management. Fuente: elaboración propia con PlantUML.</i></p>
</div>

<a id="toc-2-6-3-6-2-bounded-context-database-design-diagram"></a>

### 2.6.3.6.2. Bounded Context Database Design Diagram

MySQL mantiene la persistencia autoritativa. Room y SQLite contienen únicamente caché, metadatos de sincronización y operaciones pendientes; no sustituyen las reglas ni la fuente de verdad del backend. En IAM, las credenciales y tokens permanecen fuera de las tablas locales y se almacenan mediante mecanismos seguros del sistema operativo.

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-3-Bounded-Context-Livestock-Management/2-6-3-mysql-database-design.png" alt="MySQL Database Diagram de Livestock Management" width="900">
  <p><i>Figura 2.6.3.5. MySQL Database Design de Livestock Management. Fuente: elaboración propia a partir del esquema SQL.</i></p>
</div>

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-3-Bounded-Context-Livestock-Management/2-6-3-android-room-database-design.png" alt="Room Database Diagram de Livestock Management" width="900">
  <p><i>Figura 2.6.3.6. Android Room Database Design de Livestock Management. Fuente: elaboración propia a partir del esquema SQL.</i></p>
</div>


