<a id="toc-2-6-1-bounded-context-identity-and-access-management"></a>

# 2.6.1. Bounded Context: Identity and Access Management

Administrar identidades, credenciales, roles y sesiones para que cada operación de AniTec se ejecute con una identidad autenticada y autorizada.

La base implementada se encuentra en el módulo `Iam` de la API ASP.NET Core. El diseño móvil de Android y Flutter se presenta como **diseño objetivo** porque esos clientes todavía no existen en el workspace. Los tres productos comparten contratos REST y lenguaje ubicuo, mientras la API conserva las reglas autoritativas.

<a id="toc-2-6-1-1-domain-layer"></a>

## 2.6.1.1. Domain Layer

**Responsabilidad estable.** Esta capa documenta el modelo que representa el núcleo de **Identity and Access Management**. Las reglas autoritativas se ejecutan en la API; Android y Flutter mantienen modelos equivalentes para presentación, validación inmediata y trabajo offline. La columna de estado distingue el código heredado de la arquitectura objetivo.

**Detalle técnico evolutivo.** El siguiente diccionario identifica las clases, sus responsabilidades, atributos, métodos y relaciones. La columna **Producto y estado** distingue los elementos comprobados en el código de aquellos que aún pertenecen al diseño objetivo.

<table>
  <thead>
    <tr><th>Clase</th><th>Categoría</th><th>Producto y estado</th><th>Propósito</th><th>Atributos</th><th>Métodos u operaciones</th><th>Relaciones</th></tr>
  </thead>
  <tbody>
    <tr><td><code>User</code></td><td>Aggregate Root</td><td>Backend; modelo equivalente en Android y Flutter<br><strong>Implementado en el backend</strong></td><td>Mantener identidad, credenciales protegidas y rol del usuario.</td><td><code>id: int</code><br><code>username: string</code><br><code>passwordHash: string</code><br><code>fullName: string</code><br><code>role: UserRole</code></td><td><code>UpdateUsername(username: string): User</code><br><code>UpdatePasswordHash(hash: string): User</code><br><code>UpdateProfile(fullName: string, role: UserRole): User</code></td><td>User se relaciona con UserRole : has; AuthenticatedSession se relaciona con User : belongs to; CredentialPolicy depende de User : validates; IUserRepository depende de User : persists</td></tr>
    <tr><td><code>UserRole</code></td><td>Enumeration</td><td>Backend, Android y Flutter (modelo canónico)<br><strong>Diseño objetivo</strong></td><td>Definir los valores válidos de UserRole.</td><td><code>Rancher</code><br><code>Veterinarian</code><br><code>Administrator</code></td><td>—</td><td>User se relaciona con UserRole : has</td></tr>
    <tr><td><code>AuthenticatedSession</code></td><td>Entity</td><td>Backend, Android y Flutter (modelo canónico)<br><strong>Diseño objetivo</strong></td><td>Controlar vigencia y revocación de una sesión autenticada.</td><td><code>userId: int</code><br><code>tokenReference: string</code><br><code>expiresAt: DateTime</code></td><td><code>IsExpired(now: DateTime): bool</code><br><code>Revoke(): void</code></td><td>AuthenticatedSession se relaciona con User : belongs to</td></tr>
    <tr><td><code>CredentialPolicy</code></td><td>Domain Service</td><td>Backend, Android y Flutter (modelo canónico)<br><strong>Diseño objetivo</strong></td><td>Validar reglas de nombre de usuario y contraseña.</td><td>—</td><td><code>ValidateUsername(username: string): bool</code><br><code>ValidatePassword(password: string): bool</code></td><td>CredentialPolicy depende de User : validates</td></tr>
    <tr><td><code>IUserRepository</code></td><td>Repository Interface</td><td>Backend; modelo equivalente en Android y Flutter<br><strong>Implementado en el backend</strong></td><td>Abstraer la persistencia de User.</td><td>—</td><td><code>FindById(id: int): User?</code><br><code>FindByUsername(username: string): User?</code><br><code>Add(user: User): void</code></td><td>IUserRepository depende de User : persists</td></tr>
    <tr><td><code>IamError</code></td><td>Enumeration</td><td>Backend; modelo equivalente en Android y Flutter<br><strong>Implementado</strong></td><td>Código controlado para errores de autenticación y autorización.</td><td><code>None</code><br><code>UserNotFound</code><br><code>UsernameAlreadyTaken</code><br><code>InvalidCredentials</code><br><code>InvalidRole</code><br><code>OperationCancelled</code><br><code>DatabaseError</code><br><code>InternalServerError</code><br><code>ExternalServiceError</code></td><td>—</td><td>Es traducido a respuestas HTTP por Interface Layer.</td></tr>
  </tbody>
