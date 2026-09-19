<a id="toc-2-6-6-bounded-context-activity-management"></a>

# 2.6.6. Bounded Context: Activity Management

Planificar actividades ganaderas y sanitarias, controlar su estado y decidir cuándo corresponde generar un recordatorio.

La base implementada se encuentra en el módulo `Activities` de la API ASP.NET Core. El diseño móvil de Android y Flutter se presenta como **diseño objetivo** porque esos clientes todavía no existen en el workspace. Los tres productos comparten contratos REST y lenguaje ubicuo, mientras la API conserva las reglas autoritativas.

<a id="toc-2-6-6-1-domain-layer"></a>

## 2.6.6.1. Domain Layer

**Responsabilidad estable.** Esta capa documenta el modelo que representa el núcleo de **Activity Management**. Las reglas autoritativas se ejecutan en la API; Android y Flutter mantienen modelos equivalentes para presentación, validación inmediata y trabajo offline. La columna de estado distingue el código heredado de la arquitectura objetivo.

**Detalle técnico evolutivo.** El siguiente diccionario identifica las clases, sus responsabilidades, atributos, métodos y relaciones. La columna **Producto y estado** distingue los elementos comprobados en el código de aquellos que aún pertenecen al diseño objetivo.

<table>
  <thead>
    <tr><th>Clase</th><th>Categoría</th><th>Producto y estado</th><th>Propósito</th><th>Atributos</th><th>Métodos u operaciones</th><th>Relaciones</th></tr>
  </thead>
  <tbody>
    <tr><td><code>FarmActivity</code></td><td>Aggregate Root</td><td>Backend; modelo equivalente en Android y Flutter<br><strong>Implementado en el backend</strong></td><td>Controlar el ciclo de vida de una actividad programada.</td><td><code>id: int</code><br><code>ownerId: int?</code><br><code>veterinarianId: int?</code><br><code>animalId: int?</code><br><code>title: string</code><br><code>type: string</code><br><code>schedule: ActivitySchedule</code><br><code>priority: ActivityPriority</code><br><code>status: ActivityStatus</code></td><td><code>Reschedule(schedule: ActivitySchedule): void</code><br><code>Complete(): void</code><br><code>Cancel(): void</code></td><td>FarmActivity compone ActivitySchedule; FarmActivity se relaciona con ActivityPriority; FarmActivity se relaciona con ActivityStatus; ReminderPolicy depende de FarmActivity; IFarmActivityRepository depende de FarmActivity</td></tr>
    <tr><td><code>ActivitySchedule</code></td><td>Value Object</td><td>Backend, Android y Flutter (modelo canónico)<br><strong>Diseño objetivo</strong></td><td>Representar fecha programada y recordatorio.</td><td><code>scheduledAt: DateTime</code><br><code>reminderAt: DateTime?</code></td><td><code>IsUpcoming(now: DateTime): bool</code></td><td>FarmActivity compone ActivitySchedule</td></tr>
    <tr><td><code>ActivityPriority</code></td><td>Enumeration</td><td>Backend, Android y Flutter (modelo canónico)<br><strong>Diseño objetivo</strong></td><td>Definir los valores válidos de ActivityPriority.</td><td><code>Low</code><br><code>Medium</code><br><code>High</code></td><td>—</td><td>FarmActivity se relaciona con ActivityPriority</td></tr>
    <tr><td><code>ActivityStatus</code></td><td>Enumeration</td><td>Backend, Android y Flutter (modelo canónico)<br><strong>Diseño objetivo</strong></td><td>Definir los valores válidos de ActivityStatus.</td><td><code>Pending</code><br><code>InProgress</code><br><code>Completed</code><br><code>Cancelled</code></td><td>—</td><td>FarmActivity se relaciona con ActivityStatus</td></tr>
    <tr><td><code>ReminderPolicy</code></td><td>Domain Service</td><td>Backend, Android y Flutter (modelo canónico)<br><strong>Diseño objetivo</strong></td><td>Decidir cuándo debe emitirse una notificación.</td><td>—</td><td><code>ShouldNotify(activity: FarmActivity, now: DateTime): bool</code></td><td>ReminderPolicy depende de FarmActivity</td></tr>
    <tr><td><code>IFarmActivityRepository</code></td><td>Repository Interface</td><td>Backend; modelo equivalente en Android y Flutter<br><strong>Implementado en el backend</strong></td><td>Abstraer la persistencia de FarmActivity.</td><td>—</td><td><code>FindById(id: int): FarmActivity?</code><br><code>FindUpcoming(userId: int): List~FarmActivity~</code><br><code>Add(activity: FarmActivity): void</code><br><code>Update(activity: FarmActivity): void</code></td><td>IFarmActivityRepository depende de FarmActivity</td></tr>
  </tbody>
