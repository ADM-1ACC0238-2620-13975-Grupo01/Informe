<a id="toc-2-6-8-bounded-context-subscription-management"></a>

# 2.6.8. Bounded Context: Subscription Management

Administrar planes, vigencia de suscripciones y pagos confirmados sin introducir conceptos propios de Stripe en el dominio.

La base implementada se encuentra en el módulo `Subscriptions` de la API ASP.NET Core. El diseño móvil de Android y Flutter se presenta como **diseño objetivo** porque esos clientes todavía no existen en el workspace. Los tres productos comparten contratos REST y lenguaje ubicuo, mientras la API conserva las reglas autoritativas.

<a id="toc-2-6-8-1-domain-layer"></a>

## 2.6.8.1. Domain Layer

Esta capa documenta el modelo que representa el núcleo de **Subscription Management**. Las reglas autoritativas se ejecutan en la API; Android y Flutter mantienen modelos equivalentes para presentación, validación inmediata y trabajo offline. La columna de estado distingue el código heredado de la arquitectura objetivo.

<table>
  <thead>
    <tr><th>Clase</th><th>Categoría</th><th>Producto y estado</th><th>Propósito</th><th>Atributos</th><th>Métodos u operaciones</th><th>Relaciones</th></tr>
  </thead>
  <tbody>
    <tr><td><code>SubscriptionPlan</code></td><td>Entity</td><td>Backend; modelo equivalente en Android y Flutter<br><strong>Implementado en el backend</strong></td><td>Definir condiciones y límites de un plan comercial.</td><td><code>id: int</code><br><code>name: string</code><br><code>price: Money</code><br><code>providerPriceId: string</code><br><code>maxAnimals: int</code><br><code>isActive: bool</code></td><td><code>Deactivate(): void</code><br><code>ChangePrice(price: Money): void</code></td><td>SubscriptionPlan compone Money</td></tr>
    <tr><td><code>Subscription</code></td><td>Aggregate Root</td><td>Backend; modelo equivalente en Android y Flutter<br><strong>Implementado en el backend</strong></td><td>Controlar vigencia y estado de la suscripción de un usuario.</td><td><code>id: int</code><br><code>userId: int</code><br><code>planId: int</code><br><code>status: SubscriptionStatus</code><br><code>startedAt: Date</code><br><code>endsAt: Date?</code></td><td><code>Activate(start: Date, end: Date?): void</code><br><code>Cancel(end: Date): void</code><br><code>IsActive(on: Date): bool</code></td><td>Subscription compone Payment; Subscription se relaciona con SubscriptionStatus; ISubscriptionRepository depende de Subscription</td></tr>
    <tr><td><code>Payment</code></td><td>Entity</td><td>Backend; modelo equivalente en Android y Flutter<br><strong>Implementado en el backend</strong></td><td>Registrar el resultado de un pago.</td><td><code>id: int</code><br><code>subscriptionId: int</code><br><code>userId: int</code><br><code>amount: Money</code><br><code>providerPaymentId: string</code><br><code>status: PaymentStatus</code><br><code>paidAt: DateTime</code></td><td><code>Confirm(providerId: string, paidAt: DateTime): void</code><br><code>Reject(): void</code></td><td>Subscription compone Payment; Payment se relaciona con PaymentStatus; Payment compone Money</td></tr>
    <tr><td><code>Money</code></td><td>Value Object</td><td>Backend, Android y Flutter (modelo canónico)<br><strong>Diseño objetivo</strong></td><td>Representar un importe junto con su moneda.</td><td><code>amount: decimal</code><br><code>currency: string</code></td><td><code>IsPositive(): bool</code></td><td>Payment compone Money; SubscriptionPlan compone Money</td></tr>
    <tr><td><code>SubscriptionStatus</code></td><td>Enumeration</td><td>Backend, Android y Flutter (modelo canónico)<br><strong>Diseño objetivo</strong></td><td>Definir los valores válidos de SubscriptionStatus.</td><td><code>Pending</code><br><code>Active</code><br><code>Cancelled</code><br><code>Expired</code></td><td>—</td><td>Subscription se relaciona con SubscriptionStatus</td></tr>
    <tr><td><code>PaymentStatus</code></td><td>Enumeration</td><td>Backend, Android y Flutter (modelo canónico)<br><strong>Diseño objetivo</strong></td><td>Definir los valores válidos de PaymentStatus.</td><td><code>Pending</code><br><code>Paid</code><br><code>Failed</code></td><td>—</td><td>Payment se relaciona con PaymentStatus</td></tr>
    <tr><td><code>ISubscriptionRepository</code></td><td>Repository Interface</td><td>Backend; modelo equivalente en Android y Flutter<br><strong>Implementado en el backend</strong></td><td>Abstraer la persistencia de Subscription.</td><td>—</td><td><code>FindById(id: int): Subscription?</code><br><code>FindActiveByUser(userId: int): Subscription?</code><br><code>Add(subscription: Subscription): void</code><br><code>Update(subscription: Subscription): void</code></td><td>ISubscriptionRepository depende de Subscription</td></tr>
    <tr><td><code>ISubscriptionPlanRepository</code></td><td>Repository Interface</td><td>Backend; modelo equivalente en Android y Flutter<br><strong>Implementado en el backend</strong></td><td>Abstraer la persistencia de planes de suscripción.</td><td>—</td><td><code>FindByIdAsync(id)</code><br><code>ListAsync()</code><br><code>AddAsync(plan)</code><br><code>Update(plan)</code></td><td>Persiste SubscriptionPlan y es implementado por SubscriptionPlanRepository.</td></tr>
    <tr><td><code>IPaymentRepository</code></td><td>Repository Interface</td><td>Backend; modelo equivalente en Android y Flutter<br><strong>Implementado en el backend</strong></td><td>Abstraer la persistencia y consulta de pagos.</td><td>—</td><td><code>FindByUserIdAsync(userId)</code><br><code>FindByProviderPaymentIdAsync(providerPaymentId)</code><br><code>AddAsync(payment)</code></td><td>Persiste Payment y es implementado por PaymentRepository.</td></tr>
    <tr><td><code>PaymentGateway</code></td><td>Domain Port</td><td>Backend; modelo equivalente en Android y Flutter<br><strong>Diseño objetivo</strong></td><td>Abstraer el proveedor externo de cobros.</td><td>—</td><td><code>CreateCheckout(subscription, plan)</code><br><code>ConfirmPayment(reference)</code></td><td>Es implementado por StripePaymentGateway en Infrastructure Layer.</td></tr>
  </tbody>
