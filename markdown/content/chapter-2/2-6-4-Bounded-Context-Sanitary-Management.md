<a id="toc-2-6-4-bounded-context-sanitary-management"></a>

# 2.6.4. Bounded Context: Sanitary Management

Conservar la historia sanitaria del animal y controlar el registro de diagnósticos, tratamientos, prescripciones y seguimientos autorizados.

La base implementada se encuentra en el módulo `Sanitary` de la API ASP.NET Core. El diseño móvil de Android y Flutter se presenta como **diseño objetivo** porque esos clientes todavía no existen en el workspace. Los tres productos comparten contratos REST y lenguaje ubicuo, mientras la API conserva las reglas autoritativas.

<a id="toc-2-6-4-1-domain-layer"></a>

## 2.6.4.1. Domain Layer

Esta capa documenta el modelo que representa el núcleo de **Sanitary Management**. Las reglas autoritativas se ejecutan en la API; Android y Flutter mantienen modelos equivalentes para presentación, validación inmediata y trabajo offline. La columna de estado distingue el código heredado de la arquitectura objetivo.

<table>
  <thead>
    <tr><th>Clase</th><th>Categoría</th><th>Producto y estado</th><th>Propósito</th><th>Atributos</th><th>Métodos u operaciones</th><th>Relaciones</th></tr>
  </thead>
  <tbody>
    <tr><td><code>HealthEvent</code></td><td>Aggregate Root</td><td>Backend; modelo equivalente en Android y Flutter<br><strong>Implementado en el backend</strong></td><td>Mantener un acontecimiento clínico dentro de la historia sanitaria.</td><td><code>id: int</code><br><code>animalId: int</code><br><code>type: HealthEventType</code><br><code>date: Date</code><br><code>veterinarianId: int?</code><br><code>description: string</code><br><code>diagnosis: Diagnosis</code><br><code>treatment: Treatment</code><br><code>prescription: Prescription</code><br><code>nextDueDate: Date?</code></td><td><code>RescheduleFollowUp(date: Date): void</code><br><code>UpdateClinicalData(diagnosis: Diagnosis, treatment: Treatment): void</code></td><td>HealthEvent compone Diagnosis; HealthEvent compone Treatment; HealthEvent compone Prescription; HealthEvent se relaciona con HealthEventType; SanitaryAuthorizationPolicy depende de HealthEvent; IHealthEventRepository depende de HealthEvent</td></tr>
    <tr><td><code>Diagnosis</code></td><td>Value Object</td><td>Backend, Android y Flutter (modelo canónico)<br><strong>Diseño objetivo</strong></td><td>Representar el diagnóstico clínico.</td><td><code>description: string</code></td><td><code>IsEmpty(): bool</code></td><td>HealthEvent compone Diagnosis</td></tr>
    <tr><td><code>Treatment</code></td><td>Value Object</td><td>Backend, Android y Flutter (modelo canónico)<br><strong>Diseño objetivo</strong></td><td>Representar instrucciones de tratamiento.</td><td><code>instructions: string</code></td><td><code>IsValid(): bool</code></td><td>HealthEvent compone Treatment</td></tr>
    <tr><td><code>Prescription</code></td><td>Value Object</td><td>Backend, Android y Flutter (modelo canónico)<br><strong>Diseño objetivo</strong></td><td>Representar la prescripción asociada a un evento sanitario.</td><td><code>details: string</code></td><td><code>IsRequired(): bool</code></td><td>HealthEvent compone Prescription</td></tr>
    <tr><td><code>HealthEventType</code></td><td>Enumeration</td><td>Backend y modelos equivalentes Android/Flutter<br><strong>Implementado en el backend</strong></td><td>Definir los valores válidos de HealthEventType.</td><td><code>MedicalVisit</code><br><code>Vaccination</code><br><code>Treatment</code><br><code>SanitaryControl</code></td><td>—</td><td>HealthEvent se relaciona con HealthEventType</td></tr>
    <tr><td><code>SanitaryAuthorizationPolicy</code></td><td>Domain Service</td><td>Backend, Android y Flutter (modelo canónico)<br><strong>Diseño objetivo</strong></td><td>Decidir si un actor puede registrar información sanitaria.</td><td>—</td><td><code>CanRegister(actorId: int, animalId: int): bool</code></td><td>SanitaryAuthorizationPolicy depende de HealthEvent</td></tr>
    <tr><td><code>IHealthEventRepository</code></td><td>Repository Interface</td><td>Backend; modelo equivalente en Android y Flutter<br><strong>Implementado en el backend</strong></td><td>Abstraer la persistencia de HealthEvent.</td><td>—</td><td><code>FindById(id: int): HealthEvent?</code><br><code>FindByAnimal(animalId: int): List~HealthEvent~</code><br><code>Add(event: HealthEvent): void</code><br><code>Update(event: HealthEvent): void</code></td><td>IHealthEventRepository depende de HealthEvent</td></tr>
    <tr><td><code>MedicalVisit</code></td><td>Entity</td><td>Backend; modelo equivalente en Android y Flutter<br><strong>Diseño objetivo</strong></td><td>Representar una visita veterinaria asociada con el historial sanitario.</td><td><code>id: int</code><br><code>healthEventId: int</code><br><code>veterinarianId: int</code><br><code>scheduledAt: DateTime</code><br><code>status: string</code></td><td><code>Reschedule(date)</code><br><code>Complete()</code></td><td>Pertenece a HealthEvent y referencia al veterinario autorizado.</td></tr>
    <tr><td><code>SanitaryAlert</code></td><td>Entity</td><td>Backend; modelo equivalente en Android y Flutter<br><strong>Diseño objetivo</strong></td><td>Representar una alerta por vacunación, tratamiento o seguimiento pendiente.</td><td><code>id: int</code><br><code>animalId: int</code><br><code>dueDate: Date</code><br><code>severity: string</code></td><td><code>IsDue(on: Date): bool</code><br><code>Dismiss()</code></td><td>Se origina desde HealthEvent y puede generar una actividad.</td></tr>
  </tbody>
