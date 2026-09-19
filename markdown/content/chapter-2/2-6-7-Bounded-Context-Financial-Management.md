<a id="toc-2-6-7-bounded-context-financial-management"></a>

# 2.6.7. Bounded Context: Financial Management

Registrar ingresos y egresos operativos y producir resúmenes económicos básicos para apoyar decisiones del ganadero.

La base implementada se encuentra en el módulo `Financial` de la API ASP.NET Core. El diseño móvil de Android y Flutter se presenta como **diseño objetivo** porque esos clientes todavía no existen en el workspace. Los tres productos comparten contratos REST y lenguaje ubicuo, mientras la API conserva las reglas autoritativas.

<a id="toc-2-6-7-1-domain-layer"></a>

## 2.6.7.1. Domain Layer

**Responsabilidad estable.** Esta capa documenta el modelo que representa el núcleo de **Financial Management**. Las reglas autoritativas se ejecutan en la API; Android y Flutter mantienen modelos equivalentes para presentación, validación inmediata y trabajo offline. La columna de estado distingue el código heredado de la arquitectura objetivo.

**Detalle técnico evolutivo.** El siguiente diccionario identifica las clases, sus responsabilidades, atributos, métodos y relaciones. La columna **Producto y estado** distingue los elementos comprobados en el código de aquellos que aún pertenecen al diseño objetivo.

<table>
  <thead>
    <tr><th>Clase</th><th>Categoría</th><th>Producto y estado</th><th>Propósito</th><th>Atributos</th><th>Métodos u operaciones</th><th>Relaciones</th></tr>
  </thead>
  <tbody>
    <tr><td><code>FinancialRecord</code></td><td>Aggregate Root</td><td>Backend; modelo equivalente en Android y Flutter<br><strong>Implementado en el backend</strong></td><td>Mantener un ingreso o egreso del ganadero.</td><td><code>id: int</code><br><code>ownerId: int</code><br><code>type: FinancialRecordType</code><br><code>category: FinancialCategory</code><br><code>amount: Money</code><br><code>date: Date</code><br><code>description: string</code></td><td><code>ChangeAmount(amount: Money): void</code><br><code>ChangeCategory(category: FinancialCategory): void</code></td><td>FinancialRecord compone Money; FinancialRecord se relaciona con FinancialRecordType; FinancialRecord compone FinancialCategory; FinancialSummary depende de FinancialRecord; IFinancialRecordRepository depende de FinancialRecord</td></tr>
    <tr><td><code>Money</code></td><td>Value Object</td><td>Backend, Android y Flutter (modelo canónico)<br><strong>Diseño objetivo</strong></td><td>Representar un importe junto con su moneda.</td><td><code>amount: decimal</code><br><code>currency: string</code></td><td><code>Add(other: Money): Money</code><br><code>IsPositive(): bool</code></td><td>FinancialRecord compone Money</td></tr>
    <tr><td><code>FinancialRecordType</code></td><td>Enumeration</td><td>Backend, Android y Flutter (modelo canónico)<br><strong>Diseño objetivo</strong></td><td>Definir los valores válidos de FinancialRecordType.</td><td><code>Income</code><br><code>Expense</code></td><td>—</td><td>FinancialRecord se relaciona con FinancialRecordType</td></tr>
    <tr><td><code>FinancialCategory</code></td><td>Value Object</td><td>Backend, Android y Flutter (modelo canónico)<br><strong>Diseño objetivo</strong></td><td>Clasificar un movimiento financiero.</td><td><code>name: string</code></td><td><code>IsValid(): bool</code></td><td>FinancialRecord compone FinancialCategory</td></tr>
    <tr><td><code>FinancialSummary</code></td><td>Domain Service</td><td>Backend, Android y Flutter (modelo canónico)<br><strong>Diseño objetivo</strong></td><td>Calcular totales y balance para un conjunto de movimientos.</td><td>—</td><td><code>Calculate(records: List~FinancialRecord~): Money</code></td><td>FinancialSummary depende de FinancialRecord</td></tr>
    <tr><td><code>IFinancialRecordRepository</code></td><td>Repository Interface</td><td>Backend; modelo equivalente en Android y Flutter<br><strong>Implementado en el backend</strong></td><td>Abstraer la persistencia de FinancialRecord.</td><td>—</td><td><code>FindById(id: int): FinancialRecord?</code><br><code>FindByOwner(ownerId: int): List~FinancialRecord~</code><br><code>Add(record: FinancialRecord): void</code><br><code>Update(record: FinancialRecord): void</code></td><td>IFinancialRecordRepository depende de FinancialRecord</td></tr>
  </tbody>
