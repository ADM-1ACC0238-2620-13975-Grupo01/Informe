# 2.6.8. Bounded Context: Subscription Management

Administrar planes, vigencia de suscripciones y pagos confirmados sin introducir conceptos propios de Stripe en el dominio.

La base implementada se encuentra en el módulo `Subscriptions` de la API ASP.NET Core. El diseño móvil de Android y Flutter se presenta como **diseño objetivo** porque esos clientes todavía no existen en el workspace. Los tres productos comparten contratos REST y lenguaje ubicuo, mientras la API conserva las reglas autoritativas.

## 2.6.8.1. Domain Layer

Esta capa representa el núcleo de Subscription Management. Los elementos existentes se conservarán como punto de partida; los elementos objetivo completan las invariantes identificadas en EventStorming y en el Bounded Context Canvas.

<table>
  <thead>
    <tr><th>Clase o componente</th><th>Tipo</th><th>Producto</th><th>Propósito</th><th>Responsabilidades</th></tr>
  </thead>
  <tbody>
    <tr><td>SubscriptionPlan</td><td>Clase de dominio existente</td><td>Backend / módulo Subscriptions</td><td>Representar SubscriptionPlan dentro de Subscription Management.</td><td>Conservar las invariantes actualmente implementadas y servir como evidencia trazable.</td></tr>
    <tr><td>Subscription</td><td>Clase de dominio existente</td><td>Backend / módulo Subscriptions</td><td>Representar Subscription dentro de Subscription Management.</td><td>Conservar las invariantes actualmente implementadas y servir como evidencia trazable.</td></tr>
    <tr><td>Payment</td><td>Clase de dominio existente</td><td>Backend / módulo Subscriptions</td><td>Representar Payment dentro de Subscription Management.</td><td>Conservar las invariantes actualmente implementadas y servir como evidencia trazable.</td></tr>
    <tr><td>ISubscriptionPlanRepository</td><td>Repository Interface existente</td><td>Backend / módulo Subscriptions</td><td>Representar ISubscriptionPlanRepository dentro de Subscription Management.</td><td>Conservar las invariantes actualmente implementadas y servir como evidencia trazable.</td></tr>
    <tr><td>ISubscriptionRepository</td><td>Repository Interface existente</td><td>Backend / módulo Subscriptions</td><td>Representar ISubscriptionRepository dentro de Subscription Management.</td><td>Conservar las invariantes actualmente implementadas y servir como evidencia trazable.</td></tr>
    <tr><td>IPaymentRepository</td><td>Repository Interface existente</td><td>Backend / módulo Subscriptions</td><td>Representar IPaymentRepository dentro de Subscription Management.</td><td>Conservar las invariantes actualmente implementadas y servir como evidencia trazable.</td></tr>
    <tr><td>Money</td><td>Diseño objetivo</td><td>Modelo canónico compartido</td><td>Completar el lenguaje ubicuo de Subscription Management.</td><td>Expresar reglas o conceptos requeridos por el alcance móvil que aún no están implementados en el backend heredado.</td></tr>
    <tr><td>SubscriptionStatus</td><td>Diseño objetivo</td><td>Modelo canónico compartido</td><td>Completar el lenguaje ubicuo de Subscription Management.</td><td>Expresar reglas o conceptos requeridos por el alcance móvil que aún no están implementados en el backend heredado.</td></tr>
    <tr><td>PaymentStatus</td><td>Diseño objetivo</td><td>Modelo canónico compartido</td><td>Completar el lenguaje ubicuo de Subscription Management.</td><td>Expresar reglas o conceptos requeridos por el alcance móvil que aún no están implementados en el backend heredado.</td></tr>
    <tr><td>PaymentGateway</td><td>Diseño objetivo</td><td>Modelo canónico compartido</td><td>Completar el lenguaje ubicuo de Subscription Management.</td><td>Expresar reglas o conceptos requeridos por el alcance móvil que aún no están implementados en el backend heredado.</td></tr>
  </tbody>
</table>

## 2.6.8.2. Interface Layer

La Interface Layer traduce acciones de usuarios y contratos externos. En el backend utiliza controllers, resources y assemblers; en los clientes móviles utiliza pantallas y controladores de estado específicos de cada plataforma.