</table>

<a id="toc-2-6-4-2-interface-layer"></a>

## 2.6.4.2. Interface Layer

Esta capa recibe las acciones relacionadas con **registro y seguimiento de eventos sanitarios, diagnósticos y tratamientos** y las traduce a casos de uso. Los controllers y resources corresponden a la API; las pantallas y controladores de estado representan la presentación objetivo en Android y Flutter. Ninguna de estas clases implementa reglas de negocio.

<table>
  <thead>
    <tr><th>Clase</th><th>Categoría</th><th>Producto y estado</th><th>Propósito</th><th>Atributos</th><th>Métodos u operaciones</th><th>Relaciones</th></tr>
  </thead>
  <tbody>
    <tr><td><code>HealthEventsController</code></td><td>REST Controller</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Publicar por HTTP las capacidades de Sanitary Management.</td><td><code>IHealthEventCommandService commandService</code><br><code>IHealthEventQueryService queryService</code></td><td><code>GetAll(CancellationToken cancellationToken)</code><br><code>GetById(int id, CancellationToken cancellationToken)</code><br><code>Create(CreateHealthEventResource resource, CancellationToken cancellationToken)</code><br><code>Update(int id, CreateHealthEventResource resource, CancellationToken cancellationToken)</code><br><code>Delete(int id, CancellationToken cancellationToken)</code></td><td>Recibe resources, invoca servicios de aplicación y devuelve resources HTTP.</td></tr>
    <tr><td><code>CreateHealthEventResource</code></td><td>Resource/Assembler</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Definir un contrato estable de entrada o salida para la API REST.</td><td><code>int AnimalId</code><br><code>string Type</code><br><code>DateOnly Date</code><br><code>string Description</code><br><code>string Veterinarian</code><br><code>string Diagnosis</code><br><code>string Treatment</code><br><code>string Prescription</code><br><code>string FollowUp</code><br><code>DateOnly? NextDueDate</code></td><td><code>Create(...)</code><br><code>Deconstruct(...)</code></td><td>Es construido o traducido por assemblers y consumido por el controller y los clientes móviles.</td></tr>
    <tr><td><code>HealthEventResource</code></td><td>Resource/Assembler</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Definir un contrato estable de entrada o salida para la API REST.</td><td><code>int Id</code><br><code>int AnimalId</code><br><code>string Type</code><br><code>DateOnly Date</code><br><code>string Description</code><br><code>string Veterinarian</code><br><code>string Diagnosis</code><br><code>string Treatment</code><br><code>string Prescription</code><br><code>string FollowUp</code><br><code>DateOnly? NextDueDate</code></td><td><code>Create(...)</code><br><code>Deconstruct(...)</code></td><td>Es construido o traducido por assemblers y consumido por el controller y los clientes móviles.</td></tr>
    <tr><td><code>HealthEventScreen</code></td><td>Composable</td><td>Android / Jetpack Compose<br><strong>Diseño objetivo</strong></td><td>Presentar registro y seguimiento de eventos sanitarios, diagnósticos y tratamientos en Android.</td><td><code>uiState</code><br><code>onAction</code><br><code>navigation</code></td><td><code>Render()</code><br><code>Submit()</code><br><code>Retry()</code></td><td>Observa HealthEventViewModel y emite acciones de interfaz.</td></tr>
    <tr><td><code>HealthEventViewModel</code></td><td>Presentation Model</td><td>Android / Kotlin<br><strong>Diseño objetivo</strong></td><td>Mantener el estado observable y traducir acciones de Android a casos de uso.</td><td><code>state</code><br><code>observeUseCase</code><br><code>syncUseCase</code></td><td><code>Load()</code><br><code>Submit(action)</code><br><code>RetrySync()</code></td><td>Invoca casos de uso de Application Layer y publica un UI State inmutable.</td></tr>
    <tr><td><code>HealthEventPage</code></td><td>Widget</td><td>Flutter / Dart<br><strong>Diseño objetivo</strong></td><td>Presentar registro y seguimiento de eventos sanitarios, diagnósticos y tratamientos en Flutter.</td><td><code>state</code><br><code>onAction</code><br><code>router</code></td><td><code>build(context)</code><br><code>submit()</code><br><code>retry()</code></td><td>Observa HealthEventController y emite intenciones del usuario.</td></tr>
    <tr><td><code>HealthEventController</code></td><td>State Controller</td><td>Flutter / Dart<br><strong>Diseño objetivo</strong></td><td>Mantener el estado de presentación de Flutter y coordinar casos de uso.</td><td><code>state</code><br><code>observeUseCase</code><br><code>syncUseCase</code></td><td><code>load()</code><br><code>submit(action)</code><br><code>retrySync()</code></td><td>Invoca Application Layer y publica estados de carga, éxito y error.</td></tr>
  </tbody>
