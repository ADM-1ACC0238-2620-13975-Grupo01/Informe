<a id="toc-2-6-1-bounded-context-identity-and-access-management"></a>

# 2.6.1. Bounded Context: Identity and Access Management

Administrar identidades, credenciales, roles y sesiones para que cada operación de AniTec se ejecute con una identidad autenticada y autorizada.

La base implementada se encuentra en el módulo `Iam` de la API ASP.NET Core. El diseño móvil de Android y Flutter se presenta como **diseño objetivo** porque esos clientes todavía no existen en el workspace. Los tres productos comparten contratos REST y lenguaje ubicuo, mientras la API conserva las reglas autoritativas.

<a id="toc-2-6-1-1-domain-layer"></a>

## 2.6.1.1. Domain Layer

**Responsabilidad estable.** Esta capa documenta el modelo que representa el núcleo de **Identity and Access Management**. Las reglas autoritativas se ejecutan en la API; Android y Flutter mantienen modelos equivalentes para presentación, validación inmediata y trabajo offline. La columna de estado distingue el código heredado de la arquitectura objetivo.

**Detalle técnico evolutivo.** El siguiente diccionario identifica las clases, sus responsabilidades, atributos, métodos y relaciones. Los campos **Producto** y **Estado** distinguen los elementos comprobados en el código de aquellos que aún pertenecen al diseño objetivo.

### Aggregate Root: User

| Campo | Detalle |
|---|---|
| **Producto** | Backend; modelo equivalente en Android y Flutter |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Mantener identidad, credenciales protegidas y rol del usuario. |
| **Relaciones** | User se relaciona con UserRole : has; AuthenticatedSession se relaciona con User : belongs to; CredentialPolicy depende de User : validates; IUserRepository depende de User : persists |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `id` | `int` |
| `username` | `string` |
| `passwordHash` | `string` |
| `fullName` | `string` |
| `role` | `UserRole` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `UpdateUsername(username: string)` | `User` |
| `UpdatePasswordHash(hash: string)` | `User` |
| `UpdateProfile(fullName: string, role: UserRole)` | `User` |

---

### Enumeration: UserRole

| Campo | Detalle |
|---|---|
| **Producto** | Backend, Android y Flutter (modelo canónico) |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Definir los valores válidos de UserRole. |
| **Relaciones** | User se relaciona con UserRole : has |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `Rancher` | `No especificado` |
| `Veterinarian` | `No especificado` |
| `Administrator` | `No especificado` |

**Métodos u operaciones**

No aplica.

---

### Entity: AuthenticatedSession

| Campo | Detalle |
|---|---|
| **Producto** | Backend, Android y Flutter (modelo canónico) |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Controlar vigencia y revocación de una sesión autenticada. |
| **Relaciones** | AuthenticatedSession se relaciona con User : belongs to |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `userId` | `int` |
| `tokenReference` | `string` |
| `expiresAt` | `DateTime` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `IsExpired(now: DateTime)` | `bool` |
| `Revoke()` | `void` |

---

### Domain Service: CredentialPolicy

| Campo | Detalle |
|---|---|
| **Producto** | Backend, Android y Flutter (modelo canónico) |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Validar reglas de nombre de usuario y contraseña. |
| **Relaciones** | CredentialPolicy depende de User : validates |

**Atributos o dependencias**

No aplica.

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `ValidateUsername(username: string)` | `bool` |
| `ValidatePassword(password: string)` | `bool` |

---

### Repository Interface: IUserRepository

| Campo | Detalle |
|---|---|
| **Producto** | Backend; modelo equivalente en Android y Flutter |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Abstraer la persistencia de User. |
| **Relaciones** | IUserRepository depende de User : persists |

**Atributos o dependencias**

No aplica.

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `FindById(id: int)` | `User?` |
| `FindByUsername(username: string)` | `User?` |
| `Add(user: User)` | `void` |

---

### Enumeration: IamError

| Campo | Detalle |
|---|---|
| **Producto** | Backend; modelo equivalente en Android y Flutter |
| **Estado** | **Implementado** |
| **Propósito** | Código controlado para errores de autenticación y autorización. |
| **Relaciones** | Es traducido a respuestas HTTP por Interface Layer. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `None` | `No especificado` |
| `UserNotFound` | `No especificado` |
| `UsernameAlreadyTaken` | `No especificado` |
| `InvalidCredentials` | `No especificado` |
| `InvalidRole` | `No especificado` |
| `OperationCancelled` | `No especificado` |
| `DatabaseError` | `No especificado` |
| `InternalServerError` | `No especificado` |
| `ExternalServiceError` | `No especificado` |

**Métodos u operaciones**

No aplica.

---

<a id="toc-2-6-1-2-interface-layer"></a>

## 2.6.1.2. Interface Layer

