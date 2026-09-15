# 2.6.3. Bounded Context: Livestock Management

Gestionar fincas, hatos, animales e identificadores QR como fuente de referencia para los demás procesos ganaderos.

La base implementada se encuentra en el módulo `Livestock` de la API ASP.NET Core. El diseño móvil de Android y Flutter se presenta como **diseño objetivo** porque esos clientes todavía no existen en el workspace. Los tres productos comparten contratos REST y lenguaje ubicuo, mientras la API conserva las reglas autoritativas.

## 2.6.3.1. Domain Layer

Esta capa representa el núcleo de Livestock Management. Los elementos existentes se conservarán como punto de partida; los elementos objetivo completan las invariantes identificadas en EventStorming y en el Bounded Context Canvas.

<table>
  <thead>
    <tr><th>Clase o componente</th><th>Tipo</th><th>Producto</th><th>Propósito</th><th>Responsabilidades</th></tr>
  </thead>
  <tbody>
    <tr><td>Herd</td><td>Clase de dominio existente</td><td>Backend / módulo Livestock</td><td>Representar Herd dentro de Livestock Management.</td><td>Conservar las invariantes actualmente implementadas y servir como evidencia trazable.</td></tr>
    <tr><td>Animal</td><td>Clase de dominio existente</td><td>Backend / módulo Livestock</td><td>Representar Animal dentro de Livestock Management.</td><td>Conservar las invariantes actualmente implementadas y servir como evidencia trazable.</td></tr>
    <tr><td>IHerdRepository</td><td>Repository Interface existente</td><td>Backend / módulo Livestock</td><td>Representar IHerdRepository dentro de Livestock Management.</td><td>Conservar las invariantes actualmente implementadas y servir como evidencia trazable.</td></tr>
    <tr><td>IAnimalRepository</td><td>Repository Interface existente</td><td>Backend / módulo Livestock</td><td>Representar IAnimalRepository dentro de Livestock Management.</td><td>Conservar las invariantes actualmente implementadas y servir como evidencia trazable.</td></tr>
    <tr><td>Farm</td><td>Diseño objetivo</td><td>Modelo canónico compartido</td><td>Completar el lenguaje ubicuo de Livestock Management.</td><td>Expresar reglas o conceptos requeridos por el alcance móvil que aún no están implementados en el backend heredado.</td></tr>
    <tr><td>AnimalTag</td><td>Diseño objetivo</td><td>Modelo canónico compartido</td><td>Completar el lenguaje ubicuo de Livestock Management.</td><td>Expresar reglas o conceptos requeridos por el alcance móvil que aún no están implementados en el backend heredado.</td></tr>
    <tr><td>QrIdentifier</td><td>Diseño objetivo</td><td>Modelo canónico compartido</td><td>Completar el lenguaje ubicuo de Livestock Management.</td><td>Expresar reglas o conceptos requeridos por el alcance móvil que aún no están implementados en el backend heredado.</td></tr>
    <tr><td>AnimalOwnershipPolicy</td><td>Diseño objetivo</td><td>Modelo canónico compartido</td><td>Completar el lenguaje ubicuo de Livestock Management.</td><td>Expresar reglas o conceptos requeridos por el alcance móvil que aún no están implementados en el backend heredado.</td></tr>
  </tbody>
</table>

## 2.6.3.2. Interface Layer

La Interface Layer traduce acciones de usuarios y contratos externos. En el backend utiliza controllers, resources y assemblers; en los clientes móviles utiliza pantallas y controladores de estado específicos de cada plataforma.

