<a id="toc-2-6-5-bounded-context-veterinary-collaboration"></a>

# 2.6.5. Bounded Context: Veterinary Collaboration

Administrar solicitudes y autorizaciones entre ganaderos y veterinarios, delimitando clientes, pacientes y alcance de acceso.

La base implementada se encuentra en el módulo `Clients` de la API ASP.NET Core. El diseño móvil de Android y Flutter se presenta como **diseño objetivo** porque esos clientes todavía no existen en el workspace. Los tres productos comparten contratos REST y lenguaje ubicuo, mientras la API conserva las reglas autoritativas.

<a id="toc-2-6-5-1-domain-layer"></a>

## 2.6.5.1. Domain Layer

Esta capa documenta el modelo que representa el núcleo de **Veterinary Collaboration**. Las reglas autoritativas se ejecutan en la API; Android y Flutter mantienen modelos equivalentes para presentación, validación inmediata y trabajo offline. La columna de estado distingue el código heredado de la arquitectura objetivo.

<table>
  <thead>
    <tr><th>Clase</th><th>Categoría</th><th>Producto y estado</th><th>Propósito</th><th>Atributos</th><th>Métodos u operaciones</th><th>Relaciones</th></tr>
  </thead>
  <tbody>
    <tr><td><code>VeterinarianClient</code></td><td>Aggregate Root</td><td>Backend; modelo equivalente en Android y Flutter<br><strong>Implementado en el backend</strong></td><td>Controlar la relación y autorización entre veterinario y ganadero.</td><td><code>id: int</code><br><code>veterinarianId: int</code><br><code>rancherId: int</code><br><code>status: CollaborationStatus</code><br><code>requestedAt: DateTime</code><br><code>acceptedAt: DateTime?</code><br><code>revokedAt: DateTime?</code><br><code>scope: AuthorizationScope</code></td><td><code>Accept(at: DateTime): void</code><br><code>Reject(): void</code><br><code>Revoke(at: DateTime): void</code><br><code>IsActive(): bool</code></td><td>VeterinarianClient se relaciona con CollaborationStatus; VeterinarianClient compone AuthorizationScope; CollaborationPolicy depende de VeterinarianClient; IVeterinarianClientRepository depende de VeterinarianClient</td></tr>
    <tr><td><code>CollaborationStatus</code></td><td>Enumeration</td><td>Backend, Android y Flutter (modelo canónico)<br><strong>Diseño objetivo</strong></td><td>Definir los valores válidos de CollaborationStatus.</td><td><code>Pending</code><br><code>Accepted</code><br><code>Rejected</code><br><code>Revoked</code></td><td>—</td><td>VeterinarianClient se relaciona con CollaborationStatus</td></tr>
    <tr><td><code>AuthorizationScope</code></td><td>Value Object</td><td>Backend, Android y Flutter (modelo canónico)<br><strong>Diseño objetivo</strong></td><td>Delimitar fincas, animales y operaciones autorizadas.</td><td><code>farmIds: Set~int~</code><br><code>animalIds: Set~int~</code><br><code>canWriteHealthRecords: bool</code></td><td><code>AllowsAnimal(animalId: int): bool</code></td><td>VeterinarianClient compone AuthorizationScope</td></tr>
    <tr><td><code>CollaborationPolicy</code></td><td>Domain Service</td><td>Backend y modelos equivalentes Android/Flutter<br><strong>Diseño objetivo</strong></td><td>Evaluar aceptación y acceso dentro de una colaboración.</td><td>—</td><td><code>CanAccept(rancherId: int, relation: VeterinarianClient): bool</code><br><code>CanAccess(veterinarianId: int, animalId: int): bool</code></td><td>CollaborationPolicy depende de VeterinarianClient</td></tr>
    <tr><td><code>IVeterinarianClientRepository</code></td><td>Repository Interface</td><td>Backend; modelo equivalente en Android y Flutter<br><strong>Implementado en el backend</strong></td><td>Abstraer la persistencia de VeterinarianClient.</td><td>—</td><td><code>Find(veterinarianId: int, rancherId: int): VeterinarianClient?</code><br><code>FindByVeterinarian(id: int): List~VeterinarianClient~</code><br><code>Add(relation: VeterinarianClient): void</code><br><code>Update(relation: VeterinarianClient): void</code></td><td>IVeterinarianClientRepository depende de VeterinarianClient</td></tr>
    <tr><td><code>CollaborationRequest</code></td><td>Entity</td><td>Backend; modelo equivalente en Android y Flutter<br><strong>Diseño objetivo</strong></td><td>Representar la solicitud inicial entre veterinario y ganadero.</td><td><code>veterinarianId: int</code><br><code>rancherId: int</code><br><code>requestedAt: DateTime</code></td><td><code>Accept(at)</code><br><code>Reject()</code></td><td>Da origen o cambia el estado de VeterinarianClient.</td></tr>
    <tr><td><code>AccessGrant</code></td><td>Entity</td><td>Backend; modelo equivalente en Android y Flutter<br><strong>Diseño objetivo</strong></td><td>Materializar el permiso concedido al veterinario.</td><td><code>relationId: int</code><br><code>scope: AuthorizationScope</code><br><code>grantedAt: DateTime</code><br><code>revokedAt: DateTime?</code></td><td><code>Allows(animalId): bool</code><br><code>Revoke(at)</code></td><td>Depende de VeterinarianClient y contiene AuthorizationScope.</td></tr>
  </tbody>
