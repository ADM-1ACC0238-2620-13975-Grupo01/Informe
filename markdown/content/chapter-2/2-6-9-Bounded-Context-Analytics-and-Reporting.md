<a id="toc-2-6-9-bounded-context-analytics-and-reporting"></a>

# 2.6.9. Bounded Context: Analytics and Reporting

Construir proyecciones y métricas de consulta para los dashboards sin adquirir propiedad sobre los registros de los contextos fuente.

La base implementada se encuentra en el módulo `Analytics` de la API ASP.NET Core. El diseño móvil de Android y Flutter se presenta como **diseño objetivo** porque esos clientes todavía no existen en el workspace. Los tres productos comparten contratos REST y lenguaje ubicuo, mientras la API conserva las reglas autoritativas.

<a id="toc-2-6-9-1-domain-layer"></a>

## 2.6.9.1. Domain Layer

**Responsabilidad estable.** Esta capa documenta el modelo que representa el núcleo de **Analytics and Reporting**. Las reglas autoritativas se ejecutan en la API; Android y Flutter mantienen modelos equivalentes para presentación, validación inmediata y trabajo offline. La columna de estado distingue el código heredado de la arquitectura objetivo.

**Detalle técnico evolutivo.** El siguiente diccionario identifica las clases, sus responsabilidades, atributos, métodos y relaciones. La columna **Producto y estado** distingue los elementos comprobados en el código de aquellos que aún pertenecen al diseño objetivo.

<table>
  <thead>
    <tr><th>Clase</th><th>Categoría</th><th>Producto y estado</th><th>Propósito</th><th>Atributos</th><th>Métodos u operaciones</th><th>Relaciones</th></tr>
  </thead>
  <tbody>
    <tr><td><code>DashboardProjection</code></td><td>Aggregate Root</td><td>Backend, Android y Flutter (modelo canónico)<br><strong>Diseño objetivo</strong></td><td>Agrupar métricas calculadas para una audiencia y periodo.</td><td><code>id: int</code><br><code>ownerId: int</code><br><code>audience: string</code><br><code>period: MetricPeriod</code><br><code>generatedAt: DateTime</code><br><code>metrics: List~ReportMetric~</code></td><td><code>ReplaceMetrics(metrics: List~ReportMetric~): void</code><br><code>IsStale(now: DateTime): bool</code></td><td>DashboardProjection compone ReportMetric; DashboardProjection compone MetricPeriod; ProjectionBuilder depende de DashboardProjection; IReportMetricRepository depende de DashboardProjection</td></tr>
    <tr><td><code>ReportMetric</code></td><td>Entity</td><td>Backend; modelo equivalente en Android y Flutter<br><strong>Implementado en el backend</strong></td><td>Representar una métrica individual del dashboard.</td><td><code>id: int</code><br><code>label: string</code><br><code>slice: MetricSlice</code><br><code>trend: string</code><br><code>sourceContext: string</code></td><td><code>Update(slice: MetricSlice, trend: string): void</code></td><td>DashboardProjection compone ReportMetric; ReportMetric compone MetricSlice</td></tr>
    <tr><td><code>MetricSlice</code></td><td>Value Object</td><td>Backend, Android y Flutter (modelo canónico)<br><strong>Diseño objetivo</strong></td><td>Representar un valor, unidad y etiqueta de una métrica.</td><td><code>label: string</code><br><code>value: decimal</code><br><code>unit: string</code></td><td><code>IsComparableTo(other: MetricSlice): bool</code></td><td>ReportMetric compone MetricSlice</td></tr>
    <tr><td><code>MetricPeriod</code></td><td>Value Object</td><td>Backend, Android y Flutter (modelo canónico)<br><strong>Diseño objetivo</strong></td><td>Representar el intervalo consultado.</td><td><code>from: Date</code><br><code>to: Date</code></td><td><code>Contains(date: Date): bool</code></td><td>DashboardProjection compone MetricPeriod</td></tr>
    <tr><td><code>ProjectionBuilder</code></td><td>Domain Service</td><td>Backend, Android y Flutter (modelo canónico)<br><strong>Diseño objetivo</strong></td><td>Construir proyecciones a partir de los contextos fuente.</td><td>—</td><td><code>BuildRancher(ownerId: int, period: MetricPeriod): DashboardProjection</code><br><code>BuildVeterinarian(id: int, period: MetricPeriod): DashboardProjection</code></td><td>ProjectionBuilder depende de DashboardProjection</td></tr>
    <tr><td><code>IReportMetricRepository</code></td><td>Repository Interface</td><td>Backend; modelo equivalente en Android y Flutter<br><strong>Implementado en el backend</strong></td><td>Abstraer la persistencia de ReportMetric.</td><td>—</td><td><code>FindProjection(ownerId: int, period: MetricPeriod): DashboardProjection?</code><br><code>Save(projection: DashboardProjection): void</code></td><td>IReportMetricRepository depende de DashboardProjection</td></tr>
  </tbody>