</table>

<a id="toc-2-6-8-2-interface-layer"></a>

## 2.6.8.2. Interface Layer

Esta capa recibe las acciones relacionadas con **consulta de planes, contratación, pago y actualización de suscripciones** y las traduce a casos de uso. Los controllers y resources corresponden a la API; las pantallas y controladores de estado representan la presentación objetivo en Android y Flutter. Ninguna de estas clases implementa reglas de negocio.

<table>
  <thead>
    <tr><th>Clase</th><th>Categoría</th><th>Producto y estado</th><th>Propósito</th><th>Atributos</th><th>Métodos u operaciones</th><th>Relaciones</th></tr>
  </thead>
  <tbody>
    <tr><td><code>SubscriptionPlansController</code></td><td>REST Controller</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Publicar por HTTP las capacidades de Subscription Management.</td><td><code>ISubscriptionPlanCommandService commandService</code><br><code>ISubscriptionPlanQueryService queryService</code></td><td><code>GetAll(CancellationToken cancellationToken)</code><br><code>GetById(int id, CancellationToken cancellationToken)</code><br><code>Create(CreateSubscriptionPlanResource resource, CancellationToken cancellationToken)</code><br><code>Update(int id, CreateSubscriptionPlanResource resource, CancellationToken cancellationToken)</code><br><code>Delete(int id, CancellationToken cancellationToken)</code></td><td>Recibe resources, invoca servicios de aplicación y devuelve resources HTTP.</td></tr>
    <tr><td><code>SubscriptionsController</code></td><td>REST Controller</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Publicar por HTTP las capacidades de Subscription Management.</td><td><code>ISubscriptionCommandService commandService</code><br><code>ISubscriptionQueryService queryService</code><br><code>ISubscriptionPlanQueryService planQueryService</code><br><code>IPaymentCommandService paymentCommandService</code><br><code>IPaymentQueryService paymentQueryService</code><br><code>IConfiguration configuration</code></td><td><code>GetAll(CancellationToken cancellationToken)</code><br><code>GetById(int id, CancellationToken cancellationToken)</code><br><code>Create(CreateSubscriptionResource resource, CancellationToken cancellationToken)</code><br><code>GetActiveByUser(int userId, CancellationToken cancellationToken)</code><br><code>GetPaymentsByUser(int userId, CancellationToken cancellationToken)</code><br><code>MockCheckout(MockCheckoutResource resource, CancellationToken cancellationToken)</code><br><code>CreateStripeCheckout(StripeCheckoutResource resource, CancellationToken cancellationToken)</code><br><code>ConfirmStripeCheckout(string sessionId, CancellationToken cancellationToken)</code><br><code>Update(int id, CreateSubscriptionResource resource, CancellationToken cancellationToken)</code><br><code>Delete(int id, CancellationToken cancellationToken)</code></td><td>Recibe resources, invoca servicios de aplicación y devuelve resources HTTP.</td></tr>
    <tr><td><code>SubscriptionPlanResource</code></td><td>Resource/Assembler</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Definir un contrato estable de entrada o salida para la API REST.</td><td><code>int Id</code><br><code>string Name</code><br><code>decimal Price</code><br><code>string StripePriceId</code><br><code>int MaxAnimals</code><br><code>bool IsActive</code></td><td><code>Create(...)</code><br><code>Deconstruct(...)</code></td><td>Es construido o traducido por assemblers y consumido por el controller y los clientes móviles.</td></tr>
    <tr><td><code>SubscriptionResource</code></td><td>Resource/Assembler</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Definir un contrato estable de entrada o salida para la API REST.</td><td><code>int Id</code><br><code>int UserId</code><br><code>int PlanId</code><br><code>string StripeCustomerId</code><br><code>string StripeSubscriptionId</code><br><code>string Status</code><br><code>DateOnly StartedAt</code><br><code>DateOnly? EndsAt</code></td><td><code>Create(...)</code><br><code>Deconstruct(...)</code></td><td>Es construido o traducido por assemblers y consumido por el controller y los clientes móviles.</td></tr>
    <tr><td><code>PaymentResource</code></td><td>Resource/Assembler</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Definir un contrato estable de entrada o salida para la API REST.</td><td><code>int Id</code><br><code>int UserId</code><br><code>int SubscriptionId</code><br><code>decimal Amount</code><br><code>string Currency</code><br><code>string Provider</code><br><code>string ProviderPaymentId</code><br><code>string Status</code><br><code>DateTime PaidAt</code></td><td><code>Create(...)</code><br><code>Deconstruct(...)</code></td><td>Es construido o traducido por assemblers y consumido por el controller y los clientes móviles.</td></tr>
    <tr><td><code>StripeCheckoutResource</code></td><td>Resource/Assembler</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Definir un contrato estable de entrada o salida para la API REST.</td><td><code>int PlanId</code></td><td><code>Create(...)</code><br><code>Deconstruct(...)</code></td><td>Es construido o traducido por assemblers y consumido por el controller y los clientes móviles.</td></tr>
    <tr><td><code>SubscriptionScreen</code></td><td>Composable</td><td>Android / Jetpack Compose<br><strong>Diseño objetivo</strong></td><td>Presentar consulta de planes, contratación, pago y actualización de suscripciones en Android.</td><td><code>uiState</code><br><code>onAction</code><br><code>navigation</code></td><td><code>Render()</code><br><code>Submit()</code><br><code>Retry()</code></td><td>Observa SubscriptionViewModel y emite acciones de interfaz.</td></tr>
    <tr><td><code>SubscriptionViewModel</code></td><td>Presentation Model</td><td>Android / Kotlin<br><strong>Diseño objetivo</strong></td><td>Mantener el estado observable y traducir acciones de Android a casos de uso.</td><td><code>state</code><br><code>observeUseCase</code><br><code>syncUseCase</code></td><td><code>Load()</code><br><code>Submit(action)</code><br><code>RetrySync()</code></td><td>Invoca casos de uso de Application Layer y publica un UI State inmutable.</td></tr>
    <tr><td><code>SubscriptionPage</code></td><td>Widget</td><td>Flutter / Dart<br><strong>Diseño objetivo</strong></td><td>Presentar consulta de planes, contratación, pago y actualización de suscripciones en Flutter.</td><td><code>state</code><br><code>onAction</code><br><code>router</code></td><td><code>build(context)</code><br><code>submit()</code><br><code>retry()</code></td><td>Observa SubscriptionController y emite intenciones del usuario.</td></tr>
    <tr><td><code>SubscriptionController</code></td><td>State Controller</td><td>Flutter / Dart<br><strong>Diseño objetivo</strong></td><td>Mantener el estado de presentación de Flutter y coordinar casos de uso.</td><td><code>state</code><br><code>observeUseCase</code><br><code>syncUseCase</code></td><td><code>load()</code><br><code>submit(action)</code><br><code>retrySync()</code></td><td>Invoca Application Layer y publica estados de carga, éxito y error.</td></tr>
  </tbody>
