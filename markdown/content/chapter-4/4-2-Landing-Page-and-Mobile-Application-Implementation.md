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

### 4.2.1.4. Development Evidence for Sprint Review

Esta sección registrará únicamente commits que contribuyan al alcance comprometido. Cada evidencia debe poder localizarse en el repositorio y relacionarse con una historia o tarea.

| Repository | Branch | Commit Id | Commit Message | Commit Message Body | Committed on |
|---|---|---|---|---|---|
| anitec-backend | main | `125d53e` | chore: add initial commit with all project files | Incorpora la solución `Anitec.Platform` con bounded contexts (Iam, Profiles, Livestock, Sanitary, Financial, Activities, Analytics, Devices, Metrics, Subscriptions, Clients, Shared), controllers REST, EF Core + MySQL, JWT/BCrypt, Swagger y `Dockerfile`. | 2026-09-04 |
| anitec-backend | main | `9831844` | chore: big update to add corrals and animal corral relationship | Extiende Livestock con corrales (`CorralsController`), relación animal–corral, operaciones bulk de animales y validaciones de resources. | 2026-09-30 |
| anitec-landing-page | main | `2a88184`| chore: add initial project files | Agrega la estructura inicial del proyecto de la Landing Page, incluyendo la configuración base, componentes principales y archivos necesarios para el desarrollo de la interfaz de presentación de AniTec. | 2026-09-04 |
| anitec-android | main | `2f3b903` | feat: add Android project foundation and authentication | Implementa la estructura base nativa usando Clean Architecture. Integra `AuthApiService`, `AuthRepositoryImpl` y persistencia segura de tokens. | 2026-10-01 |
| anitec-android | main | `8ade432` | feat: add livestock management, health records and rancher dashboard | Refactoriza la capa de dominio y la persistencia local integrando la jerarquía de hatos y animales. Asegura soporte Offline-First para registro. | 2026-10-01 |
| Informe | main | `c8b8be7` | docs: update report complete generation | Agrega la estructura inicial del informe de proyecto con sus capítulos, títulos y diagramas de arquitectura C4. | 2026-09-16 |

<a id="toc-4-2-1-5-testing-suite-evidence-for-sprint-review"></a>

> **Pendiente de completar:** agregar commits de Landing Page, Android, Flutter e informe según el alcance real. Las filas anteriores corresponden solo al backend.

<a id="toc-4-2-1-5-testing-suite-evidence-for-sprint-review"></a>

### 4.2.1.5. Testing Suite Evidence for Sprint Review

La evidencia incluirá pruebas automatizadas relacionadas con las historias del sprint. Los escenarios BDD se expresarán en archivos `.feature` y sus pasos correspondientes.

| Test ID     | Product | Type | Class / Feature | Behavior | Related Story | Result |
|-------------|---|---|---|---|---|---|
| TEST-BE-001 | Web Services | Exploratoria / contrato | Swagger UI (`/swagger`) | Validar disponibilidad de OpenAPI y endpoints Animals / Authentication en el entorno publicado | Autenticación y registro esencial de animales / sanidad | Completado — Figura 4.2.1.6.1 |
| TEST-BE-002 | Web Services | Automatizada (xUnit) | **Pendiente:** no hay proyecto de pruebas en el repositorio | **Pendiente:** incorporar suite xUnit | — | No aplicable aún |
| TEST-LP-003 | Landing Page | Funcional | Navigation | Validar la navegación entre las distintas secciones de la Landing Page. | Navegación y experiencia de usuario | Completado |
| TEST-LP-004 | Landing Page | Responsive Testing | Responsive Design | Verificar la correcta adaptación de la interfaz en dispositivos móviles y escritorio. | Accesibilidad multiplataforma | Completado |

| Repository | Branch | Commit Id | Commit Message | Commit Message Body | Committed on |
|---|---|---|---|---|---|
| anitec-backend | — | — | — | **Pendiente:** no existen commits de pruebas automatizadas; el repositorio no incluye proyecto `*Tests` / xUnit. | — |
| anitec-landing-page | main | 2a88184 | chore: add initial project files | Agrega la estructura inicial del proyecto de la Landing Page, incluyendo configuración base y componentes principales para el desarrollo de la interfaz | 2026-09-04 |

> **Pendiente de completar (backend):** cuando exista proyecto xUnit, ejecutar `dotnet test`, adjuntar captura del resultado en `markdown/assets/chapter-4/backend/` y registrar el commit. Las filas de Landing / Android / Flutter las completa cada responsable.