**Responsabilidad estable.** Esta capa recibe las acciones relacionadas con **registro de cuentas, autenticación, consulta de identidad y control de sesión** y las traduce a casos de uso. Los controllers y resources corresponden a la API; las pantallas y controladores de estado representan la presentación objetivo en Android y Flutter. Ninguna de estas clases implementa reglas de negocio.

**Detalle técnico evolutivo.** El siguiente diccionario identifica las clases, sus responsabilidades, atributos, métodos y relaciones. Los campos **Producto** y **Estado** distinguen los elementos comprobados en el código de aquellos que aún pertenecen al diseño objetivo.

### REST Controller: AuthenticationController

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Publicar por HTTP las capacidades de Identity and Access Management. |
| **Relaciones** | Recibe resources, invoca servicios de aplicación y devuelve resources HTTP. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `userCommandService` | `IUserCommandService` |
| `errorLocalizer` | `IStringLocalizer<ErrorMessages>` |
| `iamLocalizer` | `IStringLocalizer<IamMessages>` |
| `problemDetailsFactory` | `ProblemDetailsFactory` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `SignIn(SignInResource signInResource, CancellationToken cancellationToken)` | `No especificado` |
| `SignUp(SignUpResource signUpResource, CancellationToken cancellationToken)` | `No especificado` |

---

### REST Controller: UsersController

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Publicar por HTTP las capacidades de Identity and Access Management. |
| **Relaciones** | Recibe resources, invoca servicios de aplicación y devuelve resources HTTP. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `userQueryService` | `IUserQueryService` |
| `errorLocalizer` | `IStringLocalizer<ErrorMessages>` |
| `problemDetailsFactory` | `ProblemDetailsFactory` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `GetUserById(int id, CancellationToken cancellationToken)` | `No especificado` |
| `GetAllUsers(CancellationToken cancellationToken)` | `No especificado` |

---

### Resource/Assembler: SignInResource

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Definir un contrato estable de entrada o salida para la API REST. |
| **Relaciones** | Es construido o traducido por assemblers y consumido por el controller y los clientes móviles. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `Username` | `string` |
| `Password` | `string` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Create(...)` | `No especificado` |
| `Deconstruct(...)` | `No especificado` |

---

### Resource/Assembler: SignUpResource

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Definir un contrato estable de entrada o salida para la API REST. |
| **Relaciones** | Es construido o traducido por assemblers y consumido por el controller y los clientes móviles. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `Username` | `string` |
| `Password` | `string` |
| `string FullName = ""` | `No especificado` |
| `string Role = "Rancher"` | `No especificado` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Create(...)` | `No especificado` |
| `Deconstruct(...)` | `No especificado` |

---

### Resource/Assembler: AuthenticatedUserResource

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
| `Username` | `string` |
| `FullName` | `string` |
| `Role` | `string` |
| `Token` | `string` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Create(...)` | `No especificado` |
| `Deconstruct(...)` | `No especificado` |

---

### Resource/Assembler: UserResource

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
| `Username` | `string` |
| `FullName` | `string` |
| `Role` | `string` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Create(...)` | `No especificado` |
| `Deconstruct(...)` | `No especificado` |

---

### Composable: UserScreen

| Campo | Detalle |
|---|---|
| **Producto** | Android / Jetpack Compose |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Presentar registro de cuentas, autenticación, consulta de identidad y control de sesión en Android. |
| **Relaciones** | Observa UserViewModel y emite acciones de interfaz. |

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

### Presentation Model: UserViewModel

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

### Widget: UserPage

| Campo | Detalle |
|---|---|
| **Producto** | Flutter / Dart |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Presentar registro de cuentas, autenticación, consulta de identidad y control de sesión en Flutter. |
| **Relaciones** | Observa UserController y emite intenciones del usuario. |

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

### State Controller: UserController

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

<a id="toc-2-6-1-3-application-layer"></a>

## 2.6.1.3. Application Layer

**Responsabilidad estable.** Esta capa coordina las capacidades de **registro de cuentas, autenticación, consulta de identidad y control de sesión**. Los commands y queries expresan intenciones; los handlers cargan aggregates, aplican reglas, persisten cambios y reaccionan a eventos. Los casos de uso móviles coordinan lectura local, actualización remota y sincronización idempotente.

**Detalle técnico evolutivo.** El siguiente diccionario identifica las clases, sus responsabilidades, atributos, métodos y relaciones. Los campos **Producto** y **Estado** distinguen los elementos comprobados en el código de aquellos que aún pertenecen al diseño objetivo.

