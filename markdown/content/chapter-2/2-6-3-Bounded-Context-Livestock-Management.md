<a id="toc-2-6-3-bounded-context-livestock-management"></a>

# 2.6.3. Bounded Context: Livestock Management

Gestionar fincas, hatos, animales e identificadores QR como fuente de referencia para los demás procesos ganaderos.

La base implementada se encuentra en el módulo `Livestock` de la API ASP.NET Core. El diseño móvil de Android y Flutter se presenta como **diseño objetivo** porque esos clientes todavía no existen en el workspace. Los tres productos comparten contratos REST y lenguaje ubicuo, mientras la API conserva las reglas autoritativas.

<a id="toc-2-6-3-1-domain-layer"></a>

## 2.6.3.1. Domain Layer

**Responsabilidad estable.** Esta capa documenta el modelo que representa el núcleo de **Livestock Management**. Las reglas autoritativas se ejecutan en la API; Android y Flutter mantienen modelos equivalentes para presentación, validación inmediata y trabajo offline. La columna de estado distingue el código heredado de la arquitectura objetivo.

**Detalle técnico evolutivo.** El siguiente diccionario identifica las clases, sus responsabilidades, atributos, métodos y relaciones. La columna **Producto y estado** distingue los elementos comprobados en el código de aquellos que aún pertenecen al diseño objetivo.

<table>
  <thead>
    <tr><th>Clase</th><th>Categoría</th><th>Producto y estado</th><th>Propósito</th><th>Atributos</th><th>Métodos u operaciones</th><th>Relaciones</th></tr>
  </thead>
  <tbody>
    <tr><td><code>Farm</code></td><td>Aggregate Root</td><td>Backend, Android y Flutter (modelo canónico)<br><strong>Diseño objetivo</strong></td><td>Agrupar los hatos de un propietario.</td><td><code>id: int</code><br><code>ownerId: int</code><br><code>name: string</code><br><code>location: string</code></td><td><code>RegisterHerd(herd: Herd): void</code><br><code>BelongsTo(ownerId: int): bool</code></td><td>Farm compone Herd</td></tr>
    <tr><td><code>Herd</code></td><td>Entity</td><td>Backend; modelo equivalente en Android y Flutter<br><strong>Implementado en el backend</strong></td><td>Administrar un conjunto de animales dentro de una finca.</td><td><code>id: int</code><br><code>farmId: int</code><br><code>name: string</code><br><code>mainType: string</code><br><code>veterinarianId: int?</code></td><td><code>AssignVeterinarian(id: int): void</code><br><code>AddAnimal(animal: Animal): void</code></td><td>Farm compone Herd; Herd compone Animal; IHerdRepository depende de Herd</td></tr>
    <tr><td><code>Animal</code></td><td>Entity</td><td>Backend; modelo equivalente en Android y Flutter<br><strong>Implementado en el backend</strong></td><td>Mantener identificación y estado productivo de un animal.</td><td><code>id: int</code><br><code>herdId: int</code><br><code>tag: AnimalTag</code><br><code>qrIdentifier: QrIdentifier</code><br><code>name: string</code><br><code>species: string</code><br><code>breed: string</code><br><code>status: AnimalStatus</code></td><td><code>UpdateWeight(weight: decimal): void</code><br><code>ChangeStatus(status: AnimalStatus): void</code></td><td>Herd compone Animal; Animal compone AnimalTag; Animal compone QrIdentifier; Animal se relaciona con AnimalStatus; IAnimalRepository depende de Animal</td></tr>
    <tr><td><code>AnimalTag</code></td><td>Value Object</td><td>Backend, Android y Flutter (modelo canónico)<br><strong>Diseño objetivo</strong></td><td>Representar el identificador visible del animal.</td><td><code>value: string</code></td><td><code>IsValid(): bool</code></td><td>Animal compone AnimalTag</td></tr>
    <tr><td><code>QrIdentifier</code></td><td>Value Object</td><td>Backend, Android y Flutter (modelo canónico)<br><strong>Diseño objetivo</strong></td><td>Representar la carga QR que identifica un animal.</td><td><code>value: string</code></td><td><code>AsPayload(): string</code></td><td>Animal compone QrIdentifier</td></tr>
    <tr><td><code>AnimalStatus</code></td><td>Enumeration</td><td>Backend y modelos equivalentes Android/Flutter<br><strong>Implementado en el backend</strong></td><td>Definir los valores válidos de AnimalStatus.</td><td><code>Active</code><br><code>Sold</code><br><code>Deceased</code></td><td>—</td><td>Animal se relaciona con AnimalStatus</td></tr>
    <tr><td><code>IAnimalRepository</code></td><td>Repository Interface</td><td>Backend; modelo equivalente en Android y Flutter<br><strong>Implementado en el backend</strong></td><td>Abstraer la persistencia de Animal.</td><td>—</td><td><code>FindById(id: int): Animal?</code><br><code>FindByQr(code: string): Animal?</code><br><code>Add(animal: Animal): void</code></td><td>IAnimalRepository depende de Animal</td></tr>
    <tr><td><code>IHerdRepository</code></td><td>Repository Interface</td><td>Backend; modelo equivalente en Android y Flutter<br><strong>Implementado en el backend</strong></td><td>Abstraer la persistencia de Herd.</td><td>—</td><td><code>FindById(id: int): Herd?</code><br><code>Add(herd: Herd): void</code></td><td>IHerdRepository depende de Herd</td></tr>
    <tr><td><code>AnimalOwnershipPolicy</code></td><td>Domain Service</td><td>Backend; modelo equivalente en Android y Flutter<br><strong>Diseño objetivo</strong></td><td>Decidir si un actor puede administrar un animal.</td><td>—</td><td><code>CanManage(actorId: int, animalId: int): bool</code></td><td>Consulta Farm, Herd y Animal sin asumir persistencia.</td></tr>
  </tbody>