</table>

<a id="toc-2-6-1-2-interface-layer"></a>

## 2.6.1.2. Interface Layer

**Responsabilidad estable.** Esta capa recibe las acciones relacionadas con **registro de cuentas, autenticación, consulta de identidad y control de sesión** y las traduce a casos de uso. Los controllers y resources corresponden a la API; las pantallas y controladores de estado representan la presentación objetivo en Android y Flutter. Ninguna de estas clases implementa reglas de negocio.

**Detalle técnico evolutivo.** El siguiente diccionario identifica las clases, sus responsabilidades, atributos, métodos y relaciones. La columna **Producto y estado** distingue los elementos comprobados en el código de aquellos que aún pertenecen al diseño objetivo.

<table>
  <thead>
    <tr><th>Clase</th><th>Categoría</th><th>Producto y estado</th><th>Propósito</th><th>Atributos</th><th>Métodos u operaciones</th><th>Relaciones</th></tr>
  </thead>
  <tbody>
    <tr><td><code>AuthenticationController</code></td><td>REST Controller</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Publicar por HTTP las capacidades de Identity and Access Management.</td><td><code>IUserCommandService userCommandService</code><br><code>IStringLocalizer&lt;ErrorMessages&gt; errorLocalizer</code><br><code>IStringLocalizer&lt;IamMessages&gt; iamLocalizer</code><br><code>ProblemDetailsFactory problemDetailsFactory</code></td><td><code>SignIn(SignInResource signInResource, CancellationToken cancellationToken)</code><br><code>SignUp(SignUpResource signUpResource, CancellationToken cancellationToken)</code></td><td>Recibe resources, invoca servicios de aplicación y devuelve resources HTTP.</td></tr>
    <tr><td><code>UsersController</code></td><td>REST Controller</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Publicar por HTTP las capacidades de Identity and Access Management.</td><td><code>IUserQueryService userQueryService</code><br><code>IStringLocalizer&lt;ErrorMessages&gt; errorLocalizer</code><br><code>ProblemDetailsFactory problemDetailsFactory</code></td><td><code>GetUserById(int id, CancellationToken cancellationToken)</code><br><code>GetAllUsers(CancellationToken cancellationToken)</code></td><td>Recibe resources, invoca servicios de aplicación y devuelve resources HTTP.</td></tr>
    <tr><td><code>SignInResource</code></td><td>Resource/Assembler</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Definir un contrato estable de entrada o salida para la API REST.</td><td><code>string Username</code><br><code>string Password</code></td><td><code>Create(...)</code><br><code>Deconstruct(...)</code></td><td>Es construido o traducido por assemblers y consumido por el controller y los clientes móviles.</td></tr>
    <tr><td><code>SignUpResource</code></td><td>Resource/Assembler</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Definir un contrato estable de entrada o salida para la API REST.</td><td><code>string Username</code><br><code>string Password</code><br><code>string FullName = ""</code><br><code>string Role = "Rancher"</code></td><td><code>Create(...)</code><br><code>Deconstruct(...)</code></td><td>Es construido o traducido por assemblers y consumido por el controller y los clientes móviles.</td></tr>
    <tr><td><code>AuthenticatedUserResource</code></td><td>Resource/Assembler</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Definir un contrato estable de entrada o salida para la API REST.</td><td><code>int Id</code><br><code>string Username</code><br><code>string FullName</code><br><code>string Role</code><br><code>string Token</code></td><td><code>Create(...)</code><br><code>Deconstruct(...)</code></td><td>Es construido o traducido por assemblers y consumido por el controller y los clientes móviles.</td></tr>
    <tr><td><code>UserResource</code></td><td>Resource/Assembler</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Definir un contrato estable de entrada o salida para la API REST.</td><td><code>int Id</code><br><code>string Username</code><br><code>string FullName</code><br><code>string Role</code></td><td><code>Create(...)</code><br><code>Deconstruct(...)</code></td><td>Es construido o traducido por assemblers y consumido por el controller y los clientes móviles.</td></tr>
    <tr><td><code>UserScreen</code></td><td>Composable</td><td>Android / Jetpack Compose<br><strong>Diseño objetivo</strong></td><td>Presentar registro de cuentas, autenticación, consulta de identidad y control de sesión en Android.</td><td><code>uiState</code><br><code>onAction</code><br><code>navigation</code></td><td><code>Render()</code><br><code>Submit()</code><br><code>Retry()</code></td><td>Observa UserViewModel y emite acciones de interfaz.</td></tr>
    <tr><td><code>UserViewModel</code></td><td>Presentation Model</td><td>Android / Kotlin<br><strong>Diseño objetivo</strong></td><td>Mantener el estado observable y traducir acciones de Android a casos de uso.</td><td><code>state</code><br><code>observeUseCase</code><br><code>syncUseCase</code></td><td><code>Load()</code><br><code>Submit(action)</code><br><code>RetrySync()</code></td><td>Invoca casos de uso de Application Layer y publica un UI State inmutable.</td></tr>
    <tr><td><code>UserPage</code></td><td>Widget</td><td>Flutter / Dart<br><strong>Diseño objetivo</strong></td><td>Presentar registro de cuentas, autenticación, consulta de identidad y control de sesión en Flutter.</td><td><code>state</code><br><code>onAction</code><br><code>router</code></td><td><code>build(context)</code><br><code>submit()</code><br><code>retry()</code></td><td>Observa UserController y emite intenciones del usuario.</td></tr>
    <tr><td><code>UserController</code></td><td>State Controller</td><td>Flutter / Dart<br><strong>Diseño objetivo</strong></td><td>Mantener el estado de presentación de Flutter y coordinar casos de uso.</td><td><code>state</code><br><code>observeUseCase</code><br><code>syncUseCase</code></td><td><code>load()</code><br><code>submit(action)</code><br><code>retrySync()</code></td><td>Invoca Application Layer y publica estados de carga, éxito y error.</td></tr>
  </tbody>
