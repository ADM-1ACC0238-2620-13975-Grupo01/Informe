<a id="toc-2-6-2-bounded-context-profile-management"></a>

# 2.6.2. Bounded Context: Profile Management

Mantener la información personal y de contacto asociada con una identidad sin mezclarla con credenciales o reglas de autenticación.

La base implementada se encuentra en el módulo `Profiles` de la API ASP.NET Core. El diseño móvil de Android y Flutter se presenta como **diseño objetivo** porque esos clientes todavía no existen en el workspace. Los tres productos comparten contratos REST y lenguaje ubicuo, mientras la API conserva las reglas autoritativas.

<a id="toc-2-6-2-1-domain-layer"></a>

## 2.6.2.1. Domain Layer

Esta capa representa el núcleo de Profile Management. Los elementos existentes se conservarán como punto de partida; los elementos objetivo completan las invariantes identificadas en EventStorming y en el Bounded Context Canvas.

<table>
  <thead>
    <tr><th>Clase o componente</th><th>Tipo</th><th>Producto</th><th>Propósito</th><th>Responsabilidades</th></tr>
  </thead>
  <tbody>
    <tr><td>Profile</td><td>Clase de dominio existente</td><td>Backend / módulo Profiles</td><td>Representar Profile dentro de Profile Management.</td><td>Conservar las invariantes actualmente implementadas y servir como evidencia trazable.</td></tr>
    <tr><td>PersonName</td><td>Clase de dominio existente</td><td>Backend / módulo Profiles</td><td>Representar PersonName dentro de Profile Management.</td><td>Conservar las invariantes actualmente implementadas y servir como evidencia trazable.</td></tr>
    <tr><td>EmailAddress</td><td>Clase de dominio existente</td><td>Backend / módulo Profiles</td><td>Representar EmailAddress dentro de Profile Management.</td><td>Conservar las invariantes actualmente implementadas y servir como evidencia trazable.</td></tr>
    <tr><td>StreetAddress</td><td>Clase de dominio existente</td><td>Backend / módulo Profiles</td><td>Representar StreetAddress dentro de Profile Management.</td><td>Conservar las invariantes actualmente implementadas y servir como evidencia trazable.</td></tr>
    <tr><td>IProfileRepository</td><td>Repository Interface existente</td><td>Backend / módulo Profiles</td><td>Representar IProfileRepository dentro de Profile Management.</td><td>Conservar las invariantes actualmente implementadas y servir como evidencia trazable.</td></tr>
    <tr><td>ProfileOwnerId</td><td>Diseño objetivo</td><td>Modelo canónico compartido</td><td>Completar el lenguaje ubicuo de Profile Management.</td><td>Expresar reglas o conceptos requeridos por el alcance móvil que aún no están implementados en el backend heredado.</td></tr>
    <tr><td>ProfileUpdated</td><td>Diseño objetivo</td><td>Modelo canónico compartido</td><td>Completar el lenguaje ubicuo de Profile Management.</td><td>Expresar reglas o conceptos requeridos por el alcance móvil que aún no están implementados en el backend heredado.</td></tr>
  </tbody>
</table>

<a id="toc-2-6-2-2-interface-layer"></a>

## 2.6.2.2. Interface Layer

La Interface Layer traduce acciones de usuarios y contratos externos. En el backend utiliza controllers, resources y assemblers; en los clientes móviles utiliza pantallas y controladores de estado específicos de cada plataforma.

<table>
  <thead>
    <tr><th>Clase o componente</th><th>Tipo</th><th>Producto</th><th>Propósito</th><th>Responsabilidades</th></tr>
  </thead>
  <tbody>
    <tr><td>ProfilesController</td><td>REST Controller existente</td><td>Backend ASP.NET Core</td><td>Exponer creación, consulta y actualización del perfil.</td><td>Validar el contrato HTTP, traducir resources y delegar el caso de uso.</td></tr>
    <tr><td>CreateProfileResource</td><td>Resource/Assembler existente</td><td>Backend ASP.NET Core</td><td>Definir el contrato público de entrada o salida.</td><td>Evitar exponer directamente entidades del dominio.</td></tr>
    <tr><td>ProfileResource</td><td>Resource/Assembler existente</td><td>Backend ASP.NET Core</td><td>Definir el contrato público de entrada o salida.</td><td>Evitar exponer directamente entidades del dominio.</td></tr>
    <tr><td>ProfileScreen</td><td>Composable objetivo</td><td>Android / Jetpack Compose</td><td>Presentar creación, consulta y actualización del perfil.</td><td>Renderizar estado, recibir acciones y mostrar errores recuperables.</td></tr>
    <tr><td>ProfileViewModel</td><td>Presentation Model objetivo</td><td>Android / Kotlin</td><td>Coordinar el estado observable de la pantalla.</td><td>Invocar casos de uso y convertir resultados en UI state.</td></tr>
    <tr><td>ProfilePage</td><td>Widget objetivo</td><td>Flutter / Dart</td><td>Presentar creación, consulta y actualización del perfil.</td><td>Renderizar estado y enviar intenciones del usuario.</td></tr>
    <tr><td>ProfileController</td><td>State Controller objetivo</td><td>Flutter / Dart</td><td>Coordinar el estado de presentación.</td><td>Invocar casos de uso y publicar estados de carga, éxito y error.</td></tr>
  </tbody>
