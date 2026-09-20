<a id="toc-2-6-9-bounded-context-analytics-and-reporting"></a>

# 2.6.9. Bounded Context: Analytics and Reporting

Construir proyecciones y métricas de consulta para los dashboards sin adquirir propiedad sobre los registros de los contextos fuente.

La base implementada se encuentra en el módulo `Analytics` de la API ASP.NET Core. El diseño móvil de Android y Flutter se documenta como **no implementado** porque esos clientes todavía no existen en el workspace. Los tres productos comparten contratos REST y lenguaje ubicuo, mientras la API conserva las reglas autoritativas.

<a id="toc-2-6-9-1-domain-layer"></a>

## 2.6.9.1. Domain Layer

**Responsabilidad estable.** Esta capa documenta el modelo que representa el núcleo de **Analytics and Reporting**. Las reglas autoritativas se ejecutan en la API; Android y Flutter mantienen modelos equivalentes para presentación, validación inmediata y trabajo offline. La columna de estado distingue el código heredado de la arquitectura objetivo.

### Aggregate Root: DashboardProjection

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend, Android y Flutter (modelo canónico) — **No implementado** |
| **Propósito** | Agrupar métricas calculadas para una audiencia y periodo. |
| **Relaciones** | DashboardProjection compone ReportMetric; DashboardProjection compone MetricPeriod; ProjectionBuilder depende de DashboardProjection; IReportMetricRepository depende de DashboardProjection |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `id` | `int` |
| `ownerId` | `int` |
| `audience` | `string` |
| `period` | `MetricPeriod` |
| `generatedAt` | `DateTime` |
| `metrics` | `List~ReportMetric~` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `ReplaceMetrics(metrics: List~ReportMetric~)` | `void` |
| `IsStale(now: DateTime)` | `bool` |

### Entity: ReportMetric

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend; modelo equivalente en Android y Flutter — **Implementado** |
| **Propósito** | Representar una métrica individual del dashboard. |
| **Relaciones** | DashboardProjection compone ReportMetric; ReportMetric compone MetricSlice |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `id` | `int` |
| `label` | `string` |
| `slice` | `MetricSlice` |
| `trend` | `string` |
| `sourceContext` | `string` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Update(slice: MetricSlice, trend: string)` | `void` |

### Value Object: MetricSlice

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend, Android y Flutter (modelo canónico) — **No implementado** |
| **Propósito** | Representar un valor, unidad y etiqueta de una métrica. |
| **Relaciones** | ReportMetric compone MetricSlice |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `label` | `string` |
| `value` | `decimal` |
| `unit` | `string` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `IsComparableTo(other: MetricSlice)` | `bool` |


### Domain Service: ProjectionBuilder

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend, Android y Flutter (modelo canónico) — **No implementado** |
| **Propósito** | Construir proyecciones a partir de los contextos fuente. |
| **Relaciones** | ProjectionBuilder depende de DashboardProjection |

**Atributos o dependencias**

No aplica.

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `BuildRancher(ownerId: int, period: MetricPeriod)` | `DashboardProjection` |
| `BuildVeterinarian(id: int, period: MetricPeriod)` | `DashboardProjection` |

### Repository Interface: IReportMetricRepository

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend; modelo equivalente en Android y Flutter — **Implementado** |
| **Propósito** | Abstraer la persistencia de ReportMetric. |
| **Relaciones** | IReportMetricRepository depende de DashboardProjection |

**Atributos o dependencias**

No aplica.

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `FindProjection(ownerId: int, period: MetricPeriod)` | `DashboardProjection?` |
| `Save(projection: DashboardProjection)` | `void` |

<a id="toc-2-6-9-2-interface-layer"></a>

## 2.6.9.2. Interface Layer

**Responsabilidad estable.** Esta capa recibe las acciones relacionadas con **construcción y consulta de dashboards, métricas y proyecciones** y las traduce a casos de uso. Los controllers y resources corresponden a la API; las pantallas y controladores de estado representan la presentación objetivo en Android y Flutter. Ninguna de estas clases implementa reglas de negocio.

### REST Controller: DashboardAnalyticsController

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend ASP.NET Core — **Implementado** |
| **Propósito** | Publicar por HTTP las capacidades de Analytics and Reporting. |
| **Relaciones** | Recibe resources, invoca servicios de aplicación y devuelve resources HTTP. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `herdQueryService` | `IHerdQueryService` |
| `animalQueryService` | `IAnimalQueryService` |
| `healthEventQueryService` | `IHealthEventQueryService` |
| `financialRecordQueryService` | `IFinancialRecordQueryService` |
| `farmActivityQueryService` | `IFarmActivityQueryService` |
| `deviceQueryService` | `IDeviceQueryService` |
| `veterinarianClientQueryService` | `IVeterinarianClientQueryService` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `GetRancherDashboard(int rancherId, CancellationToken cancellationToken)` | `No especificado` |
| `GetVeterinarianDashboard(int veterinarianId, CancellationToken cancellationToken)` | `No especificado` |
| `GetRancherHealthSummary(int rancherId, CancellationToken cancellationToken)` | `No especificado` |
| `GetRancherFinancialSummary(int rancherId, CancellationToken cancellationToken)` | `No especificado` |







### Presentation Model: DashboardProjectionViewModel

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


### State Controller: DashboardProjectionController

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

<a id="toc-2-6-9-3-application-layer"></a>

## 2.6.9.3. Application Layer

**Responsabilidad estable.** Esta capa coordina las capacidades de **construcción y consulta de dashboards, métricas y proyecciones**. Los commands y queries expresan intenciones; los handlers cargan aggregates, aplican reglas, persisten cambios y reaccionan a eventos. Los casos de uso móviles coordinan lectura local, actualización remota y sincronización idempotente.


### Application Service: ReportMetricQueryService

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend ASP.NET Core — **Implementado** |
| **Propósito** | Orquestar construcción y consulta de dashboards, métricas y proyecciones sin contener reglas del dominio. |
| **Relaciones** | Invoca agregados y repositories; confirma la transacción mediante Unit of Work. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `repository` | `IReportMetricRepository` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Handle(GetReportMetricByIdQuery query, CancellationToken cancellationToken)` | `No especificado` |
| `Handle(GetAllReportMetricsQuery query, CancellationToken cancellationToken)` | `No especificado` |