</table>

<a id="toc-2-6-1-3-application-layer"></a>

## 2.6.1.3. Application Layer

**Responsabilidad estable.** Esta capa coordina las capacidades de **registro de cuentas, autenticación, consulta de identidad y control de sesión**. Los commands y queries expresan intenciones; los handlers cargan aggregates, aplican reglas, persisten cambios y reaccionan a eventos. Los casos de uso móviles coordinan lectura local, actualización remota y sincronización idempotente.

**Detalle técnico evolutivo.** El siguiente diccionario identifica las clases, sus responsabilidades, atributos, métodos y relaciones. La columna **Producto y estado** distingue los elementos comprobados en el código de aquellos que aún pertenecen al diseño objetivo.

<table>
  <thead>
    <tr><th>Clase</th><th>Categoría</th><th>Producto y estado</th><th>Propósito</th><th>Atributos</th><th>Métodos u operaciones</th><th>Relaciones</th></tr>
  </thead>
  <tbody>
    <tr><td><code>UserCommandService</code></td><td>Application Service</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Orquestar registro de cuentas, autenticación, consulta de identidad y control de sesión sin contener reglas del dominio.</td><td><code>IUserRepository userRepository</code><br><code>ITokenService tokenService</code><br><code>IHashingService hashingService</code><br><code>IUnitOfWork unitOfWork</code><br><code>IStringLocalizer&lt;ErrorMessages&gt; localizer</code></td><td><code>Handle(SignInCommand command, CancellationToken cancellationToken)</code><br><code>Handle(SignUpCommand command, CancellationToken cancellationToken)</code></td><td>Invoca agregados y repositories; confirma la transacción mediante Unit of Work.</td></tr>
    <tr><td><code>UserQueryService</code></td><td>Application Service</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Orquestar registro de cuentas, autenticación, consulta de identidad y control de sesión sin contener reglas del dominio.</td><td><code>IUserRepository userRepository</code></td><td><code>Handle(GetUserByIdQuery query, CancellationToken cancellationToken)</code><br><code>Handle(GetAllUsersQuery query, CancellationToken cancellationToken)</code><br><code>Handle(GetUserByUsernameQuery query, CancellationToken cancellationToken)</code></td><td>Invoca agregados y repositories; confirma la transacción mediante Unit of Work.</td></tr>
    <tr><td><code>IamContextFacade</code></td><td>Application Service</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Orquestar registro de cuentas, autenticación, consulta de identidad y control de sesión sin contener reglas del dominio.</td><td><code>IUserCommandService userCommandService</code><br><code>IUserQueryService userQueryService</code></td><td><code>CreateUser(string username, string password, CancellationToken cancellationToken)</code><br><code>FetchUserIdByUsername(string username, CancellationToken cancellationToken)</code><br><code>FetchUsernameByUserId(int userId, CancellationToken cancellationToken)</code></td><td>Invoca agregados y repositories; confirma la transacción mediante Unit of Work.</td></tr>
    <tr><td><code>SignInCommand</code></td><td>Command/Query</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Transportar una intención o consulta tipada hacia su handler.</td><td><code>string Username</code><br><code>string Password</code></td><td>—</td><td>Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio.</td></tr>
    <tr><td><code>SignUpCommand</code></td><td>Command/Query</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Transportar una intención o consulta tipada hacia su handler.</td><td><code>string Username</code><br><code>string Password</code><br><code>string FullName</code><br><code>string Role</code></td><td>—</td><td>Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio.</td></tr>
    <tr><td><code>GetUserByIdQuery</code></td><td>Command/Query</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Transportar una intención o consulta tipada hacia su handler.</td><td><code>int Id</code></td><td>—</td><td>Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio.</td></tr>
    <tr><td><code>GetUserByUsernameQuery</code></td><td>Command/Query</td><td>Backend ASP.NET Core<br><strong>Implementado en el backend</strong></td><td>Transportar una intención o consulta tipada hacia su handler.</td><td><code>string Username</code></td><td>—</td><td>Es recibida por un handler o servicio de aplicación y no contiene lógica de negocio.</td></tr>
    <tr><td><code>ObserveUserUseCase</code></td><td>Use Case</td><td>Android y Flutter<br><strong>Diseño objetivo</strong></td><td>Entregar primero datos locales y actualizar la consulta cuando exista conectividad.</td><td><code>localRepository</code><br><code>remoteRepository</code><br><code>connectivityMonitor</code></td><td><code>Execute(criteria): Stream&lt;Result&gt;</code></td><td>Es invocado por ViewModel/Controller y coordina repositorios móviles.</td></tr>
    <tr><td><code>SyncUserUseCase</code></td><td>Use Case</td><td>Android y Flutter<br><strong>Diseño objetivo</strong></td><td>Procesar operaciones móviles pendientes de manera idempotente.</td><td><code>outboxRepository</code><br><code>remoteRepository</code><br><code>conflictResolver</code></td><td><code>Execute(): SyncResult</code></td><td>Lee el outbox local, consume la API y actualiza el estado de sincronización.</td></tr>
    <tr><td><code>SignUpCommandHandler</code></td><td>Command Handler</td><td>Backend ASP.NET Core<br><strong>Diseño objetivo</strong></td><td>Ejecutar una intención concreta, aplicar reglas del agregado y confirmar la transacción.</td><td><code>repository</code><br><code>unitOfWork</code><br><code>domainPolicy</code></td><td><code>Handle(command): Result</code></td><td>Consume un Command, carga el aggregate mediante su repository y puede publicar un Domain Event.</td></tr>
    <tr><td><code>SignInCommandHandler</code></td><td>Command Handler</td><td>Backend ASP.NET Core<br><strong>Diseño objetivo</strong></td><td>Ejecutar una intención concreta, aplicar reglas del agregado y confirmar la transacción.</td><td><code>repository</code><br><code>unitOfWork</code><br><code>domainPolicy</code></td><td><code>Handle(command): Result</code></td><td>Consume un Command, carga el aggregate mediante su repository y puede publicar un Domain Event.</td></tr>
    <tr><td><code>UserAuthenticatedEventHandler</code></td><td>Event Handler</td><td>Backend ASP.NET Core<br><strong>Diseño objetivo</strong></td><td>Reaccionar al evento confirmado y actualizar proyecciones o integraciones.</td><td><code>projectionRepository</code><br><code>notificationPort</code><br><code>unitOfWork</code></td><td><code>Handle(domainEvent): Task</code></td><td>Consume un Domain Event y utiliza puertos de infraestructura sin modificar directamente el agregado.</td></tr>
  </tbody>