<table>
  <thead>
    <tr><th>Clase o componente</th><th>Tipo</th><th>Producto</th><th>Propósito</th><th>Responsabilidades</th></tr>
  </thead>
  <tbody>
    <tr><td>SubscriptionPlansController</td><td>REST Controller existente</td><td>Backend ASP.NET Core</td><td>Exponer consulta de planes, checkout, confirmación de pago y vigencia.</td><td>Validar el contrato HTTP, traducir resources y delegar el caso de uso.</td></tr>
    <tr><td>SubscriptionsController</td><td>REST Controller existente</td><td>Backend ASP.NET Core</td><td>Exponer consulta de planes, checkout, confirmación de pago y vigencia.</td><td>Validar el contrato HTTP, traducir resources y delegar el caso de uso.</td></tr>
    <tr><td>SubscriptionPlanResource</td><td>Resource/Assembler existente</td><td>Backend ASP.NET Core</td><td>Definir el contrato público de entrada o salida.</td><td>Evitar exponer directamente entidades del dominio.</td></tr>
    <tr><td>SubscriptionResource</td><td>Resource/Assembler existente</td><td>Backend ASP.NET Core</td><td>Definir el contrato público de entrada o salida.</td><td>Evitar exponer directamente entidades del dominio.</td></tr>
    <tr><td>PaymentResource</td><td>Resource/Assembler existente</td><td>Backend ASP.NET Core</td><td>Definir el contrato público de entrada o salida.</td><td>Evitar exponer directamente entidades del dominio.</td></tr>
    <tr><td>StripeCheckoutResource</td><td>Resource/Assembler existente</td><td>Backend ASP.NET Core</td><td>Definir el contrato público de entrada o salida.</td><td>Evitar exponer directamente entidades del dominio.</td></tr>
    <tr><td>SubscriptionScreen</td><td>Composable objetivo</td><td>Android / Jetpack Compose</td><td>Presentar consulta de planes, checkout, confirmación de pago y vigencia.</td><td>Renderizar estado, recibir acciones y mostrar errores recuperables.</td></tr>
    <tr><td>SubscriptionViewModel</td><td>Presentation Model objetivo</td><td>Android / Kotlin</td><td>Coordinar el estado observable de la pantalla.</td><td>Invocar casos de uso y convertir resultados en UI state.</td></tr>
    <tr><td>SubscriptionPage</td><td>Widget objetivo</td><td>Flutter / Dart</td><td>Presentar consulta de planes, checkout, confirmación de pago y vigencia.</td><td>Renderizar estado y enviar intenciones del usuario.</td></tr>
    <tr><td>SubscriptionController</td><td>State Controller objetivo</td><td>Flutter / Dart</td><td>Coordinar el estado de presentación.</td><td>Invocar casos de uso y publicar estados de carga, éxito y error.</td></tr>
  </tbody>
</table>

## 2.6.8.3. Application Layer

La Application Layer orquesta comandos, consultas y sincronización. Los casos de uso móviles consultan primero el read model local, solicitan actualización remota cuando existe conectividad y procesan operaciones pendientes mediante un outbox idempotente.

