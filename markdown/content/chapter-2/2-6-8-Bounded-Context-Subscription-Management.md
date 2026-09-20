<a id="toc-2-6-8-bounded-context-subscription-management"></a>

# 2.6.8. Bounded Context: Subscription Management

Administrar planes, vigencia de suscripciones y pagos confirmados sin introducir conceptos propios de Stripe en el dominio.

La base implementada se encuentra en el módulo `Subscriptions` de la API ASP.NET Core. El diseño móvil de Android y Flutter se presenta como **diseño objetivo** porque esos clientes todavía no existen en el workspace. Los tres productos comparten contratos REST y lenguaje ubicuo, mientras la API conserva las reglas autoritativas.

<a id="toc-2-6-8-1-domain-layer"></a>

## 2.6.8.1. Domain Layer

**Responsabilidad estable.** Esta capa documenta el modelo que representa el núcleo de **Subscription Management**. Las reglas autoritativas se ejecutan en la API; Android y Flutter mantienen modelos equivalentes para presentación, validación inmediata y trabajo offline. La columna de estado distingue el código heredado de la arquitectura objetivo.

**Detalle técnico evolutivo.** El siguiente diccionario identifica las clases, sus responsabilidades, atributos, métodos y relaciones. Los campos **Producto** y **Estado** distinguen los elementos comprobados en el código de aquellos que aún pertenecen al diseño objetivo.

### Entity: SubscriptionPlan

| Campo | Detalle |
|---|---|
| **Producto** | Backend; modelo equivalente en Android y Flutter |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Definir condiciones y límites de un plan comercial. |
| **Relaciones** | SubscriptionPlan compone Money |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `id` | `int` |
| `name` | `string` |
| `price` | `Money` |
| `providerPriceId` | `string` |
| `maxAnimals` | `int` |
| `isActive` | `bool` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Deactivate()` | `void` |
| `ChangePrice(price: Money)` | `void` |

---

### Aggregate Root: Subscription

| Campo | Detalle |
|---|---|
| **Producto** | Backend; modelo equivalente en Android y Flutter |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Controlar vigencia y estado de la suscripción de un usuario. |
| **Relaciones** | Subscription compone Payment; Subscription se relaciona con SubscriptionStatus; ISubscriptionRepository depende de Subscription |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `id` | `int` |
| `userId` | `int` |
| `planId` | `int` |
| `status` | `SubscriptionStatus` |
| `startedAt` | `Date` |
| `endsAt` | `Date?` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Activate(start: Date, end: Date?)` | `void` |
| `Cancel(end: Date)` | `void` |
| `IsActive(on: Date)` | `bool` |

---

### Entity: Payment