</table>

<a id="toc-2-6-7-2-interface-layer"></a>

## 2.6.7.2. Interface Layer

**Responsabilidad estable.** Esta capa recibe las acciones relacionadas con **registro de ingresos y egresos, actualización y cálculo de resúmenes** y las traduce a casos de uso. Los controllers y resources corresponden a la API; las pantallas y controladores de estado representan la presentación objetivo en Android y Flutter. Ninguna de estas clases implementa reglas de negocio.

**Detalle técnico evolutivo.** El siguiente diccionario identifica las clases, sus responsabilidades, atributos, métodos y relaciones. La columna **Producto y estado** distingue los elementos comprobados en el código de aquellos que aún pertenecen al diseño objetivo.

<table>
  <thead>
    <tr><th>Clase</th><th>Categoría</th><th>Producto y estado</th><th>Propósito</th><th>Atributos</th><th>Métodos u operaciones</th><th>Relaciones</th></tr>
  </thead>
  <tbody>
    <tr><td><code>FinancialRecordsController</code></td><td>REST Controller</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Publicar por HTTP las capacidades de Financial Management.</td><td><code>IFinancialRecordCommandService commandService</code><br><code>IFinancialRecordQueryService queryService</code></td><td><code>GetAll(CancellationToken cancellationToken)</code><br><code>GetById(int id, CancellationToken cancellationToken)</code><br><code>Create(CreateFinancialRecordResource resource, CancellationToken cancellationToken)</code><br><code>Update(int id, CreateFinancialRecordResource resource, CancellationToken cancellationToken)</code><br><code>Delete(int id, CancellationToken cancellationToken)</code></td><td>Recibe resources, invoca servicios de aplicación y devuelve resources HTTP.</td></tr>
    <tr><td><code>CreateFinancialRecordResource</code></td><td>Resource/Assembler</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Definir un contrato estable de entrada o salida para la API REST.</td><td><code>int OwnerId</code><br><code>string Type</code><br><code>string Category</code><br><code>decimal Amount</code><br><code>DateOnly Date</code><br><code>string Description</code></td><td><code>Create(...)</code><br><code>Deconstruct(...)</code></td><td>Es construido o traducido por assemblers y consumido por el controller y los clientes móviles.</td></tr>
    <tr><td><code>FinancialRecordResource</code></td><td>Resource/Assembler</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Definir un contrato estable de entrada o salida para la API REST.</td><td><code>int Id</code><br><code>int OwnerId</code><br><code>string Type</code><br><code>string Category</code><br><code>decimal Amount</code><br><code>DateOnly Date</code><br><code>string Description</code></td><td><code>Create(...)</code><br><code>Deconstruct(...)</code></td><td>Es construido o traducido por assemblers y consumido por el controller y los clientes móviles.</td></tr>
    <tr><td><code>FinancialRecordScreen</code></td><td>Composable</td><td>Android / Jetpack Compose<br><strong>Diseño objetivo</strong></td><td>Presentar registro de ingresos y egresos, actualización y cálculo de resúmenes en Android.</td><td><code>uiState</code><br><code>onAction</code><br><code>navigation</code></td><td><code>Render()</code><br><code>Submit()</code><br><code>Retry()</code></td><td>Observa FinancialRecordViewModel y emite acciones de interfaz.</td></tr>
    <tr><td><code>FinancialRecordViewModel</code></td><td>Presentation Model</td><td>Android / Kotlin<br><strong>Diseño objetivo</strong></td><td>Mantener el estado observable y traducir acciones de Android a casos de uso.</td><td><code>state</code><br><code>observeUseCase</code><br><code>syncUseCase</code></td><td><code>Load()</code><br><code>Submit(action)</code><br><code>RetrySync()</code></td><td>Invoca casos de uso de Application Layer y publica un UI State inmutable.</td></tr>
    <tr><td><code>FinancialRecordPage</code></td><td>Widget</td><td>Flutter / Dart<br><strong>Diseño objetivo</strong></td><td>Presentar registro de ingresos y egresos, actualización y cálculo de resúmenes en Flutter.</td><td><code>state</code><br><code>onAction</code><br><code>router</code></td><td><code>build(context)</code><br><code>submit()</code><br><code>retry()</code></td><td>Observa FinancialRecordController y emite intenciones del usuario.</td></tr>
    <tr><td><code>FinancialRecordController</code></td><td>State Controller</td><td>Flutter / Dart<br><strong>Diseño objetivo</strong></td><td>Mantener el estado de presentación de Flutter y coordinar casos de uso.</td><td><code>state</code><br><code>observeUseCase</code><br><code>syncUseCase</code></td><td><code>load()</code><br><code>submit(action)</code><br><code>retrySync()</code></td><td>Invoca Application Layer y publica estados de carga, éxito y error.</td></tr>
  </tbody>