</table>

<a id="toc-2-6-4-3-application-layer"></a>

## 2.6.4.3. Application Layer

Esta capa coordina las capacidades de **registro y seguimiento de eventos sanitarios, diagnósticos y tratamientos**. Los commands y queries expresan intenciones; los handlers cargan aggregates, aplican reglas, persisten cambios y reaccionan a eventos. Los casos de uso móviles coordinan lectura local, actualización remota y sincronización idempotente.

<table>
  <thead>
    <tr><th>Clase</th><th>Categoría</th><th>Producto y estado</th><th>Propósito</th><th>Atributos</th><th>Métodos u operaciones</th><th>Relaciones</th></tr>
  </thead>
  <tbody>
    <tr><td><code>HealthEventCommandService</code></td><td>Application Service</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Orquestar registro y seguimiento de eventos sanitarios, diagnósticos y tratamientos sin contener reglas del dominio.</td><td><code>IHealthEventRepository repository</code><br><code>IUnitOfWork unitOfWork</code></td><td><code>Handle(CreateHealthEventCommand command, CancellationToken cancellationToken)</code><br><code>Handle(UpdateHealthEventCommand command, CancellationToken cancellationToken)</code><br><code>Handle(DeleteHealthEventCommand command, CancellationToken cancellationToken)</code></td><td>Invoca agregados y repositories; confirma la transacción mediante Unit of Work.</td></tr>
    <tr><td><code>HealthEventQueryService</code></td><td>Application Service</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Orquestar registro y seguimiento de eventos sanitarios, diagnósticos y tratamientos sin contener reglas del dominio.</td><td><code>IHealthEventRepository repository</code></td><td><code>Handle(GetHealthEventByIdQuery query, CancellationToken cancellationToken)</code><br><code>Handle(GetAllHealthEventsQuery query, CancellationToken cancellationToken)</code></td><td>Invoca agregados y repositories; confirma la transacción mediante Unit of Work.</td></tr>
    <tr><td><code>CreateHealthEventCommand</code></td><td>Command/Query</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Transportar una intención o consulta tipada hacia su handler.</td><td><code>int AnimalId</code><br><code>string Type</code><br><code>DateOnly Date</code><br><code>string Description</code><br><code>string Veterinarian</code><br><code>string Diagnosis</code><br><code>string Treatment</code><br><code>string Prescription</code><br><code>string FollowUp</code><br><code>DateOnly? NextDueDate</code></td><td>—</td><td>Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio.</td></tr>
    <tr><td><code>UpdateHealthEventCommand</code></td><td>Command/Query</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Transportar una intención o consulta tipada hacia su handler.</td><td><code>int Id</code><br><code>int AnimalId</code><br><code>string Type</code><br><code>DateOnly Date</code><br><code>string Description</code><br><code>string Veterinarian</code><br><code>string Diagnosis</code><br><code>string Treatment</code><br><code>string Prescription</code><br><code>string FollowUp</code><br><code>DateOnly? NextDueDate</code></td><td>—</td><td>Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio.</td></tr>
    <tr><td><code>DeleteHealthEventCommand</code></td><td>Command/Query</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Transportar una intención o consulta tipada hacia su handler.</td><td><code>int Id</code></td><td>—</td><td>Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio.</td></tr>
    <tr><td><code>GetHealthEventByIdQuery</code></td><td>Command/Query</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Transportar una intención o consulta tipada hacia su handler.</td><td><code>int Id</code></td><td>—</td><td>Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio.</td></tr>
    <tr><td><code>ObserveHealthEventUseCase</code></td><td>Use Case</td><td>Android y Flutter<br><strong>Diseño objetivo</strong></td><td>Entregar primero datos locales y actualizar la consulta cuando exista conectividad.</td><td><code>localRepository</code><br><code>remoteRepository</code><br><code>connectivityMonitor</code></td><td><code>Execute(criteria): Stream&lt;Result&gt;</code></td><td>Es invocado por ViewModel/Controller y coordina repositorios móviles.</td></tr>
    <tr><td><code>SyncHealthEventUseCase</code></td><td>Use Case</td><td>Android y Flutter<br><strong>Diseño objetivo</strong></td><td>Procesar operaciones móviles pendientes de manera idempotente.</td><td><code>outboxRepository</code><br><code>remoteRepository</code><br><code>conflictResolver</code></td><td><code>Execute(): SyncResult</code></td><td>Lee el outbox local, consume la API y actualiza el estado de sincronización.</td></tr>
    <tr><td><code>CreateHealthEventCommandHandler</code></td><td>Command Handler</td><td>Backend ASP.NET Core<br><strong>Diseño objetivo</strong></td><td>Ejecutar una intención concreta, aplicar reglas del agregado y confirmar la transacción.</td><td><code>repository</code><br><code>unitOfWork</code><br><code>domainPolicy</code></td><td><code>Handle(command): Result</code></td><td>Consume un Command, carga el aggregate mediante su repository y puede publicar un Domain Event.</td></tr>
    <tr><td><code>UpdateHealthEventCommandHandler</code></td><td>Command Handler</td><td>Backend ASP.NET Core<br><strong>Diseño objetivo</strong></td><td>Ejecutar una intención concreta, aplicar reglas del agregado y confirmar la transacción.</td><td><code>repository</code><br><code>unitOfWork</code><br><code>domainPolicy</code></td><td><code>Handle(command): Result</code></td><td>Consume un Command, carga el aggregate mediante su repository y puede publicar un Domain Event.</td></tr>
    <tr><td><code>HealthEventRegisteredEventHandler</code></td><td>Event Handler</td><td>Backend ASP.NET Core<br><strong>Diseño objetivo</strong></td><td>Reaccionar al evento confirmado y actualizar proyecciones o integraciones.</td><td><code>projectionRepository</code><br><code>notificationPort</code><br><code>unitOfWork</code></td><td><code>Handle(domainEvent): Task</code></td><td>Consume un Domain Event y utiliza puertos de infraestructura sin modificar directamente el agregado.</td></tr>
  </tbody>