| Campo | Detalle |
|---|---|
| **Producto** | Backend; modelo equivalente en Android y Flutter |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Registrar el resultado de un pago. |
| **Relaciones** | Subscription compone Payment; Payment se relaciona con PaymentStatus; Payment compone Money |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `id` | `int` |
| `subscriptionId` | `int` |
| `userId` | `int` |
| `amount` | `Money` |
| `providerPaymentId` | `string` |
| `status` | `PaymentStatus` |
| `paidAt` | `DateTime` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Confirm(providerId: string, paidAt: DateTime)` | `void` |
| `Reject()` | `void` |

---

### Value Object: Money

| Campo | Detalle |
|---|---|
| **Producto** | Backend, Android y Flutter (modelo canónico) |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Representar un importe junto con su moneda. |
| **Relaciones** | Payment compone Money; SubscriptionPlan compone Money |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `amount` | `decimal` |
| `currency` | `string` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `IsPositive()` | `bool` |

---

### Enumeration: SubscriptionStatus

| Campo | Detalle |
|---|---|
| **Producto** | Backend, Android y Flutter (modelo canónico) |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Definir los valores válidos de SubscriptionStatus. |
| **Relaciones** | Subscription se relaciona con SubscriptionStatus |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `Pending` | `No especificado` |
| `Active` | `No especificado` |
| `Cancelled` | `No especificado` |
| `Expired` | `No especificado` |

**Métodos u operaciones**

No aplica.

---

### Enumeration: PaymentStatus

| Campo | Detalle |
|---|---|
| **Producto** | Backend, Android y Flutter (modelo canónico) |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Definir los valores válidos de PaymentStatus. |
| **Relaciones** | Payment se relaciona con PaymentStatus |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `Pending` | `No especificado` |
| `Paid` | `No especificado` |
| `Failed` | `No especificado` |

**Métodos u operaciones**

No aplica.

---

### Repository Interface: ISubscriptionRepository

| Campo | Detalle |
|---|---|
| **Producto** | Backend; modelo equivalente en Android y Flutter |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Abstraer la persistencia de Subscription. |
| **Relaciones** | ISubscriptionRepository depende de Subscription |

**Atributos o dependencias**

No aplica.

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `FindById(id: int)` | `Subscription?` |
| `FindActiveByUser(userId: int)` | `Subscription?` |
| `Add(subscription: Subscription)` | `void` |
| `Update(subscription: Subscription)` | `void` |

---

### Repository Interface: ISubscriptionPlanRepository

| Campo | Detalle |
|---|---|
| **Producto** | Backend; modelo equivalente en Android y Flutter |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Abstraer la persistencia de planes de suscripción. |
| **Relaciones** | Persiste SubscriptionPlan y es implementado por SubscriptionPlanRepository. |

**Atributos o dependencias**

No aplica.

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `FindByIdAsync(id)` | `No especificado` |
| `ListAsync()` | `No especificado` |
| `AddAsync(plan)` | `No especificado` |
| `Update(plan)` | `No especificado` |

---

### Repository Interface: IPaymentRepository

| Campo | Detalle |
|---|---|
| **Producto** | Backend; modelo equivalente en Android y Flutter |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Abstraer la persistencia y consulta de pagos. |
| **Relaciones** | Persiste Payment y es implementado por PaymentRepository. |

**Atributos o dependencias**

No aplica.

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `FindByUserIdAsync(userId)` | `No especificado` |
| `FindByProviderPaymentIdAsync(providerPaymentId)` | `No especificado` |
| `AddAsync(payment)` | `No especificado` |

---

### Domain Port: PaymentGateway

| Campo | Detalle |
|---|---|
| **Producto** | Backend; modelo equivalente en Android y Flutter |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Abstraer el proveedor externo de cobros. |
| **Relaciones** | Es implementado por StripePaymentGateway en Infrastructure Layer. |

**Atributos o dependencias**

No aplica.

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `CreateCheckout(subscription, plan)` | `No especificado` |
| `ConfirmPayment(reference)` | `No especificado` |

---

<a id="toc-2-6-8-2-interface-layer"></a>

## 2.6.8.2. Interface Layer

**Responsabilidad estable.** Esta capa recibe las acciones relacionadas con **consulta de planes, contratación, pago y actualización de suscripciones** y las traduce a casos de uso. Los controllers y resources corresponden a la API; las pantallas y controladores de estado representan la presentación objetivo en Android y Flutter. Ninguna de estas clases implementa reglas de negocio.

**Detalle técnico evolutivo.** El siguiente diccionario identifica las clases, sus responsabilidades, atributos, métodos y relaciones. Los campos **Producto** y **Estado** distinguen los elementos comprobados en el código de aquellos que aún pertenecen al diseño objetivo.

### REST Controller: SubscriptionPlansController

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Publicar por HTTP las capacidades de Subscription Management. |
| **Relaciones** | Recibe resources, invoca servicios de aplicación y devuelve resources HTTP. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `commandService` | `ISubscriptionPlanCommandService` |
| `queryService` | `ISubscriptionPlanQueryService` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `GetAll(CancellationToken cancellationToken)` | `No especificado` |
| `GetById(int id, CancellationToken cancellationToken)` | `No especificado` |
| `Create(CreateSubscriptionPlanResource resource, CancellationToken cancellationToken)` | `No especificado` |
| `Update(int id, CreateSubscriptionPlanResource resource, CancellationToken cancellationToken)` | `No especificado` |
| `Delete(int id, CancellationToken cancellationToken)` | `No especificado` |

---

### REST Controller: SubscriptionsController

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Publicar por HTTP las capacidades de Subscription Management. |
| **Relaciones** | Recibe resources, invoca servicios de aplicación y devuelve resources HTTP. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `commandService` | `ISubscriptionCommandService` |
| `queryService` | `ISubscriptionQueryService` |
| `planQueryService` | `ISubscriptionPlanQueryService` |
| `paymentCommandService` | `IPaymentCommandService` |
| `paymentQueryService` | `IPaymentQueryService` |
| `configuration` | `IConfiguration` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `GetAll(CancellationToken cancellationToken)` | `No especificado` |
| `GetById(int id, CancellationToken cancellationToken)` | `No especificado` |
| `Create(CreateSubscriptionResource resource, CancellationToken cancellationToken)` | `No especificado` |
| `GetActiveByUser(int userId, CancellationToken cancellationToken)` | `No especificado` |
| `GetPaymentsByUser(int userId, CancellationToken cancellationToken)` | `No especificado` |
| `MockCheckout(MockCheckoutResource resource, CancellationToken cancellationToken)` | `No especificado` |
| `CreateStripeCheckout(StripeCheckoutResource resource, CancellationToken cancellationToken)` | `No especificado` |
| `ConfirmStripeCheckout(string sessionId, CancellationToken cancellationToken)` | `No especificado` |
| `Update(int id, CreateSubscriptionResource resource, CancellationToken cancellationToken)` | `No especificado` |
| `Delete(int id, CancellationToken cancellationToken)` | `No especificado` |

---

### Resource/Assembler: SubscriptionPlanResource

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
| `Price` | `decimal` |
| `StripePriceId` | `string` |
| `MaxAnimals` | `int` |
| `IsActive` | `bool` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Create(...)` | `No especificado` |
| `Deconstruct(...)` | `No especificado` |