</table>

<a id="toc-2-6-2-3-application-layer"></a>

## 2.6.2.3. Application Layer

La Application Layer orquesta comandos, consultas y sincronización. Los casos de uso móviles consultan primero el read model local, solicitan actualización remota cuando existe conectividad y procesan operaciones pendientes mediante un outbox idempotente.

<table>
  <thead>
    <tr><th>Clase o componente</th><th>Tipo</th><th>Producto</th><th>Propósito</th><th>Responsabilidades</th></tr>
  </thead>
  <tbody>
    <tr><td>ProfileCommandService</td><td>Application Service existente</td><td>Backend ASP.NET Core</td><td>Orquestar creación, consulta y actualización del perfil.</td><td>Coordinar repositorios, reglas del dominio y Unit of Work.</td></tr>
    <tr><td>ProfileQueryService</td><td>Application Service existente</td><td>Backend ASP.NET Core</td><td>Orquestar creación, consulta y actualización del perfil.</td><td>Coordinar repositorios, reglas del dominio y Unit of Work.</td></tr>
    <tr><td>ProfilesContextFacade</td><td>Application Service existente</td><td>Backend ASP.NET Core</td><td>Orquestar creación, consulta y actualización del perfil.</td><td>Coordinar repositorios, reglas del dominio y Unit of Work.</td></tr>
    <tr><td>CreateProfileCommand</td><td>Command/Query existente</td><td>Backend ASP.NET Core</td><td>Representar una intención o consulta explícita.</td><td>Transportar datos tipados hacia el servicio de aplicación correspondiente.</td></tr>
    <tr><td>GetProfileByIdQuery</td><td>Command/Query existente</td><td>Backend ASP.NET Core</td><td>Representar una intención o consulta explícita.</td><td>Transportar datos tipados hacia el servicio de aplicación correspondiente.</td></tr>
    <tr><td>GetProfileByEmailQuery</td><td>Command/Query existente</td><td>Backend ASP.NET Core</td><td>Representar una intención o consulta explícita.</td><td>Transportar datos tipados hacia el servicio de aplicación correspondiente.</td></tr>
    <tr><td>ProfileCommandHandler</td><td>Command Handler objetivo</td><td>Backend ASP.NET Core</td><td>Ejecutar comandos mediante una unidad de aplicación explícita.</td><td>Cargar el agregado, aplicar sus reglas, persistirlo y publicar el resultado.</td></tr>
    <tr><td>ProfileEventHandler</td><td>Event Handler objetivo</td><td>Backend ASP.NET Core</td><td>Reaccionar a cambios confirmados en el contexto.</td><td>Actualizar proyecciones o solicitar integraciones sin acoplarlas al agregado.</td></tr>
    <tr><td>ObserveProfileUseCase</td><td>Use Case objetivo</td><td>Android y Flutter</td><td>Consultar el read model local y actualizar la UI.</td><td>Combinar caché local con actualización remota.</td></tr>
    <tr><td>SyncProfileUseCase</td><td>Use Case objetivo</td><td>Android y Flutter</td><td>Sincronizar cambios pendientes.</td><td>Procesar el outbox de forma idempotente y resolver resultados del servidor.</td></tr>
  </tbody>
</table>

<a id="toc-2-6-2-4-infrastructure-layer"></a>

## 2.6.2.4. Infrastructure Layer

La Infrastructure Layer conecta el dominio con IAM Context Facade y almacenamiento local de perfiles. Los adapters implementan interfaces definidas hacia el interior y traducen errores técnicos a resultados comprendidos por los casos de uso.