</table>

<a id="toc-2-6-4-4-infrastructure-layer"></a>

## 2.6.4.4. Infrastructure Layer

Esta capa implementa los puertos definidos hacia el interior de **Sanitary Management** y concentra acceso a base de datos, red, almacenamiento local e integraciones externas. Las clases de infraestructura traducen errores y contratos técnicos antes de devolver resultados a Application Layer.

<table>
  <thead>
    <tr><th>Clase</th><th>Categoría</th><th>Producto y estado</th><th>Propósito</th><th>Atributos</th><th>Métodos u operaciones</th><th>Relaciones</th></tr>
  </thead>
  <tbody>
    <tr><td><code>HealthEventRepository</code></td><td>Repository Adapter</td><td>Backend / Entity Framework Core<br><strong>Implementado en el backend</strong></td><td>Implementar el puerto de persistencia definido por Domain Layer.</td><td><code>AppDbContext context</code></td><td><code>FindById(id)</code><br><code>Add(entity)</code><br><code>Update(entity)</code><br><code>Delete(entity)</code></td><td>Implementa IHealthEventRepository; utiliza AppDbContext/MySQL y reconstruye el aggregate.</td></tr>
    <tr><td><code>ModelBuilderExtensions</code></td><td>Persistence Configuration</td><td>Backend / Entity Framework Core<br><strong>Implementado en el backend</strong></td><td>Mapear entidades y value objects del contexto al modelo relacional.</td><td><code>EntityTypeBuilder configuration</code></td><td><code>ApplyConfiguration(modelBuilder)</code></td><td>Configura tablas, claves, relaciones, restricciones y conversiones de Entity Framework Core.</td></tr>
    <tr><td><code>HealthEventApiDataSource</code></td><td>Remote Adapter</td><td>Android / Kotlin<br><strong>Diseño objetivo</strong></td><td>Implementar el acceso remoto del cliente móvil a la API.</td><td><code>httpClient</code><br><code>tokenProvider</code><br><code>serializer</code></td><td><code>Get(criteria)</code><br><code>Create(dto)</code><br><code>Update(dto)</code><br><code>Delete(id)</code></td><td>Consume controllers REST por HTTPS/JSON y traduce errores HTTP al modelo de aplicación.</td></tr>
    <tr><td><code>HealthEventDao</code></td><td>Room Adapter</td><td>Android / Room<br><strong>Diseño objetivo</strong></td><td>Implementar persistencia local y observación reactiva en Android.</td><td><code>roomDatabase</code><br><code>entityMapper</code></td><td><code>Observe(criteria)</code><br><code>Upsert(entity)</code><br><code>Delete(id)</code><br><code>Pending()</code></td><td>Implementa el puerto local mediante Room y participa en la estrategia de caché/outbox.</td></tr>
    <tr><td><code>HealthEventRemoteDataSource</code></td><td>Remote Adapter</td><td>Flutter / Dart<br><strong>Diseño objetivo</strong></td><td>Implementar el acceso remoto del cliente móvil a la API.</td><td><code>httpClient</code><br><code>tokenProvider</code><br><code>serializer</code></td><td><code>Get(criteria)</code><br><code>Create(dto)</code><br><code>Update(dto)</code><br><code>Delete(id)</code></td><td>Consume controllers REST por HTTPS/JSON y traduce errores HTTP al modelo de aplicación.</td></tr>
    <tr><td><code>HealthEventLocalDataSource</code></td><td>SQLite Adapter</td><td>Flutter / Dart<br><strong>Diseño objetivo</strong></td><td>Implementar persistencia local equivalente en Flutter.</td><td><code>sqliteDatabase</code><br><code>entityMapper</code></td><td><code>watch(criteria)</code><br><code>upsert(entity)</code><br><code>delete(id)</code><br><code>pending()</code></td><td>Implementa el puerto local mediante SQLite y participa en la estrategia de caché/outbox.</td></tr>
    <tr><td><code>LivestockAnimalAdapter</code></td><td>Context Adapter</td><td>Backend ASP.NET Core<br><strong>Diseño objetivo</strong></td><td>Aislar una dependencia externa detrás de un puerto explícito.</td><td><code>livestockFacade</code></td><td><code>GetAnimal(animalId)</code><br><code>Exists(animalId): bool</code></td><td>Implementa el puerto de consulta de animales y consume Livestock Management.</td></tr>
    <tr><td><code>VeterinaryAuthorizationAdapter</code></td><td>Context Adapter</td><td>Backend ASP.NET Core<br><strong>Diseño objetivo</strong></td><td>Aislar una dependencia externa detrás de un puerto explícito.</td><td><code>collaborationFacade</code></td><td><code>CanWrite(veterinarianId, animalId): bool</code></td><td>Implementa el puerto de autorización y consume Veterinary Collaboration.</td></tr>
    <tr><td><code>SanitaryOutboxStore</code></td><td>Offline Adapter</td><td>Android y Flutter<br><strong>Diseño objetivo</strong></td><td>Aislar una dependencia externa detrás de un puerto explícito.</td><td><code>database, serializer</code></td><td><code>Enqueue(event)</code><br><code>Pending()</code><br><code>MarkSynced(id)</code></td><td>Implementa el puerto de sincronización sanitaria sobre Room o SQLite.</td></tr>
  </tbody>
</table>

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