<a id="toc-4-2-1-6-execution-evidence-for-sprint-review"></a>

### 4.2.1.6. Execution Evidence for Sprint Review

La evidencia de ejecución mostrará el resultado integrado del Sprint 1 mediante capturas identificables y un video que explique el recorrido implementado.

| Producto | Vista o flujo | Entorno / dispositivo | Evidencia                           | Estado     |
|---|---|---|-------------------------------------|------------|
| Landing Page | Página principal y responsive | Navegador de escritorio y móvil | Figura 4.2.1.6.2 (`landing_despliegue.png`)       | Completado |
| Android | Autenticación y funciones core comprometidas | Emulador y dispositivo físico | Pendiente de captura                | Pendiente  |
| Flutter | Autenticación y funciones core comprometidas | Dispositivo o emulador objetivo | Pendiente de captura                | Pendiente  |
| Web Services | Swagger UI: documentación OpenAPI de la API publicada | Navegador contra <https://anitec-backend.onrender.com/swagger/index.html> | Figura 4.2.1.6.1 (`swagger-ui.png`) | Completado |
| Integración | Consumo de API y manejo de errores | Aplicaciones contra backend vigente | Pendiente de captura                | Pendiente  |

<div align="center">
  <img src="../../assets/chapter-4/backend/swagger-ui.png" width="800">
  <p><i>Figura 4.2.1.6.1. Swagger UI de AniTec Platform en Render, con endpoints de Animals y Authentication. Fuente: elaboración propia.</i></p>
</div>

La captura demuestra que la documentación interactiva carga desde el entorno publicado y expone los contratos REST usados por el Sprint 1.

- **Execution video:** **Pendiente de completar:** URL del video.
- **Timing:** **Pendiente:** inicio y duración de cada demostración.

<div align="center">
  <img src="../../assets/chapter-4/landing_despliegue.png" width="800">
  <p><i>Figura 4.2.1.6.2. Landing de AniTec desplegado, Fuente: elaboración propia.</i></p>
</div>

Las capturas muestran la implementación de la Landing Page de AniTec en navegadores. Se verificó la correcta visualización del contenido, la navegación entre secciones y la adaptación responsive de la interfaz para distintos tamaños de pantalla.

- **Execution video:** 
https://upcedupe-my.sharepoint.com/:v:/g/personal/u20231c019_upc_edu_pe/IQBmZ8UxBU5zToJUnS4AN161Aa9ocLvYJcSFOja0Zogn_tE?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=V8q9eK
- **Timing:** 0:00 - 1:48 min
  <a id="toc-4-2-1-7-services-documentation-evidence-for-sprint-review"></a>

### 4.2.1.7. Services Documentation Evidence for Sprint Review

Se documentarán los endpoints utilizados por las historias comprometidas y su disponibilidad mediante OpenAPI. La documentación interactiva se genera con Swashbuckle (`Program.cs`: `AddSwaggerGen`, `UseSwagger`, `UseSwaggerUI`) e incluye esquema Bearer JWT.

| Related Story | HTTP | Endpoint | Parameters / Body | Success Response | Error Responses | Documentation URL |
|---|---|---|---|---|---|---|
| Autenticación — registro | POST | `/api/v1/authentication/sign-up` | Body `SignUpResource`: `username`, `password`, `fullName`, `role` (`Rancher` \| `Veterinarian`) | `200` — `{ "message": "..." }` | `400` — usuario no creado / datos inválidos | <https://anitec-backend.onrender.com/swagger/index.html> |
| Autenticación — inicio de sesión | POST | `/api/v1/authentication/sign-in` | Body `SignInResource`: `username`, `password` | `200` — `AuthenticatedUserResource` (`id`, `username`, `fullName`, `role`, `token`) | `400` — credenciales inválidas | Idem |
| Animales — listar | GET | `/api/v1/animals` | Header `Authorization: Bearer <JWT>` (roles Rancher, Veterinarian) | `200` — lista de `AnimalResource` | `401` sin token; `403` rol no autorizado | Idem |
| Animales — obtener por id | GET | `/api/v1/animals/{id}` | Path `id`; Bearer JWT | `200` — `AnimalResource` | `404` no encontrado; `401`/`403` | Idem |
| Animales — crear | POST | `/api/v1/animals` | Bearer JWT (Rancher); Body `CreateAnimalResource`: `tag`, `name`, `species`, `breed`, `gender`, `birthDate`, `weight`, `status`, `herdId`, `corralId`, `source`, `ageRange`, `imageUrl` | `201` — `AnimalResource` | `400` validación; `401`/`403` | Idem |
| Animales — actualizar | PUT | `/api/v1/animals/{id}` | Path `id`; Body `CreateAnimalResource`; Bearer (Rancher) | `200` — `AnimalResource` | `400`; `404`; `401`/`403` | Idem |
| Animales — eliminar | DELETE | `/api/v1/animals/{id}` | Path `id`; Bearer (Rancher) | `204` | `404`; `401`/`403` | Idem |
| Sanidad — listar eventos | GET | `/api/v1/health-events` | Bearer JWT (Rancher, Veterinarian) | `200` — lista de `HealthEventResource` | `401`/`403` | Idem |
| Sanidad — crear evento | POST | `/api/v1/health-events` | Body `CreateHealthEventResource`: `animalId`, `type`, `date`, `description`, `veterinarian`, `diagnosis`, `treatment`, `prescription`, `followUp`, `nextDueDate` | `201` — `HealthEventResource` | `401`/`403`; errores de dominio | Idem |
| Rebaños — listar (soporte) | GET | `/api/v1/herds` | Bearer JWT | `200` — lista de herds | `401`/`403` | Idem |
| Corrales — listar (soporte) | GET | `/api/v1/corrals` | Bearer JWT | `200` — lista de corrals | `401`/`403` | Idem |

