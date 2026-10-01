<a id="toc-4-2-landing-page-mobile-application-implementation"></a>

# 4.2. Landing Page & Mobile Application Implementation

Esta sección registra el avance de la Landing Page, los Web Services y las aplicaciones móviles mediante sprints. Cada iteración relaciona el Product Backlog con tareas, responsables, commits, pruebas, documentación, ejecución y despliegue verificable.

<a id="toc-4-2-1-sprint-1"></a>

## 4.2.1. Sprint 1

El Sprint 1 corresponde al TB1 y establece la base ejecutable de los productos de AniTec. El alcance candidato considera la Landing Page desplegada, el backend al 70 %, la configuración de Android y Flutter y las pantallas core de autenticación y gestión de animales. El compromiso definitivo se registrará después del Sprint Planning.

<a id="toc-4-2-1-1-sprint-planning-1"></a>

### 4.2.1.1. Sprint Planning 1

La reunión de planificación definirá el Sprint Goal, la capacidad del equipo y el subconjunto de historias que puede completarse con evidencia verificable durante la iteración.

<table>
  <tr><th>Sprint #</th><td>Sprint 1</td></tr>
  <tr><th colspan="2">Sprint Planning Background</th></tr>
  <tr><th>Date</th><td><b>Pendiente:</b> YYYY-MM-DD</td></tr>
  <tr><th>Time</th><td><b>Pendiente:</b> HH:MM AM/PM</td></tr>
  <tr><th>Location</th><td><b>Pendiente:</b> ubicación física o plataforma virtual</td></tr>
  <tr><th>Prepared By</th><td><b>Pendiente:</b> responsable del acta</td></tr>
  <tr><th>Attendees</th><td>Beingolea Montalvo, Sebastian Martin / Melgarejo Quiroz, Josep Eliu / Ortega Muñoz, Saul / Sanchez Silva, Luciana Celeste / Villanueva Rodriguez, Giuseppe</td></tr>
  <tr><th>Sprint 0 Review Summary</th><td>No aplica como sprint de implementación previo. La línea base comprende el informe hasta el capítulo II, la Landing Page, la API existente y los artefactos de arquitectura.</td></tr>
  <tr><th>Sprint 0 Retrospective Summary</th><td>El equipo deberá iniciar la iteración con responsabilidades explícitas, trazabilidad entre historias y tareas, y evidencia continua en repositorios.</td></tr>
  <tr><th colspan="2">Sprint Goal & User Stories</th></tr>
  <tr><th>Sprint 1 Goal</th><td><b>Pendiente de acordar.</b> Propuesta: ofrecer una primera experiencia móvil ejecutable para que un usuario pueda autenticarse y consultar o registrar información esencial de animales, respaldada por la API pública y la Landing Page desplegada.</td></tr>
  <tr><th>Sprint 1 Velocity</th><td><b>Pendiente:</b> capacidad acordada en Story Points</td></tr>
  <tr><th>Sum of Story Points</th><td><b>Pendiente:</b> suma de las historias finalmente comprometidas</td></tr>
</table>

El Product Backlog asigna al Sprint 1 los siguientes candidatos. La suma total es 96 Story Points; por ello, el equipo debe confirmar durante el planning cuáles se comprometen según su capacidad y mantener el resto fuera del Sprint Backlog si no puede completarlos.

| ID | Título | Story Points |
|---|---|---:|
| US-001 | Comprender la propuesta de valor de AniTec | 3 |
| US-002 | Conocer las soluciones para cada segmento | 3 |
| US-003 | Acceder a una landing page adaptable e internacionalizada | 5 |
| TS-001 | Configurar la aplicación Android nativa | 5 |
| TS-002 | Configurar la aplicación multiplataforma con Flutter | 5 |
| TS-003 | Definir la arquitectura móvil por capas y bounded contexts | 5 |
| TS-013 | Adaptar y documentar los servicios backend para móviles | 8 |
| US-004 | Registrar una cuenta según el rol | 5 |
| US-005 | Iniciar sesión | 3 |
| US-006 | Mantener y finalizar la sesión móvil | 3 |
| US-007 | Acceder únicamente a información autorizada | 5 |
| TS-008 | Proteger credenciales y datos de sesión | 5 |
| US-008 | Consultar las fincas registradas | 3 |
| US-009 | Registrar y actualizar una finca | 5 |
| US-010 | Consultar y buscar animales | 5 |
| US-011 | Registrar un animal | 5 |
| US-012 | Actualizar o archivar un animal | 5 |
| US-013 | Consultar el detalle de un animal | 3 |
| TS-004 | Integrar las aplicaciones con la API REST interna | 5 |
| TS-005 | Implementar persistencia local segura en Android | 5 |
| SP-001 | Investigar identificación de animales con Google ML Kit | 5 |