<table>
  <thead>
    <tr><th>Clase o componente</th><th>Tipo</th><th>Producto</th><th>Propósito</th><th>Responsabilidades</th></tr>
  </thead>
  <tbody>
    <tr><td>HerdsController</td><td>REST Controller existente</td><td>Backend ASP.NET Core</td><td>Exponer registro de fincas, hatos, animales y resolución de códigos QR.</td><td>Validar el contrato HTTP, traducir resources y delegar el caso de uso.</td></tr>
    <tr><td>AnimalsController</td><td>REST Controller existente</td><td>Backend ASP.NET Core</td><td>Exponer registro de fincas, hatos, animales y resolución de códigos QR.</td><td>Validar el contrato HTTP, traducir resources y delegar el caso de uso.</td></tr>
    <tr><td>HerdResource</td><td>Resource/Assembler existente</td><td>Backend ASP.NET Core</td><td>Definir el contrato público de entrada o salida.</td><td>Evitar exponer directamente entidades del dominio.</td></tr>
    <tr><td>AnimalResource</td><td>Resource/Assembler existente</td><td>Backend ASP.NET Core</td><td>Definir el contrato público de entrada o salida.</td><td>Evitar exponer directamente entidades del dominio.</td></tr>
    <tr><td>CreateHerdResource</td><td>Resource/Assembler existente</td><td>Backend ASP.NET Core</td><td>Definir el contrato público de entrada o salida.</td><td>Evitar exponer directamente entidades del dominio.</td></tr>
    <tr><td>CreateAnimalResource</td><td>Resource/Assembler existente</td><td>Backend ASP.NET Core</td><td>Definir el contrato público de entrada o salida.</td><td>Evitar exponer directamente entidades del dominio.</td></tr>
    <tr><td>FarmHerdYAnimalScreen</td><td>Composable objetivo</td><td>Android / Jetpack Compose</td><td>Presentar registro de fincas, hatos, animales y resolución de códigos QR.</td><td>Renderizar estado, recibir acciones y mostrar errores recuperables.</td></tr>
    <tr><td>FarmHerdYAnimalViewModel</td><td>Presentation Model objetivo</td><td>Android / Kotlin</td><td>Coordinar el estado observable de la pantalla.</td><td>Invocar casos de uso y convertir resultados en UI state.</td></tr>
    <tr><td>FarmHerdYAnimalPage</td><td>Widget objetivo</td><td>Flutter / Dart</td><td>Presentar registro de fincas, hatos, animales y resolución de códigos QR.</td><td>Renderizar estado y enviar intenciones del usuario.</td></tr>
    <tr><td>FarmHerdYAnimalController</td><td>State Controller objetivo</td><td>Flutter / Dart</td><td>Coordinar el estado de presentación.</td><td>Invocar casos de uso y publicar estados de carga, éxito y error.</td></tr>
  </tbody>
</table>

## 2.6.3.3. Application Layer

La Application Layer orquesta comandos, consultas y sincronización. Los casos de uso móviles consultan primero el read model local, solicitan actualización remota cuando existe conectividad y procesan operaciones pendientes mediante un outbox idempotente.