- **Web Services repository:** <https://github.com/ADM-1ACC0238-2620-13975-Grupo01/anitec-backend>
- **Swagger:** <https://anitec-backend.onrender.com/swagger/index.html>
- **Documentation commits:** `125d53e` (configuración inicial Swagger/OpenAPI y controllers); `9831844` (documentación/endpoints de corrals y ampliación de animals).
- **Interaction screenshots:** Swagger UI publicado (Figura 4.2.1.7.1). **Pendiente:** capturas adicionales de `sign-in` exitoso, llamada con Bearer token y respuesta `401`/`400`.

<div align="center">
  <img src="../../assets/chapter-4/backend/swagger-ui.png" width="800">
  <p><i>Figura 4.2.1.7.1. Evidencia de documentación de servicios: Swagger UI con Authorize y catálogo de endpoints Animals / Authentication. Fuente: elaboración propia.</i></p>
</div>

La figura respalda que OpenAPI está disponible públicamente y que los endpoints del Sprint 1 pueden ejercitarse desde Swagger.

<a id="toc-4-2-1-8-software-deployment-evidence-for-sprint-review"></a>

### 4.2.1.8. Software Deployment Evidence for Sprint Review

La evidencia explicará la configuración realizada durante el sprint y demostrará la disponibilidad de cada producto aplicable.

| Product | Platform | Configuration performed | Version / Commit | Public URL or Release | Status |
|---|---|---|---|---|---|
| Landing Page | GitHub Pages | Workflow o rama pendientes | Commit pendiente | URL pendiente | Pendiente |
| Web Services | Render | Docker; variables `ASPNETCORE_ENVIRONMENT`, `ConnectionStrings__DefaultConnection`, `TokenSettings__Secret`, `StripeSettings__*`; MySQL externo | Deploy Live verificado en Events (Figuras 4.2.1.8.1–4.2.1.8.2) | <https://anitec-backend.onrender.com> · Swagger: <https://anitec-backend.onrender.com/swagger/index.html> | Live |
| Android | Firebase App Distribution | Firma, aplicación y testers pendientes | Versión y commit pendientes | Release pendiente | Pendiente |
| Flutter | Firebase App Distribution | Plataforma, aplicación y testers pendientes | Versión y commit pendientes | Release pendiente | Pendiente |

**Pasos ejecutados (Web Services):**

1. Publicar el Web Service `anitec-backend` en Render con runtime Docker.
2. Configurar secretos de conexión MySQL, JWT y Stripe en Environment (valores no expuestos en el informe).
3. Verificar estado **Live** en Events y disponibilidad de la URL primaria.
4. Comprobar que Swagger UI responde en `/swagger/index.html`.

<div align="center">
  <img src="../../assets/chapter-4/backend/render-backend-live.png" width="800">
  <p><i>Figura 4.2.1.8.1. Evidencia de despliegue: anitec-backend en estado Live en Render. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/backend/render-backend-environment.png" width="800">
  <p><i>Figura 4.2.1.8.2. Evidencia de configuración de despliegue: variables de entorno del backend con valores ocultos. Fuente: elaboración propia.</i></p>
</div>

Las capturas demuestran la publicación del servicio y la administración de secretos fuera del código fuente. Landing, Android y Flutter quedan a cargo de sus responsables.

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