<a id="toc-4-2-1-2-aspect-leaders-and-collaborators"></a>

### 4.2.1.2. Aspect Leaders and Collaborators

La matriz LACX indicará un líder (L) y los colaboradores (C) de cada aspecto comprometido. La asignación deberá coincidir con las tareas del Sprint Backlog y asegurar participación de todos los integrantes.

| Team Member | GitHub Username | UX/UI | Android | Flutter | Backend | Landing Page | Testing | Documentation & Deployment |
|---|---|---|---|---|---|---|---|---|
| Beingolea Montalvo, Sebastian Martin | smbmontalvo | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente |
| Melgarejo Quiroz, Josep Eliu | Melga1502 | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente |
| Ortega Muñoz, Saul | Ss1lent10 | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente |
| Sanchez Silva, Luciana Celeste | luccsss | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente |
| Villanueva Rodriguez, Giuseppe | Giuseppe152004 | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente |

> **Pendiente de completar:** reemplazar “Pendiente” por L, C o — después de aprobar la distribución del Sprint 1.

<a id="toc-4-2-1-3-sprint-backlog-1"></a>

### 4.2.1.3. Sprint Backlog 1

El Sprint Backlog descompone las historias comprometidas en tareas comprobables. El tablero utilizará los estados Todo, In-Process, To-Review y Done.

- **Sprint Goal:** pendiente de confirmar en el Sprint Planning.
- **Board URL:** **Pendiente de completar:** URL pública del tablero.
- **Board screenshot:** **Pendiente de completar:** captura del tablero del Sprint 1.

| Story ID | Story Title | Task ID | Task Title | Description | Hours | Assigned To | Status |
|---|---|---|---|---|---:|---|---|
| ID pendiente | Título del Product Backlog | T-001 | Tarea concreta pendiente | Resultado verificable pendiente | Pendiente | Pendiente | Todo |
| ID pendiente | Título del Product Backlog | T-002 | Tarea concreta pendiente | Resultado verificable pendiente | Pendiente | Pendiente | Todo |
| ID pendiente | Título del Product Backlog | T-003 | Tarea concreta pendiente | Resultado verificable pendiente | Pendiente | Pendiente | Todo |

| Métrica | Valor |
|---|---|
| Historias comprometidas | Pendiente |
| Story Points comprometidos | Pendiente |
| Tareas | Pendiente |
| Horas estimadas | Pendiente |
| Tareas completadas | Pendiente al cierre |

<a id="toc-4-2-1-4-development-evidence-for-sprint-review"></a>

### 4.2.1.4. Development Evidence for Sprint Review

Esta sección registrará únicamente commits que contribuyan al alcance comprometido. Cada evidencia debe poder localizarse en el repositorio y relacionarse con una historia o tarea.

| Repository | Branch | Commit Id | Commit Message | Commit Message Body | Committed on |
|---|---|---|---|---|---|
| Repositorio pendiente | Rama pendiente | SHA pendiente | Mensaje pendiente | Propósito y relación con la tarea pendientes | YYYY-MM-DD |

> **Pendiente de completar:** agregar commits de Landing Page, backend, Android, Flutter e informe según el alcance real.

<a id="toc-4-2-1-5-testing-suite-evidence-for-sprint-review"></a>

### 4.2.1.5. Testing Suite Evidence for Sprint Review

La evidencia incluirá pruebas automatizadas relacionadas con las historias del sprint. Los escenarios BDD se expresarán en archivos `.feature` y sus pasos correspondientes.

| Test ID | Product | Type | Class / Feature | Behavior | Related Story | Result |
|---|---|---|---|---|---|---|
| TEST-001 | Producto pendiente | Tipo de prueba pendiente | Ruta o clase pendiente | Comportamiento pendiente | US/TS pendiente | Pendiente |

| Repository | Branch | Commit Id | Commit Message | Commit Message Body | Committed on |
|---|---|---|---|---|---|
| Repositorio pendiente | Rama pendiente | SHA pendiente | Mensaje de prueba pendiente | Pruebas incorporadas pendientes | YYYY-MM-DD |