</table>

<a id="toc-2-6-1-4-infrastructure-layer"></a>

## 2.6.1.4. Infrastructure Layer

**Responsabilidad estable.** Esta capa implementa los puertos definidos hacia el interior de **Identity and Access Management** y concentra acceso a base de datos, red, almacenamiento local e integraciones externas. Las clases de infraestructura traducen errores y contratos técnicos antes de devolver resultados a Application Layer.

**Detalle técnico evolutivo.** El siguiente diccionario identifica las clases, sus responsabilidades, atributos, métodos y relaciones. La columna **Producto y estado** distingue los elementos comprobados en el código de aquellos que aún pertenecen al diseño objetivo.

<table>
  <thead>
    <tr><th>Clase</th><th>Categoría</th><th>Producto y estado</th><th>Propósito</th><th>Atributos</th><th>Métodos u operaciones</th><th>Relaciones</th></tr>
  </thead>
  <tbody>
    <tr><td><code>UserRepository</code></td><td>Repository Adapter</td><td>Backend / Entity Framework Core<br><strong>Implementado en el backend</strong></td><td>Implementar el puerto de persistencia definido por Domain Layer.</td><td><code>AppDbContext context</code></td><td><code>FindByUsernameAsync(string username, CancellationToken cancellationToken)</code><br><code>ExistsByUsernameAsync(string username, CancellationToken cancellationToken)</code></td><td>Implementa IUserRepository; utiliza AppDbContext/MySQL y reconstruye el aggregate.</td></tr>
    <tr><td><code>ModelBuilderExtensions</code></td><td>Persistence Configuration</td><td>Backend / Entity Framework Core<br><strong>Implementado en el backend</strong></td><td>Mapear entidades y value objects del contexto al modelo relacional.</td><td><code>EntityTypeBuilder configuration</code></td><td><code>ApplyConfiguration(modelBuilder)</code></td><td>Configura tablas, claves, relaciones, restricciones y conversiones de Entity Framework Core.</td></tr>
    <tr><td><code>UserApiDataSource</code></td><td>Remote Adapter</td><td>Android / Kotlin<br><strong>Diseño objetivo</strong></td><td>Implementar el acceso remoto del cliente móvil a la API.</td><td><code>httpClient</code><br><code>tokenProvider</code><br><code>serializer</code></td><td><code>Get(criteria)</code><br><code>Create(dto)</code><br><code>Update(dto)</code><br><code>Delete(id)</code></td><td>Consume controllers REST por HTTPS/JSON y traduce errores HTTP al modelo de aplicación.</td></tr>
    <tr><td><code>UserDao</code></td><td>Room Adapter</td><td>Android / Room<br><strong>Diseño objetivo</strong></td><td>Implementar persistencia local y observación reactiva en Android.</td><td><code>roomDatabase</code><br><code>entityMapper</code></td><td><code>Observe(criteria)</code><br><code>Upsert(entity)</code><br><code>Delete(id)</code><br><code>Pending()</code></td><td>Implementa el puerto local mediante Room y participa en la estrategia de caché/outbox.</td></tr>
    <tr><td><code>UserRemoteDataSource</code></td><td>Remote Adapter</td><td>Flutter / Dart<br><strong>Diseño objetivo</strong></td><td>Implementar el acceso remoto del cliente móvil a la API.</td><td><code>httpClient</code><br><code>tokenProvider</code><br><code>serializer</code></td><td><code>Get(criteria)</code><br><code>Create(dto)</code><br><code>Update(dto)</code><br><code>Delete(id)</code></td><td>Consume controllers REST por HTTPS/JSON y traduce errores HTTP al modelo de aplicación.</td></tr>
    <tr><td><code>UserLocalDataSource</code></td><td>SQLite Adapter</td><td>Flutter / Dart<br><strong>Diseño objetivo</strong></td><td>Implementar persistencia local equivalente en Flutter.</td><td><code>sqliteDatabase</code><br><code>entityMapper</code></td><td><code>watch(criteria)</code><br><code>upsert(entity)</code><br><code>delete(id)</code><br><code>pending()</code></td><td>Implementa el puerto local mediante SQLite y participa en la estrategia de caché/outbox.</td></tr>
    <tr><td><code>HashingService</code></td><td>Security Adapter</td><td>Backend ASP.NET Core<br><strong>Implementado</strong></td><td>Aislar una dependencia externa detrás de un puerto explícito.</td><td><code>password, passwordHash</code></td><td><code>HashPassword(password): string</code><br><code>VerifyPassword(password, passwordHash): bool</code></td><td>Implementa el puerto de hashing y utiliza BCrypt.</td></tr>
    <tr><td><code>TokenService</code></td><td>Token Adapter</td><td>Backend ASP.NET Core<br><strong>Implementado</strong></td><td>Aislar una dependencia externa detrás de un puerto explícito.</td><td><code>issuer, audience, signingKey, expiration</code></td><td><code>GenerateToken(user): string</code><br><code>ValidateToken(token): Task&lt;int?&gt;</code></td><td>Implementa el puerto de tokens y utiliza JWT.</td></tr>
    <tr><td><code>SecureSessionStore</code></td><td>Secure Storage Adapter</td><td>Android y Flutter<br><strong>Diseño objetivo</strong></td><td>Aislar una dependencia externa detrás de un puerto explícito.</td><td><code>tokenReference, expiresAt</code></td><td><code>Save(session)</code><br><code>Read()</code><br><code>Clear()</code></td><td>Implementa el puerto local de sesión sobre Keystore/EncryptedSharedPreferences o Secure Storage.</td></tr>
  </tbody>
</table>

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