</table>

<a id="toc-2-6-7-3-application-layer"></a>

## 2.6.7.3. Application Layer

**Responsabilidad estable.** Esta capa coordina las capacidades de **registro de ingresos y egresos, actualización y cálculo de resúmenes**. Los commands y queries expresan intenciones; los handlers cargan aggregates, aplican reglas, persisten cambios y reaccionan a eventos. Los casos de uso móviles coordinan lectura local, actualización remota y sincronización idempotente.

**Detalle técnico evolutivo.** El siguiente diccionario identifica las clases, sus responsabilidades, atributos, métodos y relaciones. La columna **Producto y estado** distingue los elementos comprobados en el código de aquellos que aún pertenecen al diseño objetivo.

<table>
  <thead>
    <tr><th>Clase</th><th>Categoría</th><th>Producto y estado</th><th>Propósito</th><th>Atributos</th><th>Métodos u operaciones</th><th>Relaciones</th></tr>
  </thead>
  <tbody>
    <tr><td><code>FinancialRecordCommandService</code></td><td>Application Service</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Orquestar registro de ingresos y egresos, actualización y cálculo de resúmenes sin contener reglas del dominio.</td><td><code>IFinancialRecordRepository repository</code><br><code>IUnitOfWork unitOfWork</code></td><td><code>Handle(CreateFinancialRecordCommand command, CancellationToken cancellationToken)</code><br><code>Handle(UpdateFinancialRecordCommand command, CancellationToken cancellationToken)</code><br><code>Handle(DeleteFinancialRecordCommand command, CancellationToken cancellationToken)</code></td><td>Invoca agregados y repositories; confirma la transacción mediante Unit of Work.</td></tr>
    <tr><td><code>FinancialRecordQueryService</code></td><td>Application Service</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Orquestar registro de ingresos y egresos, actualización y cálculo de resúmenes sin contener reglas del dominio.</td><td><code>IFinancialRecordRepository repository</code></td><td><code>Handle(GetFinancialRecordByIdQuery query, CancellationToken cancellationToken)</code><br><code>Handle(GetAllFinancialRecordsQuery query, CancellationToken cancellationToken)</code></td><td>Invoca agregados y repositories; confirma la transacción mediante Unit of Work.</td></tr>
    <tr><td><code>CreateFinancialRecordCommand</code></td><td>Command/Query</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Transportar una intención o consulta tipada hacia su handler.</td><td><code>int OwnerId</code><br><code>string Type</code><br><code>string Category</code><br><code>decimal Amount</code><br><code>DateOnly Date</code><br><code>string Description</code></td><td>—</td><td>Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio.</td></tr>
    <tr><td><code>UpdateFinancialRecordCommand</code></td><td>Command/Query</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Transportar una intención o consulta tipada hacia su handler.</td><td><code>int Id</code><br><code>int OwnerId</code><br><code>string Type</code><br><code>string Category</code><br><code>decimal Amount</code><br><code>DateOnly Date</code><br><code>string Description</code></td><td>—</td><td>Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio.</td></tr>
    <tr><td><code>DeleteFinancialRecordCommand</code></td><td>Command/Query</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Transportar una intención o consulta tipada hacia su handler.</td><td><code>int Id</code></td><td>—</td><td>Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio.</td></tr>
    <tr><td><code>GetFinancialRecordByIdQuery</code></td><td>Command/Query</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Transportar una intención o consulta tipada hacia su handler.</td><td><code>int Id</code></td><td>—</td><td>Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio.</td></tr>
    <tr><td><code>ObserveFinancialRecordUseCase</code></td><td>Use Case</td><td>Android y Flutter<br><strong>Diseño objetivo</strong></td><td>Entregar primero datos locales y actualizar la consulta cuando exista conectividad.</td><td><code>localRepository</code><br><code>remoteRepository</code><br><code>connectivityMonitor</code></td><td><code>Execute(criteria): Stream&lt;Result&gt;</code></td><td>Es invocado por ViewModel/Controller y coordina repositorios móviles.</td></tr>
    <tr><td><code>SyncFinancialRecordUseCase</code></td><td>Use Case</td><td>Android y Flutter<br><strong>Diseño objetivo</strong></td><td>Procesar operaciones móviles pendientes de manera idempotente.</td><td><code>outboxRepository</code><br><code>remoteRepository</code><br><code>conflictResolver</code></td><td><code>Execute(): SyncResult</code></td><td>Lee el outbox local, consume la API y actualiza el estado de sincronización.</td></tr>
    <tr><td><code>CreateFinancialRecordCommandHandler</code></td><td>Command Handler</td><td>Backend ASP.NET Core<br><strong>Diseño objetivo</strong></td><td>Ejecutar una intención concreta, aplicar reglas del agregado y confirmar la transacción.</td><td><code>repository</code><br><code>unitOfWork</code><br><code>domainPolicy</code></td><td><code>Handle(command): Result</code></td><td>Consume un Command, carga el aggregate mediante su repository y puede publicar un Domain Event.</td></tr>
    <tr><td><code>UpdateFinancialRecordCommandHandler</code></td><td>Command Handler</td><td>Backend ASP.NET Core<br><strong>Diseño objetivo</strong></td><td>Ejecutar una intención concreta, aplicar reglas del agregado y confirmar la transacción.</td><td><code>repository</code><br><code>unitOfWork</code><br><code>domainPolicy</code></td><td><code>Handle(command): Result</code></td><td>Consume un Command, carga el aggregate mediante su repository y puede publicar un Domain Event.</td></tr>
    <tr><td><code>FinancialRecordRegisteredEventHandler</code></td><td>Event Handler</td><td>Backend ASP.NET Core<br><strong>Diseño objetivo</strong></td><td>Reaccionar al evento confirmado y actualizar proyecciones o integraciones.</td><td><code>projectionRepository</code><br><code>notificationPort</code><br><code>unitOfWork</code></td><td><code>Handle(domainEvent): Task</code></td><td>Consume un Domain Event y utiliza puertos de infraestructura sin modificar directamente el agregado.</td></tr>
  </tbody>