</table>

<a id="toc-2-6-9-2-interface-layer"></a>

## 2.6.9.2. Interface Layer

**Responsabilidad estable.** Esta capa recibe las acciones relacionadas con **construcción y consulta de dashboards, métricas y proyecciones** y las traduce a casos de uso. Los controllers y resources corresponden a la API; las pantallas y controladores de estado representan la presentación objetivo en Android y Flutter. Ninguna de estas clases implementa reglas de negocio.

**Detalle técnico evolutivo.** El siguiente diccionario identifica las clases, sus responsabilidades, atributos, métodos y relaciones. La columna **Producto y estado** distingue los elementos comprobados en el código de aquellos que aún pertenecen al diseño objetivo.

<table>
  <thead>
    <tr><th>Clase</th><th>Categoría</th><th>Producto y estado</th><th>Propósito</th><th>Atributos</th><th>Métodos u operaciones</th><th>Relaciones</th></tr>
  </thead>
  <tbody>
    <tr><td><code>DashboardAnalyticsController</code></td><td>REST Controller</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Publicar por HTTP las capacidades de Analytics and Reporting.</td><td><code>IHerdQueryService herdQueryService</code><br><code>IAnimalQueryService animalQueryService</code><br><code>IHealthEventQueryService healthEventQueryService</code><br><code>IFinancialRecordQueryService financialRecordQueryService</code><br><code>IFarmActivityQueryService farmActivityQueryService</code><br><code>IDeviceQueryService deviceQueryService</code><br><code>IVeterinarianClientQueryService veterinarianClientQueryService</code></td><td><code>GetRancherDashboard(int rancherId, CancellationToken cancellationToken)</code><br><code>GetVeterinarianDashboard(int veterinarianId, CancellationToken cancellationToken)</code><br><code>GetRancherHealthSummary(int rancherId, CancellationToken cancellationToken)</code><br><code>GetRancherFinancialSummary(int rancherId, CancellationToken cancellationToken)</code></td><td>Recibe resources, invoca servicios de aplicación y devuelve resources HTTP.</td></tr>
    <tr><td><code>ReportMetricsController</code></td><td>REST Controller</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Publicar por HTTP las capacidades de Analytics and Reporting.</td><td><code>IReportMetricCommandService commandService</code><br><code>IReportMetricQueryService queryService</code></td><td><code>GetAll(CancellationToken cancellationToken)</code><br><code>GetById(int id, CancellationToken cancellationToken)</code><br><code>Create(CreateReportMetricResource resource, CancellationToken cancellationToken)</code><br><code>Update(int id, CreateReportMetricResource resource, CancellationToken cancellationToken)</code><br><code>Delete(int id, CancellationToken cancellationToken)</code></td><td>Recibe resources, invoca servicios de aplicación y devuelve resources HTTP.</td></tr>
    <tr><td><code>RancherDashboardResource</code></td><td>Resource/Assembler</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Definir un contrato estable de entrada o salida para la API REST.</td><td><code>int Herds</code><br><code>int Animals</code><br><code>int HealthyAnimals</code><br><code>int HealthEvents</code><br><code>int UpcomingActivities</code><br><code>int Devices</code><br><code>decimal Income</code><br><code>decimal Expenses</code><br><code>decimal Balance</code></td><td><code>Create(...)</code><br><code>Deconstruct(...)</code></td><td>Es construido o traducido por assemblers y consumido por el controller y los clientes móviles.</td></tr>
    <tr><td><code>VeterinarianDashboardResource</code></td><td>Resource/Assembler</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Definir un contrato estable de entrada o salida para la API REST.</td><td><code>int Clients</code><br><code>int Herds</code><br><code>int Patients</code><br><code>int HealthEvents</code><br><code>int UpcomingVisits</code><br><code>int ActiveTreatments</code></td><td><code>Create(...)</code><br><code>Deconstruct(...)</code></td><td>Es construido o traducido por assemblers y consumido por el controller y los clientes móviles.</td></tr>
    <tr><td><code>FinancialSummaryResource</code></td><td>Resource/Assembler</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Definir un contrato estable de entrada o salida para la API REST.</td><td><code>decimal Income</code><br><code>decimal Expenses</code><br><code>decimal Balance</code><br><code>IEnumerable&lt;MetricSliceResource&gt; ByCategory</code></td><td><code>Create(...)</code><br><code>Deconstruct(...)</code></td><td>Es construido o traducido por assemblers y consumido por el controller y los clientes móviles.</td></tr>
    <tr><td><code>HealthSummaryResource</code></td><td>Resource/Assembler</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Definir un contrato estable de entrada o salida para la API REST.</td><td><code>int TotalEvents</code><br><code>IEnumerable&lt;MetricSliceResource&gt; ByType</code></td><td><code>Create(...)</code><br><code>Deconstruct(...)</code></td><td>Es construido o traducido por assemblers y consumido por el controller y los clientes móviles.</td></tr>
    <tr><td><code>DashboardProjectionScreen</code></td><td>Composable</td><td>Android / Jetpack Compose<br><strong>Diseño objetivo</strong></td><td>Presentar construcción y consulta de dashboards, métricas y proyecciones en Android.</td><td><code>uiState</code><br><code>onAction</code><br><code>navigation</code></td><td><code>Render()</code><br><code>Submit()</code><br><code>Retry()</code></td><td>Observa DashboardProjectionViewModel y emite acciones de interfaz.</td></tr>
    <tr><td><code>DashboardProjectionViewModel</code></td><td>Presentation Model</td><td>Android / Kotlin<br><strong>Diseño objetivo</strong></td><td>Mantener el estado observable y traducir acciones de Android a casos de uso.</td><td><code>state</code><br><code>observeUseCase</code><br><code>syncUseCase</code></td><td><code>Load()</code><br><code>Submit(action)</code><br><code>RetrySync()</code></td><td>Invoca casos de uso de Application Layer y publica un UI State inmutable.</td></tr>
    <tr><td><code>DashboardProjectionPage</code></td><td>Widget</td><td>Flutter / Dart<br><strong>Diseño objetivo</strong></td><td>Presentar construcción y consulta de dashboards, métricas y proyecciones en Flutter.</td><td><code>state</code><br><code>onAction</code><br><code>router</code></td><td><code>build(context)</code><br><code>submit()</code><br><code>retry()</code></td><td>Observa DashboardProjectionController y emite intenciones del usuario.</td></tr>
    <tr><td><code>DashboardProjectionController</code></td><td>State Controller</td><td>Flutter / Dart<br><strong>Diseño objetivo</strong></td><td>Mantener el estado de presentación de Flutter y coordinar casos de uso.</td><td><code>state</code><br><code>observeUseCase</code><br><code>syncUseCase</code></td><td><code>load()</code><br><code>submit(action)</code><br><code>retrySync()</code></td><td>Invoca Application Layer y publica estados de carga, éxito y error.</td></tr>
  </tbody>