</table>

<a id="toc-2-6-6-2-interface-layer"></a>

## 2.6.6.2. Interface Layer

**Responsabilidad estable.** Esta capa recibe las acciones relacionadas con **programación, reprogramación, finalización y recordatorio de actividades** y las traduce a casos de uso. Los controllers y resources corresponden a la API; las pantallas y controladores de estado representan la presentación objetivo en Android y Flutter. Ninguna de estas clases implementa reglas de negocio.

**Detalle técnico evolutivo.** El siguiente diccionario identifica las clases, sus responsabilidades, atributos, métodos y relaciones. La columna **Producto y estado** distingue los elementos comprobados en el código de aquellos que aún pertenecen al diseño objetivo.

<table>
  <thead>
    <tr><th>Clase</th><th>Categoría</th><th>Producto y estado</th><th>Propósito</th><th>Atributos</th><th>Métodos u operaciones</th><th>Relaciones</th></tr>
  </thead>
  <tbody>
    <tr><td><code>FarmActivitiesController</code></td><td>REST Controller</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Publicar por HTTP las capacidades de Activity Management.</td><td><code>IFarmActivityCommandService commandService</code><br><code>IFarmActivityQueryService queryService</code></td><td><code>GetAll(CancellationToken cancellationToken)</code><br><code>GetById(int id, CancellationToken cancellationToken)</code><br><code>Create(CreateFarmActivityResource resource, CancellationToken cancellationToken)</code><br><code>Update(int id, CreateFarmActivityResource resource, CancellationToken cancellationToken)</code><br><code>Delete(int id, CancellationToken cancellationToken)</code></td><td>Recibe resources, invoca servicios de aplicación y devuelve resources HTTP.</td></tr>
    <tr><td><code>CreateFarmActivityResource</code></td><td>Resource/Assembler</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Definir un contrato estable de entrada o salida para la API REST.</td><td><code>int? OwnerId</code><br><code>int? VeterinarianId</code><br><code>string Title</code><br><code>string Type</code><br><code>DateOnly Date</code><br><code>string Priority</code><br><code>string Status</code></td><td><code>Create(...)</code><br><code>Deconstruct(...)</code></td><td>Es construido o traducido por assemblers y consumido por el controller y los clientes móviles.</td></tr>
    <tr><td><code>FarmActivityResource</code></td><td>Resource/Assembler</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Definir un contrato estable de entrada o salida para la API REST.</td><td><code>int Id</code><br><code>int? OwnerId</code><br><code>int? VeterinarianId</code><br><code>string Title</code><br><code>string Type</code><br><code>DateOnly Date</code><br><code>string Priority</code><br><code>string Status</code></td><td><code>Create(...)</code><br><code>Deconstruct(...)</code></td><td>Es construido o traducido por assemblers y consumido por el controller y los clientes móviles.</td></tr>
    <tr><td><code>FarmActivityScreen</code></td><td>Composable</td><td>Android / Jetpack Compose<br><strong>Diseño objetivo</strong></td><td>Presentar programación, reprogramación, finalización y recordatorio de actividades en Android.</td><td><code>uiState</code><br><code>onAction</code><br><code>navigation</code></td><td><code>Render()</code><br><code>Submit()</code><br><code>Retry()</code></td><td>Observa FarmActivityViewModel y emite acciones de interfaz.</td></tr>
    <tr><td><code>FarmActivityViewModel</code></td><td>Presentation Model</td><td>Android / Kotlin<br><strong>Diseño objetivo</strong></td><td>Mantener el estado observable y traducir acciones de Android a casos de uso.</td><td><code>state</code><br><code>observeUseCase</code><br><code>syncUseCase</code></td><td><code>Load()</code><br><code>Submit(action)</code><br><code>RetrySync()</code></td><td>Invoca casos de uso de Application Layer y publica un UI State inmutable.</td></tr>
    <tr><td><code>FarmActivityPage</code></td><td>Widget</td><td>Flutter / Dart<br><strong>Diseño objetivo</strong></td><td>Presentar programación, reprogramación, finalización y recordatorio de actividades en Flutter.</td><td><code>state</code><br><code>onAction</code><br><code>router</code></td><td><code>build(context)</code><br><code>submit()</code><br><code>retry()</code></td><td>Observa FarmActivityController y emite intenciones del usuario.</td></tr>
    <tr><td><code>FarmActivityController</code></td><td>State Controller</td><td>Flutter / Dart<br><strong>Diseño objetivo</strong></td><td>Mantener el estado de presentación de Flutter y coordinar casos de uso.</td><td><code>state</code><br><code>observeUseCase</code><br><code>syncUseCase</code></td><td><code>load()</code><br><code>submit(action)</code><br><code>retrySync()</code></td><td>Invoca Application Layer y publica estados de carga, éxito y error.</td></tr>
  </tbody>