<table>
  <thead>
    <tr><th>Clase o componente</th><th>Tipo</th><th>Producto</th><th>Propósito</th><th>Responsabilidades</th></tr>
  </thead>
  <tbody>
    <tr><td>SubscriptionPlanCommandService</td><td>Application Service existente</td><td>Backend ASP.NET Core</td><td>Orquestar consulta de planes, checkout, confirmación de pago y vigencia.</td><td>Coordinar repositorios, reglas del dominio y Unit of Work.</td></tr>
    <tr><td>SubscriptionCommandService</td><td>Application Service existente</td><td>Backend ASP.NET Core</td><td>Orquestar consulta de planes, checkout, confirmación de pago y vigencia.</td><td>Coordinar repositorios, reglas del dominio y Unit of Work.</td></tr>
    <tr><td>PaymentCommandService</td><td>Application Service existente</td><td>Backend ASP.NET Core</td><td>Orquestar consulta de planes, checkout, confirmación de pago y vigencia.</td><td>Coordinar repositorios, reglas del dominio y Unit of Work.</td></tr>
    <tr><td>SubscriptionQueryService</td><td>Application Service existente</td><td>Backend ASP.NET Core</td><td>Orquestar consulta de planes, checkout, confirmación de pago y vigencia.</td><td>Coordinar repositorios, reglas del dominio y Unit of Work.</td></tr>
    <tr><td>CreateSubscriptionCommand</td><td>Command/Query existente</td><td>Backend ASP.NET Core</td><td>Representar una intención o consulta explícita.</td><td>Transportar datos tipados hacia el servicio de aplicación correspondiente.</td></tr>
    <tr><td>CreatePaymentCommand</td><td>Command/Query existente</td><td>Backend ASP.NET Core</td><td>Representar una intención o consulta explícita.</td><td>Transportar datos tipados hacia el servicio de aplicación correspondiente.</td></tr>
    <tr><td>GetSubscriptionByIdQuery</td><td>Command/Query existente</td><td>Backend ASP.NET Core</td><td>Representar una intención o consulta explícita.</td><td>Transportar datos tipados hacia el servicio de aplicación correspondiente.</td></tr>
    <tr><td>GetAllSubscriptionPlansQuery</td><td>Command/Query existente</td><td>Backend ASP.NET Core</td><td>Representar una intención o consulta explícita.</td><td>Transportar datos tipados hacia el servicio de aplicación correspondiente.</td></tr>
    <tr><td>SubscriptionCommandHandler</td><td>Command Handler objetivo</td><td>Backend ASP.NET Core</td><td>Ejecutar comandos mediante una unidad de aplicación explícita.</td><td>Cargar el agregado, aplicar sus reglas, persistirlo y publicar el resultado.</td></tr>
    <tr><td>SubscriptionEventHandler</td><td>Event Handler objetivo</td><td>Backend ASP.NET Core</td><td>Reaccionar a cambios confirmados en el contexto.</td><td>Actualizar proyecciones o solicitar integraciones sin acoplarlas al agregado.</td></tr>
    <tr><td>ObserveSubscriptionUseCase</td><td>Use Case objetivo</td><td>Android y Flutter</td><td>Consultar el read model local y actualizar la UI.</td><td>Combinar caché local con actualización remota.</td></tr>
    <tr><td>SyncSubscriptionUseCase</td><td>Use Case objetivo</td><td>Android y Flutter</td><td>Sincronizar cambios pendientes.</td><td>Procesar el outbox de forma idempotente y resolver resultados del servidor.</td></tr>
  </tbody>
</table>

## 2.6.8.4. Infrastructure Layer

La Infrastructure Layer conecta el dominio con IAM y Stripe mediante Anti-Corruption Layer. Los adapters implementan interfaces definidas hacia el interior y traducen errores técnicos a resultados comprendidos por los casos de uso.

<table>
  <thead>
    <tr><th>Clase o componente</th><th>Tipo</th><th>Producto</th><th>Propósito</th><th>Responsabilidades</th></tr>
  </thead>
  <tbody>
    <tr><td>SubscriptionPlanRepository / SubscriptionRepository / PaymentRepository</td><td>Repository Adapter existente</td><td>Backend / Entity Framework Core</td><td>Implementar los puertos de persistencia del dominio.</td><td>Consultar y guardar las entidades mediante AppDbContext y MySQL.</td></tr>
    <tr><td>ModelBuilderExtensions</td><td>Persistence Configuration existente</td><td>Backend / Entity Framework Core</td><td>Configurar tablas, columnas, constraints y conversiones.</td><td>Mantener el modelo relacional alineado con las entidades.</td></tr>
    <tr><td>SubscriptionApiDataSource</td><td>Remote Adapter objetivo</td><td>Android / Kotlin</td><td>Consumir los endpoints REST del contexto.</td><td>Enviar JWT, serializar JSON y normalizar errores HTTP.</td></tr>
    <tr><td>SubscriptionDao</td><td>Room Adapter objetivo</td><td>Android / Room</td><td>Acceder al almacenamiento local.</td><td>Mantener caché, estado de sincronización y operaciones pendientes.</td></tr>
    <tr><td>SubscriptionRemoteDataSource</td><td>Remote Adapter objetivo</td><td>Flutter / Dart</td><td>Consumir los mismos contratos REST.</td><td>Serializar DTOs y traducir errores de red.</td></tr>
    <tr><td>SubscriptionLocalDataSource</td><td>SQLite Adapter objetivo</td><td>Flutter / Dart</td><td>Acceder a la persistencia local equivalente.</td><td>Mantener el mismo comportamiento offline que Android.</td></tr>
    <tr><td>IAM y Stripe mediante Anti-Corruption Layer</td><td>Integración/ACL</td><td>Infraestructura compartida</td><td>Conectar el contexto con capacidades externas.</td><td>Traducir contratos técnicos sin contaminar el modelo del dominio.</td></tr>
  </tbody>