</table>

<a id="toc-2-6-8-3-application-layer"></a>

## 2.6.8.3. Application Layer

Esta capa coordina las capacidades de **consulta de planes, contratación, pago y actualización de suscripciones**. Los commands y queries expresan intenciones; los handlers cargan aggregates, aplican reglas, persisten cambios y reaccionan a eventos. Los casos de uso móviles coordinan lectura local, actualización remota y sincronización idempotente.

<table>
  <thead>
    <tr><th>Clase</th><th>Categoría</th><th>Producto y estado</th><th>Propósito</th><th>Atributos</th><th>Métodos u operaciones</th><th>Relaciones</th></tr>
  </thead>
  <tbody>
    <tr><td><code>SubscriptionPlanCommandService</code></td><td>Application Service</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Orquestar consulta de planes, contratación, pago y actualización de suscripciones sin contener reglas del dominio.</td><td><code>ISubscriptionPlanRepository repository</code><br><code>IUnitOfWork unitOfWork</code></td><td><code>Handle(CreateSubscriptionPlanCommand command, CancellationToken cancellationToken)</code><br><code>Handle(UpdateSubscriptionPlanCommand command, CancellationToken cancellationToken)</code><br><code>Handle(DeleteSubscriptionPlanCommand command, CancellationToken cancellationToken)</code></td><td>Invoca agregados y repositories; confirma la transacción mediante Unit of Work.</td></tr>
    <tr><td><code>SubscriptionCommandService</code></td><td>Application Service</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Orquestar consulta de planes, contratación, pago y actualización de suscripciones sin contener reglas del dominio.</td><td><code>ISubscriptionRepository repository</code><br><code>IUnitOfWork unitOfWork</code></td><td><code>Handle(CreateSubscriptionCommand command, CancellationToken cancellationToken)</code><br><code>Handle(UpdateSubscriptionCommand command, CancellationToken cancellationToken)</code><br><code>Handle(DeleteSubscriptionCommand command, CancellationToken cancellationToken)</code></td><td>Invoca agregados y repositories; confirma la transacción mediante Unit of Work.</td></tr>
    <tr><td><code>PaymentCommandService</code></td><td>Application Service</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Orquestar consulta de planes, contratación, pago y actualización de suscripciones sin contener reglas del dominio.</td><td><code>IPaymentRepository repository</code><br><code>IUnitOfWork unitOfWork</code></td><td><code>Handle(CreatePaymentCommand command, CancellationToken cancellationToken)</code></td><td>Invoca agregados y repositories; confirma la transacción mediante Unit of Work.</td></tr>
    <tr><td><code>SubscriptionQueryService</code></td><td>Application Service</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Orquestar consulta de planes, contratación, pago y actualización de suscripciones sin contener reglas del dominio.</td><td><code>ISubscriptionRepository repository</code></td><td><code>Handle(GetSubscriptionByIdQuery query, CancellationToken cancellationToken)</code><br><code>Handle(GetAllSubscriptionsQuery query, CancellationToken cancellationToken)</code></td><td>Invoca agregados y repositories; confirma la transacción mediante Unit of Work.</td></tr>
    <tr><td><code>CreateSubscriptionCommand</code></td><td>Command/Query</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Transportar una intención o consulta tipada hacia su handler.</td><td><code>int UserId</code><br><code>int PlanId</code><br><code>string StripeCustomerId</code><br><code>string StripeSubscriptionId</code><br><code>string Status</code><br><code>DateOnly StartedAt</code><br><code>DateOnly? EndsAt</code></td><td>—</td><td>Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio.</td></tr>
    <tr><td><code>CreatePaymentCommand</code></td><td>Command/Query</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Transportar una intención o consulta tipada hacia su handler.</td><td><code>int UserId</code><br><code>int SubscriptionId</code><br><code>decimal Amount</code><br><code>string Currency</code><br><code>string Provider</code><br><code>string ProviderPaymentId</code><br><code>string Status</code><br><code>DateTime PaidAt</code></td><td>—</td><td>Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio.</td></tr>
    <tr><td><code>GetSubscriptionByIdQuery</code></td><td>Command/Query</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Transportar una intención o consulta tipada hacia su handler.</td><td><code>int Id</code></td><td>—</td><td>Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio.</td></tr>
    <tr><td><code>GetAllSubscriptionPlansQuery</code></td><td>Command/Query</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Transportar una intención o consulta tipada hacia su handler.</td><td><code>filters: optional</code></td><td>—</td><td>Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio.</td></tr>
    <tr><td><code>ObserveSubscriptionUseCase</code></td><td>Use Case</td><td>Android y Flutter<br><strong>Diseño objetivo</strong></td><td>Entregar primero datos locales y actualizar la consulta cuando exista conectividad.</td><td><code>localRepository</code><br><code>remoteRepository</code><br><code>connectivityMonitor</code></td><td><code>Execute(criteria): Stream&lt;Result&gt;</code></td><td>Es invocado por ViewModel/Controller y coordina repositorios móviles.</td></tr>
    <tr><td><code>SyncSubscriptionUseCase</code></td><td>Use Case</td><td>Android y Flutter<br><strong>Diseño objetivo</strong></td><td>Procesar operaciones móviles pendientes de manera idempotente.</td><td><code>outboxRepository</code><br><code>remoteRepository</code><br><code>conflictResolver</code></td><td><code>Execute(): SyncResult</code></td><td>Lee el outbox local, consume la API y actualiza el estado de sincronización.</td></tr>
    <tr><td><code>CreateSubscriptionCommandHandler</code></td><td>Command Handler</td><td>Backend ASP.NET Core<br><strong>Diseño objetivo</strong></td><td>Ejecutar una intención concreta, aplicar reglas del agregado y confirmar la transacción.</td><td><code>repository</code><br><code>unitOfWork</code><br><code>domainPolicy</code></td><td><code>Handle(command): Result</code></td><td>Consume un Command, carga el aggregate mediante su repository y puede publicar un Domain Event.</td></tr>
    <tr><td><code>CreatePaymentCommandHandler</code></td><td>Command Handler</td><td>Backend ASP.NET Core<br><strong>Diseño objetivo</strong></td><td>Ejecutar una intención concreta, aplicar reglas del agregado y confirmar la transacción.</td><td><code>repository</code><br><code>unitOfWork</code><br><code>domainPolicy</code></td><td><code>Handle(command): Result</code></td><td>Consume un Command, carga el aggregate mediante su repository y puede publicar un Domain Event.</td></tr>
    <tr><td><code>PaymentConfirmedEventHandler</code></td><td>Event Handler</td><td>Backend ASP.NET Core<br><strong>Diseño objetivo</strong></td><td>Reaccionar al evento confirmado y actualizar proyecciones o integraciones.</td><td><code>projectionRepository</code><br><code>notificationPort</code><br><code>unitOfWork</code></td><td><code>Handle(domainEvent): Task</code></td><td>Consume un Domain Event y utiliza puertos de infraestructura sin modificar directamente el agregado.</td></tr>
  </tbody>