<table>
  <thead>
    <tr><th>Clase o componente</th><th>Tipo</th><th>Producto</th><th>Propósito</th><th>Responsabilidades</th></tr>
  </thead>
  <tbody>
    <tr><td>ProfileRepository</td><td>Repository Adapter existente</td><td>Backend / Entity Framework Core</td><td>Implementar los puertos de persistencia del dominio.</td><td>Consultar y guardar las entidades mediante AppDbContext y MySQL.</td></tr>
    <tr><td>ModelBuilderExtensions</td><td>Persistence Configuration existente</td><td>Backend / Entity Framework Core</td><td>Configurar tablas, columnas, constraints y conversiones.</td><td>Mantener el modelo relacional alineado con las entidades.</td></tr>
    <tr><td>ProfileApiDataSource</td><td>Remote Adapter objetivo</td><td>Android / Kotlin</td><td>Consumir los endpoints REST del contexto.</td><td>Enviar JWT, serializar JSON y normalizar errores HTTP.</td></tr>
    <tr><td>ProfileDao</td><td>Room Adapter objetivo</td><td>Android / Room</td><td>Acceder al almacenamiento local.</td><td>Mantener caché, estado de sincronización y operaciones pendientes.</td></tr>
    <tr><td>ProfileRemoteDataSource</td><td>Remote Adapter objetivo</td><td>Flutter / Dart</td><td>Consumir los mismos contratos REST.</td><td>Serializar DTOs y traducir errores de red.</td></tr>
    <tr><td>ProfileLocalDataSource</td><td>SQLite Adapter objetivo</td><td>Flutter / Dart</td><td>Acceder a la persistencia local equivalente.</td><td>Mantener el mismo comportamiento offline que Android.</td></tr>
    <tr><td>IAM Context Facade y almacenamiento local de perfiles</td><td>Integración/ACL</td><td>Infraestructura compartida</td><td>Conectar el contexto con capacidades externas.</td><td>Traducir contratos técnicos sin contaminar el modelo del dominio.</td></tr>
  </tbody>
</table>

<a id="toc-2-6-2-5-bounded-context-software-architecture-component-level-diagrams"></a>

## 2.6.2.5. Bounded Context Software Architecture Component Level Diagrams

El archivo [`component-level.dsl`](<../../assets/codefordiagrams/2.6.2. Bounded Context Profile Management/component-level.dsl>) contiene las vistas `BC2-ApiComponents`, `BC2-AndroidComponents` y `BC2-FlutterComponents`. Las tres parten del mismo modelo C4 y muestran la separación entre presentación, aplicación, dominio y adaptadores.

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-2-Bounded-Context-Profile-Management/2-6-2-BC2-ApiComponents.svg" alt="Componentes API de Profile Management" width="900">
  <p><i>Figura 2.6.2.1. Componentes de la API para Profile Management. Fuente: elaboración propia con Structurizr DSL.</i></p>
</div>

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-2-Bounded-Context-Profile-Management/2-6-2-BC2-AndroidComponents.svg" alt="Componentes Android de Profile Management" width="900">
  <p><i>Figura 2.6.2.2. Componentes Android para Profile Management. Fuente: elaboración propia con Structurizr DSL.</i></p>
</div>

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-2-Bounded-Context-Profile-Management/2-6-2-BC2-FlutterComponents.svg" alt="Componentes Flutter de Profile Management" width="900">
  <p><i>Figura 2.6.2.3. Componentes Flutter para Profile Management. Fuente: elaboración propia con Structurizr DSL.</i></p>
</div>

<a id="toc-2-6-2-6-bounded-context-software-architecture-code-level-diagrams"></a>

## 2.6.2.6. Bounded Context Software Architecture Code Level Diagrams

Los diagramas de código detallan el modelo del dominio y los objetos de persistencia. El UML diferencia los elementos existentes de las incorporaciones objetivo, mientras los esquemas SQL señalan mediante comentarios las columnas propuestas. Los archivos ERD quedan disponibles para completar la importación manual.

<a id="toc-2-6-2-6-1-bounded-context-domain-layer-class-diagrams"></a>

### 2.6.2.6.1. Bounded Context Domain Layer Class Diagrams

El Class Diagram incluye agregados, entidades, value objects, enumeraciones, servicios de dominio e interfaces de repositorio con atributos, operaciones, visibilidad y multiplicidades.

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-2-Bounded-Context-Profile-Management/2-6-2-domain-layer-class-diagram.svg" alt="Class Diagram de Profile Management" width="900">
  <p><i>Figura 2.6.2.4. Domain Layer Class Diagram de Profile Management. Fuente: elaboración propia con PlantUML.</i></p>
</div>

<a id="toc-2-6-2-6-2-bounded-context-database-design-diagram"></a>

### 2.6.2.6.2. Bounded Context Database Design Diagram

MySQL mantiene la persistencia autoritativa. Room y SQLite contienen únicamente caché, metadatos de sincronización y operaciones pendientes; no sustituyen las reglas ni la fuente de verdad del backend. En IAM, las credenciales y tokens permanecen fuera de las tablas locales y se almacenan mediante mecanismos seguros del sistema operativo.

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-2-Bounded-Context-Profile-Management/2-6-2-mysql-database-design.png" alt="MySQL Database Diagram de Profile Management" width="900">
  <p><i>Figura 2.6.2.5. MySQL Database Design de Profile Management. Fuente: elaboración propia a partir del esquema SQL.</i></p>
</div>

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-2-Bounded-Context-Profile-Management/2-6-2-android-room-database-design.png" alt="Room Database Diagram de Profile Management" width="900">
  <p><i>Figura 2.6.2.6. Android Room Database Design de Profile Management. Fuente: elaboración propia a partir del esquema SQL.</i></p>
</div>