---

### Resource/Assembler: SubscriptionResource

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
| `UserId` | `int` |
| `PlanId` | `int` |
| `StripeCustomerId` | `string` |
| `StripeSubscriptionId` | `string` |
| `Status` | `string` |
| `StartedAt` | `DateOnly` |
| `EndsAt` | `DateOnly?` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Create(...)` | `No especificado` |
| `Deconstruct(...)` | `No especificado` |

---

### Resource/Assembler: PaymentResource

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
| `UserId` | `int` |
| `SubscriptionId` | `int` |
| `Amount` | `decimal` |
| `Currency` | `string` |
| `Provider` | `string` |
| `ProviderPaymentId` | `string` |
| `Status` | `string` |
| `PaidAt` | `DateTime` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Create(...)` | `No especificado` |
| `Deconstruct(...)` | `No especificado` |

---

### Resource/Assembler: StripeCheckoutResource

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Definir un contrato estable de entrada o salida para la API REST. |
| **Relaciones** | Es construido o traducido por assemblers y consumido por el controller y los clientes móviles. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `PlanId` | `int` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Create(...)` | `No especificado` |
| `Deconstruct(...)` | `No especificado` |

---

### Composable: SubscriptionScreen

| Campo | Detalle |
|---|---|
| **Producto** | Android / Jetpack Compose |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Presentar consulta de planes, contratación, pago y actualización de suscripciones en Android. |
| **Relaciones** | Observa SubscriptionViewModel y emite acciones de interfaz. |

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

### Presentation Model: SubscriptionViewModel

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

### Widget: SubscriptionPage

| Campo | Detalle |
|---|---|
| **Producto** | Flutter / Dart |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Presentar consulta de planes, contratación, pago y actualización de suscripciones en Flutter. |
| **Relaciones** | Observa SubscriptionController y emite intenciones del usuario. |

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

### State Controller: SubscriptionController

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

<a id="toc-2-6-8-3-application-layer"></a>

## 2.6.8.3. Application Layer

**Responsabilidad estable.** Esta capa coordina las capacidades de **consulta de planes, contratación, pago y actualización de suscripciones**. Los commands y queries expresan intenciones; los handlers cargan aggregates, aplican reglas, persisten cambios y reaccionan a eventos. Los casos de uso móviles coordinan lectura local, actualización remota y sincronización idempotente.

**Detalle técnico evolutivo.** El siguiente diccionario identifica las clases, sus responsabilidades, atributos, métodos y relaciones. Los campos **Producto** y **Estado** distinguen los elementos comprobados en el código de aquellos que aún pertenecen al diseño objetivo.

### Application Service: SubscriptionPlanCommandService

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Orquestar consulta de planes, contratación, pago y actualización de suscripciones sin contener reglas del dominio. |
| **Relaciones** | Invoca agregados y repositories; confirma la transacción mediante Unit of Work. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `repository` | `ISubscriptionPlanRepository` |
| `unitOfWork` | `IUnitOfWork` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Handle(CreateSubscriptionPlanCommand command, CancellationToken cancellationToken)` | `No especificado` |
| `Handle(UpdateSubscriptionPlanCommand command, CancellationToken cancellationToken)` | `No especificado` |
| `Handle(DeleteSubscriptionPlanCommand command, CancellationToken cancellationToken)` | `No especificado` |