</table>

<a id="toc-2-6-9-3-application-layer"></a>

## 2.6.9.3. Application Layer

**Responsabilidad estable.** Esta capa coordina las capacidades de **construcción y consulta de dashboards, métricas y proyecciones**. Los commands y queries expresan intenciones; los handlers cargan aggregates, aplican reglas, persisten cambios y reaccionan a eventos. Los casos de uso móviles coordinan lectura local, actualización remota y sincronización idempotente.

**Detalle técnico evolutivo.** El siguiente diccionario identifica las clases, sus responsabilidades, atributos, métodos y relaciones. La columna **Producto y estado** distingue los elementos comprobados en el código de aquellos que aún pertenecen al diseño objetivo.

<table>
  <thead>
    <tr><th>Clase</th><th>Categoría</th><th>Producto y estado</th><th>Propósito</th><th>Atributos</th><th>Métodos u operaciones</th><th>Relaciones</th></tr>
  </thead>
  <tbody>
    <tr><td><code>ReportMetricCommandService</code></td><td>Application Service</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Orquestar construcción y consulta de dashboards, métricas y proyecciones sin contener reglas del dominio.</td><td><code>IReportMetricRepository repository</code><br><code>IUnitOfWork unitOfWork</code></td><td><code>Handle(CreateReportMetricCommand command, CancellationToken cancellationToken)</code><br><code>Handle(UpdateReportMetricCommand command, CancellationToken cancellationToken)</code><br><code>Handle(DeleteReportMetricCommand command, CancellationToken cancellationToken)</code></td><td>Invoca agregados y repositories; confirma la transacción mediante Unit of Work.</td></tr>
    <tr><td><code>ReportMetricQueryService</code></td><td>Application Service</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Orquestar construcción y consulta de dashboards, métricas y proyecciones sin contener reglas del dominio.</td><td><code>IReportMetricRepository repository</code></td><td><code>Handle(GetReportMetricByIdQuery query, CancellationToken cancellationToken)</code><br><code>Handle(GetAllReportMetricsQuery query, CancellationToken cancellationToken)</code></td><td>Invoca agregados y repositories; confirma la transacción mediante Unit of Work.</td></tr>
    <tr><td><code>CreateReportMetricCommand</code></td><td>Command/Query</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Transportar una intención o consulta tipada hacia su handler.</td><td><code>string Label</code><br><code>string Value</code><br><code>string Trend</code></td><td>—</td><td>Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio.</td></tr>
    <tr><td><code>UpdateReportMetricCommand</code></td><td>Command/Query</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Transportar una intención o consulta tipada hacia su handler.</td><td><code>int Id</code><br><code>string Label</code><br><code>string Value</code><br><code>string Trend</code></td><td>—</td><td>Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio.</td></tr>
    <tr><td><code>GetAllReportMetricsQuery</code></td><td>Command/Query</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Transportar una intención o consulta tipada hacia su handler.</td><td><code>filters: optional</code></td><td>—</td><td>Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio.</td></tr>
    <tr><td><code>GetReportMetricByIdQuery</code></td><td>Command/Query</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Transportar una intención o consulta tipada hacia su handler.</td><td><code>int Id</code></td><td>—</td><td>Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio.</td></tr>
    <tr><td><code>ObserveDashboardProjectionUseCase</code></td><td>Use Case</td><td>Android y Flutter<br><strong>Diseño objetivo</strong></td><td>Entregar primero datos locales y actualizar la consulta cuando exista conectividad.</td><td><code>localRepository</code><br><code>remoteRepository</code><br><code>connectivityMonitor</code></td><td><code>Execute(criteria): Stream&lt;Result&gt;</code></td><td>Es invocado por ViewModel/Controller y coordina repositorios móviles.</td></tr>
    <tr><td><code>SyncDashboardProjectionUseCase</code></td><td>Use Case</td><td>Android y Flutter<br><strong>Diseño objetivo</strong></td><td>Procesar operaciones móviles pendientes de manera idempotente.</td><td><code>outboxRepository</code><br><code>remoteRepository</code><br><code>conflictResolver</code></td><td><code>Execute(): SyncResult</code></td><td>Lee el outbox local, consume la API y actualiza el estado de sincronización.</td></tr>
    <tr><td><code>CreateReportMetricCommandHandler</code></td><td>Command Handler</td><td>Backend ASP.NET Core<br><strong>Diseño objetivo</strong></td><td>Ejecutar una intención concreta, aplicar reglas del agregado y confirmar la transacción.</td><td><code>repository</code><br><code>unitOfWork</code><br><code>domainPolicy</code></td><td><code>Handle(command): Result</code></td><td>Consume un Command, carga el aggregate mediante su repository y puede publicar un Domain Event.</td></tr>
    <tr><td><code>BuildDashboardQueryHandler</code></td><td>Query Handler</td><td>Backend ASP.NET Core<br><strong>Diseño objetivo</strong></td><td>Resolver una consulta de aplicación y construir el modelo de lectura requerido.</td><td><code>queryRepository</code><br><code>projectionBuilder</code></td><td><code>Handle(query): Result</code></td><td>Consume una Query y consulta repositories o proyecciones.</td></tr>
    <tr><td><code>SourceRecordChangedEventHandler</code></td><td>Event Handler</td><td>Backend ASP.NET Core<br><strong>Diseño objetivo</strong></td><td>Reaccionar al evento confirmado y actualizar proyecciones o integraciones.</td><td><code>projectionRepository</code><br><code>notificationPort</code><br><code>unitOfWork</code></td><td><code>Handle(domainEvent): Task</code></td><td>Consume un Domain Event y utiliza puertos de infraestructura sin modificar directamente el agregado.</td></tr>
  </tbody>