### Use Case: ObserveDashboardProjectionUseCase

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



### Query Handler: BuildDashboardQueryHandler

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend ASP.NET Core — **No implementado** |
| **Propósito** | Resolver una consulta de aplicación y construir el modelo de lectura requerido. |
| **Relaciones** | Consume una Query y consulta repositories o proyecciones. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `queryRepository` | `No especificado` |
| `projectionBuilder` | `No especificado` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Handle(query)` | `Result` |

### Event Handler: SourceRecordChangedEventHandler

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

<a id="toc-2-6-9-4-infrastructure-layer"></a>

## 2.6.9.4. Infrastructure Layer

**Responsabilidad estable.** Esta capa implementa los puertos definidos hacia el interior de **Analytics and Reporting** y concentra acceso a base de datos, red, almacenamiento local e integraciones externas. Las clases de infraestructura traducen errores y contratos técnicos antes de devolver resultados a Application Layer.

### Repository Adapter: ReportMetricRepository

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend / Entity Framework Core — **Implementado** |
| **Propósito** | Implementar el puerto de persistencia definido por Domain Layer. |
| **Relaciones** | Implementa IReportMetricRepository; utiliza AppDbContext/MySQL y reconstruye el aggregate. |

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



### Room Adapter: DashboardProjectionDao

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


### SQLite Adapter: DashboardProjectionLocalDataSource

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

### Projection Source Adapter: LivestockMetricsAdapter

| Campo | Detalle |
|---|---|
| **Producto y estado** | Backend ASP.NET Core — **No implementado** |
| **Propósito** | Aislar una dependencia externa detrás de un puerto explícito. |
| **Relaciones** | Implementa una fuente de proyección desde Livestock Management. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `livestockQueries` | `No especificado` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `ReadLivestockMetrics(ownerId, period)` | `No especificado` |




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