</table>

<a id="toc-2-6-5-2-interface-layer"></a>

## 2.6.5.2. Interface Layer

Esta capa recibe las acciones relacionadas con **solicitud, aceptación, revocación y consulta de colaboraciones veterinarias** y las traduce a casos de uso. Los controllers y resources corresponden a la API; las pantallas y controladores de estado representan la presentación objetivo en Android y Flutter. Ninguna de estas clases implementa reglas de negocio.

<table>
  <thead>
    <tr><th>Clase</th><th>Categoría</th><th>Producto y estado</th><th>Propósito</th><th>Atributos</th><th>Métodos u operaciones</th><th>Relaciones</th></tr>
  </thead>
  <tbody>
    <tr><td><code>VeterinarianClientsController</code></td><td>REST Controller</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Publicar por HTTP las capacidades de Veterinary Collaboration.</td><td><code>IVeterinarianClientCommandService commandService</code><br><code>IVeterinarianClientQueryService queryService</code><br><code>IUserQueryService userQueryService</code><br><code>IHerdQueryService herdQueryService</code><br><code>IAnimalQueryService animalQueryService</code></td><td><code>GetClients(int veterinarianId, CancellationToken cancellationToken)</code><br><code>GetAvailableRanchers(int veterinarianId, CancellationToken cancellationToken)</code><br><code>AddClient(int veterinarianId, int rancherId, CancellationToken cancellationToken)</code><br><code>RemoveClient(int veterinarianId, int rancherId, CancellationToken cancellationToken)</code></td><td>Recibe resources, invoca servicios de aplicación y devuelve resources HTTP.</td></tr>
    <tr><td><code>AvailableRancherResource</code></td><td>Resource/Assembler</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Definir un contrato estable de entrada o salida para la API REST.</td><td><code>int Id</code><br><code>string Username</code><br><code>string FullName</code><br><code>int Herds</code><br><code>int Animals</code></td><td><code>Create(...)</code><br><code>Deconstruct(...)</code></td><td>Es construido o traducido por assemblers y consumido por el controller y los clientes móviles.</td></tr>
    <tr><td><code>VeterinarianClientResource</code></td><td>Resource/Assembler</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Definir un contrato estable de entrada o salida para la API REST.</td><td><code>int Id</code><br><code>int VeterinarianId</code><br><code>int RancherId</code><br><code>string RancherName</code><br><code>string Status</code><br><code>int Herds</code><br><code>int Animals</code><br><code>DateTime RequestedAt</code><br><code>DateTime? AcceptedAt</code></td><td><code>Create(...)</code><br><code>Deconstruct(...)</code></td><td>Es construido o traducido por assemblers y consumido por el controller y los clientes móviles.</td></tr>
    <tr><td><code>VeterinarianClientScreen</code></td><td>Composable</td><td>Android / Jetpack Compose<br><strong>Diseño objetivo</strong></td><td>Presentar solicitud, aceptación, revocación y consulta de colaboraciones veterinarias en Android.</td><td><code>uiState</code><br><code>onAction</code><br><code>navigation</code></td><td><code>Render()</code><br><code>Submit()</code><br><code>Retry()</code></td><td>Observa VeterinarianClientViewModel y emite acciones de interfaz.</td></tr>
    <tr><td><code>VeterinarianClientViewModel</code></td><td>Presentation Model</td><td>Android / Kotlin<br><strong>Diseño objetivo</strong></td><td>Mantener el estado observable y traducir acciones de Android a casos de uso.</td><td><code>state</code><br><code>observeUseCase</code><br><code>syncUseCase</code></td><td><code>Load()</code><br><code>Submit(action)</code><br><code>RetrySync()</code></td><td>Invoca casos de uso de Application Layer y publica un UI State inmutable.</td></tr>
    <tr><td><code>VeterinarianClientPage</code></td><td>Widget</td><td>Flutter / Dart<br><strong>Diseño objetivo</strong></td><td>Presentar solicitud, aceptación, revocación y consulta de colaboraciones veterinarias en Flutter.</td><td><code>state</code><br><code>onAction</code><br><code>router</code></td><td><code>build(context)</code><br><code>submit()</code><br><code>retry()</code></td><td>Observa VeterinarianClientController y emite intenciones del usuario.</td></tr>
    <tr><td><code>VeterinarianClientController</code></td><td>State Controller</td><td>Flutter / Dart<br><strong>Diseño objetivo</strong></td><td>Mantener el estado de presentación de Flutter y coordinar casos de uso.</td><td><code>state</code><br><code>observeUseCase</code><br><code>syncUseCase</code></td><td><code>load()</code><br><code>submit(action)</code><br><code>retrySync()</code></td><td>Invoca Application Layer y publica estados de carga, éxito y error.</td></tr>
  </tbody>
