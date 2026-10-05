<a id="toc-4-2-landing-page-mobile-application-implementation"></a>

# 4.2. Landing Page & Mobile Application Implementation

Esta sección registra el avance de la Landing Page, los Web Services y las aplicaciones móviles mediante sprints. Cada iteración relaciona el Product Backlog con tareas, responsables, commits, pruebas, documentación, ejecución y despliegue verificable.

<a id="toc-4-2-1-sprint-1"></a>

## 4.2.1. Sprint 1

El Sprint 1 corresponde al TB1 y establece la base ejecutable de los productos de AniTec. Su alcance es el publicado en la rama `main` del repositorio de la aplicación Android (<https://github.com/ADM-1ACC0238-2620-13975-Grupo01/anitec-android>): la Landing Page, la adaptación del backend para el uso móvil y la aplicación Android nativa con autenticación, gestión de fincas, corrales y animales, y registros sanitarios básicos. La aplicación Flutter queda como placeholder para un sprint posterior.

<a id="toc-4-2-1-1-sprint-planning-1"></a>

### 4.2.1.1. Sprint Planning 1

La reunión de planificación definió el Sprint Goal, la capacidad del equipo y el conjunto de historias que podía completarse con evidencia verificable. El Product Backlog del AV1 asignaba al Sprint 1 veintiuna historias (96 Story Points); al contrastarlas con lo realmente publicado en `main`, el compromiso quedó ajustado a las historias de la tabla siguiente y el Product Backlog de la sección 2.4.3 se actualizó con ese ajuste: 24 historias y 105 Story Points.

<table>
  <tr><th>Sprint #</th><td>Sprint 1</td></tr>
  <tr><th colspan="2">Sprint Planning Background</th></tr>
  <tr><th>Date</th><td>2026-09-25</td></tr>
  <tr><th>Time</th><td>10:53 PM</td></tr>
  <tr><th>Location</th><td>Discord (reunión virtual)</td></tr>
  <tr><th>Prepared By</th><td>Melgarejo Quiroz, Josep Eliu</td></tr>
  <tr><th>Attendees</th><td>Beingolea Montalvo, Sebastian Martin / Melgarejo Quiroz, Josep Eliu / Ortega Muñoz, Saul / Sanchez Silva, Luciana Celeste / Villanueva Rodriguez, Giuseppe</td></tr>
  <tr><th>Sprint 0 Review Summary</th><td>No existe un sprint de implementación previo. La línea base del Sprint 1 es el AV1: el informe hasta el capítulo II (requisitos, Product Backlog y diseño estratégico y táctico), la Landing Page inicial y el backend ASP.NET Core con sus bounded contexts.</td></tr>
  <tr><th>Sprint 0 Retrospective Summary</th><td>Como aciertos del AV1, el equipo valoró haber cerrado los capítulos I y II con los requisitos y el diseño estratégico y táctico, y contar con una Landing Page inicial y un backend organizado por bounded contexts. Como oportunidades de mejora, identificó definir el alcance móvil (Android nativo y Flutter para una etapa posterior) antes de empezar a implementar, mantener alineados el informe y el código, y incorporar pruebas automatizadas al backend desde el inicio.</td></tr>
  <tr><th colspan="2">Sprint Goal &amp; User Stories</th></tr>
  <tr><th>Sprint 1 Goal</th><td><b>Nuestro foco</b> es ofrecer una primera aplicación Android ejecutable para ganaderos y veterinarios. <b>Creemos que</b> entrega una forma rápida de registrar y consultar sus fincas, animales y registros sanitarios desde el teléfono a los ganaderos y veterinarios de pequeñas y medianas explotaciones. <b>Lo confirmaremos cuando</b> un usuario pueda registrarse, iniciar sesión y registrar y consultar un animal desde la aplicación instalada, usando la API del backend, con la Landing Page publicada.</td></tr>
  <tr><th>Sprint 1 Velocity</th><td>105 Story Points, igual a la suma de las historias comprometidas. Es la capacidad acordada por el equipo para el sprint; al no existir un sprint previo, no hay una velocidad histórica de referencia.</td></tr>
  <tr><th>Sum of Story Points</th><td>105</td></tr>
</table>

La tabla siguiente lista las 24 historias comprometidas, sus Story Points y su estado al cierre del sprint. Las historias US-014, US-015 y US-016 se adelantaron desde el Sprint 2; TS-002 (configurar Flutter) y SP-001 (investigar ML Kit) pasan al Sprint 2, y US-044 y US-045 son historias nuevas incorporadas al Product Backlog (sección 2.4).

| ID | Título | Story Points | Estado al cierre |
|---|---|---:|---|
| US-011 | Registrar un animal | 5 | Completa: registro individual y masivo. |
| US-010 | Consultar y buscar animales | 5 | Completa. |
| US-013 | Consultar el detalle de un animal | 3 | Completa: ficha técnica. |
| US-009 | Registrar y actualizar una finca | 5 | Completa. |
| US-008 | Consultar las fincas registradas | 3 | Completa. |
| US-044 | Gestionar los corrales de una finca | 3 | Completa. |
| US-012 | Actualizar o archivar un animal | 5 | Parcial: se actualiza y se elimina; el archivado no está implementado. |
| US-015 | Registrar una incidencia sanitaria | 5 | Completa. |
| US-016 | Registrar diagnóstico y tratamiento | 5 | Completa. |
| US-014 | Consultar eventos sanitarios | 3 | Completa. |
| US-045 | Adjuntar una fotografía al animal | 3 | Completa. |
| US-001 | Comprender la propuesta de valor de AniTec | 3 | Completa. |
| US-002 | Conocer las soluciones para cada segmento | 3 | Completa. |
| TS-013 | Adaptar y documentar los servicios backend para móviles | 8 | Completa: corrales, operaciones masivas, OpenAPI y pruebas automatizadas del backend (sección 4.2.1.5). |
| TS-004 | Integrar las aplicaciones con la API REST interna | 5 | Completa para Android. |
| TS-003 | Definir la arquitectura móvil por capas y bounded contexts | 5 | Completa. |
| TS-001 | Configurar la aplicación Android nativa | 5 | Completa. |
| TS-005 | Implementar persistencia local segura en Android | 5 | Completa: Room y sesión cifrada. |
| US-004 | Registrar una cuenta según el rol | 5 | Completa. |
| US-005 | Iniciar sesión | 3 | Completa. |
| US-007 | Acceder únicamente a información autorizada | 5 | Parcial: el filtrado se hace en la aplicación; el backend aún no filtra por usuario. |
| US-006 | Mantener y finalizar la sesión móvil | 3 | Completa. |
| TS-008 | Proteger credenciales y datos de sesión | 5 | Completa. |
| US-003 | Acceder a una landing page adaptable e internacionalizada | 5 | Completa. |

<a id="toc-4-2-1-2-aspect-leaders-and-collaborators"></a>

### 4.2.1.2. Aspect Leaders and Collaborators

La matriz LACX indica un líder (L) y los colaboradores (C) de cada aspecto del sprint. Los aspectos corresponden a los productos y actividades del Sprint 1: diseño UX/UI, aplicación Android, aplicación Flutter, backend, Landing Page, pruebas, y documentación y despliegue. La matriz se deriva de las tareas asignadas en el Sprint Backlog (sección 4.2.1.3) y de las contribuciones al Informe; la aplicación Flutter no tiene responsables porque su desarrollo no forma parte de este sprint.

| Team Member | GitHub Username | UX/UI | Android | Flutter | Backend | Landing Page | Testing | Documentation & Deployment |
|---|---|---|---|---|---|---|---|---|
| Beingolea Montalvo, Sebastian Martin | smbmontalvo | — | C | — | L | — | C | C |
| Melgarejo Quiroz, Josep Eliu | Melga1502 | — | L | — | — | — | — | C |
| Ortega Muñoz, Saul | Ss1lent10 | C | C | — | — | L | — | C |
| Sanchez Silva, Luciana Celeste | luccsss | L | C | — | — | — | — | C |
| Villanueva Rodriguez, Giuseppe | Giuseppe152004 | — | C | — | — | — | L | L |


<a id="toc-4-2-1-3-sprint-backlog-1"></a>

### 4.2.1.3. Sprint Backlog 1

El Sprint Backlog descompone las historias comprometidas en tareas comprobables y refleja el objetivo del sprint: una primera aplicación Android ejecutable, respaldada por la API del backend y por la Landing Page publicada. El tablero utiliza los estados Todo, In-Process, To-Review y Done.

- **Sprint Goal:** ofrecer una primera aplicación Android ejecutable para ganaderos y veterinarios (ver 4.2.1.1).
- **Board URL:** [URL pública del tablero.](https://trello.com/invite/b/6a4ecb3af66dcec21f2d23be/ATTIc5c2e19d1656e989be48cf69d975850827DF607A/sprint1-anitec)

<div align="center">
  <img src="../../assets/chapter-4/TrelloSprin1Appmoviles.png" width="800">
  <p><i>Figura 4.2.1.3.1 Tablero de Trello Sprint 1 Fuente: elaboración propia.</i></p>
</div>


| Story ID | Story Title | Task ID | Task Title | Description | Hours | Assigned To | Status |
|---|---|---|---|---|---:|---|---|
| US-001 | Comprender la propuesta de valor de AniTec | T-001 | Diseñar la sección de propuesta de valor | Encabezado, mensaje principal e indicadores de la Landing Page. | 4 | Ortega Muñoz, Saul | Done |
| US-002 | Conocer las soluciones para cada segmento | T-002 | Implementar las secciones para ganaderos y veterinarios | Páginas por segmento con sus funcionalidades. | 6 | Ortega Muñoz, Saul | Done |
| US-003 | Acceder a una landing page adaptable e internacionalizada | T-003 | Implementar el diseño responsive y el selector de idioma | Adaptación a móvil y textos en inglés y español. | 8 | Ortega Muñoz, Saul | Done |
| TS-001 | Configurar la aplicación Android nativa | T-004 | Crear el proyecto Android | Proyecto Kotlin con Jetpack Compose, Hilt y la configuración de compilación. | 6 | Villanueva Rodriguez, Giuseppe | Done |
| TS-003 | Definir la arquitectura móvil por capas y bounded contexts | T-005 | Organizar el código por bounded contexts y capas | Paquetes domain, application, infrastructure e interfaces por contexto. | 6 | Villanueva Rodriguez, Giuseppe | Done |
| TS-004 | Integrar las aplicaciones con la API REST interna | T-006 | Implementar el cliente REST | Retrofit y OkHttp con interceptor de token y mapeo de errores HTTP. | 8 | Beingolea Montalvo, Sebastian Martin | Done |
| TS-005 | Implementar persistencia local segura en Android | T-007 | Implementar la caché local con Room | Entidades y DAO por contexto; limpieza de la caché al cerrar sesión. | 8 | Melgarejo Quiroz, Josep Eliu | Done |
| TS-013 | Adaptar y documentar los servicios backend para móviles | T-008 | Agregar corrales y operaciones masivas al backend | Entidad Corral, relación animal-corral y endpoints de alta, estado y baja masiva. | 10 | Beingolea Montalvo, Sebastian Martin | Done |
| TS-013 | Adaptar y documentar los servicios backend para móviles | T-009 | Documentar los endpoints con OpenAPI | Swagger UI con esquema Bearer JWT para los endpoints del Sprint. | 4 | Beingolea Montalvo, Sebastian Martin | Done |
| US-004 | Registrar una cuenta según el rol | T-010 | Pantalla de registro | Formulario con selección de rol y aceptación de los Términos de Servicio. | 6 | Ortega Muñoz, Saul | Done |
| US-005 | Iniciar sesión | T-011 | Pantalla de inicio de sesión | Formulario, validaciones y mensajes de error recuperables. | 4 | Ortega Muñoz, Saul | Done |
| US-006 | Mantener y finalizar la sesión móvil | T-012 | Mantener y finalizar la sesión | Sesión persistente, cierre de sesión y retorno al inicio al vencer el token. | 6 | Ortega Muñoz, Saul | Done |
| US-007 | Acceder únicamente a información autorizada | T-013 | Navegación por rol y filtrado de datos | Barra de navegación por rol y filtrado de fincas, animales y registros del usuario en la aplicación. | 8 | Melgarejo Quiroz, Josep Eliu | To-Review |
| TS-008 | Proteger credenciales y datos de sesión | T-014 | Cifrar el token de sesión | Almacenamiento con DataStore, Tink (AES-256-GCM) y Android Keystore. | 6 | Beingolea Montalvo, Sebastian Martin | Done |
| US-008 | Consultar las fincas registradas | T-015 | Lista de fincas | Tarjetas con ubicación, propietario y conteo de corrales y animales. | 4 | Sanchez Silva, Luciana Celeste | Done |
| US-009 | Registrar y actualizar una finca | T-016 | Formulario de fincas | Alta y edición con validaciones y eliminación con confirmación. | 5 | Sanchez Silva, Luciana Celeste | Done |
| US-010 | Consultar y buscar animales | T-017 | Lista de animales con búsqueda y filtro | Búsqueda por varios campos y filtro por corral. | 8 | Melgarejo Quiroz, Josep Eliu | Done |
| US-011 | Registrar un animal | T-018 | Formulario de registro de animales | Registro individual y masivo de 1 a 500 animales. | 10 | Melgarejo Quiroz, Josep Eliu | Done |
| US-012 | Actualizar o archivar un animal | T-019 | Edición y eliminación de animales | Edición, eliminación individual y acciones sobre varios animales con confirmación. | 6 | Villanueva Rodriguez, Giuseppe | To-Review |
| US-013 | Consultar el detalle de un animal | T-020 | Ficha técnica del animal | Hoja de detalle con todos los datos y la fotografía. | 6 | Ortega Muñoz, Saul | Done |
| US-014 | Consultar eventos sanitarios | T-021 | Lista de registros sanitarios | Tarjetas con tipo, fecha y seguimiento. | 5 | Sanchez Silva, Luciana Celeste | Done |
| US-015 | Registrar una incidencia sanitaria | T-022 | Formulario de registro sanitario | Tipo, fecha, descripción y fecha de seguimiento. | 6 | Sanchez Silva, Luciana Celeste | Done |
| US-016 | Registrar diagnóstico y tratamiento | T-023 | Diagnóstico y tratamiento | Campos de diagnóstico, tratamiento y prescripción del registro sanitario. | 3 | Sanchez Silva, Luciana Celeste | Done |
| US-044 | Gestionar los corrales de una finca | T-024 | Lista y formulario de corrales | Alta, edición y eliminación de corrales por finca. | 6 | Sanchez Silva, Luciana Celeste | Done |
| US-045 | Adjuntar una fotografía al animal | T-025 | Fotografía del animal | Captura con cámara o elección de galería, reducción de tamaño y subida al servidor. | 8 | Melgarejo Quiroz, Josep Eliu | Done |
| Sin historia | Tarea técnica sin historia asociada | T-026 | Pruebas unitarias e instrumentadas de Android | JUnit, MockK y pruebas de DAO de Room sobre dominio, casos de uso, repositorios y ViewModels. | 12 | Villanueva Rodriguez, Giuseppe | Done |
| Sin historia | Tarea técnica sin historia asociada | T-027 | Pantalla de inicio del ganadero | Contadores del hato, alertas y registros sanitarios recientes. | 6 | Villanueva Rodriguez, Giuseppe | Done |
| TS-013 | Adaptar y documentar los servicios backend para móviles | T-028 | Crear la suite de pruebas automatizadas del backend | Proyecto `Anitec.Platform.Tests` con pruebas unitarias, de integración y BDD (xUnit, NSubstitute y Reqnroll) de Iam, Livestock y Sanitary. | 12 | Beingolea Montalvo, Sebastian Martin | Done |
| Sin historia | Tarea de diseño sin historia asociada | T-029 | Elaborar los mock-ups móviles | Mock-ups de Android y Flutter organizados por aplicación y rol, base de las pantallas de la aplicación. | 12 | Sanchez Silva, Luciana Celeste | Done |
| Sin historia | Tarea de despliegue sin historia asociada | T-030 | Registrar las aplicaciones en Firebase y documentar su despliegue | Aplicaciones Android y Flutter registradas en Firebase App Distribution y documentación del proceso de publicación. | 6 | Villanueva Rodriguez, Giuseppe | Done |

| Métrica | Valor |
|---|---|
| Historias comprometidas | 24 |
| Story Points comprometidos | 105 |
| Tareas | 30 |
| Horas estimadas | 205 |
| Tareas completadas (Done) | 28 de 30; las 2 restantes están en To-Review |


<a id="toc-4-2-1-4-development-evidence-for-sprint-review"></a>

### 4.2.1.4. Development Evidence for Sprint Review

Esta sección registra los commits que contribuyen al alcance comprometido. La aplicación Android se desarrolló durante el sprint sobre la rama `main`; el backend y la aplicación web parten de proyectos creados antes del sprint, por lo que se registra su commit de creación, y el backend suma el commit de sus pruebas automatizadas. El Informe documenta el diseño, la configuración y las evidencias del sprint.

| Repository | Branch | Commit Id | Commit Message | Commit Message Body | Committed on |
|---|---|---|---|---|---|
| anitec-android | main | `2f3b903` | feat: add Android project foundation and authentication | Aplicación Compose con el sistema de diseño de AniTec y localización es-419/en; red con Retrofit/OkHttp, sesión cifrada y manejo de 401; inicio de sesión, registro, términos de servicio y navegación por rol; pruebas unitarias del mapeo de errores y de los ViewModels de autenticación. | 2026-10-01 |
| anitec-android | main | `8ade432` | feat: add livestock management, health records and rancher dashboard | Fincas, corrales y animales con búsqueda, filtro por corral, selección múltiple con acciones masivas, ficha técnica y subida de fotografía; lista y formulario de registros sanitarios; inicio del ganadero con contadores y registros recientes; caché Room limitada al usuario y limpiada al cerrar sesión; pruebas instrumentadas. | 2026-10-01 |
| anitec-backend | main | `125d53e` | chore: add initial commit with all project files | Solución `Anitec.Platform` con sus bounded contexts (Iam, Profiles, Livestock, Sanitary, Financial, Activities, Analytics, Devices, Metrics, Subscriptions, Clients, Shared), controllers REST, Entity Framework Core con MySQL, JWT y Swagger. | 2026-09-04 |
| anitec-backend | main | `888f1b9` | chore: add tests for Anitec.Platform | Proyecto `Anitec.Platform.Tests` con 52 pruebas unitarias, 32 de integración y 20 escenarios BDD (4 archivos `.feature` con sus pasos); respuesta `403` en lugar de `500` para un rol sin permiso y entorno `Testing` para ejecutar la API con SQLite en memoria. | 2026-10-04 |
| anitec-frontend | main | `f12794d` | chore: add initial project files | Estructura inicial de la aplicación web en Vue. | 2026-09-04 |
| Informe | main | `c8b8be7` | docs: update report complete generation | Estructura del informe con sus capítulos, títulos y diagramas de arquitectura C4. | 2026-09-16 |
| Informe | main | `d09a7e2` | docs(chapter-4): add backend evidence | Evidencias del despliegue y de la documentación del backend. | 2026-10-01 |
| Informe | main | `cd83263` | docs(update): mockups organized | Mock-ups móviles organizados por aplicación y rol. | 2026-10-02 |

<a id="toc-4-2-1-5-testing-suite-evidence-for-sprint-review"></a>

### 4.2.1.5. Testing Suite Evidence for Sprint Review

Los Web Services cuentan con una suite de pruebas automatizadas en el proyecto `Anitec.Platform.Tests` (xUnit), dentro del repositorio `anitec-backend`: <https://github.com/ADM-1ACC0238-2620-13975-Grupo01/anitec-backend/tree/main/Anitec.Platform.Tests>. La suite reúne tres tipos de pruebas, todas relacionadas con las historias del Sprint 1:

| Tipo | Herramientas | Carpeta del proyecto | Pruebas |
|---|---|---|---|
| Unit Tests | xUnit y NSubstitute (repositorios simulados) | `Unit/` | 52 |
| Integration Tests | xUnit y `WebApplicationFactory` | `Integration/` | 32 |
| Acceptance Tests (BDD) | Reqnroll sobre xUnit, archivos `.feature` en Gherkin | `Bdd/Features/` y `Bdd/Steps/` | 20 escenarios |
| **Total** | | | **104** |

Las pruebas de integración y de BDD arrancan la API real en memoria con `WebApplicationFactory`. Para no depender de un servidor MySQL, la base de datos es SQLite en memoria y el entorno es `Testing`: en él la API crea el esquema con `EnsureCreated()` en lugar de aplicar las migraciones de MySQL. Las pruebas se ejecutan con `dotnet test` desde la carpeta del repositorio.

**Unit Tests.** Cada clase valida un servicio de la capa de aplicación o de infraestructura con sus dependencias simuladas.

| Test ID | Clase probada | Clase de pruebas | Comportamientos verificados | Historias relacionadas | Pruebas | Resultado |
|---|---|---|---|---|---|---|
| TEST-BE-U01 | `UserCommandService` | `UserCommandServiceTests` | Registro con la contraseña cifrada; nombre de usuario repetido; rol inválido y normalización del rol; correo mal formado, repetido y normalizado a minúsculas; nombre completo vacío; error de base de datos; inicio de sesión con credenciales válidas, usuario inexistente y contraseña incorrecta. | US-004, US-005 | 18 | Completado |
| TEST-BE-U02 | `TokenService` | `TokenServiceTests` | El token incluye usuario y rol y vence a los 7 días; un token válido devuelve el id del usuario; un token ausente, mal formado, firmado con otra clave, alterado o vencido se rechaza. | US-005, US-007 | 9 | Completado |
| TEST-BE-U03 | `HashingService` | `HashingServiceTests` | La contraseña no se guarda en claro, cada cifrado produce un hash distinto y la verificación acepta solo la contraseña original. | US-004, US-005 | 3 | Completado |
| TEST-BE-U04 | `AnimalCommandService` | `AnimalCommandServiceTests` | Alta, edición y baja de un animal con y sin registro existente; alta masiva de 1 a 500 animales, rechazo de cantidades fuera de rango y de un corral inexistente, y códigos consecutivos por corral; cambio de estado y baja de varios animales ignorando los inexistentes. | US-011, US-012, TS-013 | 17 | Completado |
| TEST-BE-U05 | `CorralCommandService` | `CorralCommandServiceTests` | Alta, edición y baja de un corral, y respuesta de «no encontrado» cuando no existe. | US-044, TS-013 | 5 | Completado |

**Integration Tests.** Cada prueba llama a los endpoints REST de la API en memoria con usuarios registrados durante la prueba.

| Test ID | Clase de pruebas | Endpoints y comportamientos verificados | Historias relacionadas | Pruebas | Resultado |
|---|---|---|---|---|---|
| TEST-BE-I01 | `AuthenticationApiTests` | `POST /authentication/sign-up` (alta, usuario repetido `409`, rol inválido `400`), `POST /authentication/sign-in` (token, contraseña incorrecta `400`) y `401` en `/animals`, `/herds`, `/corrals` y `/health-events` sin token o con un token inválido. | US-004, US-005, US-007 | 11 | Completado |
| TEST-BE-I02 | `LivestockApiTests` | Fincas (`POST`, `GET`, validación `400`, no encontrada `404`), corrales (`POST`, listado, `DELETE`), animales (`POST` con corral obligatorio, `GET`, `PUT`, `DELETE`, `POST /animals/bulk`, `PATCH /animals/bulk-status` y `DELETE /animals/bulk` con cuerpo JSON) y permisos por rol: el veterinario consulta animales, pero no los crea (`403`). | US-007, US-008, US-009, US-010, US-011, US-012, US-044, TS-013 | 16 | Completado |
| TEST-BE-I03 | `HealthEventsApiTests` | `POST`, `GET` y `DELETE` de `/health-events`, evento inexistente `404` y registro de un evento por un veterinario. | US-014, US-015, US-016 | 5 | Completado |

**Acceptance Tests (BDD).** Los escenarios se escriben en Gherkin (Given-When-Then) en cuatro archivos `.feature` dentro de `Anitec.Platform.Tests/Bdd/Features`. Los pasos se implementan en C# en `Anitec.Platform.Tests/Bdd/Steps` y ejecutan los escenarios contra la API en memoria.

| Archivo `.feature` | Escenarios | Historias relacionadas |
|---|---|---|
| `Authentication.feature` | 7 | US-004, US-005, US-007 |
| `AnimalManagement.feature` | 7 | US-010, US-011, US-012, US-044, TS-013 |
| `HealthRecords.feature` | 3 | US-014, US-015, US-016 |
| `RolePermissions.feature` | 3 | US-007 |

Código de `Authentication.feature`:

<pre>
Feature: Authentication
  As a rancher or a veterinarian
  I want to create an account and sign in
  So that I can work with my own information in AniTec

  Scenario: A new rancher signs up and signs in
    Given I am a new visitor
    When I sign up as a "Rancher"
    And I sign in with my credentials
    Then I receive a session token
    And my role is "Rancher"

  Scenario: A new veterinarian signs up and signs in
    Given I am a new visitor
    When I sign up as a "Veterinarian"
    And I sign in with my credentials
    Then I receive a session token
    And my role is "Veterinarian"

  Scenario: Signing up with an unknown role is rejected
    Given I am a new visitor
    When I sign up as a "Administrator"
    Then the request is rejected with status 400

  Scenario: Signing up twice with the same username is rejected
    Given I have an account as a "Rancher"
    When I sign up as a "Rancher"
    Then the request is rejected with status 409

  Scenario: Signing in with a wrong password is rejected
    Given I have an account as a "Rancher"
    When I sign in with the password "wrong-password"
    Then the request is rejected with status 400
    And I do not receive a session token

  Scenario: Protected information requires a session
    Given I am a new visitor
    When I request the list of animals
    Then the request is rejected with status 401

  Scenario: A signed-in user can request protected information
    Given I am signed in as a "Rancher"
    When I request the list of animals
    Then the request succeeds
</pre>

Código de `AnimalManagement.feature`:

<pre>
Feature: Animal management
  As a rancher
  I want to register and organize my animals by farm and corral
  So that I always know what I have and in what condition

  Background:
    Given I am signed in as a "Rancher"
    And I have a farm called "La Esperanza"
    And the farm has a corral called "Corral A"

  Scenario: Register an animal in a corral
    When I register an animal with the code "COW-001" in "Corral A"
    Then the animal "COW-001" appears in the animal list

  Scenario: An animal must belong to a corral
    When I register an animal without a corral
    Then the request is rejected with status 400

  Scenario: Register several animals at once
    When I register 3 animals in bulk in "Corral A"
    Then the codes "CorralA-001, CorralA-002, CorralA-003" are assigned

  Scenario: Bulk registration is limited to 500 animals
    When I register 501 animals in bulk in "Corral A"
    Then the request is rejected with status 400

  Scenario: Mark several animals as sold
    Given the corral "Corral A" has the animal "COW-001"
    And the corral "Corral A" has the animal "COW-002"
    When I mark the animals "COW-001, COW-002" as "Vendido"
    Then the animals "COW-001, COW-002" have the status "Vendido"

  Scenario: Remove an animal
    Given the corral "Corral A" has the animal "COW-003"
    When I delete the animal "COW-003"
    Then the animal "COW-003" no longer appears in the animal list

  Scenario: Remove several animals at once
    Given the corral "Corral A" has the animal "COW-004"
    And the corral "Corral A" has the animal "COW-005"
    When I delete the animals "COW-004, COW-005"
    Then the animal "COW-004" no longer appears in the animal list
    And the animal "COW-005" no longer appears in the animal list
</pre>

Código de `HealthRecords.feature`:

<pre>
Feature: Health records
  As a rancher or a veterinarian
  I want to keep the health history of each animal
  So that incidents, vaccines and treatments are never forgotten

  Background:
    Given a rancher has a farm called "La Esperanza"
    And the farm has a corral called "Corral A"
    And the corral "Corral A" has the animal "COW-001"

  Scenario: A rancher records a health incident
    Given I am signed in as a "Rancher"
    When I record a "Incidencia" health event for the animal "COW-001" with the description "Cojera en la pata trasera"
    Then the health event is created
    And the health record of the animal "COW-001" includes the description "Cojera en la pata trasera"

  Scenario: A veterinarian records a treatment
    Given I am signed in as a "Veterinarian"
    When I record a "Tratamiento" health event for the animal "COW-001" with the description "Antibiótico por 5 días"
    Then the health event is created
    And the health record of the animal "COW-001" includes the description "Antibiótico por 5 días"

  Scenario: Health records require a session
    Given I am a new visitor
    When I request the health records
    Then the request is rejected with status 401
</pre>

Código de `RolePermissions.feature`:

<pre>
Feature: Role permissions
  As the owner of the information
  I want each role to do only what it is meant to do
  So that a veterinarian can follow animals without changing the herd

  Background:
    Given a rancher has a farm called "La Esperanza"
    And the farm has a corral called "Corral A"
    And the corral "Corral A" has the animal "COW-001"

  Scenario: A veterinarian can see the animals
    Given I am signed in as a "Veterinarian"
    When I request the list of animals
    Then the request succeeds
    And the animal "COW-001" appears in the animal list

  Scenario: A veterinarian cannot register animals
    Given I am signed in as a "Veterinarian"
    When I register an animal with the code "COW-009" in "Corral A"
    Then the request is rejected with status 403

  Scenario: A veterinarian cannot delete animals
    Given I am signed in as a "Veterinarian"
    When I delete the animal "COW-001"
    Then the request is rejected with status 403
</pre>

**Resultado de la ejecución.** Las 104 pruebas del backend (52 unitarias, 32 de integración y 20 escenarios BDD) pasan sin errores. Las pruebas de integración detectaron un defecto: un veterinario que intentaba crear un animal recibía `500` en lugar de `403`. Se corrigió en `AuthorizeAttribute`, que ahora responde `403 Forbidden`, y quedó cubierto por la prueba `AVeterinarian_CannotCreateAnimals` y por el escenario «A veterinarian cannot register animals».

<div align="center">
  <img src="../../assets/chapter-4/PruebasTest104Exitos.png" width="800">
  <p><i>Figura 4.2.1.5.1. Captura de los 104 tests exitosos. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/ListaTests.png" width="800">
  <p><i>Figura 4.2.1.5.2. Captura de la lista de tests. Fuente: elaboración propia.</i></p>
</div>

**Otras pruebas del sprint.** Pruebas de la documentación publicada, de la Landing Page y de la aplicación Android.

| Test ID     | Product | Type | Class / Feature | Behavior | Related Story | Result |
|-------------|---|---|---|---|---|---|
| TEST-BE-001 | Web Services | Exploratoria / contrato | Swagger UI (`/swagger`) | Validar disponibilidad de OpenAPI y endpoints Animals / Authentication en el entorno publicado | Autenticación y registro esencial de animales / sanidad | Completado — Figura 4.2.1.6.1 |
| TEST-LP-003 | Landing Page | Funcional | Navigation | Validar la navegación entre las distintas secciones de la Landing Page. | Navegación y experiencia de usuario | Completado |
| TEST-LP-004 | Landing Page | Responsive Testing | Responsive Design | Verificar la correcta adaptación de la interfaz en dispositivos móviles y escritorio. | Accesibilidad multiplataforma | Completado |
| TEST-AN-001 | Android | Automatizada (JUnit) | `AuthViewModelsTest`, `HomeViewModelTest` | Validar flujos de estado de autenticación (Login) y carga del dashboard inicial. | Autenticación de usuario | Completado |
| TEST-AN-002 | Android | Automatizada (JUnit) | `LivestockDomainTest`, `LivestockUseCasesTest`, `SanitaryTest` | Validar reglas de negocio del dominio de ganado, sanidad y casos de uso. | Gestión de ganado y Sanidad | Completado |
| TEST-AN-003 | Android | Automatizada (Instrumentada) | `RoomDaoTest` | Verificar operaciones CRUD y persistencia local de la base de datos con Room (Offline-First). | Gestión de ganado | Completado |

| Repository | Branch | Commit Id | Commit Message | Commit Message Body | Committed on |
|---|---|---|---|---|---|
| anitec-backend | main | `888f1b9` | chore: add tests for Anitec.Platform | Agrega el proyecto `Anitec.Platform.Tests` con las pruebas unitarias, de integración y BDD, y la corrección de `AuthorizeAttribute` (`403` en lugar de `500`). | 2026-10-04 |
| anitec-landing-page | main | 2a88184 | chore: add initial project files | Agrega la estructura inicial del proyecto de la Landing Page, incluyendo configuración base y componentes principales para el desarrollo de la interfaz | 2026-09-04 |
| anitec-android | main | `2f3b903` | feat: add Android project foundation and authentication | Configura la arquitectura base e incluye pruebas unitarias iniciales para los flujos de autenticación (`AuthViewModelsTest`, `HomeViewModelTest`). | 2026-10-01 |
| anitec-android | main | `8ade432` | feat: add livestock management, health records and rancher dashboard | Implementa la lógica de ganado/sanidad y adjunta las suites de pruebas unitarias e instrumentadas (`LivestockDomainTest`, `SanitaryTest`, `RoomDaoTest`). | 2026-10-01 |

<a id="toc-4-2-1-6-execution-evidence-for-sprint-review"></a>

### 4.2.1.6. Execution Evidence for Sprint Review

El Sprint 1 permite recorrer la Landing Page publicada, consultar la documentación de la API y ejecutar la aplicación Android con autenticación, fincas, corrales, animales y registros sanitarios. La evidencia de ejecución muestra el resultado mediante capturas identificables y un video que explica el recorrido implementado.

| Producto | Vista o flujo | Entorno / dispositivo | Evidencia | Estado |
|---|---|---|---|---|
| Landing Page | Página principal y responsive | Navegador de escritorio y móvil | Figura 4.2.1.6.2 (`landing_despliegue.png`) | Completado |
| Android | Registro, inicio de sesión, inicio del ganadero, fincas, corrales, animales (lista, ficha y formulario) y registros sanitarios | Emulador y dispositivo físico | Figuras 4.2.1.6.3 a 4.2.1.6.10 | Parcial: captura del inicio de sesión; el resto pendiente |
| Flutter | Autenticación y funciones core comprometidas | Dispositivo o emulador objetivo | Pendiente | Pendiente (placeholder) |
| Web Services | Swagger UI: documentación OpenAPI de la API publicada | Navegador contra el Swagger del servicio publicado en Render | Figura 4.2.1.6.1 (`swagger-ui.png`) | Completado |
| Integración | Consumo de la API y manejo de errores desde la aplicación Android | Aplicación contra el backend vigente | Figura 4.2.1.6.11 | Pendiente de captura |

<div align="center">
  <img src="../../assets/chapter-4/backend/swagger-ui.png" width="800">
  <p><i>Figura 4.2.1.6.1. Swagger UI de AniTec Platform en Render, con endpoints de Animals y Authentication. Fuente: elaboración propia.</i></p>
</div>

La captura demuestra que la documentación interactiva carga desde el entorno publicado y expone los contratos REST usados por el Sprint 1.

<div align="center">
  <img src="../../assets/chapter-4/landing_despliegue.png" width="800">
  <p><i>Figura 4.2.1.6.2. Landing de AniTec desplegado, Fuente: elaboración propia.</i></p>
</div>

Las capturas muestran la implementación de la Landing Page de AniTec en navegadores. Se verificó la correcta visualización del contenido, la navegación entre secciones y la adaptación responsive de la interfaz para distintos tamaños de pantalla.

**Aplicación Android.** La captura del inicio de sesión ya está incorporada; las demás se añadirán desde el emulador y el dispositivo físico.

<div align="center">
  <img src="../../assets/chapter-4/android-login.png" width="300">
  <p><i>Figura 4.2.1.6.3. Ejecución de la aplicación nativa Android mostrando el flujo de Autenticación. Fuente: elaboración propia.</i></p>
</div>

La captura evidencia el correcto funcionamiento de la aplicación Android instalada en el emulador, mostrando la interfaz nativa para el inicio de sesión de ganaderos y veterinarios.

<div align="center">
  <img src="../../assets/chapter-4/AndroidSS/android-home.png" alt="Captura pendiente: Inicio del ganadero" width="400">
  <p><i>Figura 4.2.1.6.4. Inicio del ganadero. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/AndroidSS/android-farms.png" alt="Captura pendiente: Lista de fincas y formulario" width="400">
  <p><i>Figura 4.2.1.6.5. Lista de fincas. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/AndroidSS/android-activities.png" alt="Captura pendiente: Lista de corrales y formulario" width="400">
  <p><i>Figura 4.2.1.6.6. Lista de actividades. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/AndroidSS/android-finance.png" alt="Captura pendiente: Lista de animales con búsqueda y selección múltiple" width="400">
  <p><i>Figura 4.2.1.6.7. Pantalla de fiananzas Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/AndroidSS/android-analytics.png" alt="Captura pendiente: Ficha técnica del animal" width="400">
  <p><i>Figura 4.2.1.6.8. Pantalla de analiticas. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/AndroidSS/android-health.png" alt="Captura pendiente: Formulario de registro de animal con fotografía" width="400">
  <p><i>Figura 4.2.1.6.9. Pantalla de sanidad Fuente: elaboración propia.</i></p>
</div>


**Videos de Ejecución del Sprint 1:**

- **Landing Page:** [Ver video de ejecución (0:00 - 1:48)](https://upcedupe-my.sharepoint.com/:v:/g/personal/u20231c019_upc_edu_pe/IQBmZ8UxBU5zToJUnS4AN161Aa9ocLvYJcSFOja0Zogn_tE?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=V8q9eK)
- **Aplicación Android:** [Ver video de ejecución (0:00 - 2:15)](https://upcedupe-my.sharepoint.com/personal/u20221c554_upc_edu_pe/_layouts/15/stream.aspx?id=%2Fpersonal%2Fu20221c554%5Fupc%5Fedu%5Fpe%2FDocuments%2FVideos%2FClipchamp%2FVideo%20Project%2FExports%2FVideo%20Project%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E1bd670fc%2Db74c%2D4708%2Dafd0%2D3ea986759d22)
- **Backend (Web Services):** **Pendiente de completar:** URL del video del backend.
- **Aplicación Flutter:** **Pendiente de completar** cuando exista la aplicación.

<a id="toc-4-2-1-7-services-documentation-evidence-for-sprint-review"></a>

### 4.2.1.7. Services Documentation Evidence for Sprint Review

El backend documenta su API con OpenAPI mediante Swashbuckle (`AddSwaggerGen`, `UseSwagger` y `UseSwaggerUI` en `Program.cs`) e incluye el esquema Bearer JWT para autorizar las llamadas desde la interfaz de Swagger. Durante el Sprint 1 quedaron documentados los endpoints de autenticación, fincas, corrales, animales y registros sanitarios que consume la aplicación Android, incluidos los de corrales y las operaciones masivas añadidos para el uso móvil.

**Convención de llamada.** Todas las rutas parten de `{BASE_URL}/api/v1`, donde `{BASE_URL}` es la URL del servicio (local o publicado). Las solicitudes con cuerpo usan `Content-Type: application/json`. Salvo el registro y el inicio de sesión, cada llamada envía el token en la cabecera `Authorization: Bearer <token>` y recibe `401` si falta o no es válido. Las fechas usan el formato `yyyy-MM-dd`. Los valores de estado, tipo y especie son texto en español, por ejemplo `Saludable` o `Vacuna`. En los ejemplos, `<token>` y `<password>` representan los valores reales.

**Autenticación** (`/authentication`)

| Related story | HTTP | Call syntax | Parameters / body | Success response | Error responses |
|---|---|---|---|---|---|
| US-004 | POST | `curl -X POST "{BASE_URL}/api/v1/authentication/sign-up" -H "Content-Type: application/json" -d '{"fullName":"Carlos Mendoza","username":"cmendoza","password":"<password>","role":"Rancher"}'` | Body `SignUpResource`: `username`, `password`, `fullName` y `role` (`Rancher` o `Veterinarian`). | `200` con `{"message": ...}`: la cuenta se creó. El registro no devuelve token; la aplicación inicia sesión a continuación. | `400` si los datos son inválidos o el usuario ya existe. |
| US-005 | POST | `curl -X POST "{BASE_URL}/api/v1/authentication/sign-in" -H "Content-Type: application/json" -d '{"username":"ganadero","password":"<password>"}'` | Body `SignInResource`: `username` y `password`. | `200` con `{"id":1,"username":"ganadero","fullName":"Carlos Mendoza","role":"Rancher","token":"eyJhbGciOi..."}`: el token JWT identifica al usuario y su rol y se envía en las demás llamadas. | `400` si las credenciales son inválidas. |

**Fincas** (`/herds`; lectura para Rancher y Veterinarian, escritura solo para Rancher)

Ejemplo de `HerdResource`: `{"id":1,"name":"Hato Los Alamos","location":"Cajamarca","owner":"Carlos Mendoza","ownerId":1,"veterinarianId":2,"mainType":"Mixto"}`.

| Related story | HTTP | Call syntax | Parameters / body | Success response | Error responses |
|---|---|---|---|---|---|
| US-008 | GET | `curl "{BASE_URL}/api/v1/herds" -H "Authorization: Bearer <token>"` | Ninguno. | `200` con la lista de fincas (un `HerdResource` por elemento). | `401` sin token; `403` si el rol no está autorizado. |
| US-008 | GET | `curl "{BASE_URL}/api/v1/herds/1" -H "Authorization: Bearer <token>"` | Ruta: `id`. | `200` con el `HerdResource` de la finca. | `404` si no existe; `401`. |
| US-009 | POST | `curl -X POST "{BASE_URL}/api/v1/herds" -H "Authorization: Bearer <token>" -H "Content-Type: application/json" -d '{"name":"Hato Los Alamos","location":"Cajamarca","owner":"Carlos Mendoza","ownerId":1,"veterinarianId":null,"mainType":"Mixto"}'` | Body `CreateHerdResource`: `name`, `location`, `owner`, `ownerId`, `veterinarianId` (opcional) y `mainType`. | `201` con el `HerdResource` creado. | `400` datos inválidos; `401`; `403` solo Rancher. |
| US-009 | PUT | `curl -X PUT "{BASE_URL}/api/v1/herds/1" -H "Authorization: Bearer <token>" -H "Content-Type: application/json" -d '{...}'` | Ruta: `id`. Body `CreateHerdResource`. | `200` con la finca actualizada. | `404` si no existe; `400`; `401`; `403`. |
| US-009 | DELETE | `curl -X DELETE "{BASE_URL}/api/v1/herds/1" -H "Authorization: Bearer <token>"` | Ruta: `id`. | `204` sin contenido. | `404` si no existe; `401`; `403`. |

**Corrales** (`/corrals`; lectura para Rancher y Veterinarian, escritura solo para Rancher)

Ejemplo de `CorralResource`: `{"id":1,"name":"Corral ALAMOS 1","herdId":1}`.

| Related story | HTTP | Call syntax | Parameters / body | Success response | Error responses |
|---|---|---|---|---|---|
| US-044 | GET | `curl "{BASE_URL}/api/v1/corrals" -H "Authorization: Bearer <token>"` | Ninguno. | `200` con la lista de corrales. | `401`; `403`. |
| US-044 | GET | `curl "{BASE_URL}/api/v1/corrals/1" -H "Authorization: Bearer <token>"` | Ruta: `id`. | `200` con el `CorralResource`. | `404`; `401`. |
| US-044 | POST | `curl -X POST "{BASE_URL}/api/v1/corrals" -H "Authorization: Bearer <token>" -H "Content-Type: application/json" -d '{"name":"Corral ALAMOS 1","herdId":1}'` | Body `CreateCorralResource`: `name` y `herdId`. | `201` con el corral creado. | `400`; `401`; `403`. |
| US-044 | PUT | `curl -X PUT "{BASE_URL}/api/v1/corrals/1" -H "Authorization: Bearer <token>" -H "Content-Type: application/json" -d '{...}'` | Ruta: `id`. Body `CreateCorralResource`. | `200` con el corral actualizado. | `404`; `400`; `401`; `403`. |
| US-044 | DELETE | `curl -X DELETE "{BASE_URL}/api/v1/corrals/1" -H "Authorization: Bearer <token>"` | Ruta: `id`. | `204` sin contenido. | `404`; `401`; `403`. |

**Animales** (`/animals`; lectura para Rancher y Veterinarian, escritura solo para Rancher)

Ejemplo de `AnimalResource`: `{"id":1,"tag":"BOV-001","name":"Luna","species":"Bovino","breed":"Brown Swiss","gender":"Hembra","birthDate":"2021-03-14","weight":410.0,"status":"Saludable","herdId":1,"corralId":1,"source":"Comprado","ageRange":"Adulto","imageUrl":"/uploads/animals/<archivo>.jpg"}`.

| Related story | HTTP | Call syntax | Parameters / body | Success response | Error responses |
|---|---|---|---|---|---|
| US-010 | GET | `curl "{BASE_URL}/api/v1/animals" -H "Authorization: Bearer <token>"` | Ninguno. | `200` con la lista de animales (un `AnimalResource` por elemento). La aplicación filtra los del usuario y busca localmente. | `401`; `403`. |
| US-013 | GET | `curl "{BASE_URL}/api/v1/animals/1" -H "Authorization: Bearer <token>"` | Ruta: `id`. | `200` con el `AnimalResource`. | `404`; `401`. |
| US-011 | POST | `curl -X POST "{BASE_URL}/api/v1/animals" -H "Authorization: Bearer <token>" -H "Content-Type: application/json" -d '{"tag":"BOV-900","name":"Nube","species":"Bovino","breed":"Holstein","gender":"Hembra","birthDate":"2024-02-01","weight":280.0,"status":"Saludable","herdId":1,"corralId":1}'` | Body `CreateAnimalResource`: `tag`, `name`, `species`, `breed`, `gender`, `birthDate`, `weight`, `status`, `herdId`, `corralId`, `source`, `ageRange` e `imageUrl`. | `201` con el `AnimalResource` creado. | `400` datos inválidos; `401`; `403`. |
| US-012 | PUT | `curl -X PUT "{BASE_URL}/api/v1/animals/1" -H "Authorization: Bearer <token>" -H "Content-Type: application/json" -d '{...}'` | Ruta: `id`. Body `CreateAnimalResource`. | `200` con el animal actualizado. | `404`; `400`; `401`; `403`. |
| US-012 | DELETE | `curl -X DELETE "{BASE_URL}/api/v1/animals/1" -H "Authorization: Bearer <token>"` | Ruta: `id`. | `204` sin contenido. | `404`; `401`; `403`. |
| US-011 | POST | `curl -X POST "{BASE_URL}/api/v1/animals/bulk" -H "Authorization: Bearer <token>" -H "Content-Type: application/json" -d '{"species":"Bovino","breed":"Holstein","gender":"Hembra","weight":120.0,"status":"Saludable","herdId":1,"corralId":1,"quantity":10}'` | Body `CreateAnimalBatchResource`: los datos comunes del lote y `quantity` (de 1 a 500). | `201` con la lista de animales creados; el servidor asigna un código a cada uno. | `400` si el lote es inválido; `401`; `403`. |
| US-012 | PATCH | `curl -X PATCH "{BASE_URL}/api/v1/animals/bulk-status" -H "Authorization: Bearer <token>" -H "Content-Type: application/json" -d '{"animalIds":[1,2],"status":"Observacion"}'` | Body `UpdateAnimalsStatusResource`: `animalIds` y `status`. | `200` con la lista de animales actualizados. | `400` si no hay animales seleccionados o falta el estado; `401`; `403`. |
| US-012 | DELETE | `curl -X DELETE "{BASE_URL}/api/v1/animals/bulk" -H "Authorization: Bearer <token>" -H "Content-Type: application/json" -d '{"animalIds":[1,2]}'` | Body `DeleteAnimalsResource`: `animalIds`. La baja masiva envía cuerpo JSON. | `204` sin contenido. | `400` si no hay animales seleccionados; `401`; `403`. |
| US-045 | POST | `curl -X POST "{BASE_URL}/api/v1/animals/upload-image" -H "Authorization: Bearer <token>" -F "file=@foto.jpg"` | Formulario `multipart/form-data` con la parte `file` (JPEG, PNG, WEBP o GIF). | `200` con `{"url":"/uploads/animals/<guid>.jpg"}`; esa ruta, relativa a la raíz del servidor, se guarda en `imageUrl` del animal. | `400` si falta el archivo o su formato no es válido; `401`; `403`. |

**Registros sanitarios** (`/health-events`; Rancher y Veterinarian)

Ejemplo de `HealthEventResource`: `{"id":1,"animalId":1,"type":"Vacuna","date":"2026-05-10","description":"Vacuna anual contra carbunco","veterinarian":"Dra. Ana Lopez","diagnosis":"Control preventivo","treatment":"Aplicacion de vacuna","prescription":"Refuerzo anual","followUp":"Revisar proxima campana","nextDueDate":"2026-11-10"}`.

| Related story | HTTP | Call syntax | Parameters / body | Success response | Error responses |
|---|---|---|---|---|---|
| US-014 | GET | `curl "{BASE_URL}/api/v1/health-events" -H "Authorization: Bearer <token>"` | Ninguno. | `200` con la lista de registros sanitarios. | `401`; `403`. |
| US-014 | GET | `curl "{BASE_URL}/api/v1/health-events/1" -H "Authorization: Bearer <token>"` | Ruta: `id`. | `200` con el `HealthEventResource`. | `404`; `401`. |
| US-015, US-016 | POST | `curl -X POST "{BASE_URL}/api/v1/health-events" -H "Authorization: Bearer <token>" -H "Content-Type: application/json" -d '{"animalId":1,"type":"Incidencia","date":"2026-10-01","description":"Cojera en la pata trasera","veterinarian":"Dra. Ana Lopez","diagnosis":"","treatment":"","prescription":"","followUp":"","nextDueDate":null}'` | Body `CreateHealthEventResource`: `animalId`, `type`, `date`, `description`, `veterinarian`, `diagnosis`, `treatment`, `prescription`, `followUp` y `nextDueDate` (opcional). | `201` con el `HealthEventResource` creado. | `400` datos inválidos; `401`; `403`. |
| US-015 | PUT | `curl -X PUT "{BASE_URL}/api/v1/health-events/1" -H "Authorization: Bearer <token>" -H "Content-Type: application/json" -d '{...}'` | Ruta: `id`. Body `CreateHealthEventResource`. | `200` con el registro actualizado. | `404`; `400`; `401`; `403`. |
| US-015 | DELETE | `curl -X DELETE "{BASE_URL}/api/v1/health-events/1" -H "Authorization: Bearer <token>"` | Ruta: `id`. | `204` sin contenido. | `404`; `401`; `403`. |

Una solicitud con un rol no autorizado responde `403`: las pruebas de integración (sección 4.2.1.5) detectaron que antes respondía `500` y se corrigió en `AuthorizeAttribute`. El servidor aún devuelve todos los registros sin filtrarlos por usuario; ese punto se corregirá en el backend y mientras tanto la aplicación filtra en el cliente.

- **Web Services repository:** <https://github.com/ADM-1ACC0238-2620-13975-Grupo01/anitec-backend/tree/main>
- **Swagger:** <https://anitec-backend-android.onrender.com/swagger/index.html>
- **API publicada:** <https://anitec-backend-android.onrender.com>
- **Documentation commits:** `125d53e` (configuración inicial de Swagger/OpenAPI y controllers) y `9831844` (endpoints de corrales y operaciones masivas de animales).
- **Interaction screenshots:** las capturas siguientes muestran llamadas con datos de muestra desde Swagger.


<div align="center">
  <img src="../../assets/chapter-4/backend/swagger-ui.png" width="800">
  <p><i>Figura 4.2.1.7.1. Evidencia de documentación de servicios: Swagger UI con Authorize y catálogo de endpoints Animals / Authentication. Fuente: elaboración propia.</i></p>
</div>

La figura respalda que OpenAPI está disponible públicamente y que los endpoints del Sprint 1 pueden ejercitarse desde Swagger.

<div align="center">
  <img src="../../assets/chapter-4/backend/LoginToken.png" alt="Captura pendiente: POST /authentication/sign-in con datos de muestra y su respuesta con token" width="800">
  <p><i>Figura 4.2.1.7.2. POST /authentication/sign-in con datos de muestra y su respuesta con token. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/backend/getAnimals.png" alt="Captura pendiente: GET /animals autorizado con el token" width="800">
  <p><i>Figura 4.2.1.7.3. GET /animals autorizado con el token. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/backend/postAnimales.png" alt="Captura pendiente: POST /animals con un animal de muestra y su respuesta 201" width="800">
  <p><i>Figura 4.2.1.7.4. POST /animals con un animal de muestra y su respuesta 201. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/backend/SinToken.png" alt="Captura pendiente: Respuesta 401 al llamar un endpoint sin token" width="800">
  <p><i>Figura 4.2.1.7.5. Respuesta 401 al llamar un endpoint sin token. Fuente: elaboración propia.</i></p>
</div>

<a id="toc-4-2-1-8-software-deployment-evidence-for-sprint-review"></a>

### 4.2.1.8. Software Deployment Evidence for Sprint Review

Durante el Sprint 1 se prepararon los entornos de publicación de cada producto: el backend se configuró como servicio Docker en Render con una base de datos MySQL externa, la Landing Page se publicó en GitHub Pages y el proyecto de Firebase tiene registradas las aplicaciones Android y Flutter para su distribución. Las cuentas utilizadas son la organización de GitHub del equipo, Render, Firebase (plan Spark) y el proveedor de MySQL. Los pasos detallados de cada despliegue se describen en la sección 4.1.4.

| Product | Platform | Configuration performed | Version / Commit | Public URL or Release | Status |
|---|---|---|---|---|---|
| Landing Page | GitHub Pages | Repositorio `anitec-landing-page`; publicación desde la rama `main` y la carpeta raíz. | Commit `d774fb1` | <https://adm-1acc0238-2620-13975-grupo01.github.io/anitec-landing-page/> | Publicada |
| Web Services | Render | Docker con el `Dockerfile` de la raíz; variables `ASPNETCORE_ENVIRONMENT`, `ConnectionStrings__DefaultConnection`, `TokenSettings__Secret` y `StripeSettings__*`; MySQL externo; migraciones automáticas al iniciar. | Commit `2d08551` | API: <https://anitec-backend-android.onrender.com>. Swagger: <https://anitec-backend-android.onrender.com/swagger/index.html> | Publicado |
| Android | Firebase App Distribution | Proyecto «Anitec» y aplicación «AniTec Android» registrada con el paquete `com.anitec.platform` (App ID `1:969068830564:android:5a2dafc1bf9a7f44652471`). Firma, grupo de testers y release pendientes. | `versionName` `0.1.0`; commit `8ade432` | Release pendiente | Registrada; release pendiente |
| Flutter | Firebase App Distribution | Aplicación «AniTec Flutter» registrada como aplicación de Apple en el proyecto. El desarrollo y la distribución están pendientes. | Pendiente | Release pendiente | Pendiente (placeholder) |

**Pasos ejecutados (Web Services):**

1. Publicar el Web Service `anitec-backend-android` en Render con runtime Docker desde la rama `main` de `anitec-backend`.
2. Configurar los secretos de conexión MySQL, JWT y Stripe en Environment (los valores no se exponen en el informe).
3. Verificar el estado **Live** en Events y la disponibilidad de la URL primaria (<https://anitec-backend-android.onrender.com>).
4. Comprobar que Swagger UI responde en `/swagger/index.html` (<https://anitec-backend-android.onrender.com/swagger/index.html>). Verificado: responde `200`, y los endpoints protegidos responden `401` sin token.

<div align="center">
  <img src="../../assets/chapter-4/backend/render-backend-live.png" width="800">
  <p><i>Figura 4.2.1.8.1. Evidencia de despliegue: anitec-backend-android en estado Live en Render. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/backend/render-backend-environment.png" width="800">
  <p><i>Figura 4.2.1.8.2. Evidencia de configuración de despliegue: variables de entorno del backend con valores ocultos. Fuente: elaboración propia.</i></p>
</div>

Las capturas demuestran la publicación del servicio y la administración de secretos fuera del código fuente.

**Pasos ejecutados (aplicaciones móviles):**

1. Crear el proyecto «Anitec» en Firebase Console.
2. Registrar la aplicación Android con el nombre de paquete `com.anitec.platform` y la aplicación Flutter (Figuras 4.1.4.4 y 4.1.4.5).
3. Generar la compilación firmada de la aplicación Android y subirla a App Distribution. **Pendiente.**
4. Crear el grupo de testers (equipo y profesores) e invitarlos. **Pendiente.**

**Pasos ejecutados (Landing Page):**

1. Integrar el contenido aprobado en la rama `main`.
2. Activar GitHub Pages en **Settings → Pages**, con la rama `main` y la carpeta raíz.
3. Verificar la URL pública (<https://adm-1acc0238-2620-13975-grupo01.github.io/anitec-landing-page/>). Verificado: carga la versión de la aplicación móvil y sus imágenes responden `200`.

<div align="center">
  <img src="../../assets/chapter-4/githubLandingpage.png" alt="Captura pendiente: Configuración de GitHub Pages del repositorio de la Landing Page" width="800">
  <p><i>Figura 4.2.1.8.3. Configuración de GitHub Pages del repositorio de la Landing Page. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/Ladingconurl.png" alt="Captura pendiente: Landing Page publicada en la URL de la organización" width="800">
  <p><i>Figura 4.2.1.8.4. Landing Page publicada en la URL de la organización. Fuente: elaboración propia.</i></p>
</div>



<a id="toc-4-2-1-9-team-collaboration-insights-during-sprint"></a>

### 4.2.1.9. Team Collaboration Insights during Sprint

Esta sección interpreta la participación del equipo a partir de commits, Pull Requests, revisiones y colaboración por producto. Las métricas se analizan en contexto y no se usan de forma aislada para medir aporte. La tabla registra la contribución de cada integrante a partir de las tareas del Sprint Backlog (sección 4.2.1.3) y de los commits de los repositorios del proyecto, y se complementa con los analíticos de colaboración de GitHub.

| Integrante | Productos / aspectos | Contribución en el sprint | Evidencia | Reflexión |
|---|---|---|---|---|
| Sebastian Martin Beingolea Montalvo | Backend, aplicación Android (red y seguridad) y documentación | Implementó el cliente REST de la aplicación, agregó los corrales y las operaciones masivas al backend, documentó los endpoints con OpenAPI, cifró el token de sesión y creó la suite de pruebas automatizadas del backend. Documentó la evidencia del despliegue del backend en Render y de Swagger. | Tareas T-006, T-008, T-009, T-014 y T-028. Informe: `d09a7e2` | Trabajar el cliente REST, los corrales del backend y las pruebas me mostró que un contrato de API estable permite que la aplicación y el servicio avancen por separado. Aprendí a proteger el token de sesión con Tink y Android Keystore, a documentar con OpenAPI y a comprobar con pruebas unitarias, de integración y BDD que cada endpoint responde lo acordado. Me llevo la importancia de probar también los casos de error, como un rol sin permiso, y no solo el camino feliz. |
| Josep Eliu Melgarejo Quiroz | Aplicación Android e informe | Implementó la caché local con Room, la navegación por rol con el filtrado de datos del usuario, la lista de animales con búsqueda y filtro, el registro individual y masivo de animales y la fotografía del animal. Mantiene la estructura del informe y su generación. | Tareas T-007, T-013, T-017, T-018 y T-025. anitec-android: `2f3b903`, `8ade432`. anitec-backend: `125d53e`, `9831844`. anitec-frontend: `f12794d`. anitec-landing-page: `2a88184`. Informe: `cd00045` | Diseñar la caché con Room, limpiarla al cerrar sesión y filtrar los datos del usuario en la aplicación me enseñó que la seguridad de la información también depende de cómo se guarda y se muestra en el teléfono. El registro masivo y la fotografía me obligaron a cuidar los límites, como de 1 a 500 animales o el tamaño de la imagen, y a mostrar errores que el usuario pueda corregir. Queda pendiente que el backend filtre por usuario para no depender solo de la aplicación. |
| Saul Ortega Muñoz | Landing Page, aplicación Android (acceso y ficha del animal) y documentación | Diseñó el wireframe y el mock-up móvil de la Landing Page, implementó sus secciones, el diseño responsive y el selector de idioma, las pantallas de registro e inicio de sesión, el mantenimiento de la sesión y la ficha técnica del animal. Documentó las evidencias de desarrollo, ejecución, pruebas y despliegue de la Landing Page. | Tareas T-001, T-002, T-003, T-010, T-011, T-012 y T-020. Informe: `e2d2cd6`, `9beefe6`, `bbff341`, `c150062` | Diseñar una Landing Page adaptable y bilingüe, y las pantallas de acceso, me enseñó a cuidar el primer contacto del usuario con mensajes claros, validaciones y formas de recuperarse de un error. Implementar la sesión persistente y su cierre al vencer el token me mostró que la seguridad también forma parte de la experiencia. La ficha técnica me dejó la lección de presentar mucha información de forma legible en pantallas pequeñas. |
| Luciana Celeste Sanchez Silva | Diseño UX/UI y aplicación Android (fincas, corrales y sanidad) | Elaboró los mock-ups móviles de Android y Flutter, los organizó por aplicación y rol, y construyó las pantallas de fincas, corrales y registros sanitarios con sus formularios y validaciones. Actualizó el Product Backlog. | Tareas T-015, T-016, T-021, T-022, T-023, T-024 y T-029. Informe: `da15998`, `cd83263`, `5f57a44` | Llevar los mock-ups de Figma a pantallas reales me mostró que un diseño debe prever los estados vacíos, los errores y las confirmaciones antes de implementarse. Reutilizar los mismos componentes en fincas, corrales y sanidad dio coherencia visual y ahorró trabajo. Aprendí que el diseño y el desarrollo deben revisarse juntos para que lo prototipado sea lo que usa el ganadero. |
| Giuseppe Villanueva Rodriguez | Aplicación Android (base y pruebas), configuración y despliegue móvil | Creó el proyecto Android y organizó el código por bounded contexts y capas, implementó la edición y eliminación de animales y la pantalla de inicio del ganadero, escribió las pruebas unitarias e instrumentadas de Android y registró las aplicaciones en Firebase. Actualizó la configuración del entorno y del despliegue (4.1). | Tareas T-004, T-005, T-019, T-026, T-027 y T-030. Informe: `0cf6d49`, `66de467`, `e01ac6f`, `a5835de` | Crear el proyecto y organizar el código por capas me enseñó que una estructura clara facilita el trabajo de todos y hace posibles las pruebas. Escribir pruebas del dominio, de los casos de uso y de los ViewModels me ayudó a detectar errores antes de añadir nuevas pantallas, y registrar las aplicaciones en Firebase me dio una visión completa del camino hasta la distribución. Me llevo que probar desde el inicio reduce el costo de los cambios. |

Los repositorios del proyecto son:

- Informe: <https://github.com/ADM-1ACC0238-2620-13975-Grupo01/Informe>
- Landing Page: <https://github.com/ADM-1ACC0238-2620-13975-Grupo01/anitec-landing-page>
- Web Services: <https://github.com/ADM-1ACC0238-2620-13975-Grupo01/anitec-backend>
- Aplicación web: <https://github.com/ADM-1ACC0238-2620-13975-Grupo01/anitec-frontend>
- Android: <https://github.com/ADM-1ACC0238-2620-13975-Grupo01/anitec-android>

Las capturas siguientes muestran los analíticos de colaboración y de commits de GitHub (**Insights → Contributors** y **Insights → Commits**) de cada repositorio.

<div align="center">
  <img src="../../assets/chapter-4/commitsInformeSprint1.png" alt="Captura pendiente: Analíticos de colaboración del repositorio Informe" width="800">
  <p><i>Figura 4.2.1.9.1. Analíticos de colaboración del repositorio Informe. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/captura-pendiente.svg" alt="Captura pendiente: Analíticos de colaboración del repositorio anitec-android" width="800">
  <p><i>Figura 4.2.1.9.2. Analíticos de colaboración del repositorio anitec-android. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/CommitsbackSprint1.png" alt="Captura pendiente: Analíticos de colaboración del repositorio anitec-backend" width="800">
  <p><i>Figura 4.2.1.9.3. Analíticos de colaboración del repositorio anitec-backend. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/CommitLandingSprint1.png" alt="Captura pendiente: Analíticos de colaboración del repositorio anitec-landing-page" width="800">
  <p><i>Figura 4.2.1.9.4. Analíticos de colaboración del repositorio anitec-landing-page. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/CommitsFrontSprint1.png" alt="Captura pendiente: Analíticos de colaboración del repositorio anitec-frontend" width="800">
  <p><i>Figura 4.2.1.9.5. Analíticos de colaboración del repositorio anitec-frontend. Fuente: elaboración propia.</i></p>
</div>

**Interpretación de los analíticos.** Los analíticos de GitHub muestran la actividad de cada repositorio durante el sprint y se leen junto con las tareas del Sprint Backlog (sección 4.2.1.3), porque el número de commits por autor no mide por sí solo el aporte de cada integrante. El trabajo se concentró en la aplicación Android, que reúne 143 de las 205 horas estimadas del sprint (cerca del 70 %) y en la que participaron los cinco integrantes: Josep Melgarejo con 42 horas, Giuseppe Villanueva con 36, Luciana Sanchez con 29, Saul Ortega con 22 y Sebastian Beingolea con 14. El resto se repartió por producto: el backend, con 26 horas a cargo de Sebastian Beingolea (corrales, documentación OpenAPI y pruebas automatizadas); la Landing Page, con 18 horas a cargo de Saul Ortega; los mock-ups móviles, con 12 horas de Luciana Sanchez; y el registro de las aplicaciones en Firebase, con 6 horas de Giuseppe Villanueva. Cada integrante lideró un aspecto y colaboró en al menos otro, como indica la matriz de la sección 4.2.1.2, y el reparto por persona quedó entre 40 y 42 horas.

**Conclusión del trabajo en equipo.** Al cierre del Sprint 1 el equipo entregó la Landing Page publicada, el backend desplegado y respaldado por 104 pruebas automatizadas, y una aplicación Android que permite registrarse, iniciar sesión y gestionar fincas, corrales, animales y registros sanitarios. De las 30 tareas del sprint, 28 quedaron en Done y 2 en To-Review, y las historias US-007 y US-012 quedaron parciales: falta que el backend filtre la información por usuario y que se implemente el archivado de animales. El trabajo por productos con un líder por aspecto permitió avanzar en paralelo en Android, backend, Landing Page y diseño. Como aprendizajes, el equipo destaca definir el alcance móvil antes de implementar, probar desde el inicio y mantener alineados el informe y el código. Para el Sprint 2, el foco será la vista del veterinario, la colaboración con el ganadero, las actividades, el trabajo sin conexión y la identificación de animales con la cámara.