<table>
  <thead>
    <tr><th>Clase o componente</th><th>Tipo</th><th>Producto</th><th>Propósito</th><th>Responsabilidades</th></tr>
  </thead>
  <tbody>
    <tr><td>HerdCommandService</td><td>Application Service existente</td><td>Backend ASP.NET Core</td><td>Orquestar registro de fincas, hatos, animales y resolución de códigos QR.</td><td>Coordinar repositorios, reglas del dominio y Unit of Work.</td></tr>
    <tr><td>HerdQueryService</td><td>Application Service existente</td><td>Backend ASP.NET Core</td><td>Orquestar registro de fincas, hatos, animales y resolución de códigos QR.</td><td>Coordinar repositorios, reglas del dominio y Unit of Work.</td></tr>
    <tr><td>AnimalCommandService</td><td>Application Service existente</td><td>Backend ASP.NET Core</td><td>Orquestar registro de fincas, hatos, animales y resolución de códigos QR.</td><td>Coordinar repositorios, reglas del dominio y Unit of Work.</td></tr>
    <tr><td>AnimalQueryService</td><td>Application Service existente</td><td>Backend ASP.NET Core</td><td>Orquestar registro de fincas, hatos, animales y resolución de códigos QR.</td><td>Coordinar repositorios, reglas del dominio y Unit of Work.</td></tr>
    <tr><td>CreateHerdCommand</td><td>Command/Query existente</td><td>Backend ASP.NET Core</td><td>Representar una intención o consulta explícita.</td><td>Transportar datos tipados hacia el servicio de aplicación correspondiente.</td></tr>
    <tr><td>UpdateHerdCommand</td><td>Command/Query existente</td><td>Backend ASP.NET Core</td><td>Representar una intención o consulta explícita.</td><td>Transportar datos tipados hacia el servicio de aplicación correspondiente.</td></tr>
    <tr><td>CreateAnimalCommand</td><td>Command/Query existente</td><td>Backend ASP.NET Core</td><td>Representar una intención o consulta explícita.</td><td>Transportar datos tipados hacia el servicio de aplicación correspondiente.</td></tr>
    <tr><td>UpdateAnimalCommand</td><td>Command/Query existente</td><td>Backend ASP.NET Core</td><td>Representar una intención o consulta explícita.</td><td>Transportar datos tipados hacia el servicio de aplicación correspondiente.</td></tr>
    <tr><td>GetAnimalByIdQuery</td><td>Command/Query existente</td><td>Backend ASP.NET Core</td><td>Representar una intención o consulta explícita.</td><td>Transportar datos tipados hacia el servicio de aplicación correspondiente.</td></tr>
    <tr><td>FarmHerdYAnimalCommandHandler</td><td>Command Handler objetivo</td><td>Backend ASP.NET Core</td><td>Ejecutar comandos mediante una unidad de aplicación explícita.</td><td>Cargar el agregado, aplicar sus reglas, persistirlo y publicar el resultado.</td></tr>
    <tr><td>FarmHerdYAnimalEventHandler</td><td>Event Handler objetivo</td><td>Backend ASP.NET Core</td><td>Reaccionar a cambios confirmados en el contexto.</td><td>Actualizar proyecciones o solicitar integraciones sin acoplarlas al agregado.</td></tr>
    <tr><td>ObserveFarmHerdYAnimalUseCase</td><td>Use Case objetivo</td><td>Android y Flutter</td><td>Consultar el read model local y actualizar la UI.</td><td>Combinar caché local con actualización remota.</td></tr>
    <tr><td>SyncFarmHerdYAnimalUseCase</td><td>Use Case objetivo</td><td>Android y Flutter</td><td>Sincronizar cambios pendientes.</td><td>Procesar el outbox de forma idempotente y resolver resultados del servidor.</td></tr>
  </tbody>
</table>

## 2.6.3.4. Infrastructure Layer

La Infrastructure Layer conecta el dominio con Profiles, cámara, Google ML Kit, Room y SQLite. Los adapters implementan interfaces definidas hacia el interior y traducen errores técnicos a resultados comprendidos por los casos de uso.

<table>
  <thead>
    <tr><th>Clase o componente</th><th>Tipo</th><th>Producto</th><th>Propósito</th><th>Responsabilidades</th></tr>
  </thead>
  <tbody>
    <tr><td>HerdRepository / AnimalRepository</td><td>Repository Adapter existente</td><td>Backend / Entity Framework Core</td><td>Implementar los puertos de persistencia del dominio.</td><td>Consultar y guardar las entidades mediante AppDbContext y MySQL.</td></tr>
    <tr><td>ModelBuilderExtensions</td><td>Persistence Configuration existente</td><td>Backend / Entity Framework Core</td><td>Configurar tablas, columnas, constraints y conversiones.</td><td>Mantener el modelo relacional alineado con las entidades.</td></tr>
    <tr><td>FarmHerdYAnimalApiDataSource</td><td>Remote Adapter objetivo</td><td>Android / Kotlin</td><td>Consumir los endpoints REST del contexto.</td><td>Enviar JWT, serializar JSON y normalizar errores HTTP.</td></tr>
    <tr><td>FarmHerdYAnimalDao</td><td>Room Adapter objetivo</td><td>Android / Room</td><td>Acceder al almacenamiento local.</td><td>Mantener caché, estado de sincronización y operaciones pendientes.</td></tr>
    <tr><td>FarmHerdYAnimalRemoteDataSource</td><td>Remote Adapter objetivo</td><td>Flutter / Dart</td><td>Consumir los mismos contratos REST.</td><td>Serializar DTOs y traducir errores de red.</td></tr>
    <tr><td>FarmHerdYAnimalLocalDataSource</td><td>SQLite Adapter objetivo</td><td>Flutter / Dart</td><td>Acceder a la persistencia local equivalente.</td><td>Mantener el mismo comportamiento offline que Android.</td></tr>
    <tr><td>Profiles, cámara, Google ML Kit, Room y SQLite</td><td>Integración/ACL</td><td>Infraestructura compartida</td><td>Conectar el contexto con capacidades externas.</td><td>Traducir contratos técnicos sin contaminar el modelo del dominio.</td></tr>
  </tbody>