</table>

<a id="toc-2-6-5-3-application-layer"></a>

## 2.6.5.3. Application Layer

Esta capa coordina las capacidades de **solicitud, aceptación, revocación y consulta de colaboraciones veterinarias**. Los commands y queries expresan intenciones; los handlers cargan aggregates, aplican reglas, persisten cambios y reaccionan a eventos. Los casos de uso móviles coordinan lectura local, actualización remota y sincronización idempotente.

<table>
  <thead>
    <tr><th>Clase</th><th>Categoría</th><th>Producto y estado</th><th>Propósito</th><th>Atributos</th><th>Métodos u operaciones</th><th>Relaciones</th></tr>
  </thead>
  <tbody>
    <tr><td><code>VeterinarianClientCommandService</code></td><td>Application Service</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Orquestar solicitud, aceptación, revocación y consulta de colaboraciones veterinarias sin contener reglas del dominio.</td><td><code>IVeterinarianClientRepository repository</code><br><code>IUnitOfWork unitOfWork</code></td><td><code>Handle(CreateVeterinarianClientCommand command, CancellationToken cancellationToken)</code><br><code>Handle(DeleteVeterinarianClientCommand command, CancellationToken cancellationToken)</code></td><td>Invoca agregados y repositories; confirma la transacción mediante Unit of Work.</td></tr>
    <tr><td><code>VeterinarianClientQueryService</code></td><td>Application Service</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Orquestar solicitud, aceptación, revocación y consulta de colaboraciones veterinarias sin contener reglas del dominio.</td><td><code>IVeterinarianClientRepository repository</code></td><td><code>Handle(GetVeterinarianClientsByVeterinarianIdQuery query, CancellationToken cancellationToken)</code></td><td>Invoca agregados y repositories; confirma la transacción mediante Unit of Work.</td></tr>
    <tr><td><code>CreateVeterinarianClientCommand</code></td><td>Command/Query</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Transportar una intención o consulta tipada hacia su handler.</td><td><code>int VeterinarianId</code><br><code>int RancherId</code><br><code>string Status = "Accepted"</code></td><td>—</td><td>Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio.</td></tr>
    <tr><td><code>DeleteVeterinarianClientCommand</code></td><td>Command/Query</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Transportar una intención o consulta tipada hacia su handler.</td><td><code>int VeterinarianId</code><br><code>int RancherId</code></td><td>—</td><td>Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio.</td></tr>
    <tr><td><code>GetVeterinarianClientsByVeterinarianIdQuery</code></td><td>Command/Query</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Transportar una intención o consulta tipada hacia su handler.</td><td><code>int VeterinarianId</code></td><td>—</td><td>Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio.</td></tr>
    <tr><td><code>ObserveVeterinarianClientUseCase</code></td><td>Use Case</td><td>Android y Flutter<br><strong>Diseño objetivo</strong></td><td>Entregar primero datos locales y actualizar la consulta cuando exista conectividad.</td><td><code>localRepository</code><br><code>remoteRepository</code><br><code>connectivityMonitor</code></td><td><code>Execute(criteria): Stream&lt;Result&gt;</code></td><td>Es invocado por ViewModel/Controller y coordina repositorios móviles.</td></tr>
    <tr><td><code>SyncVeterinarianClientUseCase</code></td><td>Use Case</td><td>Android y Flutter<br><strong>Diseño objetivo</strong></td><td>Procesar operaciones móviles pendientes de manera idempotente.</td><td><code>outboxRepository</code><br><code>remoteRepository</code><br><code>conflictResolver</code></td><td><code>Execute(): SyncResult</code></td><td>Lee el outbox local, consume la API y actualiza el estado de sincronización.</td></tr>
    <tr><td><code>RequestCollaborationCommandHandler</code></td><td>Command Handler</td><td>Backend ASP.NET Core<br><strong>Diseño objetivo</strong></td><td>Ejecutar una intención concreta, aplicar reglas del agregado y confirmar la transacción.</td><td><code>repository</code><br><code>unitOfWork</code><br><code>domainPolicy</code></td><td><code>Handle(command): Result</code></td><td>Consume un Command, carga el aggregate mediante su repository y puede publicar un Domain Event.</td></tr>
    <tr><td><code>AcceptCollaborationCommandHandler</code></td><td>Command Handler</td><td>Backend ASP.NET Core<br><strong>Diseño objetivo</strong></td><td>Ejecutar una intención concreta, aplicar reglas del agregado y confirmar la transacción.</td><td><code>repository</code><br><code>unitOfWork</code><br><code>domainPolicy</code></td><td><code>Handle(command): Result</code></td><td>Consume un Command, carga el aggregate mediante su repository y puede publicar un Domain Event.</td></tr>
    <tr><td><code>CollaborationAcceptedEventHandler</code></td><td>Event Handler</td><td>Backend ASP.NET Core<br><strong>Diseño objetivo</strong></td><td>Reaccionar al evento confirmado y actualizar proyecciones o integraciones.</td><td><code>projectionRepository</code><br><code>notificationPort</code><br><code>unitOfWork</code></td><td><code>Handle(domainEvent): Task</code></td><td>Consume un Domain Event y utiliza puertos de infraestructura sin modificar directamente el agregado.</td></tr>
  </tbody>