</table>

<a id="toc-2-6-3-2-interface-layer"></a>

## 2.6.3.2. Interface Layer

**Responsabilidad estable.** Esta capa recibe las acciones relacionadas con **gestión de fincas, hatos, animales e identificación QR** y las traduce a casos de uso. Los controllers y resources corresponden a la API; las pantallas y controladores de estado representan la presentación objetivo en Android y Flutter. Ninguna de estas clases implementa reglas de negocio.

**Detalle técnico evolutivo.** El siguiente diccionario identifica las clases, sus responsabilidades, atributos, métodos y relaciones. La columna **Producto y estado** distingue los elementos comprobados en el código de aquellos que aún pertenecen al diseño objetivo.

<table>
  <thead>
    <tr><th>Clase</th><th>Categoría</th><th>Producto y estado</th><th>Propósito</th><th>Atributos</th><th>Métodos u operaciones</th><th>Relaciones</th></tr>
  </thead>
  <tbody>
    <tr><td><code>HerdsController</code></td><td>REST Controller</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Publicar por HTTP las capacidades de Livestock Management.</td><td><code>IHerdCommandService commandService</code><br><code>IHerdQueryService queryService</code></td><td><code>GetAll(CancellationToken cancellationToken)</code><br><code>GetById(int id, CancellationToken cancellationToken)</code><br><code>Create(CreateHerdResource resource, CancellationToken cancellationToken)</code><br><code>Update(int id, CreateHerdResource resource, CancellationToken cancellationToken)</code><br><code>Delete(int id, CancellationToken cancellationToken)</code></td><td>Recibe resources, invoca servicios de aplicación y devuelve resources HTTP.</td></tr>
    <tr><td><code>AnimalsController</code></td><td>REST Controller</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Publicar por HTTP las capacidades de Livestock Management.</td><td><code>IAnimalCommandService commandService</code><br><code>IAnimalQueryService queryService</code></td><td><code>GetAll(CancellationToken cancellationToken)</code><br><code>GetById(int id, CancellationToken cancellationToken)</code><br><code>Create(CreateAnimalResource resource, CancellationToken cancellationToken)</code><br><code>Update(int id, CreateAnimalResource resource, CancellationToken cancellationToken)</code><br><code>Delete(int id, CancellationToken cancellationToken)</code></td><td>Recibe resources, invoca servicios de aplicación y devuelve resources HTTP.</td></tr>
    <tr><td><code>HerdResource</code></td><td>Resource/Assembler</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Definir un contrato estable de entrada o salida para la API REST.</td><td><code>int Id</code><br><code>string Name</code><br><code>string Location</code><br><code>string Owner</code><br><code>int OwnerId</code><br><code>int? VeterinarianId</code><br><code>string MainType</code></td><td><code>Create(...)</code><br><code>Deconstruct(...)</code></td><td>Es construido o traducido por assemblers y consumido por el controller y los clientes móviles.</td></tr>
    <tr><td><code>AnimalResource</code></td><td>Resource/Assembler</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Definir un contrato estable de entrada o salida para la API REST.</td><td><code>int Id</code><br><code>string Tag</code><br><code>string Name</code><br><code>string Species</code><br><code>string Breed</code><br><code>string Gender</code><br><code>DateOnly? BirthDate</code><br><code>decimal Weight</code><br><code>string Status</code><br><code>int HerdId</code></td><td><code>Create(...)</code><br><code>Deconstruct(...)</code></td><td>Es construido o traducido por assemblers y consumido por el controller y los clientes móviles.</td></tr>
    <tr><td><code>CreateHerdResource</code></td><td>Resource/Assembler</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Definir un contrato estable de entrada o salida para la API REST.</td><td><code>string Name</code><br><code>string Location</code><br><code>string Owner</code><br><code>int OwnerId</code><br><code>int? VeterinarianId</code><br><code>string MainType</code></td><td><code>Create(...)</code><br><code>Deconstruct(...)</code></td><td>Es construido o traducido por assemblers y consumido por el controller y los clientes móviles.</td></tr>
    <tr><td><code>CreateAnimalResource</code></td><td>Resource/Assembler</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Definir un contrato estable de entrada o salida para la API REST.</td><td><code>string Tag</code><br><code>string Name</code><br><code>string Species</code><br><code>string Breed</code><br><code>string Gender</code><br><code>DateOnly? BirthDate</code><br><code>decimal Weight</code><br><code>string Status</code><br><code>int HerdId</code></td><td><code>Create(...)</code><br><code>Deconstruct(...)</code></td><td>Es construido o traducido por assemblers y consumido por el controller y los clientes móviles.</td></tr>
    <tr><td><code>FarmHerdYAnimalScreen</code></td><td>Composable</td><td>Android / Jetpack Compose<br><strong>Diseño objetivo</strong></td><td>Presentar gestión de fincas, hatos, animales e identificación QR en Android.</td><td><code>uiState</code><br><code>onAction</code><br><code>navigation</code></td><td><code>Render()</code><br><code>Submit()</code><br><code>Retry()</code></td><td>Observa FarmHerdYAnimalViewModel y emite acciones de interfaz.</td></tr>
    <tr><td><code>FarmHerdYAnimalViewModel</code></td><td>Presentation Model</td><td>Android / Kotlin<br><strong>Diseño objetivo</strong></td><td>Mantener el estado observable y traducir acciones de Android a casos de uso.</td><td><code>state</code><br><code>observeUseCase</code><br><code>syncUseCase</code></td><td><code>Load()</code><br><code>Submit(action)</code><br><code>RetrySync()</code></td><td>Invoca casos de uso de Application Layer y publica un UI State inmutable.</td></tr>
    <tr><td><code>FarmHerdYAnimalPage</code></td><td>Widget</td><td>Flutter / Dart<br><strong>Diseño objetivo</strong></td><td>Presentar gestión de fincas, hatos, animales e identificación QR en Flutter.</td><td><code>state</code><br><code>onAction</code><br><code>router</code></td><td><code>build(context)</code><br><code>submit()</code><br><code>retry()</code></td><td>Observa FarmHerdYAnimalController y emite intenciones del usuario.</td></tr>
    <tr><td><code>FarmHerdYAnimalController</code></td><td>State Controller</td><td>Flutter / Dart<br><strong>Diseño objetivo</strong></td><td>Mantener el estado de presentación de Flutter y coordinar casos de uso.</td><td><code>state</code><br><code>observeUseCase</code><br><code>syncUseCase</code></td><td><code>load()</code><br><code>submit(action)</code><br><code>retrySync()</code></td><td>Invoca Application Layer y publica estados de carga, éxito y error.</td></tr>
  </tbody>