</table>

## 2.6.3.5. Bounded Context Software Architecture Component Level Diagrams

El archivo [`component-level.dsl`](<../../assets/codefordiagrams/2.6.3. Bounded Context Livestock Management/component-level.dsl>) contiene las vistas `BC3-ApiComponents`, `BC3-AndroidComponents` y `BC3-FlutterComponents`. Las tres parten del mismo modelo C4 y muestran la separación entre presentación, aplicación, dominio y adaptadores.

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-3-Bounded-Context-Livestock-Management/2-6-3-BC3-ApiComponents.svg" alt="Componentes API de Livestock Management" width="900">
  <p><i>Figura 2.6.3.1. Componentes de la API para Livestock Management. Fuente: elaboración propia con Structurizr DSL.</i></p>
</div>

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-3-Bounded-Context-Livestock-Management/2-6-3-BC3-AndroidComponents.svg" alt="Componentes Android de Livestock Management" width="900">
  <p><i>Figura 2.6.3.2. Componentes Android para Livestock Management. Fuente: elaboración propia con Structurizr DSL.</i></p>
</div>

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-3-Bounded-Context-Livestock-Management/2-6-3-BC3-FlutterComponents.svg" alt="Componentes Flutter de Livestock Management" width="900">
  <p><i>Figura 2.6.3.3. Componentes Flutter para Livestock Management. Fuente: elaboración propia con Structurizr DSL.</i></p>
</div>

## 2.6.3.6. Bounded Context Software Architecture Code Level Diagrams

Los diagramas de código detallan el modelo del dominio y los objetos de persistencia. El UML diferencia los elementos existentes de las incorporaciones objetivo, mientras los esquemas SQL señalan mediante comentarios las columnas propuestas. Los archivos ERD quedan disponibles para completar la importación manual.

### 2.6.3.6.1. Bounded Context Domain Layer Class Diagrams

El Class Diagram incluye agregados, entidades, value objects, enumeraciones, servicios de dominio e interfaces de repositorio con atributos, operaciones, visibilidad y multiplicidades.

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-3-Bounded-Context-Livestock-Management/2-6-3-domain-layer-class-diagram.svg" alt="Class Diagram de Livestock Management" width="900">
  <p><i>Figura 2.6.3.4. Domain Layer Class Diagram de Livestock Management. Fuente: elaboración propia con PlantUML.</i></p>
</div>

### 2.6.3.6.2. Bounded Context Database Design Diagram

MySQL mantiene la persistencia autoritativa. Room y SQLite contienen únicamente caché, metadatos de sincronización y operaciones pendientes; no sustituyen las reglas ni la fuente de verdad del backend. En IAM, las credenciales y tokens permanecen fuera de las tablas locales y se almacenan mediante mecanismos seguros del sistema operativo.

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-3-Bounded-Context-Livestock-Management/2-6-3-mysql-database-design.png" alt="MySQL Database Diagram de Livestock Management" width="900">
  <p><i>Figura 2.6.3.5. MySQL Database Design de Livestock Management. Fuente: elaboración propia a partir del esquema SQL.</i></p>
</div>

<div align="center">
  <img src="../../assets/codefordiagrams/2-6-3-Bounded-Context-Livestock-Management/2-6-3-android-room-database-design.png" alt="Room Database Diagram de Livestock Management" width="900">
  <p><i>Figura 2.6.3.6. Android Room Database Design de Livestock Management. Fuente: elaboración propia a partir del esquema SQL.</i></p>
</div>