</table>

<a id="toc-2-6-7-4-infrastructure-layer"></a>

## 2.6.7.4. Infrastructure Layer

**Responsabilidad estable.** Esta capa implementa los puertos definidos hacia el interior de **Financial Management** y concentra acceso a base de datos, red, almacenamiento local e integraciones externas. Las clases de infraestructura traducen errores y contratos técnicos antes de devolver resultados a Application Layer.

**Detalle técnico evolutivo.** El siguiente diccionario identifica las clases, sus responsabilidades, atributos, métodos y relaciones. La columna **Producto y estado** distingue los elementos comprobados en el código de aquellos que aún pertenecen al diseño objetivo.

<table>
  <thead>
    <tr><th>Clase</th><th>Categoría</th><th>Producto y estado</th><th>Propósito</th><th>Atributos</th><th>Métodos u operaciones</th><th>Relaciones</th></tr>
  </thead>
  <tbody>
    <tr><td><code>FinancialRecordRepository</code></td><td>Repository Adapter</td><td>Backend / Entity Framework Core<br><strong>Implementado en el backend</strong></td><td>Implementar el puerto de persistencia definido por Domain Layer.</td><td><code>AppDbContext context</code></td><td><code>FindById(id)</code><br><code>Add(entity)</code><br><code>Update(entity)</code><br><code>Delete(entity)</code></td><td>Implementa IFinancialRecordRepository; utiliza AppDbContext/MySQL y reconstruye el aggregate.</td></tr>
    <tr><td><code>ModelBuilderExtensions</code></td><td>Persistence Configuration</td><td>Backend / Entity Framework Core<br><strong>Implementado en el backend</strong></td><td>Mapear entidades y value objects del contexto al modelo relacional.</td><td><code>EntityTypeBuilder configuration</code></td><td><code>ApplyConfiguration(modelBuilder)</code></td><td>Configura tablas, claves, relaciones, restricciones y conversiones de Entity Framework Core.</td></tr>
    <tr><td><code>FinancialRecordApiDataSource</code></td><td>Remote Adapter</td><td>Android / Kotlin<br><strong>Diseño objetivo</strong></td><td>Implementar el acceso remoto del cliente móvil a la API.</td><td><code>httpClient</code><br><code>tokenProvider</code><br><code>serializer</code></td><td><code>Get(criteria)</code><br><code>Create(dto)</code><br><code>Update(dto)</code><br><code>Delete(id)</code></td><td>Consume controllers REST por HTTPS/JSON y traduce errores HTTP al modelo de aplicación.</td></tr>
    <tr><td><code>FinancialRecordDao</code></td><td>Room Adapter</td><td>Android / Room<br><strong>Diseño objetivo</strong></td><td>Implementar persistencia local y observación reactiva en Android.</td><td><code>roomDatabase</code><br><code>entityMapper</code></td><td><code>Observe(criteria)</code><br><code>Upsert(entity)</code><br><code>Delete(id)</code><br><code>Pending()</code></td><td>Implementa el puerto local mediante Room y participa en la estrategia de caché/outbox.</td></tr>
    <tr><td><code>FinancialRecordRemoteDataSource</code></td><td>Remote Adapter</td><td>Flutter / Dart<br><strong>Diseño objetivo</strong></td><td>Implementar el acceso remoto del cliente móvil a la API.</td><td><code>httpClient</code><br><code>tokenProvider</code><br><code>serializer</code></td><td><code>Get(criteria)</code><br><code>Create(dto)</code><br><code>Update(dto)</code><br><code>Delete(id)</code></td><td>Consume controllers REST por HTTPS/JSON y traduce errores HTTP al modelo de aplicación.</td></tr>
    <tr><td><code>FinancialRecordLocalDataSource</code></td><td>SQLite Adapter</td><td>Flutter / Dart<br><strong>Diseño objetivo</strong></td><td>Implementar persistencia local equivalente en Flutter.</td><td><code>sqliteDatabase</code><br><code>entityMapper</code></td><td><code>watch(criteria)</code><br><code>upsert(entity)</code><br><code>delete(id)</code><br><code>pending()</code></td><td>Implementa el puerto local mediante SQLite y participa en la estrategia de caché/outbox.</td></tr>
    <tr><td><code>ProfilesFinancialOwnerAdapter</code></td><td>Context Adapter</td><td>Backend ASP.NET Core<br><strong>Diseño objetivo</strong></td><td>Aislar una dependencia externa detrás de un puerto explícito.</td><td><code>profilesFacade</code></td><td><code>ValidateOwner(ownerId): bool</code></td><td>Implementa el puerto de propietarios y consume Profile Management.</td></tr>
    <tr><td><code>FinancialOutboxStore</code></td><td>Offline Adapter</td><td>Android y Flutter<br><strong>Diseño objetivo</strong></td><td>Aislar una dependencia externa detrás de un puerto explícito.</td><td><code>database, serializer</code></td><td><code>Enqueue(record)</code><br><code>Pending()</code><br><code>MarkSynced(id)</code></td><td>Implementa el puerto de sincronización financiera sobre Room o SQLite.</td></tr>
  </tbody>