</table>

<a id="toc-2-6-5-4-infrastructure-layer"></a>

## 2.6.5.4. Infrastructure Layer

Esta capa implementa los puertos definidos hacia el interior de **Veterinary Collaboration** y concentra acceso a base de datos, red, almacenamiento local e integraciones externas. Las clases de infraestructura traducen errores y contratos técnicos antes de devolver resultados a Application Layer.

<table>
  <thead>
    <tr><th>Clase</th><th>Categoría</th><th>Producto y estado</th><th>Propósito</th><th>Atributos</th><th>Métodos u operaciones</th><th>Relaciones</th></tr>
  </thead>
  <tbody>
    <tr><td><code>VeterinarianClientRepository</code></td><td>Repository Adapter</td><td>Backend / Entity Framework Core<br><strong>Implementado en el backend</strong></td><td>Implementar el puerto de persistencia definido por Domain Layer.</td><td><code>AppDbContext context</code></td><td><code>FindByVeterinarianIdAsync(int veterinarianId, CancellationToken cancellationToken)</code><br><code>FindByVeterinarianIdAndRancherIdAsync(int veterinarianId, int rancherId, CancellationToken cancellationToken)</code><br><code>ExistsByVeterinarianIdAndRancherIdAsync(int veterinarianId, int rancherId, CancellationToken cancellationToken)</code></td><td>Implementa IVeterinarianClientRepository; utiliza AppDbContext/MySQL y reconstruye el aggregate.</td></tr>
    <tr><td><code>ModelBuilderExtensions</code></td><td>Persistence Configuration</td><td>Backend / Entity Framework Core<br><strong>Implementado en el backend</strong></td><td>Mapear entidades y value objects del contexto al modelo relacional.</td><td><code>EntityTypeBuilder configuration</code></td><td><code>ApplyConfiguration(modelBuilder)</code></td><td>Configura tablas, claves, relaciones, restricciones y conversiones de Entity Framework Core.</td></tr>
    <tr><td><code>VeterinarianClientApiDataSource</code></td><td>Remote Adapter</td><td>Android / Kotlin<br><strong>Diseño objetivo</strong></td><td>Implementar el acceso remoto del cliente móvil a la API.</td><td><code>httpClient</code><br><code>tokenProvider</code><br><code>serializer</code></td><td><code>Get(criteria)</code><br><code>Create(dto)</code><br><code>Update(dto)</code><br><code>Delete(id)</code></td><td>Consume controllers REST por HTTPS/JSON y traduce errores HTTP al modelo de aplicación.</td></tr>
    <tr><td><code>VeterinarianClientDao</code></td><td>Room Adapter</td><td>Android / Room<br><strong>Diseño objetivo</strong></td><td>Implementar persistencia local y observación reactiva en Android.</td><td><code>roomDatabase</code><br><code>entityMapper</code></td><td><code>Observe(criteria)</code><br><code>Upsert(entity)</code><br><code>Delete(id)</code><br><code>Pending()</code></td><td>Implementa el puerto local mediante Room y participa en la estrategia de caché/outbox.</td></tr>
    <tr><td><code>VeterinarianClientRemoteDataSource</code></td><td>Remote Adapter</td><td>Flutter / Dart<br><strong>Diseño objetivo</strong></td><td>Implementar el acceso remoto del cliente móvil a la API.</td><td><code>httpClient</code><br><code>tokenProvider</code><br><code>serializer</code></td><td><code>Get(criteria)</code><br><code>Create(dto)</code><br><code>Update(dto)</code><br><code>Delete(id)</code></td><td>Consume controllers REST por HTTPS/JSON y traduce errores HTTP al modelo de aplicación.</td></tr>
    <tr><td><code>VeterinarianClientLocalDataSource</code></td><td>SQLite Adapter</td><td>Flutter / Dart<br><strong>Diseño objetivo</strong></td><td>Implementar persistencia local equivalente en Flutter.</td><td><code>sqliteDatabase</code><br><code>entityMapper</code></td><td><code>watch(criteria)</code><br><code>upsert(entity)</code><br><code>delete(id)</code><br><code>pending()</code></td><td>Implementa el puerto local mediante SQLite y participa en la estrategia de caché/outbox.</td></tr>
    <tr><td><code>IamIdentityAdapter</code></td><td>Context Adapter</td><td>Backend ASP.NET Core<br><strong>Diseño objetivo</strong></td><td>Aislar una dependencia externa detrás de un puerto explícito.</td><td><code>iamFacade</code></td><td><code>GetRole(userId)</code><br><code>Exists(userId): bool</code></td><td>Implementa el puerto de identidad y consume IAM.</td></tr>
    <tr><td><code>ProfilesDirectoryAdapter</code></td><td>Context Adapter</td><td>Backend ASP.NET Core<br><strong>Diseño objetivo</strong></td><td>Aislar una dependencia externa detrás de un puerto explícito.</td><td><code>profilesFacade</code></td><td><code>GetDisplayName(userId)</code><br><code>FindRanchers()</code></td><td>Implementa el puerto de directorio y consume Profile Management.</td></tr>
    <tr><td><code>LivestockPatientAdapter</code></td><td>Context Adapter</td><td>Backend ASP.NET Core<br><strong>Diseño objetivo</strong></td><td>Aislar una dependencia externa detrás de un puerto explícito.</td><td><code>livestockFacade</code></td><td><code>GetAnimals(rancherId)</code><br><code>ValidateScope(scope)</code></td><td>Implementa el puerto de pacientes y consume Livestock Management.</td></tr>
  </tbody>
</table>

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