</table>

<a id="toc-2-6-3-3-application-layer"></a>

## 2.6.3.3. Application Layer

**Responsabilidad estable.** Esta capa coordina las capacidades de **gestión de fincas, hatos, animales e identificación QR**. Los commands y queries expresan intenciones; los handlers cargan aggregates, aplican reglas, persisten cambios y reaccionan a eventos. Los casos de uso móviles coordinan lectura local, actualización remota y sincronización idempotente.

**Detalle técnico evolutivo.** El siguiente diccionario identifica las clases, sus responsabilidades, atributos, métodos y relaciones. La columna **Producto y estado** distingue los elementos comprobados en el código de aquellos que aún pertenecen al diseño objetivo.

<table>
  <thead>
    <tr><th>Clase</th><th>Categoría</th><th>Producto y estado</th><th>Propósito</th><th>Atributos</th><th>Métodos u operaciones</th><th>Relaciones</th></tr>
  </thead>
  <tbody>
    <tr><td><code>HerdCommandService</code></td><td>Application Service</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Orquestar gestión de fincas, hatos, animales e identificación QR sin contener reglas del dominio.</td><td><code>IHerdRepository repository</code><br><code>IUnitOfWork unitOfWork</code></td><td><code>Handle(CreateHerdCommand command, CancellationToken cancellationToken)</code><br><code>Handle(UpdateHerdCommand command, CancellationToken cancellationToken)</code><br><code>Handle(DeleteHerdCommand command, CancellationToken cancellationToken)</code></td><td>Invoca agregados y repositories; confirma la transacción mediante Unit of Work.</td></tr>
    <tr><td><code>HerdQueryService</code></td><td>Application Service</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Orquestar gestión de fincas, hatos, animales e identificación QR sin contener reglas del dominio.</td><td><code>IHerdRepository repository</code></td><td><code>Handle(GetHerdByIdQuery query, CancellationToken cancellationToken)</code><br><code>Handle(GetAllHerdsQuery query, CancellationToken cancellationToken)</code></td><td>Invoca agregados y repositories; confirma la transacción mediante Unit of Work.</td></tr>
    <tr><td><code>AnimalCommandService</code></td><td>Application Service</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Orquestar gestión de fincas, hatos, animales e identificación QR sin contener reglas del dominio.</td><td><code>IAnimalRepository repository</code><br><code>IUnitOfWork unitOfWork</code></td><td><code>Handle(CreateAnimalCommand command, CancellationToken cancellationToken)</code><br><code>Handle(UpdateAnimalCommand command, CancellationToken cancellationToken)</code><br><code>Handle(DeleteAnimalCommand command, CancellationToken cancellationToken)</code></td><td>Invoca agregados y repositories; confirma la transacción mediante Unit of Work.</td></tr>
    <tr><td><code>AnimalQueryService</code></td><td>Application Service</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Orquestar gestión de fincas, hatos, animales e identificación QR sin contener reglas del dominio.</td><td><code>IAnimalRepository repository</code></td><td><code>Handle(GetAnimalByIdQuery query, CancellationToken cancellationToken)</code><br><code>Handle(GetAllAnimalsQuery query, CancellationToken cancellationToken)</code></td><td>Invoca agregados y repositories; confirma la transacción mediante Unit of Work.</td></tr>
    <tr><td><code>CreateHerdCommand</code></td><td>Command/Query</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Transportar una intención o consulta tipada hacia su handler.</td><td><code>string Name</code><br><code>string Location</code><br><code>string Owner</code><br><code>int OwnerId</code><br><code>int? VeterinarianId</code><br><code>string MainType</code></td><td>—</td><td>Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio.</td></tr>
    <tr><td><code>UpdateHerdCommand</code></td><td>Command/Query</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Transportar una intención o consulta tipada hacia su handler.</td><td><code>int Id</code><br><code>string Name</code><br><code>string Location</code><br><code>string Owner</code><br><code>int OwnerId</code><br><code>int? VeterinarianId</code><br><code>string MainType</code></td><td>—</td><td>Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio.</td></tr>
    <tr><td><code>CreateAnimalCommand</code></td><td>Command/Query</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Transportar una intención o consulta tipada hacia su handler.</td><td><code>string Tag</code><br><code>string Name</code><br><code>string Species</code><br><code>string Breed</code><br><code>string Gender</code><br><code>DateOnly? BirthDate</code><br><code>decimal Weight</code><br><code>string Status</code><br><code>int HerdId</code></td><td>—</td><td>Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio.</td></tr>
    <tr><td><code>UpdateAnimalCommand</code></td><td>Command/Query</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Transportar una intención o consulta tipada hacia su handler.</td><td><code>int Id</code><br><code>string Tag</code><br><code>string Name</code><br><code>string Species</code><br><code>string Breed</code><br><code>string Gender</code><br><code>DateOnly? BirthDate</code><br><code>decimal Weight</code><br><code>string Status</code><br><code>int HerdId</code></td><td>—</td><td>Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio.</td></tr>
    <tr><td><code>GetAnimalByIdQuery</code></td><td>Command/Query</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Transportar una intención o consulta tipada hacia su handler.</td><td><code>int Id</code></td><td>—</td><td>Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio.</td></tr>
    <tr><td><code>ObserveFarmHerdYAnimalUseCase</code></td><td>Use Case</td><td>Android y Flutter<br><strong>Diseño objetivo</strong></td><td>Entregar primero datos locales y actualizar la consulta cuando exista conectividad.</td><td><code>localRepository</code><br><code>remoteRepository</code><br><code>connectivityMonitor</code></td><td><code>Execute(criteria): Stream&lt;Result&gt;</code></td><td>Es invocado por ViewModel/Controller y coordina repositorios móviles.</td></tr>
    <tr><td><code>SyncFarmHerdYAnimalUseCase</code></td><td>Use Case</td><td>Android y Flutter<br><strong>Diseño objetivo</strong></td><td>Procesar operaciones móviles pendientes de manera idempotente.</td><td><code>outboxRepository</code><br><code>remoteRepository</code><br><code>conflictResolver</code></td><td><code>Execute(): SyncResult</code></td><td>Lee el outbox local, consume la API y actualiza el estado de sincronización.</td></tr>
    <tr><td><code>CreateHerdCommandHandler</code></td><td>Command Handler</td><td>Backend ASP.NET Core<br><strong>Diseño objetivo</strong></td><td>Ejecutar una intención concreta, aplicar reglas del agregado y confirmar la transacción.</td><td><code>repository</code><br><code>unitOfWork</code><br><code>domainPolicy</code></td><td><code>Handle(command): Result</code></td><td>Consume un Command, carga el aggregate mediante su repository y puede publicar un Domain Event.</td></tr>
    <tr><td><code>CreateAnimalCommandHandler</code></td><td>Command Handler</td><td>Backend ASP.NET Core<br><strong>Diseño objetivo</strong></td><td>Ejecutar una intención concreta, aplicar reglas del agregado y confirmar la transacción.</td><td><code>repository</code><br><code>unitOfWork</code><br><code>domainPolicy</code></td><td><code>Handle(command): Result</code></td><td>Consume un Command, carga el aggregate mediante su repository y puede publicar un Domain Event.</td></tr>
    <tr><td><code>AnimalRegisteredEventHandler</code></td><td>Event Handler</td><td>Backend ASP.NET Core<br><strong>Diseño objetivo</strong></td><td>Reaccionar al evento confirmado y actualizar proyecciones o integraciones.</td><td><code>projectionRepository</code><br><code>notificationPort</code><br><code>unitOfWork</code></td><td><code>Handle(domainEvent): Task</code></td><td>Consume un Domain Event y utiliza puertos de infraestructura sin modificar directamente el agregado.</td></tr>
  </tbody>