</table>

<a id="toc-2-6-7-5-bounded-context-software-architecture-component-level-diagrams"></a>

## 2.6.7.5. Bounded Context Software Architecture Component Level Diagrams

El archivo [`component-level.dsl`](<../../assets/codefordiagrams/2.6.7. Bounded Context Financial Management/component-level.dsl>) contiene las vistas `BC7-ApiComponents`, `BC7-AndroidComponents` y `BC7-FlutterComponents`. Las tres parten del mismo modelo C4 y muestran la separación entre presentación, aplicación, dominio y adaptadores.

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-7-Bounded-Context-Financial-Management/2-6-7-BC7-ApiComponents.svg" alt="Componentes API de Financial Management" width="900">
  <p><i>Figura 2.6.7.1. Componentes de la API para Financial Management. Fuente: elaboración propia con Structurizr DSL.</i></p>
</div>

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-7-Bounded-Context-Financial-Management/2-6-7-BC7-AndroidComponents.svg" alt="Componentes Android de Financial Management" width="900">
  <p><i>Figura 2.6.7.2. Componentes Android para Financial Management. Fuente: elaboración propia con Structurizr DSL.</i></p>
</div>

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-7-Bounded-Context-Financial-Management/2-6-7-BC7-FlutterComponents.svg" alt="Componentes Flutter de Financial Management" width="900">
  <p><i>Figura 2.6.7.3. Componentes Flutter para Financial Management. Fuente: elaboración propia con Structurizr DSL.</i></p>