### Application Service: UserCommandService

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Orquestar registro de cuentas, autenticación, consulta de identidad y control de sesión sin contener reglas del dominio. |
| **Relaciones** | Invoca agregados y repositories; confirma la transacción mediante Unit of Work. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `userRepository` | `IUserRepository` |
| `tokenService` | `ITokenService` |
| `hashingService` | `IHashingService` |
| `unitOfWork` | `IUnitOfWork` |
| `localizer` | `IStringLocalizer<ErrorMessages>` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Handle(SignInCommand command, CancellationToken cancellationToken)` | `No especificado` |
| `Handle(SignUpCommand command, CancellationToken cancellationToken)` | `No especificado` |

---

### Application Service: UserQueryService

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Orquestar registro de cuentas, autenticación, consulta de identidad y control de sesión sin contener reglas del dominio. |
| **Relaciones** | Invoca agregados y repositories; confirma la transacción mediante Unit of Work. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `userRepository` | `IUserRepository` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Handle(GetUserByIdQuery query, CancellationToken cancellationToken)` | `No especificado` |
| `Handle(GetAllUsersQuery query, CancellationToken cancellationToken)` | `No especificado` |
| `Handle(GetUserByUsernameQuery query, CancellationToken cancellationToken)` | `No especificado` |

---

### Application Service: IamContextFacade

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Orquestar registro de cuentas, autenticación, consulta de identidad y control de sesión sin contener reglas del dominio. |
| **Relaciones** | Invoca agregados y repositories; confirma la transacción mediante Unit of Work. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `userCommandService` | `IUserCommandService` |
| `userQueryService` | `IUserQueryService` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `CreateUser(string username, string password, CancellationToken cancellationToken)` | `No especificado` |
| `FetchUserIdByUsername(string username, CancellationToken cancellationToken)` | `No especificado` |
| `FetchUsernameByUserId(int userId, CancellationToken cancellationToken)` | `No especificado` |

---

### Command/Query: SignInCommand

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Transportar una intención o consulta tipada hacia su handler. |
| **Relaciones** | Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `Username` | `string` |
| `Password` | `string` |

**Métodos u operaciones**

No aplica.

---

### Command/Query: SignUpCommand

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Transportar una intención o consulta tipada hacia su handler. |
| **Relaciones** | Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `Username` | `string` |
| `Password` | `string` |
| `FullName` | `string` |
| `Role` | `string` |

**Métodos u operaciones**

No aplica.

---

### Command/Query: GetUserByIdQuery

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

### Command/Query: GetUserByUsernameQuery

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Transportar una intención o consulta tipada hacia su handler. |
| **Relaciones** | Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `Username` | `string` |

**Métodos u operaciones**

No aplica.

---

### Use Case: ObserveUserUseCase

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

### Use Case: SyncUserUseCase

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

### Command Handler: SignUpCommandHandler

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

### Command Handler: SignInCommandHandler

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

### Event Handler: UserAuthenticatedEventHandler

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

<a id="toc-2-6-1-4-infrastructure-layer"></a>

## 2.6.1.4. Infrastructure Layer

**Responsabilidad estable.** Esta capa implementa los puertos definidos hacia el interior de **Identity and Access Management** y concentra acceso a base de datos, red, almacenamiento local e integraciones externas. Las clases de infraestructura traducen errores y contratos técnicos antes de devolver resultados a Application Layer.

**Detalle técnico evolutivo.** El siguiente diccionario identifica las clases, sus responsabilidades, atributos, métodos y relaciones. Los campos **Producto** y **Estado** distinguen los elementos comprobados en el código de aquellos que aún pertenecen al diseño objetivo.

### Repository Adapter: UserRepository

| Campo | Detalle |
|---|---|
| **Producto** | Backend / Entity Framework Core |
| **Estado** | **Implementado en el backend** |
| **Propósito** | Implementar el puerto de persistencia definido por Domain Layer. |
| **Relaciones** | Implementa IUserRepository; utiliza AppDbContext/MySQL y reconstruye el aggregate. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `context` | `AppDbContext` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `FindByUsernameAsync(string username, CancellationToken cancellationToken)` | `No especificado` |
| `ExistsByUsernameAsync(string username, CancellationToken cancellationToken)` | `No especificado` |

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

### Remote Adapter: UserApiDataSource

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

### Room Adapter: UserDao

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

### Remote Adapter: UserRemoteDataSource

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

### SQLite Adapter: UserLocalDataSource

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

### Security Adapter: HashingService

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado** |
| **Propósito** | Aislar una dependencia externa detrás de un puerto explícito. |
| **Relaciones** | Implementa el puerto de hashing y utiliza BCrypt. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `passwordHash` | `password,` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `HashPassword(password)` | `string` |
| `VerifyPassword(password, passwordHash)` | `bool` |

---

### Token Adapter: TokenService

| Campo | Detalle |
|---|---|
| **Producto** | Backend ASP.NET Core |
| **Estado** | **Implementado** |
| **Propósito** | Aislar una dependencia externa detrás de un puerto explícito. |
| **Relaciones** | Implementa el puerto de tokens y utiliza JWT. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `expiration` | `issuer, audience, signingKey,` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `GenerateToken(user)` | `string` |
| `ValidateToken(token)` | `Task<int?>` |