</table>

<a id="toc-2-6-6-3-application-layer"></a>

## 2.6.6.3. Application Layer

**Responsabilidad estable.** Esta capa coordina las capacidades de **programación, reprogramación, finalización y recordatorio de actividades**. Los commands y queries expresan intenciones; los handlers cargan aggregates, aplican reglas, persisten cambios y reaccionan a eventos. Los casos de uso móviles coordinan lectura local, actualización remota y sincronización idempotente.

**Detalle técnico evolutivo.** El siguiente diccionario identifica las clases, sus responsabilidades, atributos, métodos y relaciones. La columna **Producto y estado** distingue los elementos comprobados en el código de aquellos que aún pertenecen al diseño objetivo.

<table>
  <thead>
    <tr><th>Clase</th><th>Categoría</th><th>Producto y estado</th><th>Propósito</th><th>Atributos</th><th>Métodos u operaciones</th><th>Relaciones</th></tr>
  </thead>
  <tbody>
    <tr><td><code>FarmActivityCommandService</code></td><td>Application Service</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Orquestar programación, reprogramación, finalización y recordatorio de actividades sin contener reglas del dominio.</td><td><code>IFarmActivityRepository repository</code><br><code>IUnitOfWork unitOfWork</code></td><td><code>Handle(CreateFarmActivityCommand command, CancellationToken cancellationToken)</code><br><code>Handle(UpdateFarmActivityCommand command, CancellationToken cancellationToken)</code><br><code>Handle(DeleteFarmActivityCommand command, CancellationToken cancellationToken)</code></td><td>Invoca agregados y repositories; confirma la transacción mediante Unit of Work.</td></tr>
    <tr><td><code>FarmActivityQueryService</code></td><td>Application Service</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Orquestar programación, reprogramación, finalización y recordatorio de actividades sin contener reglas del dominio.</td><td><code>IFarmActivityRepository repository</code></td><td><code>Handle(GetFarmActivityByIdQuery query, CancellationToken cancellationToken)</code><br><code>Handle(GetAllFarmActivitiesQuery query, CancellationToken cancellationToken)</code></td><td>Invoca agregados y repositories; confirma la transacción mediante Unit of Work.</td></tr>
    <tr><td><code>CreateFarmActivityCommand</code></td><td>Command/Query</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Transportar una intención o consulta tipada hacia su handler.</td><td><code>int? OwnerId</code><br><code>int? VeterinarianId</code><br><code>string Title</code><br><code>string Type</code><br><code>DateOnly Date</code><br><code>string Priority</code><br><code>string Status</code></td><td>—</td><td>Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio.</td></tr>
    <tr><td><code>UpdateFarmActivityCommand</code></td><td>Command/Query</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Transportar una intención o consulta tipada hacia su handler.</td><td><code>int Id</code><br><code>int? OwnerId</code><br><code>int? VeterinarianId</code><br><code>string Title</code><br><code>string Type</code><br><code>DateOnly Date</code><br><code>string Priority</code><br><code>string Status</code></td><td>—</td><td>Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio.</td></tr>
    <tr><td><code>DeleteFarmActivityCommand</code></td><td>Command/Query</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Transportar una intención o consulta tipada hacia su handler.</td><td><code>int Id</code></td><td>—</td><td>Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio.</td></tr>
    <tr><td><code>GetFarmActivityByIdQuery</code></td><td>Command/Query</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Transportar una intención o consulta tipada hacia su handler.</td><td><code>int Id</code></td><td>—</td><td>Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio.</td></tr>
    <tr><td><code>ObserveFarmActivityUseCase</code></td><td>Use Case</td><td>Android y Flutter<br><strong>Diseño objetivo</strong></td><td>Entregar primero datos locales y actualizar la consulta cuando exista conectividad.</td><td><code>localRepository</code><br><code>remoteRepository</code><br><code>connectivityMonitor</code></td><td><code>Execute(criteria): Stream&lt;Result&gt;</code></td><td>Es invocado por ViewModel/Controller y coordina repositorios móviles.</td></tr>
    <tr><td><code>SyncFarmActivityUseCase</code></td><td>Use Case</td><td>Android y Flutter<br><strong>Diseño objetivo</strong></td><td>Procesar operaciones móviles pendientes de manera idempotente.</td><td><code>outboxRepository</code><br><code>remoteRepository</code><br><code>conflictResolver</code></td><td><code>Execute(): SyncResult</code></td><td>Lee el outbox local, consume la API y actualiza el estado de sincronización.</td></tr>
    <tr><td><code>CreateFarmActivityCommandHandler</code></td><td>Command Handler</td><td>Backend ASP.NET Core<br><strong>Diseño objetivo</strong></td><td>Ejecutar una intención concreta, aplicar reglas del agregado y confirmar la transacción.</td><td><code>repository</code><br><code>unitOfWork</code><br><code>domainPolicy</code></td><td><code>Handle(command): Result</code></td><td>Consume un Command, carga el aggregate mediante su repository y puede publicar un Domain Event.</td></tr>
    <tr><td><code>CompleteFarmActivityCommandHandler</code></td><td>Command Handler</td><td>Backend ASP.NET Core<br><strong>Diseño objetivo</strong></td><td>Ejecutar una intención concreta, aplicar reglas del agregado y confirmar la transacción.</td><td><code>repository</code><br><code>unitOfWork</code><br><code>domainPolicy</code></td><td><code>Handle(command): Result</code></td><td>Consume un Command, carga el aggregate mediante su repository y puede publicar un Domain Event.</td></tr>
    <tr><td><code>ActivityScheduledEventHandler</code></td><td>Event Handler</td><td>Backend ASP.NET Core<br><strong>Diseño objetivo</strong></td><td>Reaccionar al evento confirmado y actualizar proyecciones o integraciones.</td><td><code>projectionRepository</code><br><code>notificationPort</code><br><code>unitOfWork</code></td><td><code>Handle(domainEvent): Task</code></td><td>Consume un Domain Event y utiliza puertos de infraestructura sin modificar directamente el agregado.</td></tr>
  </tbody>