</table>

## 2.6.8.5. Bounded Context Software Architecture Component Level Diagrams

El archivo [`component-level.dsl`](<../../assets/codefordiagrams/2.6.8. Bounded Context Subscription Management/component-level.dsl>) contiene las vistas `BC8-ApiComponents`, `BC8-AndroidComponents` y `BC8-FlutterComponents`. Las tres parten del mismo modelo C4 y muestran la separación entre presentación, aplicación, dominio y adaptadores.

<div align="center">
  <!-- Placeholder: exportar la vista BC8-ApiComponents. -->
  <img src="../../assets/chapter-2/tactical-ddd/subscription-management/subscription-management-api-components.png" alt="Componentes API de Subscription Management" width="900">
  <p><i>Figura 2.6.8.1. Componentes de la API para Subscription Management. Fuente: elaboración propia con Structurizr DSL.</i></p>
</div>

<div align="center">
  <!-- Placeholder: exportar la vista BC8-AndroidComponents. -->
  <img src="../../assets/chapter-2/tactical-ddd/subscription-management/subscription-management-android-components.png" alt="Componentes Android de Subscription Management" width="900">
  <p><i>Figura 2.6.8.2. Componentes Android para Subscription Management. Fuente: elaboración propia con Structurizr DSL.</i></p>
</div>

<div align="center">
  <!-- Placeholder: exportar la vista BC8-FlutterComponents. -->
  <img src="../../assets/chapter-2/tactical-ddd/subscription-management/subscription-management-flutter-components.png" alt="Componentes Flutter de Subscription Management" width="900">
  <p><i>Figura 2.6.8.3. Componentes Flutter para Subscription Management. Fuente: elaboración propia con Structurizr DSL.</i></p>
</div>

## 2.6.8.6. Bounded Context Software Architecture Code Level Diagrams

Los diagramas de código detallan el modelo del dominio y los objetos de persistencia. El UML diferencia los elementos existentes de las incorporaciones objetivo, mientras los esquemas SQL señalan mediante comentarios las columnas propuestas. Los archivos ERD quedan disponibles para completar la importación manual.

### 2.6.8.6.1. Bounded Context Domain Layer Class Diagrams

El Class Diagram incluye agregados, entidades, value objects, enumeraciones, servicios de dominio e interfaces de repositorio con atributos, operaciones, visibilidad y multiplicidades.

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-8-Bounded-Context-Subscription-Management/2-6-8-domain-layer-class-diagram.svg" alt="Class Diagram de Subscription Management" width="900">
  <p><i>Figura 2.6.8.4. Domain Layer Class Diagram de Subscription Management. Fuente: elaboración propia con PlantUML.</i></p>
</div>

### 2.6.8.6.2. Bounded Context Database Design Diagram

MySQL mantiene la persistencia autoritativa. Room y SQLite contienen únicamente caché, metadatos de sincronización y operaciones pendientes; no sustituyen las reglas ni la fuente de verdad del backend. En IAM, las credenciales y tokens permanecen fuera de las tablas locales y se almacenan mediante mecanismos seguros del sistema operativo.

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-8-Bounded-Context-Subscription-Management/2-6-8-mysql-database-design.png" alt="MySQL Database Diagram de Subscription Management" width="900">
  <p><i>Figura 2.6.8.5. MySQL Database Design de Subscription Management. Fuente: elaboración propia a partir del esquema SQL.</i></p>
</div>

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-8-Bounded-Context-Subscription-Management/2-6-8-android-room-database-design.png" alt="Room Database Diagram de Subscription Management" width="900">
  <p><i>Figura 2.6.8.6. Android Room Database Design de Subscription Management. Fuente: elaboración propia a partir del esquema SQL.</i></p>
</div>