> **Pendiente de completar:** incluir resultados, capturas o reportes y enlaces a los archivos de pruebas.

<a id="toc-4-2-1-6-execution-evidence-for-sprint-review"></a>

### 4.2.1.6. Execution Evidence for Sprint Review

La evidencia de ejecución mostrará el resultado integrado del Sprint 1 mediante capturas identificables y un video que explique el recorrido implementado.

| Producto | Vista o flujo | Entorno / dispositivo | Evidencia | Estado |
|---|---|---|---|---|
| Landing Page | Página principal y responsive | Navegador de escritorio y móvil | Pendiente de captura | Pendiente |
| Android | Autenticación y funciones core comprometidas | Emulador y dispositivo físico | Pendiente de captura | Pendiente |
| Flutter | Autenticación y funciones core comprometidas | Dispositivo o emulador objetivo | Pendiente de captura | Pendiente |
| Integración | Consumo de API y manejo de errores | Aplicaciones contra backend vigente | Pendiente de captura | Pendiente |

- **Execution video:** **Pendiente de completar:** URL del video.
- **Timing:** **Pendiente:** inicio y duración de cada demostración.

<a id="toc-4-2-1-7-services-documentation-evidence-for-sprint-review"></a>

### 4.2.1.7. Services Documentation Evidence for Sprint Review

Se documentarán los endpoints utilizados por las historias comprometidas y su disponibilidad mediante OpenAPI.

| Related Story | HTTP | Endpoint | Parameters / Body | Success Response | Error Responses | Documentation URL |
|---|---|---|---|---|---|---|
| US/TS pendiente | Verbo HTTP pendiente | Ruta pendiente | Parámetros o resource pendientes | Código y resource pendientes | Códigos y condiciones pendientes | URL Swagger pendiente |

- **Web Services repository:** <https://github.com/ADM-1ACC0238-2620-13975-Grupo01/anitec-backend>
- **Swagger:** **Pendiente de confirmar:** URL pública vigente.
- **Documentation commits:** **Pendiente de completar:** identificadores de commits.
- **Interaction screenshots:** **Pendiente de completar:** llamadas con datos de muestra y respuestas.

<a id="toc-4-2-1-8-software-deployment-evidence-for-sprint-review"></a>

### 4.2.1.8. Software Deployment Evidence for Sprint Review

La evidencia explicará la configuración realizada durante el sprint y demostrará la disponibilidad de cada producto aplicable.

| Product | Platform | Configuration performed | Version / Commit | Public URL or Release | Status |
|---|---|---|---|---|---|
| Landing Page | GitHub Pages | Workflow o rama pendientes | Commit pendiente | URL pendiente | Pendiente |
| Web Services | Render | Build, variables y base de datos pendientes | Commit pendiente | URL y Swagger pendientes | Pendiente |
| Android | Firebase App Distribution | Firma, aplicación y testers pendientes | Versión y commit pendientes | Release pendiente | Pendiente |
| Flutter | Firebase App Distribution | Plataforma, aplicación y testers pendientes | Versión y commit pendientes | Release pendiente | Pendiente |

> **Pendiente de completar:** insertar capturas y explicar los pasos efectivamente ejecutados durante el Sprint 1.

<a id="toc-4-2-1-9-team-collaboration-insights-during-sprint"></a>

### 4.2.1.9. Team Collaboration Insights during Sprint

Esta sección interpretará la participación del equipo a partir de commits, Pull Requests, revisiones y colaboración por producto. Las métricas se analizarán en contexto y no se usarán de forma aislada para medir aporte.

| Integrante | Productos / aspectos | Contribución verificable | Evidencia | Reflexión |
|---|---|---|---|---|
| Sebastian Martin Beingolea Montalvo | Pendiente | Pendiente | Pendiente | Pendiente |
| Josep Eliu Melgarejo Quiroz | Pendiente | Pendiente | Pendiente | Pendiente |
| Saul Ortega Muñoz | Pendiente | Pendiente | Pendiente | Pendiente |
| Luciana Celeste Sanchez Silva | Pendiente | Pendiente | Pendiente | Pendiente |
| Giuseppe Villanueva Rodriguez | Pendiente | Pendiente | Pendiente | Pendiente |

> **Pendiente de completar:** incorporar analíticos de GitHub por repositorio, capturas de colaboración y conclusiones del equipo al cierre del sprint.