</table>

<a id="toc-2-6-6-4-infrastructure-layer"></a>

## 2.6.6.4. Infrastructure Layer

**Responsabilidad estable.** Esta capa implementa los puertos definidos hacia el interior de **Activity Management** y concentra acceso a base de datos, red, almacenamiento local e integraciones externas. Las clases de infraestructura traducen errores y contratos técnicos antes de devolver resultados a Application Layer.

**Detalle técnico evolutivo.** El siguiente diccionario identifica las clases, sus responsabilidades, atributos, métodos y relaciones. La columna **Producto y estado** distingue los elementos comprobados en el código de aquellos que aún pertenecen al diseño objetivo.

<table>
  <thead>
    <tr><th>Clase</th><th>Categoría</th><th>Producto y estado</th><th>Propósito</th><th>Atributos</th><th>Métodos u operaciones</th><th>Relaciones</th></tr>
  </thead>
  <tbody>
    <tr><td><code>FarmActivityRepository</code></td><td>Repository Adapter</td><td>Backend / Entity Framework Core<br><strong>Implementado en el backend</strong></td><td>Implementar el puerto de persistencia definido por Domain Layer.</td><td><code>AppDbContext context</code></td><td><code>FindById(id)</code><br><code>Add(entity)</code><br><code>Update(entity)</code><br><code>Delete(entity)</code></td><td>Implementa IFarmActivityRepository; utiliza AppDbContext/MySQL y reconstruye el aggregate.</td></tr>
    <tr><td><code>ModelBuilderExtensions</code></td><td>Persistence Configuration</td><td>Backend / Entity Framework Core<br><strong>Implementado en el backend</strong></td><td>Mapear entidades y value objects del contexto al modelo relacional.</td><td><code>EntityTypeBuilder configuration</code></td><td><code>ApplyConfiguration(modelBuilder)</code></td><td>Configura tablas, claves, relaciones, restricciones y conversiones de Entity Framework Core.</td></tr>
    <tr><td><code>FarmActivityApiDataSource</code></td><td>Remote Adapter</td><td>Android / Kotlin<br><strong>Diseño objetivo</strong></td><td>Implementar el acceso remoto del cliente móvil a la API.</td><td><code>httpClient</code><br><code>tokenProvider</code><br><code>serializer</code></td><td><code>Get(criteria)</code><br><code>Create(dto)</code><br><code>Update(dto)</code><br><code>Delete(id)</code></td><td>Consume controllers REST por HTTPS/JSON y traduce errores HTTP al modelo de aplicación.</td></tr>
    <tr><td><code>FarmActivityDao</code></td><td>Room Adapter</td><td>Android / Room<br><strong>Diseño objetivo</strong></td><td>Implementar persistencia local y observación reactiva en Android.</td><td><code>roomDatabase</code><br><code>entityMapper</code></td><td><code>Observe(criteria)</code><br><code>Upsert(entity)</code><br><code>Delete(id)</code><br><code>Pending()</code></td><td>Implementa el puerto local mediante Room y participa en la estrategia de caché/outbox.</td></tr>
    <tr><td><code>FarmActivityRemoteDataSource</code></td><td>Remote Adapter</td><td>Flutter / Dart<br><strong>Diseño objetivo</strong></td><td>Implementar el acceso remoto del cliente móvil a la API.</td><td><code>httpClient</code><br><code>tokenProvider</code><br><code>serializer</code></td><td><code>Get(criteria)</code><br><code>Create(dto)</code><br><code>Update(dto)</code><br><code>Delete(id)</code></td><td>Consume controllers REST por HTTPS/JSON y traduce errores HTTP al modelo de aplicación.</td></tr>
    <tr><td><code>FarmActivityLocalDataSource</code></td><td>SQLite Adapter</td><td>Flutter / Dart<br><strong>Diseño objetivo</strong></td><td>Implementar persistencia local equivalente en Flutter.</td><td><code>sqliteDatabase</code><br><code>entityMapper</code></td><td><code>watch(criteria)</code><br><code>upsert(entity)</code><br><code>delete(id)</code><br><code>pending()</code></td><td>Implementa el puerto local mediante SQLite y participa en la estrategia de caché/outbox.</td></tr>
    <tr><td><code>LivestockReferenceAdapter</code></td><td>Context Adapter</td><td>Backend ASP.NET Core<br><strong>Diseño objetivo</strong></td><td>Aislar una dependencia externa detrás de un puerto explícito.</td><td><code>livestockFacade</code></td><td><code>ExistsAnimal(animalId): bool</code></td><td>Implementa el puerto de referencia de animales.</td></tr>
    <tr><td><code>SanitaryReferenceAdapter</code></td><td>Context Adapter</td><td>Backend ASP.NET Core<br><strong>Diseño objetivo</strong></td><td>Aislar una dependencia externa detrás de un puerto explícito.</td><td><code>sanitaryFacade</code></td><td><code>GetFollowUpDate(eventId): Date?</code></td><td>Implementa el puerto de seguimiento sanitario.</td></tr>
    <tr><td><code>FirebaseReminderPublisher</code></td><td>Messaging Adapter</td><td>Backend y Android<br><strong>Diseño objetivo</strong></td><td>Aislar una dependencia externa detrás de un puerto explícito.</td><td><code>fcmClient, localNotifier</code></td><td><code>Publish(reminder)</code><br><code>ScheduleLocal(reminder)</code></td><td>Implementa el puerto de notificaciones mediante FCM y notificaciones locales.</td></tr>
  </tbody>
</table>

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