---

### Application Service: SubscriptionCommandService

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Orquestar consulta de planes, contratación, pago y actualización de suscripciones sin contener reglas del dominio. |
| **Relaciones** | Invoca agregados y repositories; confirma la transacción mediante Unit of Work. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `repository` | `ISubscriptionRepository` |
| `unitOfWork` | `IUnitOfWork` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Handle(CreateSubscriptionCommand command, CancellationToken cancellationToken)` | `No especificado` |
| `Handle(UpdateSubscriptionCommand command, CancellationToken cancellationToken)` | `No especificado` |
| `Handle(DeleteSubscriptionCommand command, CancellationToken cancellationToken)` | `No especificado` |

---

### Application Service: PaymentCommandService

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Orquestar consulta de planes, contratación, pago y actualización de suscripciones sin contener reglas del dominio. |
| **Relaciones** | Invoca agregados y repositories; confirma la transacción mediante Unit of Work. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `repository` | `IPaymentRepository` |
| `unitOfWork` | `IUnitOfWork` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Handle(CreatePaymentCommand command, CancellationToken cancellationToken)` | `No especificado` |

---

### Application Service: SubscriptionQueryService

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Orquestar consulta de planes, contratación, pago y actualización de suscripciones sin contener reglas del dominio. |
| **Relaciones** | Invoca agregados y repositories; confirma la transacción mediante Unit of Work. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `repository` | `ISubscriptionRepository` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Handle(GetSubscriptionByIdQuery query, CancellationToken cancellationToken)` | `No especificado` |
| `Handle(GetAllSubscriptionsQuery query, CancellationToken cancellationToken)` | `No especificado` |

---

### Command/Query: CreateSubscriptionCommand

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Transportar una intención o consulta tipada hacia su handler. |
| **Relaciones** | Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `UserId` | `int` |
| `PlanId` | `int` |
| `StripeCustomerId` | `string` |
| `StripeSubscriptionId` | `string` |
| `Status` | `string` |
| `StartedAt` | `DateOnly` |
| `EndsAt` | `DateOnly?` |

**Métodos u operaciones**

No aplica.

---

### Command/Query: CreatePaymentCommand

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Transportar una intención o consulta tipada hacia su handler. |
| **Relaciones** | Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `UserId` | `int` |
| `SubscriptionId` | `int` |
| `Amount` | `decimal` |
| `Currency` | `string` |
| `Provider` | `string` |
| `ProviderPaymentId` | `string` |
| `Status` | `string` |
| `PaidAt` | `DateTime` |

**Métodos u operaciones**

No aplica.

---

### Command/Query: GetSubscriptionByIdQuery

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

### Command/Query: GetAllSubscriptionPlansQuery

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Transportar una intención o consulta tipada hacia su handler. |
| **Relaciones** | Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `filters` | `optional` |

**Métodos u operaciones**

No aplica.

---

### Use Case: ObserveSubscriptionUseCase

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

### Use Case: SyncSubscriptionUseCase

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

### Command Handler: CreateSubscriptionCommandHandler

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

### Command Handler: CreatePaymentCommandHandler

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

### Event Handler: PaymentConfirmedEventHandler

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

<a id="toc-2-6-8-4-infrastructure-layer"></a>

## 2.6.8.4. Infrastructure Layer

**Responsabilidad estable.** Esta capa implementa los puertos definidos hacia el interior de **Subscription Management** y concentra acceso a base de datos, red, almacenamiento local e integraciones externas. Las clases de infraestructura traducen errores y contratos técnicos antes de devolver resultados a Application Layer.

**Detalle técnico evolutivo.** El siguiente diccionario identifica las clases, sus responsabilidades, atributos, métodos y relaciones. Los campos **Producto** y **Estado** distinguen los elementos comprobados en el código de aquellos que aún pertenecen al diseño objetivo.

### Repository Adapter: SubscriptionPlanRepository / SubscriptionRepository / PaymentRepository

| Campo | Detalle |
|---|---|
| **Producto** | Backend / Entity Framework Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Implementar el puerto de persistencia definido por Domain Layer. |
| **Relaciones** | Implementa ISubscriptionPlanRepository / ISubscriptionRepository / IPaymentRepository; utiliza AppDbContext/MySQL y reconstruye el aggregate. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `SubscriptionPlanRepository` | `AppDbContext context` |
| `SubscriptionRepository` | `AppDbContext context` |
| `PaymentRepository` | `AppDbContext context` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `PaymentRepository.FindByUserIdAsync(int userId, CancellationToken cancellationToken)` | `No especificado` |
| `PaymentRepository.FindByProviderPaymentIdAsync(string providerPaymentId, CancellationToken cancellationToken)` | `No especificado` |

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

### Remote Adapter: SubscriptionApiDataSource

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

### Room Adapter: SubscriptionDao

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

### Remote Adapter: SubscriptionRemoteDataSource

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

### SQLite Adapter: SubscriptionLocalDataSource

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

### Context Adapter: IamSubscriberAdapter

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Aislar una dependencia externa detrás de un puerto explícito. |
| **Relaciones** | Implementa el puerto de suscriptor y consume IAM. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `iamFacade` | `No especificado` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Exists(userId)` | `bool` |
| `GetEmail(userId)` | `string` |

---

### Anti-Corruption Layer: StripePaymentGateway

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Aislar una dependencia externa detrás de un puerto explícito. |
| **Relaciones** | Implementa PaymentGateway y traduce Stripe al lenguaje del dominio. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `webhookSecret` | `stripeClient,` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `CreateCheckout(command)` | `No especificado` |
| `ConfirmWebhook(payload)` | `No especificado` |
| `Refund(paymentId)` | `No especificado` |

---

### Local Cache Adapter: SubscriptionCacheStore

| Campo | Detalle |
|---|---|
| **Producto** | Android y Flutter |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Aislar una dependencia externa detrás de un puerto explícito. |
| **Relaciones** | Implementa el puerto local de consulta mediante Room o SQLite. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `subscriptionDao` | `No especificado` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `ReadActive(userId)` | `No especificado` |
| `Save(subscription)` | `No especificado` |
| `Invalidate()` | `No especificado` |

---

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