</table>

<a id="toc-2-6-9-4-infrastructure-layer"></a>

## 2.6.9.4. Infrastructure Layer

**Responsabilidad estable.** Esta capa implementa los puertos definidos hacia el interior de **Analytics and Reporting** y concentra acceso a base de datos, red, almacenamiento local e integraciones externas. Las clases de infraestructura traducen errores y contratos técnicos antes de devolver resultados a Application Layer.

**Detalle técnico evolutivo.** El siguiente diccionario identifica las clases, sus responsabilidades, atributos, métodos y relaciones. La columna **Producto y estado** distingue los elementos comprobados en el código de aquellos que aún pertenecen al diseño objetivo.

<table>
  <thead>
    <tr><th>Clase</th><th>Categoría</th><th>Producto y estado</th><th>Propósito</th><th>Atributos</th><th>Métodos u operaciones</th><th>Relaciones</th></tr>
  </thead>
  <tbody>
    <tr><td><code>ReportMetricRepository</code></td><td>Repository Adapter</td><td>Backend / Entity Framework Core<br><strong>Implementado en el backend</strong></td><td>Implementar el puerto de persistencia definido por Domain Layer.</td><td><code>AppDbContext context</code></td><td><code>FindById(id)</code><br><code>Add(entity)</code><br><code>Update(entity)</code><br><code>Delete(entity)</code></td><td>Implementa IReportMetricRepository; utiliza AppDbContext/MySQL y reconstruye el aggregate.</td></tr>
    <tr><td><code>ModelBuilderExtensions</code></td><td>Persistence Configuration</td><td>Backend / Entity Framework Core<br><strong>Implementado en el backend</strong></td><td>Mapear entidades y value objects del contexto al modelo relacional.</td><td><code>EntityTypeBuilder configuration</code></td><td><code>ApplyConfiguration(modelBuilder)</code></td><td>Configura tablas, claves, relaciones, restricciones y conversiones de Entity Framework Core.</td></tr>
    <tr><td><code>DashboardProjectionApiDataSource</code></td><td>Remote Adapter</td><td>Android / Kotlin<br><strong>Diseño objetivo</strong></td><td>Implementar el acceso remoto del cliente móvil a la API.</td><td><code>httpClient</code><br><code>tokenProvider</code><br><code>serializer</code></td><td><code>Get(criteria)</code><br><code>Create(dto)</code><br><code>Update(dto)</code><br><code>Delete(id)</code></td><td>Consume controllers REST por HTTPS/JSON y traduce errores HTTP al modelo de aplicación.</td></tr>
    <tr><td><code>DashboardProjectionDao</code></td><td>Room Adapter</td><td>Android / Room<br><strong>Diseño objetivo</strong></td><td>Implementar persistencia local y observación reactiva en Android.</td><td><code>roomDatabase</code><br><code>entityMapper</code></td><td><code>Observe(criteria)</code><br><code>Upsert(entity)</code><br><code>Delete(id)</code><br><code>Pending()</code></td><td>Implementa el puerto local mediante Room y participa en la estrategia de caché/outbox.</td></tr>
    <tr><td><code>DashboardProjectionRemoteDataSource</code></td><td>Remote Adapter</td><td>Flutter / Dart<br><strong>Diseño objetivo</strong></td><td>Implementar el acceso remoto del cliente móvil a la API.</td><td><code>httpClient</code><br><code>tokenProvider</code><br><code>serializer</code></td><td><code>Get(criteria)</code><br><code>Create(dto)</code><br><code>Update(dto)</code><br><code>Delete(id)</code></td><td>Consume controllers REST por HTTPS/JSON y traduce errores HTTP al modelo de aplicación.</td></tr>
    <tr><td><code>DashboardProjectionLocalDataSource</code></td><td>SQLite Adapter</td><td>Flutter / Dart<br><strong>Diseño objetivo</strong></td><td>Implementar persistencia local equivalente en Flutter.</td><td><code>sqliteDatabase</code><br><code>entityMapper</code></td><td><code>watch(criteria)</code><br><code>upsert(entity)</code><br><code>delete(id)</code><br><code>pending()</code></td><td>Implementa el puerto local mediante SQLite y participa en la estrategia de caché/outbox.</td></tr>
    <tr><td><code>LivestockMetricsAdapter</code></td><td>Projection Source Adapter</td><td>Backend ASP.NET Core<br><strong>Diseño objetivo</strong></td><td>Aislar una dependencia externa detrás de un puerto explícito.</td><td><code>livestockQueries</code></td><td><code>ReadLivestockMetrics(ownerId, period)</code></td><td>Implementa una fuente de proyección desde Livestock Management.</td></tr>
    <tr><td><code>SanitaryMetricsAdapter</code></td><td>Projection Source Adapter</td><td>Backend ASP.NET Core<br><strong>Diseño objetivo</strong></td><td>Aislar una dependencia externa detrás de un puerto explícito.</td><td><code>sanitaryQueries</code></td><td><code>ReadHealthMetrics(ownerId, period)</code></td><td>Implementa una fuente de proyección desde Sanitary Management.</td></tr>
    <tr><td><code>ActivityMetricsAdapter</code></td><td>Projection Source Adapter</td><td>Backend ASP.NET Core<br><strong>Diseño objetivo</strong></td><td>Aislar una dependencia externa detrás de un puerto explícito.</td><td><code>activityQueries</code></td><td><code>ReadActivityMetrics(ownerId, period)</code></td><td>Implementa una fuente de proyección desde Activity Management.</td></tr>
    <tr><td><code>FinancialMetricsAdapter</code></td><td>Projection Source Adapter</td><td>Backend ASP.NET Core<br><strong>Diseño objetivo</strong></td><td>Aislar una dependencia externa detrás de un puerto explícito.</td><td><code>financialQueries</code></td><td><code>ReadFinancialMetrics(ownerId, period)</code></td><td>Implementa una fuente de proyección desde Financial Management.</td></tr>
  </tbody>