</div>

<a id="toc-2-6-7-6-bounded-context-software-architecture-code-level-diagrams"></a>

## 2.6.7.6. Bounded Context Software Architecture Code Level Diagrams

Los diagramas de código detallan el modelo del dominio y los objetos de persistencia. El UML diferencia los elementos existentes de las incorporaciones objetivo, mientras los esquemas SQL señalan mediante comentarios las columnas propuestas. Los archivos ERD quedan disponibles para completar la importación manual.

<a id="toc-2-6-7-6-1-bounded-context-domain-layer-class-diagrams"></a>

### 2.6.7.6.1. Bounded Context Domain Layer Class Diagrams

El Class Diagram incluye agregados, entidades, value objects, enumeraciones, servicios de dominio e interfaces de repositorio con atributos, operaciones, visibilidad y multiplicidades.

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-7-Bounded-Context-Financial-Management/2-6-7-domain-layer-class-diagram.svg" alt="Class Diagram de Financial Management" width="900">
  <p><i>Figura 2.6.7.4. Domain Layer Class Diagram de Financial Management. Fuente: elaboración propia con PlantUML.</i></p>
</div>

<a id="toc-2-6-7-6-2-bounded-context-database-design-diagram"></a>

### 2.6.7.6.2. Bounded Context Database Design Diagram

MySQL mantiene la persistencia autoritativa. Room y SQLite contienen únicamente caché, metadatos de sincronización y operaciones pendientes; no sustituyen las reglas ni la fuente de verdad del backend. En IAM, las credenciales y tokens permanecen fuera de las tablas locales y se almacenan mediante mecanismos seguros del sistema operativo.

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-7-Bounded-Context-Financial-Management/2-6-7-mysql-database-design.png" alt="MySQL Database Diagram de Financial Management" width="900">
  <p><i>Figura 2.6.7.5. MySQL Database Design de Financial Management. Fuente: elaboración propia a partir del esquema SQL.</i></p>
</div>

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-7-Bounded-Context-Financial-Management/2-6-7-android-room-database-design.png" alt="Room Database Diagram de Financial Management" width="900">
  <p><i>Figura 2.6.7.6. Android Room Database Design de Financial Management. Fuente: elaboración propia a partir del esquema SQL.</i></p>
</div>