</table>

<a id="toc-2-6-3-4-infrastructure-layer"></a>

## 2.6.3.4. Infrastructure Layer

**Responsabilidad estable.** Esta capa implementa los puertos definidos hacia el interior de **Livestock Management** y concentra acceso a base de datos, red, almacenamiento local e integraciones externas. Las clases de infraestructura traducen errores y contratos técnicos antes de devolver resultados a Application Layer.

**Detalle técnico evolutivo.** El siguiente diccionario identifica las clases, sus responsabilidades, atributos, métodos y relaciones. La columna **Producto y estado** distingue los elementos comprobados en el código de aquellos que aún pertenecen al diseño objetivo.

<table>
  <thead>
    <tr><th>Clase</th><th>Categoría</th><th>Producto y estado</th><th>Propósito</th><th>Atributos</th><th>Métodos u operaciones</th><th>Relaciones</th></tr>
  </thead>
  <tbody>
    <tr><td><code>HerdRepository / AnimalRepository</code></td><td>Repository Adapter</td><td>Backend / Entity Framework Core<br><strong>Implementado en el backend</strong></td><td>Implementar el puerto de persistencia definido por Domain Layer.</td><td><code>HerdRepository: AppDbContext context</code><br><code>AnimalRepository: AppDbContext context</code></td><td><code>FindById(id)</code><br><code>Add(entity)</code><br><code>Update(entity)</code><br><code>Delete(entity)</code></td><td>Implementa IHerdRepository / IAnimalRepository; utiliza AppDbContext/MySQL y reconstruye el aggregate.</td></tr>
    <tr><td><code>ModelBuilderExtensions</code></td><td>Persistence Configuration</td><td>Backend / Entity Framework Core<br><strong>Implementado en el backend</strong></td><td>Mapear entidades y value objects del contexto al modelo relacional.</td><td><code>EntityTypeBuilder configuration</code></td><td><code>ApplyConfiguration(modelBuilder)</code></td><td>Configura tablas, claves, relaciones, restricciones y conversiones de Entity Framework Core.</td></tr>
    <tr><td><code>FarmHerdYAnimalApiDataSource</code></td><td>Remote Adapter</td><td>Android / Kotlin<br><strong>Diseño objetivo</strong></td><td>Implementar el acceso remoto del cliente móvil a la API.</td><td><code>httpClient</code><br><code>tokenProvider</code><br><code>serializer</code></td><td><code>Get(criteria)</code><br><code>Create(dto)</code><br><code>Update(dto)</code><br><code>Delete(id)</code></td><td>Consume controllers REST por HTTPS/JSON y traduce errores HTTP al modelo de aplicación.</td></tr>
    <tr><td><code>FarmHerdYAnimalDao</code></td><td>Room Adapter</td><td>Android / Room<br><strong>Diseño objetivo</strong></td><td>Implementar persistencia local y observación reactiva en Android.</td><td><code>roomDatabase</code><br><code>entityMapper</code></td><td><code>Observe(criteria)</code><br><code>Upsert(entity)</code><br><code>Delete(id)</code><br><code>Pending()</code></td><td>Implementa el puerto local mediante Room y participa en la estrategia de caché/outbox.</td></tr>
    <tr><td><code>FarmHerdYAnimalRemoteDataSource</code></td><td>Remote Adapter</td><td>Flutter / Dart<br><strong>Diseño objetivo</strong></td><td>Implementar el acceso remoto del cliente móvil a la API.</td><td><code>httpClient</code><br><code>tokenProvider</code><br><code>serializer</code></td><td><code>Get(criteria)</code><br><code>Create(dto)</code><br><code>Update(dto)</code><br><code>Delete(id)</code></td><td>Consume controllers REST por HTTPS/JSON y traduce errores HTTP al modelo de aplicación.</td></tr>
    <tr><td><code>FarmHerdYAnimalLocalDataSource</code></td><td>SQLite Adapter</td><td>Flutter / Dart<br><strong>Diseño objetivo</strong></td><td>Implementar persistencia local equivalente en Flutter.</td><td><code>sqliteDatabase</code><br><code>entityMapper</code></td><td><code>watch(criteria)</code><br><code>upsert(entity)</code><br><code>delete(id)</code><br><code>pending()</code></td><td>Implementa el puerto local mediante SQLite y participa en la estrategia de caché/outbox.</td></tr>
    <tr><td><code>ProfilesOwnerAdapter</code></td><td>Context Adapter</td><td>Backend ASP.NET Core<br><strong>Diseño objetivo</strong></td><td>Aislar una dependencia externa detrás de un puerto explícito.</td><td><code>profilesFacade</code></td><td><code>ValidateOwner(ownerId): bool</code></td><td>Implementa el puerto de propietarios y consume Profile Management.</td></tr>
    <tr><td><code>MlKitQrScanner</code></td><td>Device Adapter</td><td>Android / ML Kit<br><strong>Diseño objetivo</strong></td><td>Aislar una dependencia externa detrás de un puerto explícito.</td><td><code>scannerClient</code></td><td><code>Scan(image): QrIdentifier</code></td><td>Implementa el puerto de lectura QR mediante la cámara y Google ML Kit.</td></tr>
    <tr><td><code>LivestockOutboxStore</code></td><td>Offline Adapter</td><td>Android y Flutter<br><strong>Diseño objetivo</strong></td><td>Aislar una dependencia externa detrás de un puerto explícito.</td><td><code>database, serializer</code></td><td><code>Enqueue(operation)</code><br><code>Pending()</code><br><code>MarkSynced(id)</code></td><td>Implementa el puerto de sincronización local sobre Room o SQLite.</td></tr>
  </tbody>
</table>

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