</table>

<a id="toc-2-6-9-5-bounded-context-software-architecture-component-level-diagrams"></a>

## 2.6.9.5. Bounded Context Software Architecture Component Level Diagrams

El archivo [`component-level.dsl`](<../../assets/codefordiagrams/2.6.9. Bounded Context Analytics and Reporting/component-level.dsl>) contiene las vistas `BC9-ApiComponents`, `BC9-AndroidComponents` y `BC9-FlutterComponents`. Las tres parten del mismo modelo C4 y muestran la separación entre presentación, aplicación, dominio y adaptadores.

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-9-Bounded-Context-Analytics-and-Reporting/2-6-9-BC9-ApiComponents.svg" alt="Componentes API de Analytics and Reporting" width="900">
  <p><i>Figura 2.6.9.1. Componentes de la API para Analytics and Reporting. Fuente: elaboración propia con Structurizr DSL.</i></p>
</div>

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-9-Bounded-Context-Analytics-and-Reporting/2-6-9-BC9-AndroidComponents.svg" alt="Componentes Android de Analytics and Reporting" width="900">
  <p><i>Figura 2.6.9.2. Componentes Android para Analytics and Reporting. Fuente: elaboración propia con Structurizr DSL.</i></p>
</div>

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-9-Bounded-Context-Analytics-and-Reporting/2-6-9-BC9-FlutterComponents.svg" alt="Componentes Flutter de Analytics and Reporting" width="900">
  <p><i>Figura 2.6.9.3. Componentes Flutter para Analytics and Reporting. Fuente: elaboración propia con Structurizr DSL.</i></p>