</table>

<a id="toc-2-6-8-4-infrastructure-layer"></a>

## 2.6.8.4. Infrastructure Layer

Esta capa implementa los puertos definidos hacia el interior de **Subscription Management** y concentra acceso a base de datos, red, almacenamiento local e integraciones externas. Las clases de infraestructura traducen errores y contratos técnicos antes de devolver resultados a Application Layer.

<table>
  <thead>
    <tr><th>Clase</th><th>Categoría</th><th>Producto y estado</th><th>Propósito</th><th>Atributos</th><th>Métodos u operaciones</th><th>Relaciones</th></tr>
  </thead>
  <tbody>
    <tr><td><code>SubscriptionPlanRepository / SubscriptionRepository / PaymentRepository</code></td><td>Repository Adapter</td><td>Backend / Entity Framework Core<br><strong>Implementado en el backend</strong></td><td>Implementar el puerto de persistencia definido por Domain Layer.</td><td><code>SubscriptionPlanRepository: AppDbContext context</code><br><code>SubscriptionRepository: AppDbContext context</code><br><code>PaymentRepository: AppDbContext context</code></td><td><code>PaymentRepository.FindByUserIdAsync(int userId, CancellationToken cancellationToken)</code><br><code>PaymentRepository.FindByProviderPaymentIdAsync(string providerPaymentId, CancellationToken cancellationToken)</code></td><td>Implementa ISubscriptionPlanRepository / ISubscriptionRepository / IPaymentRepository; utiliza AppDbContext/MySQL y reconstruye el aggregate.</td></tr>
    <tr><td><code>ModelBuilderExtensions</code></td><td>Persistence Configuration</td><td>Backend / Entity Framework Core<br><strong>Implementado en el backend</strong></td><td>Mapear entidades y value objects del contexto al modelo relacional.</td><td><code>EntityTypeBuilder configuration</code></td><td><code>ApplyConfiguration(modelBuilder)</code></td><td>Configura tablas, claves, relaciones, restricciones y conversiones de Entity Framework Core.</td></tr>
    <tr><td><code>SubscriptionApiDataSource</code></td><td>Remote Adapter</td><td>Android / Kotlin<br><strong>Diseño objetivo</strong></td><td>Implementar el acceso remoto del cliente móvil a la API.</td><td><code>httpClient</code><br><code>tokenProvider</code><br><code>serializer</code></td><td><code>Get(criteria)</code><br><code>Create(dto)</code><br><code>Update(dto)</code><br><code>Delete(id)</code></td><td>Consume controllers REST por HTTPS/JSON y traduce errores HTTP al modelo de aplicación.</td></tr>
    <tr><td><code>SubscriptionDao</code></td><td>Room Adapter</td><td>Android / Room<br><strong>Diseño objetivo</strong></td><td>Implementar persistencia local y observación reactiva en Android.</td><td><code>roomDatabase</code><br><code>entityMapper</code></td><td><code>Observe(criteria)</code><br><code>Upsert(entity)</code><br><code>Delete(id)</code><br><code>Pending()</code></td><td>Implementa el puerto local mediante Room y participa en la estrategia de caché/outbox.</td></tr>
    <tr><td><code>SubscriptionRemoteDataSource</code></td><td>Remote Adapter</td><td>Flutter / Dart<br><strong>Diseño objetivo</strong></td><td>Implementar el acceso remoto del cliente móvil a la API.</td><td><code>httpClient</code><br><code>tokenProvider</code><br><code>serializer</code></td><td><code>Get(criteria)</code><br><code>Create(dto)</code><br><code>Update(dto)</code><br><code>Delete(id)</code></td><td>Consume controllers REST por HTTPS/JSON y traduce errores HTTP al modelo de aplicación.</td></tr>
    <tr><td><code>SubscriptionLocalDataSource</code></td><td>SQLite Adapter</td><td>Flutter / Dart<br><strong>Diseño objetivo</strong></td><td>Implementar persistencia local equivalente en Flutter.</td><td><code>sqliteDatabase</code><br><code>entityMapper</code></td><td><code>watch(criteria)</code><br><code>upsert(entity)</code><br><code>delete(id)</code><br><code>pending()</code></td><td>Implementa el puerto local mediante SQLite y participa en la estrategia de caché/outbox.</td></tr>
    <tr><td><code>IamSubscriberAdapter</code></td><td>Context Adapter</td><td>Backend ASP.NET Core<br><strong>Diseño objetivo</strong></td><td>Aislar una dependencia externa detrás de un puerto explícito.</td><td><code>iamFacade</code></td><td><code>Exists(userId): bool</code><br><code>GetEmail(userId): string</code></td><td>Implementa el puerto de suscriptor y consume IAM.</td></tr>
    <tr><td><code>StripePaymentGateway</code></td><td>Anti-Corruption Layer</td><td>Backend ASP.NET Core<br><strong>Diseño objetivo</strong></td><td>Aislar una dependencia externa detrás de un puerto explícito.</td><td><code>stripeClient, webhookSecret</code></td><td><code>CreateCheckout(command)</code><br><code>ConfirmWebhook(payload)</code><br><code>Refund(paymentId)</code></td><td>Implementa PaymentGateway y traduce Stripe al lenguaje del dominio.</td></tr>
    <tr><td><code>SubscriptionCacheStore</code></td><td>Local Cache Adapter</td><td>Android y Flutter<br><strong>Diseño objetivo</strong></td><td>Aislar una dependencia externa detrás de un puerto explícito.</td><td><code>subscriptionDao</code></td><td><code>ReadActive(userId)</code><br><code>Save(subscription)</code><br><code>Invalidate()</code></td><td>Implementa el puerto local de consulta mediante Room o SQLite.</td></tr>
  </tbody>