---

### Secure Storage Adapter: SecureSessionStore

| Campo | Detalle |
|---|---|
| **Producto** | Android y Flutter |
| **Estado** | **Diseño objetivo** |
| **Propósito** | Aislar una dependencia externa detrás de un puerto explícito. |
| **Relaciones** | Implementa el puerto local de sesión sobre Keystore/EncryptedSharedPreferences o Secure Storage. |

**Atributos o dependencias**

| Nombre | Tipo |
|---|---|
| `expiresAt` | `tokenReference,` |

**Métodos u operaciones**

| Firma | Retorno |
|---|---|
| `Save(session)` | `No especificado` |
| `Read()` | `No especificado` |
| `Clear()` | `No especificado` |

---

<a id="toc-2-6-1-5-bounded-context-software-architecture-component-level-diagrams"></a>

## 2.6.1.5. Bounded Context Software Architecture Component Level Diagrams

El archivo [`component-level.dsl`](<../../assets/codefordiagrams/2.6.1. Bounded Context Identity and Access Management/component-level.dsl>) contiene las vistas `BC1-ApiComponents`, `BC1-AndroidComponents` y `BC1-FlutterComponents`. Las tres parten del mismo modelo C4 y muestran la separación entre presentación, aplicación, dominio y adaptadores.

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-1-Bounded-Context-Identity-and-Access-Management/2-6-1-BC1-ApiComponents.svg" alt="Componentes API de Identity and Access Management" width="900">
  <p><i>Figura 2.6.1.1. Componentes de la API para Identity and Access Management. Fuente: elaboración propia con Structurizr DSL.</i></p>
</div>

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-1-Bounded-Context-Identity-and-Access-Management/2-6-1-BC1-AndroidComponents.svg" alt="Componentes Android de Identity and Access Management" width="900">
  <p><i>Figura 2.6.1.2. Componentes Android para Identity and Access Management. Fuente: elaboración propia con Structurizr DSL.</i></p>
</div>

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-1-Bounded-Context-Identity-and-Access-Management/2-6-1-BC1-FlutterComponents.svg" alt="Componentes Flutter de Identity and Access Management" width="900">
  <p><i>Figura 2.6.1.3. Componentes Flutter para Identity and Access Management. Fuente: elaboración propia con Structurizr DSL.</i></p>
</div>

<a id="toc-2-6-1-6-bounded-context-software-architecture-code-level-diagrams"></a>

## 2.6.1.6. Bounded Context Software Architecture Code Level Diagrams

Los diagramas de código detallan el modelo del dominio y los objetos de persistencia. El UML diferencia los elementos existentes de las incorporaciones objetivo, mientras los esquemas SQL señalan mediante comentarios las columnas propuestas. Los archivos ERD quedan disponibles para completar la importación manual.

<a id="toc-2-6-1-6-1-bounded-context-domain-layer-class-diagrams"></a>

### 2.6.1.6.1. Bounded Context Domain Layer Class Diagrams

El Class Diagram incluye agregados, entidades, value objects, enumeraciones, servicios de dominio e interfaces de repositorio con atributos, operaciones, visibilidad y multiplicidades.

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-1-Bounded-Context-Identity-and-Access-Management/2-6-1-domain-layer-class-diagram.svg" alt="Class Diagram de Identity and Access Management" width="900">
  <p><i>Figura 2.6.1.4. Domain Layer Class Diagram de Identity and Access Management. Fuente: elaboración propia con PlantUML.</i></p>
</div>

<a id="toc-2-6-1-6-2-bounded-context-database-design-diagram"></a>

### 2.6.1.6.2. Bounded Context Database Design Diagram

MySQL mantiene la persistencia autoritativa. Room y SQLite contienen únicamente caché, metadatos de sincronización y operaciones pendientes; no sustituyen las reglas ni la fuente de verdad del backend. En IAM, las credenciales y tokens permanecen fuera de las tablas locales y se almacenan mediante mecanismos seguros del sistema operativo.

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-1-Bounded-Context-Identity-and-Access-Management/2-6-1-mysql-database-design.png" alt="MySQL Database Diagram de Identity and Access Management" width="900">
  <p><i>Figura 2.6.1.5. MySQL Database Design de Identity and Access Management. Fuente: elaboración propia a partir del esquema SQL.</i></p>
</div>

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-1-Bounded-Context-Identity-and-Access-Management/2-6-1-android-room-database-design.png" alt="Room Database Diagram de Identity and Access Management" width="900">
  <p><i>Figura 2.6.1.6. Android Room Database Design de Identity and Access Management. Fuente: elaboración propia a partir del esquema SQL.</i></p>
</div>