</div>

<a id="toc-2-6-9-6-bounded-context-software-architecture-code-level-diagrams"></a>

## 2.6.9.6. Bounded Context Software Architecture Code Level Diagrams

Los diagramas de código detallan el modelo del dominio y los objetos de persistencia. El UML diferencia los elementos existentes de las incorporaciones objetivo, mientras los esquemas SQL señalan mediante comentarios las columnas propuestas. Los archivos ERD quedan disponibles para completar la importación manual.

<a id="toc-2-6-9-6-1-bounded-context-domain-layer-class-diagrams"></a>

### 2.6.9.6.1. Bounded Context Domain Layer Class Diagrams

El Class Diagram incluye agregados, entidades, value objects, enumeraciones, servicios de dominio e interfaces de repositorio con atributos, operaciones, visibilidad y multiplicidades.

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-9-Bounded-Context-Analytics-and-Reporting/2-6-9-domain-layer-class-diagram.svg" alt="Class Diagram de Analytics and Reporting" width="900">
  <p><i>Figura 2.6.9.4. Domain Layer Class Diagram de Analytics and Reporting. Fuente: elaboración propia con PlantUML.</i></p>
</div>

<a id="toc-2-6-9-6-2-bounded-context-database-design-diagram"></a>

### 2.6.9.6.2. Bounded Context Database Design Diagram

MySQL mantiene la persistencia autoritativa. Room y SQLite contienen únicamente caché, metadatos de sincronización y operaciones pendientes; no sustituyen las reglas ni la fuente de verdad del backend. En IAM, las credenciales y tokens permanecen fuera de las tablas locales y se almacenan mediante mecanismos seguros del sistema operativo.

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-9-Bounded-Context-Analytics-and-Reporting/2-6-9-mysql-database-design.png" alt="MySQL Database Diagram de Analytics and Reporting" width="900">
  <p><i>Figura 2.6.9.5. MySQL Database Design de Analytics and Reporting. Fuente: elaboración propia a partir del esquema SQL.</i></p>
</div>

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-9-Bounded-Context-Analytics-and-Reporting/2-6-9-android-room-database-design.png" alt="Room Database Diagram de Analytics and Reporting" width="900">
  <p><i>Figura 2.6.9.6. Android Room Database Design de Analytics and Reporting. Fuente: elaboración propia a partir del esquema SQL.</i></p>
</div>