</table>

<a id="toc-2-6-8-5-bounded-context-software-architecture-component-level-diagrams"></a>

## 2.6.8.5. Bounded Context Software Architecture Component Level Diagrams

El archivo [`component-level.dsl`](<../../assets/codefordiagrams/2.6.8. Bounded Context Subscription Management/component-level.dsl>) contiene las vistas `BC8-ApiComponents`, `BC8-AndroidComponents` y `BC8-FlutterComponents`. Las tres parten del mismo modelo C4 y muestran la separación entre presentación, aplicación, dominio y adaptadores.

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-8-Bounded-Context-Subscription-Management/2-6-8-BC8-ApiComponents.svg" alt="Componentes API de Subscription Management" width="900">
  <p><i>Figura 2.6.8.1. Componentes de la API para Subscription Management. Fuente: elaboración propia con Structurizr DSL.</i></p>
</div>

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-8-Bounded-Context-Subscription-Management/2-6-8-BC8-AndroidComponents.svg" alt="Componentes Android de Subscription Management" width="900">
  <p><i>Figura 2.6.8.2. Componentes Android para Subscription Management. Fuente: elaboración propia con Structurizr DSL.</i></p>
</div>

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-8-Bounded-Context-Subscription-Management/2-6-8-BC8-FlutterComponents.svg" alt="Componentes Flutter de Subscription Management" width="900">
  <p><i>Figura 2.6.8.3. Componentes Flutter para Subscription Management. Fuente: elaboración propia con Structurizr DSL.</i></p>
</div>

<a id="toc-2-6-8-6-bounded-context-software-architecture-code-level-diagrams"></a>

## 2.6.8.6. Bounded Context Software Architecture Code Level Diagrams

Los diagramas de código detallan el modelo del dominio y los objetos de persistencia. El UML diferencia los elementos existentes de las incorporaciones objetivo, mientras los esquemas SQL señalan mediante comentarios las columnas propuestas. Los archivos ERD quedan disponibles para completar la importación manual.

<a id="toc-2-6-8-6-1-bounded-context-domain-layer-class-diagrams"></a>

### 2.6.8.6.1. Bounded Context Domain Layer Class Diagrams

El Class Diagram incluye agregados, entidades, value objects, enumeraciones, servicios de dominio e interfaces de repositorio con atributos, operaciones, visibilidad y multiplicidades.

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-8-Bounded-Context-Subscription-Management/2-6-8-domain-layer-class-diagram.svg" alt="Class Diagram de Subscription Management" width="900">
  <p><i>Figura 2.6.8.4. Domain Layer Class Diagram de Subscription Management. Fuente: elaboración propia con PlantUML.</i></p>
</div>

<a id="toc-2-6-8-6-2-bounded-context-database-design-diagram"></a>

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

