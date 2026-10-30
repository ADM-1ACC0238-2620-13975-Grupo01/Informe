<a id="toc-4-2-2-sprint-2"></a>

## 4.2.2. Sprint 2

El Sprint 2 corresponde al AV2 y completa la base ejecutable del Sprint 1. Su alcance es el publicado en la rama `main` de los repositorios del backend (<https://github.com/ADM-1ACC0238-2620-13975-Grupo01/anitec-backend>), de la aplicación Android (<https://github.com/ADM-1ACC0238-2620-13975-Grupo01/anitec-android>) y de la aplicación Flutter (<https://github.com/ADM-1ACC0238-2620-13975-Grupo01/anitec-flutter>): el backend completo, que filtra la información por usuario, gestiona las suscripciones con Stripe y archiva animales; la aplicación Android con la vista del veterinario, las actividades, las finanzas, la analítica, los dispositivos IoT, el escáner de códigos QR, el trabajo sin conexión y las suscripciones; una primera versión de la aplicación Flutter con el inicio de sesión y el inicio del ganadero; y la distribución de las dos aplicaciones en Firebase App Distribution. El consentimiento del ganadero sobre el acceso veterinario, las notificaciones, la persistencia local en Flutter y la sincronización idempotente quedan para el Sprint 3.

<a id="toc-4-2-2-1-sprint-planning-2"></a>

### 4.2.2.1. Sprint Planning 2

La planificación del Sprint 2 parte del Product Backlog del AV1, que asignaba al Sprint 2 veintiuna historias (99 Story Points). Al contrastarlas con lo realmente construido, el compromiso se ajustó como en el Sprint 1: siete historias pasaron al Sprint 3 (US-020, US-021, US-022, TS-009, US-027, TS-006 y TS-007) y diez historias del Sprint 3 se adelantaron porque ya estaban construidas (US-035, US-036, US-037, US-038, TS-011, US-039, US-040, US-041, US-043 y TS-015). El Product Backlog de la sección 2.4.3 se actualizó con ese ajuste: el Sprint 2 queda con 24 historias y 114 Story Points.

<table>
  <tr><th>Sprint #</th><td>Sprint 2</td></tr>
  <tr><th colspan="2">Sprint Planning Background</th></tr>
  <tr><th>Date</th><td>Pendiente de completar</td></tr>
  <tr><th>Time</th><td>Pendiente de completar</td></tr>
  <tr><th>Location</th><td>Pendiente de completar</td></tr>
  <tr><th>Prepared By</th><td>Melgarejo Quiroz, Josep Eliu</td></tr>
  <tr><th>Attendees</th><td>Pendiente de completar</td></tr>
  <tr><th>Sprint 1 Review Summary</th><td>El Sprint 1 entregó la Landing Page publicada, el backend desplegado con 104 pruebas automatizadas y la aplicación Android con autenticación, fincas, corrales, animales y registros sanitarios. De las 30 tareas, 28 quedaron en Done y 2 en To-Review; de las 24 historias, 22 se completaron y 2 quedaron parciales (US-007, porque el backend aún no filtraba por usuario, y US-012, porque faltaba archivar animales), por lo que se completaron 95 de los 105 Story Points comprometidos. La retroalimentación recibida en la revisión del TB1: pendiente de completar.</td></tr>
  <tr><th>Sprint 1 Retrospective Summary</th><td>Como aciertos, el equipo valoró repartir el trabajo por aspecto con un líder por producto, haber escrito pruebas automatizadas del backend que descubrieron un error de permisos y mantener el informe alineado con el código. Como oportunidades de mejora, identificó cerrar antes las historias parciales (filtrado por usuario en el servidor y archivado), preparar la firma y la distribución de la aplicación desde el inicio del sprint y comprobar en un dispositivo físico lo que el emulador no permite probar, como la cámara y la lectura de códigos QR.</td></tr>
  <tr><th colspan="2">Sprint Goal &amp; User Stories</th></tr>
  <tr><th>Sprint 2 Goal</th><td><b>Nuestro foco</b> es completar la aplicación Android para ganaderos y veterinarios, con el backend completo y publicado, y ofrecer una primera versión de la aplicación Flutter. <b>Creemos que</b> entrega al ganadero el control de su hato (finanzas, analítica, trabajo sin conexión, identificación de animales con el QR y suscripción) y al veterinario la atención de sus clientes y pacientes, desde aplicaciones que los evaluadores pueden instalar. <b>Lo confirmaremos cuando</b> los evaluadores instalen las dos aplicaciones desde Firebase App Distribution con el vínculo de invitación, inicien sesión contra el backend publicado y recorran los flujos del ganadero y del veterinario con los datos de demostración.</td></tr>
  <tr><th>Sprint 2 Velocity</th><td>114 Story Points, igual a la suma de las historias comprometidas tras contrastar el backlog con lo construido. Como referencia, el Sprint 1 comprometió 105 Story Points y completó 95.</td></tr>
  <tr><th>Sum of Story Points</th><td>114</td></tr>
</table>

La tabla siguiente lista las 24 historias comprometidas, sus Story Points y su estado al cierre del sprint. Se señalan como parciales las historias que no cumplen todos sus criterios de aceptación; en particular, la lectura de códigos QR y el pago con Stripe están implementados y probados de forma automática, pero falta verificarlos con la cámara real y con una tarjeta de prueba en un dispositivo.

| ID | Título | Story Points | Estado al cierre |
|---|---|---:|---|
| US-017 | Consultar el historial sanitario de un animal | 5 | Parcial: el veterinario consulta el historial clínico de cada paciente y el ganadero su lista de registros; la copia local no indica cuándo se actualizó. |
| US-024 | Consultar antecedentes de un paciente autorizado | 3 | Completa: el servidor solo entrega la información de los clientes del veterinario. |
| US-023 | Consultar clientes y pacientes autorizados | 5 | Completa: clientes, fincas y pacientes del veterinario. |
| US-026 | Gestionar una actividad o recordatorio | 5 | Parcial: se crean, editan y eliminan actividades; no se programa un recordatorio ni existe el estado cancelada. |
| US-025 | Consultar actividades programadas | 3 | Completa. |
| US-037 | Registrar y consultar movimientos financieros | 5 | Completa: ingresos y gastos, también sin conexión. |
| US-035 | Consultar indicadores del hato | 5 | Completa: pantalla de analítica del ganadero. |
| US-036 | Consultar indicadores sanitarios de clientes | 5 | Completa: pantalla de analítica del veterinario. |
| TS-002 | Configurar la aplicación multiplataforma con Flutter | 5 | Completa: proyecto, arquitectura, diseño, idiomas, inicio de sesión e inicio del ganadero. |
| US-029 | Consultar información esencial sin conexión | 5 | Parcial: la caché local de Room permite consultar sin conexión; no se muestra la última sincronización. |
| US-030 | Guardar trabajo pendiente sin conexión | 5 | Completa: animales, registros sanitarios, actividades y movimientos financieros. |
| US-031 | Sincronizar operaciones pendientes | 8 | Parcial: la cola se envía en segundo plano y conserva solo lo rechazado; el servidor aún no garantiza procesar cada operación una sola vez. |
| SP-001 | Investigar identificación de animales con Google ML Kit | 5 | Parcial: spike resuelto con un prototipo funcional; falta la prueba con cámara real. |
| TS-010 | Integrar identificación QR mediante Google ML Kit | 5 | Parcial: integrada con CameraX y ML Kit; falta la prueba con cámara real. |
| US-033 | Identificar un animal mediante código QR | 5 | Parcial: escaneo y rechazo de códigos fuera del alcance del usuario implementados; falta la prueba con cámara real. |
| US-034 | Identificar un animal sin utilizar la cámara | 3 | Completa: búsqueda por código o nombre y mensaje si se deniega el permiso. |
| SP-002 | Investigar la integración de Stripe para suscripciones móviles | 5 | Completa: Checkout en una Custom Tab y retorno por enlace a la aplicación. |
| US-038 | Consultar planes de suscripción | 3 | Completa. |
| TS-011 | Integrar el checkout externo de Stripe | 8 | Parcial: implementada y probada de forma automática; falta un pago de prueba real en el dispositivo. |
| US-039 | Iniciar un pago mediante un proveedor externo | 5 | Parcial: falta un pago de prueba real en el dispositivo. |
| US-040 | Consultar el resultado del pago y la suscripción | 5 | Parcial: falta un pago de prueba real en el dispositivo. |
| US-041 | Cambiar el idioma de la aplicación | 3 | Completa: English y español (es-419) en Android y en Flutter. |
| US-043 | Comprender errores y estados de conectividad | 3 | Completa: mensajes por tipo de error y aviso de sincronización pendiente. |
| TS-015 | Configurar compilación y distribución de versiones móviles | 5 | Completa: compilación firmada con R8 y distribución en Firebase App Distribution. |

Además, el sprint cierra dos historias que habían quedado parciales en el Sprint 1. Sus Story Points ya se contaron en ese sprint y no se suman de nuevo.

| ID | Título | Estado al cierre del Sprint 2 |
|---|---|---|
| US-007 | Acceder únicamente a información autorizada | Completa: el backend filtra fincas, corrales, animales, registros sanitarios, actividades, finanzas, dispositivos, suscripciones y paneles por usuario, y responde `403` ante recursos ajenos. |
| US-012 | Actualizar o archivar un animal | Completa: el animal puede archivarse y restaurarse (estado «Archivado») de forma individual o múltiple, y la lista activa excluye los archivados. |

Las historias US-020, US-021 y US-022 (solicitud, aceptación y revocación del acceso veterinario por parte del ganadero) pasan al Sprint 3: en este sprint el veterinario agrega y retira a sus clientes directamente. Las notificaciones (TS-009 y US-027), la persistencia local en Flutter (TS-006) y la sincronización idempotente (TS-007) también pasan al Sprint 3.

<a id="toc-4-2-2-2-aspect-leaders-and-collaborators"></a>

### 4.2.2.2. Aspect Leaders and Collaborators

La matriz LACX indica un líder (L) y los colaboradores (C) de cada aspecto del Sprint 2: diseño UX/UI, aplicación Android, aplicación Flutter, backend, Landing Page, pruebas, y documentación y despliegue. La matriz se deriva de las tareas asignadas en el Sprint Backlog (sección 4.2.2.3) y de las contribuciones al Informe. A diferencia del Sprint 1, la aplicación Flutter ya tiene responsables porque su primera versión forma parte de este sprint.

| Team Member | GitHub Username | UX/UI | Android | Flutter | Backend | Landing Page | Testing | Documentation & Deployment |
|---|---|---|---|---|---|---|---|---|
| Beingolea Montalvo, Sebastian Martin | smbmontalvo | — | — | C | L | — | C | C |
| Melgarejo Quiroz, Josep Eliu | Melga1502 | — | L | — | — | — | — | C |
| Ortega Muñoz, Saul | Ss1lent10 | C | C | C | C | L | C | — |
| Sanchez Silva, Luciana Celeste | luccsss | L | C | L | — | — | — | C |
| Villanueva Rodriguez, Giuseppe | Giuseppe152004 | — | C | — | — | — | L | L |

<a id="toc-4-2-2-3-sprint-backlog-2"></a>

### 4.2.2.3. Sprint Backlog 2

El Sprint Backlog descompone las historias comprometidas en tareas comprobables y refleja el objetivo del sprint: una aplicación Android completa y una primera versión de Flutter, respaldadas por el backend publicado y distribuidas en Firebase. El tablero utiliza los estados Todo, In-Process, To-Review y Done. Las tareas se repartieron en partes iguales entre los cinco integrantes, 40 horas estimadas por persona.

- **Sprint Goal:** completar la aplicación Android y ofrecer una primera versión de Flutter, con el backend publicado (ver 4.2.2.1).
- **Board URL:** pendiente de completar (URL pública del tablero de Trello del Sprint 2).

<div align="center">
  <img src="../../assets/chapter-4/captura-pendiente.svg" alt="Captura pendiente: tablero de Trello del Sprint 2 con las columnas Todo, In-Process, To-Review y Done y las 31 tarjetas T-031 a T-061" width="800">
  <p><i>Figura 4.2.2.3.1. Tablero de Trello del Sprint 2. Fuente: elaboración propia.</i></p>
</div>

| Story ID | Story Title | Task ID | Task Title | Description | Hours | Assigned To | Status |
|---|---|---|---|---|---:|---|---|
| US-007 | Acceder únicamente a información autorizada | T-031 | Filtrar los datos por usuario en el servidor | Servicio de alcance de acceso y su uso en los controladores de fincas, corrales, animales, registros sanitarios, actividades, finanzas, dispositivos, suscripciones y paneles; `403` ante recursos ajenos. | 10 | Beingolea Montalvo, Sebastian Martin | Done |
| TS-011, SP-002 | Integrar el checkout externo de Stripe; Investigar Stripe | T-032 | Retorno móvil de Stripe y confirmación del pago | Páginas HTTPS de retorno que abren la aplicación por enlace, parámetro de plataforma en el checkout, confirmación del pago y cierre del pago simulado en producción. | 8 | Beingolea Montalvo, Sebastian Martin | Done |
| US-038 | Consultar planes de suscripción | T-033 | Sembrar y consultar los planes de suscripción | Carga de los tres planes en cualquier entorno cuando la tabla está vacía y consulta desde la aplicación. | 3 | Beingolea Montalvo, Sebastian Martin | Done |
| US-012 | Actualizar o archivar un animal | T-034 | Archivar animales en el backend | Estado «Archivado», `PATCH animals/{id}/status` y filtro `archived` en la lista de animales. | 3 | Beingolea Montalvo, Sebastian Martin | Done |
| Sin historia | Mejora de US-011 (registro de animales) | T-035 | Nombre base en el alta masiva y datos de demostración | Nombres consecutivos `base-001`, `base-002`… por finca y datos de demostración con corrales y animales para tres ganaderos y sus veterinarios. | 5 | Beingolea Montalvo, Sebastian Martin | Done |
| TS-015 | Configurar compilación y distribución de versiones móviles | T-036 | Configurar el backend publicado | Variable `SeedDemoData` para cargar los datos de demostración, límite de conexiones de la cadena de conexión y redespliegue en Render. | 3 | Beingolea Montalvo, Sebastian Martin | Done |
| Sin historia | Tarea técnica sin historia asociada | T-037 | Pruebas unitarias y de widgets de Flutter | Pruebas del dominio, el estado, el cliente HTTP y las pantallas de la aplicación Flutter con `flutter_test` y `mocktail`. | 8 | Beingolea Montalvo, Sebastian Martin | Done |
| US-023, US-024, US-017 | Clientes, pacientes y antecedentes del veterinario | T-038 | Vista del veterinario | Inicio, clientes (alta y baja), pacientes por finca e historial clínico de cada paciente. | 12 | Melgarejo Quiroz, Josep Eliu | Done |
| US-029, US-030, US-031 | Trabajo sin conexión | T-039 | Trabajo sin conexión y sincronización | Cola de operaciones con WorkManager para animales, registros sanitarios, actividades y movimientos financieros, aviso de sincronización y reintentos. | 10 | Melgarejo Quiroz, Josep Eliu | Done |
| US-039, US-040 | Iniciar un pago; Consultar el resultado del pago | T-040 | Suscripciones en Android | Planes, plan activo, historial de pagos, checkout de Stripe en una Custom Tab, enlace de retorno y confirmación del resultado. | 8 | Melgarejo Quiroz, Josep Eliu | To-Review |
| Sin historia | Tarea técnica sin historia asociada | T-041 | Corregir la navegación inferior | Volver a Inicio desde Pacientes o Sanidad tras abrir los pacientes de un cliente, con una prueba instrumentada que reproduce el defecto. | 3 | Melgarejo Quiroz, Josep Eliu | Done |
| Sin historia | Tarea técnica sin historia asociada | T-042 | Permiso de red local en la compilación de depuración | Solicitud del permiso de red local de Android 17 solo en depuración, para llegar al backend del equipo. | 2 | Melgarejo Quiroz, Josep Eliu | Done |
| Sin historia | Documentación | T-043 | Documentar el Sprint 2 en el informe | Capítulos 4.1 y 4.2.2, ajuste del Product Backlog, registro de versiones, student outcomes y collaboration insights. | 5 | Melgarejo Quiroz, Josep Eliu | In-Process |
| US-025, US-026 | Consultar actividades; Gestionar una actividad | T-044 | Actividades | Lista por fecha, formulario de alta y edición y eliminación con confirmación. | 8 | Sanchez Silva, Luciana Celeste | Done |
| US-037 | Registrar y consultar movimientos financieros | T-045 | Finanzas | Lista, resumen de ingresos, gastos y saldo, y formulario de ingresos y gastos. | 8 | Sanchez Silva, Luciana Celeste | Done |
| Sin historia | Mejora de US-011 (registro de animales) | T-046 | Nombre base en el formulario de lotes | Campo de nombre base opcional con vista previa de los nombres y textos en inglés y español. | 3 | Sanchez Silva, Luciana Celeste | Done |
| TS-002 | Configurar la aplicación multiplataforma con Flutter | T-047 | Inicio de sesión y sesión segura en Flutter | Pantalla de inicio de sesión, mensaje para el rol veterinario, sesión cifrada, cierre de sesión y cierre automático ante un `401`. | 7 | Sanchez Silva, Luciana Celeste | Done |
| US-035 | Consultar indicadores del hato | T-048 | Inicio del ganadero en Flutter | Saludo, selector de finca, contadores, próximas actividades, registros sanitarios recientes y cambio de idioma. | 10 | Sanchez Silva, Luciana Celeste | Done |
| Sin historia | Tarea de documentación sin historia asociada | T-049 | Elaborar los videos del AV2 | Videos de validación de la aplicación, About-the-Product y About-the-Team. | 4 | Sanchez Silva, Luciana Celeste | Todo |
| US-035, US-036 | Indicadores del hato y de los clientes | T-050 | Analítica en Android | Gráficos dibujados con Canvas del hato del ganadero y de los clientes del veterinario. | 9 | Villanueva Rodriguez, Giuseppe | Done |
| US-012 | Actualizar o archivar un animal | T-051 | Archivar animales en Android | Archivado y restauración individual y múltiple con confirmación y filtro de archivados. | 5 | Villanueva Rodriguez, Giuseppe | Done |
| TS-015 | Configurar compilación y distribución de versiones móviles | T-052 | Compilación firmada con R8 | Firma desde `keystore.properties`, R8 activado, versión 0.2.0 y comprobación del APK. | 7 | Villanueva Rodriguez, Giuseppe | Done |
| TS-015 | Configurar compilación y distribución de versiones móviles | T-053 | Distribución en Firebase de las dos aplicaciones | Proyecto «AniTec», registro de las dos aplicaciones, subida de los APK, grupo «Equipo AniTec» y vínculos de invitación. | 6 | Villanueva Rodriguez, Giuseppe | Done |
| Sin historia | Tarea técnica sin historia asociada | T-054 | Pruebas unitarias e instrumentadas de Android | Pruebas de dominio, casos de uso, repositorios y ViewModels de los contextos nuevos y pruebas de DAO y de navegación. | 10 | Villanueva Rodriguez, Giuseppe | Done |
| Sin historia | Tarea de verificación sin historia asociada | T-055 | Verificar en un dispositivo físico el escáner QR y el pago de prueba | Lectura de un código QR con la cámara real y un pago de prueba de Stripe con una tarjeta de prueba. | 3 | Villanueva Rodriguez, Giuseppe | Todo |
| Sin historia | Tarea técnica sin historia asociada | T-056 | Dispositivos IoT | Lista y formulario de dispositivos asignados a una finca o a un animal, con su última lectura y el número de lecturas. | 7 | Ortega Muñoz, Saul | Done |
| SP-001, TS-010, US-033, US-034 | Identificación de animales con ML Kit | T-057 | Escáner QR con ML Kit y búsqueda manual | CameraX con ML Kit Barcode Scanning, resolución del código a un animal del usuario, permiso de cámara y búsqueda manual. | 10 | Ortega Muñoz, Saul | To-Review |
| TS-002 | Configurar la aplicación multiplataforma con Flutter | T-058 | Proyecto Flutter: arquitectura, diseño e idiomas | Proyecto `anitec-flutter`, carpetas por contexto, tema con los tokens de AniTec, enrutamiento y textos en inglés y español. | 9 | Ortega Muñoz, Saul | Done |
| Sin historia | Tarea técnica sin historia asociada | T-059 | Pruebas de integración y BDD del backend | Pruebas de alcance por usuario, suscripciones, archivado, nombre de lote y datos de demostración, y escenarios Gherkin ampliados. | 8 | Ortega Muñoz, Saul | Done |
| US-041, US-043 | Cambiar el idioma; Comprender errores y conectividad | T-060 | Idioma y mensajes de error y conectividad | Mensajes de validación específicos, cambio de idioma y textos localizados. | 4 | Ortega Muñoz, Saul | Done |
| Sin historia | Tarea de despliegue sin historia asociada | T-061 | Actualizar la Landing Page con el vínculo de descarga | Reemplazar el botón de descarga de Android por el vínculo de invitación de Firebase. | 2 | Ortega Muñoz, Saul | Todo |

| Métrica | Valor |
|---|---|
| Historias comprometidas | 24 (más el cierre de US-007 y US-012) |
| Story Points comprometidos | 114 |
| Tareas | 31 |
| Horas estimadas | 200 |
| Tareas completadas (Done) | 25 de 31; 2 en To-Review, 1 en In-Process y 3 en Todo |

<a id="toc-4-2-2-4-development-evidence-for-sprint-review"></a>

### 4.2.2.4. Development Evidence for Sprint Review

Esta sección registra los commits que contribuyen al alcance del Sprint 2. Los avances por producto son los siguientes.

- **Backend (`anitec-backend`).** Un servicio de alcance de acceso filtra por usuario las fincas, los corrales, los animales, los registros sanitarios, las actividades, los movimientos financieros, los dispositivos, las suscripciones y los paneles, y responde `403` ante recursos ajenos. El módulo de suscripciones carga los planes en cualquier entorno, inicia el Checkout de Stripe para Android, devuelve al usuario a la aplicación mediante páginas HTTPS de retorno y confirma el pago; el pago simulado deja de estar disponible en producción. Los animales pueden archivarse y restaurarse (`PATCH animals/{id}/status`), el alta masiva admite un nombre base y la semilla de demostración incluye tres ganaderos con fincas, corrales y animales, y los veterinarios que los atienden.
- **Aplicación Android (`anitec-android`).** Se completan la vista del veterinario (clientes, pacientes e historial clínico), las actividades, las finanzas, la analítica del ganadero y de los clientes, los dispositivos IoT, el escáner de códigos QR con CameraX y ML Kit, y la cola de operaciones sin conexión que ahora incluye los movimientos financieros. Se añaden las suscripciones con el Checkout de Stripe en una Custom Tab y el retorno por enlace, el archivado de animales, el nombre base de los lotes, la compilación `release` firmada con R8 y la corrección de la navegación inferior.
- **Aplicación Flutter (`anitec-flutter`).** Primera versión con el inicio de sesión del ganadero, el inicio con selector de finca, contadores, próximas actividades y registros sanitarios recientes, cambio de idioma, sesión cifrada y compilación `release` firmada.
- **Informe.** Documentación del Sprint 2, ajuste del Product Backlog y actualización de la configuración de despliegue.

**Pendiente de completar:** las tablas siguientes se llenarán con los commits reales del sprint.

| Repository | Branch | Commit Id | Commit Message | Commit Message Body | Committed on |
|---|---|---|---|---|---|

<a id="toc-4-2-2-5-testing-suite-evidence-for-sprint-review"></a>

### 4.2.2.5. Testing Suite Evidence for Sprint Review

La suite de pruebas del backend (`Anitec.Platform.Tests`, <https://github.com/ADM-1ACC0238-2620-13975-Grupo01/anitec-backend/tree/main/Anitec.Platform.Tests>) crece de 104 a 150 pruebas. Además, la aplicación Android cuenta con 214 pruebas unitarias y 16 instrumentadas, y la aplicación Flutter con 88 pruebas unitarias y de widgets. Las pruebas del backend siguen el mismo esquema que en el Sprint 1 (sección 4.2.1.5): una API en memoria con SQLite y el entorno `Testing`.

| Tipo | Herramientas | Carpeta del proyecto | Sprint 1 | Sprint 2 |
|---|---|---|---:|---:|
| Unit Tests | xUnit y NSubstitute | `Unit/` | 52 | 52 |
| Integration Tests | xUnit y `WebApplicationFactory` | `Integration/` | 32 | 74 |
| Acceptance Tests (BDD) | Reqnroll sobre xUnit, archivos `.feature` en Gherkin | `Bdd/Features/` y `Bdd/Steps/` | 20 | 24 |
| **Total** | | | **104** | **150** |

**Unit Tests.** Las 52 pruebas unitarias (`UserCommandService`, `TokenService`, `HashingService`, `AnimalCommandService` y `CorralCommandService`) no cambiaron respecto al Sprint 1 y se describen en la sección 4.2.1.5; el servicio de animales mantiene cubierta el alta masiva, ahora con nombre base.

**Integration Tests.** Cada prueba llama a los endpoints REST de la API en memoria. Las clases nuevas del sprint verifican que cada usuario vea y modifique solo lo suyo, la gestión de suscripciones y la semilla de demostración.

| Test ID | Clase de pruebas | Endpoints y comportamientos verificados | Historias relacionadas | Pruebas | Resultado |
|---|---|---|---|---:|---|
| TEST-BE-I01 | `AuthenticationApiTests` | Registro, inicio de sesión y `401` sin token (sin cambios). | US-004, US-005 | 11 | Completado |
| TEST-BE-I02 | `LivestockApiTests` | Fincas, corrales y animales (sin cambios) y, nuevas: alta masiva con nombre base y continuación de la numeración, alta masiva sin nombre base, archivar y restaurar un animal con su efecto en la lista activa, validación del cambio de estado y permisos por rol del veterinario. | US-011, US-012, US-007 | 22 | Completado |
| TEST-BE-I03 | `HealthEventsApiTests` | `POST`, `GET` y `DELETE` de registros sanitarios, y un veterinario que no puede registrar un evento sobre el animal de un ganadero que no es su cliente. | US-014, US-015, US-016, US-024 | 6 | Completado |
| TEST-BE-I04 | `AccessScopeApiTests` | Fincas, corrales, animales, registros sanitarios, actividades, movimientos financieros, dispositivos y paneles ocultos para otros ganaderos; `403` al crear, modificar o eliminar recursos ajenos, incluidas las operaciones masivas; el veterinario ve solo las fincas de sus clientes, programa actividades para ellos y no gestiona los clientes de otro veterinario; un dispositivo requiere una finca o un animal visibles para el usuario. | US-007, US-023, US-024, US-025, US-026, US-037, TS-013 | 23 | Completado |
| TEST-BE-I05 | `SubscriptionsApiTests` | Los planes se cargan solo cuando no existen; una suscripción, la suscripción activa y los pagos solo son visibles para su dueño; un ganadero no puede suscribir a otra persona; las páginas de retorno de Stripe abren la aplicación con la sesión de pago, descartan un identificador con caracteres inesperados y manejan la cancelación. | US-038, US-040, TS-011 | 7 | Completado |
| TEST-BE-I06 | `SeedDataTests` | Todo animal de la semilla pertenece a un corral de su finca, un ganadero nunca tiene dos animales con el mismo nombre, tres ganaderos tienen varias fincas, corrales y animales, la veterinaria tiene a los tres como clientes y la semilla incluye animales archivados, aves numeradas y seguimientos próximos. | Datos de demostración | 5 | Completado |

**Acceptance Tests (BDD).** Los escenarios siguen escritos en Gherkin en cuatro archivos `.feature` dentro de `Anitec.Platform.Tests/Bdd/Features`, con sus pasos en C#. En este sprint se amplían los escenarios de sanidad y de permisos, que ahora distinguen a los clientes del veterinario.

| Archivo `.feature` | Escenarios | Historias relacionadas |
|---|---:|---|
| `Authentication.feature` | 7 | US-004, US-005, US-007 |
| `AnimalManagement.feature` | 7 | US-010, US-011, US-012, US-044, TS-013 |
| `HealthRecords.feature` | 4 | US-014, US-015, US-016, US-024 |
| `RolePermissions.feature` | 6 | US-007, US-023, US-024 |

Los archivos `Authentication.feature` y `AnimalManagement.feature` no cambiaron y su código está en la sección 4.2.1.5. Código de `HealthRecords.feature`:

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

  Scenario: A veterinarian records a treatment for a client
    Given I am signed in as a "Veterinarian"
    And I am a client of the rancher
    When I record a "Tratamiento" health event for the animal "COW-001" with the description "Antibiótico por 5 días"
    Then the health event is created
    And the health record of the animal "COW-001" includes the description "Antibiótico por 5 días"

  Scenario: A veterinarian cannot record a treatment for a rancher who is not their client
    Given I am signed in as a "Veterinarian"
    When I record a "Tratamiento" health event for the animal "COW-001" with the description "Antibiótico por 5 días"
    Then the request is rejected with status 403

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

  Scenario: A veterinarian can see the animals of their clients
    Given I am signed in as a "Veterinarian"
    And I am a client of the rancher
    When I request the list of animals
    Then the request succeeds
    And the animal "COW-001" appears in the animal list

  Scenario: A veterinarian does not see the animals of ranchers who are not their clients
    Given I am signed in as a "Veterinarian"
    When I request the list of animals
    Then the request succeeds
    And the animal "COW-001" no longer appears in the animal list

  Scenario: A rancher does not see the animals of another rancher
    Given I am signed in as another "Rancher"
    When I request the list of animals
    Then the request succeeds
    And the animal "COW-001" no longer appears in the animal list

  Scenario: A rancher cannot delete the animals of another rancher
    Given I am signed in as another "Rancher"
    When I delete the animal "COW-001"
    Then the request is rejected with status 403

  Scenario: A veterinarian cannot register animals
    Given I am signed in as a "Veterinarian"
    When I register an animal with the code "COW-009" in "Corral A"
    Then the request is rejected with status 403

  Scenario: A veterinarian cannot delete animals
    Given I am signed in as a "Veterinarian"
    When I delete the animal "COW-001"
    Then the request is rejected with status 403
</pre>

**Pruebas de la aplicación Android.** Las 214 pruebas unitarias se ejecutan con JUnit 4, MockK, Turbine, Coroutines Test y MockWebServer, y se agrupan por bounded context.

| Test ID | Contexto | Clases de pruebas | Comportamientos verificados | Historias relacionadas | Pruebas | Resultado |
|---|---|---|---|---|---:|---|
| TEST-AN-U01 | `iam` | `AuthViewModelsTest`, `EmailRegistrationTest`, `EmailValidatorTest`, `SignUpRequestTest`, `SignUpResponseTest` | Estado de inicio de sesión y registro, validación del correo, registro con correo opcional y lectura de las respuestas del servidor. | US-004, US-005 | 24 | Completado |
| TEST-AN-U02 | `core` | `SafeApiCallTest`, `AuthInterceptorTest`, `ErrorMessagesTest`, `StringResourcesTest`, `LocalNetworkAccessTest` | Mapeo de errores HTTP, cierre de sesión ante un `401` solo si el token sigue vigente, mensajes de validación específicos, textos en los dos idiomas y solicitud del permiso de red local en depuración. | US-043, US-041 | 23 | Completado |
| TEST-AN-U03 | `livestock` | `LivestockUseCasesTest`, `LivestockRepositoryTest`, `LivestockScopeTest`, `AnimalSearchTest`, `AnimalPlacementPolicyTest`, `AnimalStatusTest`, `ArchivedStatusTest`, `ArchiveAnimalRepositoryTest`, `ArchiveAnimalsUseCasesTest`, `BatchNamingTest`, `MediaUrlTest` | Alcance de los datos del usuario, búsqueda, reglas de ubicación en corrales, estados del animal, archivado y restauración individual y múltiple, nombres `base-001` del lote y rutas de las fotos. | US-010, US-011, US-012, US-045 | 50 | Completado |
| TEST-AN-U04 | `sanitary` | `SanitaryRepositoryTest`, `SanitaryScopeTest` | Lectura y escritura de registros sanitarios y alcance por usuario. | US-014, US-015, US-016 | 6 | Completado |
| TEST-AN-U05 | `veterinary` | `VeterinaryRepositoryTest`, `VeterinaryHelpersTest`, `VetHomeViewModelTest` | Clientes del veterinario (alta y baja tras la confirmación del servidor, conservación de la caché ante un fallo), ganaderos disponibles, resumen de los animales y registros de cada cliente y totales del inicio de todos los clientes o del cliente elegido. | US-017, US-023, US-024 | 12 | Completado |
| TEST-AN-U06 | `activities` | `ActivityRulesTest`, `ActivitiesRepositoryTest` | Actividades próximas primero, alcance por rol (el ganadero ve lo suyo; el veterinario lo que creó y lo de sus clientes), propietario al crear y eliminación solo cuando el servidor lo confirma. | US-025, US-026 | 9 | Completado |
| TEST-AN-U07 | `financial` | `FinancialRulesTest`, `FinancialRepositoryTest` | Totales de ingresos, gastos y saldo sin errores de centavos, montos positivos con dos decimales y coma decimal, formato en soles y registro sin conexión con identificador negativo. | US-037 | 14 | Completado |
| TEST-AN-U08 | `devices` | `DeviceRulesTest`, `DevicesRepositoryTest` | Solo dispositivos de fincas o animales visibles, última lectura y conteo por dispositivo, historial de lecturas más reciente primero y dispositivo sin lecturas. | Sin historia (dispositivos IoT) | 13 | Completado |
| TEST-AN-U09 | `analytics` | `AnalyticsCalculatorTest` | Animales por estado de salud, exclusión de fincas no visibles, registros por tipo y por finca, caché vacía y resumen en palabras de los gráficos para lectores de pantalla. | US-035, US-036 | 6 | Completado |
| TEST-AN-U10 | `scanner` | `ScannerViewModelTest`, `TagResolverTest` | Código exacto o dentro de un enlace que encuentra al animal sin distinguir mayúsculas, código desconocido, resultado que ignora nuevas lecturas, nuevo escaneo y código manual vacío. | US-033, US-034 | 8 | Completado |
| TEST-AN-U11 | `sync` | `OutboxProcessorTest`, `OfflineCreationTest` | Envío de la cola de animales, registros sanitarios, actividades y movimientos financieros, registros que siguen a su animal, reintento sin conexión, animal no duplicado tras perder una respuesta, operación rechazada marcada como fallida sin detener las siguientes, sesión vencida, reintento y descarte. | US-029, US-030, US-031 | 14 | Completado |
| TEST-AN-U12 | `subscriptions` | `SubscriptionsRepositoryTest`, `SubscriptionsViewModelTest`, `CheckoutReturnParserTest`, `CheckoutReturnsTest`, `PlanAudienceTest` | Planes según el rol y solo los activos, plan activo y pagos, dirección de pago que debe ser HTTPS, mensajes cuando no se puede iniciar el pago, lectura de los enlaces de retorno `anitec://subscriptions` y confirmación del resultado, incluido un pago que Stripe no completó. | US-038, US-039, US-040, TS-011 | 28 | Completado |
| TEST-AN-U13 | `app` | `HomeViewModelTest`, `NavigationLayoutTest` | Contadores del inicio de todas las fincas o de la finca elegida, máximo de cuatro registros recientes, barra inferior en teléfonos y riel de navegación en pantallas anchas. | US-007, US-035 | 7 | Completado |

Las 16 pruebas instrumentadas se ejecutan en el emulador (`Medium_Phone_API_37.0`, Android 17):

| Test ID | Clase de pruebas | Comportamientos verificados | Pruebas | Resultado |
|---|---|---|---:|---|
| TEST-AN-I01 | `RoomDaoTest` | Operaciones de la base de datos local por contexto y limpieza de la caché. | 7 | Completado |
| TEST-AN-I02 | `AnimalImageUploaderTest` | Reducción y subida de la fotografía del animal. | 5 | Completado |
| TEST-AN-I03 | `BottomNavigationTest` | La navegación inferior vuelve a Inicio desde Pacientes o Sanidad aunque se hayan abierto los pacientes de un cliente, permite repetir el recorrido y cambia entre pestañas en cualquier orden. | 4 | Completado |

**Pruebas de la aplicación Flutter.** Las 88 pruebas usan `flutter_test` y `mocktail`.

| Test ID | Archivos de pruebas | Comportamientos verificados | Pruebas | Resultado |
|---|---|---|---:|---|
| TEST-FL-001 | `iam/sign_in_controller_test.dart`, `core/session_controller_test.dart`, `app/router_test.dart` | Campos vacíos, usuario sin espacios, inicio de sesión del ganadero, mensaje para el veterinario sin conservar la sesión, credenciales incorrectas, sesión guardada y restaurada, cierre de sesión, cierre ante un `401` y redirección según la sesión. | 17 | Completado |
| TEST-FL-002 | `core/api_client_test.dart`, `core/language_controller_test.dart`, `data/repositories_test.dart` | Cabecera Bearer, manejo de `401` que no cierra una sesión nueva por una respuesta tardía, lectura de los recursos del backend y cambio de idioma. | 21 | Completado |
| TEST-FL-003 | `livestock/livestock_domain_test.dart`, `livestock/archived_animals_test.dart`, `activities/activity_test.dart`, `app/home_summary_test.dart` | Reglas del dominio, exclusión de los animales archivados y cálculo de los contadores, las próximas actividades y los registros recientes. | 24 | Completado |
| TEST-FL-004 | `app/home_controller_test.dart`, `app/home_screen_test.dart`, `app/app_flow_test.dart` | Estado del inicio, pantalla de inicio con sus contadores y recorrido completo desde el inicio de sesión hasta el inicio del ganadero, con estados de carga, vacío y error. | 26 | Completado |

**Resultado de la ejecución.** Las 150 pruebas del backend, las 214 pruebas unitarias de Android, las 16 instrumentadas y las 88 de Flutter pasan sin errores. Las pruebas ayudaron a detectar defectos durante el sprint. La prueba `BottomNavigationTest` reprodujo el defecto de la navegación inferior reportado al usar la aplicación: antes de la corrección fallaban 3 de sus 4 casos, porque la barra restauraba la pila guardada con los pacientes de un cliente en lugar de volver a Inicio; la corrección, que vuelve directamente a Inicio, hizo que pasaran los 4. Al verificar la pantalla de suscripciones en el emulador apareció un cierre inesperado por claves duplicadas en una lista (un plan y un pago con el mismo identificador), que se corrigió con claves distintas por tipo de elemento. El filtrado por usuario del backend quedó cubierto por las 23 pruebas de `AccessScopeApiTests`.

<div align="center">
  <img src="../../assets/chapter-4/captura-pendiente.svg" alt="Captura pendiente: terminal con la salida de dotnet test en la carpeta anitec-backend mostrando 150 pruebas superadas y 0 con error" width="800">
  <p><i>Figura 4.2.2.5.1. Captura de las 150 pruebas exitosas del backend. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/captura-pendiente.svg" alt="Captura pendiente: Explorador de pruebas del IDE (Rider o Visual Studio) con los grupos Unit, Integration y Bdd expandidos y todas las pruebas en verde" width="800">
  <p><i>Figura 4.2.2.5.2. Lista de pruebas del backend por tipo. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/captura-pendiente.svg" alt="Captura pendiente: Android Studio con la ventana Run mostrando el resultado de testDebugUnitTest (214 pruebas correctas) o el informe HTML de app/build/reports/tests/testDebugUnitTest/index.html" width="800">
  <p><i>Figura 4.2.2.5.3. Resultado de las pruebas unitarias de Android. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/captura-pendiente.svg" alt="Captura pendiente: resultado de connectedDebugAndroidTest en el emulador con las 16 pruebas instrumentadas correctas, incluidas las 4 de BottomNavigationTest" width="800">
  <p><i>Figura 4.2.2.5.4. Resultado de las pruebas instrumentadas de Android. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/captura-pendiente.svg" alt="Captura pendiente: terminal en la carpeta anitec-flutter con la salida de flutter test mostrando 88 pruebas correctas" width="800">
  <p><i>Figura 4.2.2.5.5. Resultado de las pruebas de la aplicación Flutter. Fuente: elaboración propia.</i></p>
</div>

**Pendiente de completar:** las tablas siguientes se llenarán con los commits reales de pruebas del sprint.

| Repository | Branch | Commit Id | Commit Message | Commit Message Body | Committed on |
|---|---|---|---|---|---|

<a id="toc-4-2-2-6-execution-evidence-for-sprint-review"></a>

### 4.2.2.6. Execution Evidence for Sprint Review

El Sprint 2 permite instalar las aplicaciones Android y Flutter desde Firebase App Distribution, iniciar sesión contra el backend publicado y recorrer los flujos del ganadero y del veterinario con los datos de demostración: inicio, fincas, corrales, animales (con archivado y registro masivo con nombre base), registros sanitarios, actividades, finanzas, analítica, dispositivos IoT, escáner de códigos QR, trabajo sin conexión, suscripciones y, para el veterinario, clientes, pacientes e historial clínico. La aplicación Flutter muestra el inicio del ganadero. Las capturas de las figuras 4.2.2.6.1 a 4.2.2.6.8 y 4.2.2.6.13 a 4.2.2.6.22 se tomaron en el emulador `Medium_Phone_API_37.0` (Android 17): las de Android con la compilación de depuración y las de Flutter con la compilación de perfil (la pantalla de inicio de sesión, con la compilación `release`), conectadas al backend local con los datos de demostración, e identifican el usuario de demostración usado. Las pantallas de pago con Stripe, del escáner de códigos QR y de la instalación desde Firebase requieren un dispositivo físico y se capturarán en él.

| Producto | Vista o flujo | Entorno / dispositivo | Evidencia | Estado |
|---|---|---|---|---|
| Android (ganadero) | Inicio, animales y archivado, registro masivo con nombre base, actividades, finanzas, analítica, dispositivos IoT | Emulador, usuario `ganadero` | Figuras 4.2.2.6.1 a 4.2.2.6.7 | Completado |
| Android (ganadero) | Suscripciones: planes, pago con Stripe, resultado e historial | Planes e historial en el emulador; pago en un dispositivo físico con tarjeta de prueba de Stripe | Figuras 4.2.2.6.8 a 4.2.2.6.10 | Parcial: capturada la figura 4.2.2.6.8; pendientes el pago y su resultado |
| Android (ganadero) | Escáner de códigos QR y búsqueda manual | Dispositivo físico | Figuras 4.2.2.6.11 y 4.2.2.6.12 | Pendiente de captura y de la prueba con cámara real |
| Android (ganadero) | Trabajo sin conexión y aviso de sincronización | Emulador con el modo avión activado | Figura 4.2.2.6.13 | Completado |
| Android (veterinario) | Inicio, clientes, pacientes, historial clínico y analítica | Emulador, usuario `veterinaria` | Figuras 4.2.2.6.14 a 4.2.2.6.18 | Completado |
| Flutter | Inicio de sesión, inicio del ganadero, cambio de idioma y mensaje para el veterinario | Emulador, usuarios `ganadero` y `veterinaria` | Figuras 4.2.2.6.19 a 4.2.2.6.22 | Completado |
| Distribución | Instalación desde Firebase App Distribution | Dispositivo físico | Figura 4.2.2.6.23 | Pendiente de captura |
| Web Services | Swagger UI con los endpoints del Sprint 2 | Navegador contra el Swagger del servicio publicado | Figuras de la sección 4.2.2.7 | Pendiente de captura |

**Aplicación Android: ganadero.** Se inicia sesión con el usuario `ganadero` (los datos de demostración se describen en 4.1.4).

<div align="center">
  <img src="../../assets/chapter-4/sprint2/fig-4-2-2-6-01-android-inicio-ganadero.png" alt="Inicio de la aplicación Android con el usuario ganadero: contadores de animales, requieren atención, registros sanitarios, seguimientos y actividades próximas" width="300">
  <p><i>Figura 4.2.2.6.1. Inicio del ganadero con los datos de demostración. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/sprint2/fig-4-2-2-6-02a-android-animales-filtro-archivados.png" alt="Pestaña Animales con el filtro Activos y Archivados" width="300"> <img src="../../assets/chapter-4/sprint2/fig-4-2-2-6-02b-android-animales-seleccion-archivar.png" alt="Selección múltiple de animales con las acciones de archivar y eliminar" width="300">
  <p><i>Figura 4.2.2.6.2. Lista de animales con selección múltiple, acción de archivar y filtro de archivados. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/sprint2/fig-4-2-2-6-03-android-registro-masivo-nombre-base.png" alt="Formulario de registro masivo con el nombre base polloComercio y la vista previa de los nombres polloComercio-001 a polloComercio-010" width="300">
  <p><i>Figura 4.2.2.6.3. Registro masivo de animales con nombre base y vista previa. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/sprint2/fig-4-2-2-6-04-android-actividades.png" alt="Lista de actividades ordenada por fecha, con los botones Editar y Eliminar y el botón para agregar una actividad" width="300">
  <p><i>Figura 4.2.2.6.4. Lista de actividades. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/sprint2/fig-4-2-2-6-05-android-finanzas.png" alt="Pantalla de finanzas con el resumen de ingresos, gastos y saldo y la lista de movimientos" width="300">
  <p><i>Figura 4.2.2.6.5. Pantalla de finanzas. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/sprint2/fig-4-2-2-6-06-android-analitica-ganadero.png" alt="Pantalla de analítica del ganadero con el gráfico del estado del hato y los registros por tipo" width="300">
  <p><i>Figura 4.2.2.6.6. Pantalla de analítica del ganadero. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/sprint2/fig-4-2-2-6-07-android-dispositivos-iot.png" alt="Lista de dispositivos IoT con su ubicación, el número de lecturas y la última lectura" width="300">
  <p><i>Figura 4.2.2.6.7. Dispositivos IoT con su última lectura. Fuente: elaboración propia.</i></p>
</div>

**Aplicación Android: suscripciones.** Se captura en un dispositivo físico con una tarjeta de prueba de Stripe.

<div align="center">
  <img src="../../assets/chapter-4/sprint2/fig-4-2-2-6-08-android-suscripciones-planes.png" alt="Pantalla de suscripciones con el plan actual, los planes disponibles con sus precios y el historial de pagos" width="300">
  <p><i>Figura 4.2.2.6.8. Planes de suscripción. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/captura-pendiente.svg" alt="Captura pendiente: página del Checkout de Stripe abierta en la pestaña del navegador (Custom Tab) con la tarjeta de prueba 4242 4242 4242 4242 escrita, sin datos reales" width="300">
  <p><i>Figura 4.2.2.6.9. Checkout de Stripe en modo de prueba abierto desde la aplicación. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/captura-pendiente.svg" alt="Captura pendiente: pantalla de resultado de la suscripción tras volver a la aplicación, y la pantalla Suscripciones con el plan activo y el historial de pagos" width="300">
  <p><i>Figura 4.2.2.6.10. Resultado del pago, plan activo e historial de pagos. Fuente: elaboración propia.</i></p>
</div>

**Aplicación Android: escáner de códigos QR.** Se captura en un dispositivo físico, porque el emulador no lee códigos.

<div align="center">
  <img src="../../assets/chapter-4/captura-pendiente.svg" alt="Captura pendiente: pantalla del escáner QR (botón de escáner en el inicio) con la cámara apuntando a un código QR de un animal y el resultado con la ficha del animal; el código QR puede generarse con el código del animal (por ejemplo BOV-001)" width="300">
  <p><i>Figura 4.2.2.6.11. Lectura de un código QR con la cámara. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/captura-pendiente.svg" alt="Captura pendiente: pantalla del escáner con la sección de búsqueda manual, escribiendo un código de animal, o con el permiso de cámara denegado" width="300">
  <p><i>Figura 4.2.2.6.12. Búsqueda manual de un animal sin cámara. Fuente: elaboración propia.</i></p>
</div>

**Aplicación Android: trabajo sin conexión.**

<div align="center">
  <img src="../../assets/chapter-4/sprint2/fig-4-2-2-6-13a-android-sin-conexion-pendiente.png" alt="Con el modo avión activo, aviso de un cambio pendiente de sincronizar después de registrar una actividad" width="300"> <img src="../../assets/chapter-4/sprint2/fig-4-2-2-6-13b-android-sincronizado.png" alt="Después de recuperar la conexión, el aviso desaparece porque la actividad se envió al servidor" width="300">
  <p><i>Figura 4.2.2.6.13. Registro sin conexión y aviso de sincronización pendiente. Fuente: elaboración propia.</i></p>
</div>

**Aplicación Android: veterinario.** Se inicia sesión con el usuario `veterinaria`.

<div align="center">
  <img src="../../assets/chapter-4/sprint2/fig-4-2-2-6-14a-android-vet-inicio.png" alt="Inicio del veterinario con los contadores de clientes, animales que requieren atención, registros clínicos y seguimientos" width="300"> <img src="../../assets/chapter-4/sprint2/fig-4-2-2-6-14b-android-vet-clientes-inicio.png" alt="Lista de clientes del veterinario en el inicio, con sus fincas, alertas y el botón Ver pacientes" width="300">
  <p><i>Figura 4.2.2.6.14. Inicio del veterinario. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/sprint2/fig-4-2-2-6-15-android-vet-clientes.png" alt="Pantalla Clientes del veterinario con los botones Ver pacientes y Quitar cliente y el botón para agregar un cliente" width="300">
  <p><i>Figura 4.2.2.6.15. Clientes del veterinario. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/sprint2/fig-4-2-2-6-16-android-vet-pacientes.png" alt="Pestaña Pacientes con el cliente Carlos Mendoza y la finca Hato Los Alamos elegidos y la lista de sus 18 animales" width="300">
  <p><i>Figura 4.2.2.6.16. Pacientes de un cliente por finca. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/sprint2/fig-4-2-2-6-17-android-vet-historial-clinico.png" alt="Historial clínico del animal Lola con sus registros sanitarios, el más reciente primero" width="300">
  <p><i>Figura 4.2.2.6.17. Historial clínico de un paciente. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/sprint2/fig-4-2-2-6-18a-android-vet-analitica.png" alt="Analítica del veterinario con los clientes asignados, los pacientes monitoreados y los registros sanitarios" width="300"> <img src="../../assets/chapter-4/sprint2/fig-4-2-2-6-18b-android-vet-analitica-graficos.png" alt="Analítica del veterinario con los registros por tipo y las visitas sanitarias por finca" width="300">
  <p><i>Figura 4.2.2.6.18. Analítica del veterinario. Fuente: elaboración propia.</i></p>
</div>

**Aplicación Flutter.** Se captura en un dispositivo o emulador, con el usuario `ganadero`.

<div align="center">
  <img src="../../assets/chapter-4/sprint2/fig-4-2-2-6-19-flutter-inicio-sesion.png" alt="Pantalla de inicio de sesión de la aplicación Flutter" width="300">
  <p><i>Figura 4.2.2.6.19. Inicio de sesión de la aplicación Flutter. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/sprint2/fig-4-2-2-6-20a-flutter-inicio-ganadero.png" alt="Inicio del ganadero en Flutter con el selector de finca, los contadores y las próximas actividades" width="300"> <img src="../../assets/chapter-4/sprint2/fig-4-2-2-6-20b-flutter-registros-recientes.png" alt="Registros sanitarios recientes en el inicio del ganadero en Flutter" width="300">
  <p><i>Figura 4.2.2.6.20. Inicio del ganadero en la aplicación Flutter. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/sprint2/fig-4-2-2-6-21a-flutter-menu-idioma.png" alt="Menú de idioma de la aplicación Flutter con English y Español" width="300"> <img src="../../assets/chapter-4/sprint2/fig-4-2-2-6-21b-flutter-espanol.png" alt="Inicio del ganadero en Flutter después de cambiar el idioma a Español" width="300">
  <p><i>Figura 4.2.2.6.21. Cambio de idioma en la aplicación Flutter. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/sprint2/fig-4-2-2-6-22-flutter-veterinario-mensaje.png" alt="Inicio de sesión en Flutter con una cuenta de veterinario y el mensaje de que la aplicación es solo para ganaderos" width="300">
  <p><i>Figura 4.2.2.6.22. Mensaje al iniciar sesión con el rol de veterinario en Flutter. Fuente: elaboración propia.</i></p>
</div>

**Distribución.**

<div align="center">
  <img src="../../assets/chapter-4/captura-pendiente.svg" alt="Captura pendiente: dispositivo físico con el correo de invitación de Firebase App Distribution o la aplicación App Tester mostrando la versión 0.2.0 lista para instalar" width="300">
  <p><i>Figura 4.2.2.6.23. Instalación de la aplicación desde Firebase App Distribution. Fuente: elaboración propia.</i></p>
</div>

**Videos de ejecución del Sprint 2.** Pendiente de completar: los enlaces se agregarán cuando estén grabados.

- **Backend:** pendiente de completar (enlace al video).
- **App Android:** pendiente de completar (enlace al video).
- **App Flutter:** pendiente de completar (enlace al video).

<a id="toc-4-2-2-7-services-documentation-evidence-for-sprint-review"></a>

### 4.2.2.7. Services Documentation Evidence for Sprint Review

Con el Sprint 2 el backend queda completo y publicado, con su documentación OpenAPI en Swagger. Esta sección documenta los endpoints que se añaden o cambian en el sprint: el archivado de animales, el nombre base del alta masiva, las suscripciones y sus planes, las actividades, los movimientos financieros, los dispositivos y sus lecturas, los clientes del veterinario y los paneles analíticos. Los endpoints de autenticación, fincas, corrales, animales y registros sanitarios del Sprint 1 se describen en la sección 4.2.1.7.

**Alcance por usuario.** El cambio transversal del sprint es que el servidor devuelve y modifica solo lo que corresponde al usuario autenticado: un ganadero ve sus fincas, corrales, animales, registros, actividades, movimientos, dispositivos y suscripciones; un veterinario ve lo de sus clientes. Una lista solo contiene los recursos del usuario, y consultar, crear, modificar o eliminar un recurso ajeno responde `403 Forbidden`. Las llamadas con un identificador que no existe siguen respondiendo `404`.

**Convención de llamada.** Es la de la sección 4.2.1.7: las rutas parten de `{BASE_URL}/api/v1`, las solicitudes con cuerpo usan `Content-Type: application/json`, cada llamada envía `Authorization: Bearer <token>` y las fechas usan `yyyy-MM-dd`. En los ejemplos, `<token>` representa el token real.

**Animales: cambios del sprint** (`/animals`; escritura solo para Rancher)

| Related story | HTTP | Call syntax | Parameters / body | Success response | Error responses |
|---|---|---|---|---|---|
| US-012 | PATCH | `curl -X PATCH "{BASE_URL}/api/v1/animals/1/status" -H "Authorization: Bearer <token>" -H "Content-Type: application/json" -d '{"status":"Archivado"}'` | Ruta: `id`. Body `UpdateAnimalStatusResource`: `status`. El valor `Archivado` archiva el animal y cualquier otro estado lo restaura. | `200` con el `AnimalResource` actualizado. | `400` si falta el estado; `404` si no existe; `401`; `403` si el animal es ajeno o el rol no es Rancher. |
| US-010, US-012 | GET | `curl "{BASE_URL}/api/v1/animals?archived=false" -H "Authorization: Bearer <token>"` | Query opcional `archived`: `false` excluye los archivados, `true` devuelve solo los archivados y, sin el parámetro, se devuelven todos. | `200` con la lista de animales del usuario. | `401`; `403`. |
| US-011 | POST | `curl -X POST "{BASE_URL}/api/v1/animals/bulk" -H "Authorization: Bearer <token>" -H "Content-Type: application/json" -d '{"name":"polloComercio","species":"Ave","breed":"Cobb","gender":"Mixto","weight":1.8,"status":"Saludable","herdId":2,"corralId":4,"quantity":10}'` | Body `CreateAnimalBatchResource`: los datos del lote, `quantity` (de 1 a 500) y `name` opcional. | `201` con los animales creados. Con `name` se llaman `polloComercio-001`, `polloComercio-002`… y la numeración continúa si se repite el nombre en la finca; sin `name`, el nombre es el código generado. | `400` si el lote es inválido; `401`; `403`. |

**Planes de suscripción** (`/subscription-plans`)

Ejemplo de `SubscriptionPlanResource`: `{"id":1,"name":"Ganadero Basico","price":49.00,"stripePriceId":"mock_price_rancher_basic","maxAnimals":80,"isActive":true}`. Los planes se cargan al iniciar la API en cualquier entorno, solo si la tabla está vacía.

| Related story | HTTP | Call syntax | Parameters / body | Success response | Error responses |
|---|---|---|---|---|---|
| US-038 | GET | `curl "{BASE_URL}/api/v1/subscription-plans" -H "Authorization: Bearer <token>"` | Ninguno. | `200` con la lista de planes: Ganadero Básico (S/ 49, hasta 80 animales), Ganadero Pro (S/ 99, hasta 250) y Veterinario Profesional (S/ 129, hasta 1000). | `401`; `403`. |
| US-038 | GET | `curl "{BASE_URL}/api/v1/subscription-plans/1" -H "Authorization: Bearer <token>"` | Ruta: `id`. | `200` con el `SubscriptionPlanResource`. | `404` si no existe; `401`. |

**Suscripciones** (`/subscriptions`; Rancher y Veterinarian)

Ejemplo de `SubscriptionResource`: `{"id":1,"userId":1,"planId":2,"stripeCustomerId":"cus_...","stripeSubscriptionId":"sub_...","status":"Active","startedAt":"2026-10-25","endsAt":null}`. Ejemplo de `PaymentResource`: `{"id":1,"userId":1,"subscriptionId":1,"amount":99.00,"currency":"PEN","provider":"StripeTest","providerPaymentId":"cs_test_...","status":"Paid","paidAt":"2026-10-25T10:15:00"}`.

| Related story | HTTP | Call syntax | Parameters / body | Success response | Error responses |
|---|---|---|---|---|---|
| US-039 | POST | `curl -X POST "{BASE_URL}/api/v1/subscriptions/stripe-checkout" -H "Authorization: Bearer <token>" -H "Content-Type: application/json" -d '{"planId":2,"platform":"android"}'` | Body `StripeCheckoutResource`: `planId` y `platform`. Con `android`, Stripe vuelve a una página HTTPS de la API que abre la aplicación. El cobro es mensual, en soles y en modo de prueba. | `200` con `{"sessionId":"cs_test_...","checkoutUrl":"https://checkout.stripe.com/..."}`; la aplicación abre `checkoutUrl` en una Custom Tab. | `404` si el plan no existe o está inactivo; `400` si Stripe no está configurado; `401`. |
| US-040 | GET | `curl "{BASE_URL}/api/v1/subscriptions/stripe-checkout/cs_test_.../confirm" -H "Authorization: Bearer <token>"` | Ruta: `sessionId`. | `200` con `{"subscription":{...},"payment":{...}}`: se desactivan las suscripciones activas anteriores y se registra la nueva con su pago. Repetir la confirmación devuelve el mismo resultado. | `400` si el pago no se completó; `403` si la sesión pertenece a otro usuario; `404` si el plan no existe; `401`. |
| US-040 | GET | `curl "{BASE_URL}/api/v1/subscriptions/users/1/active" -H "Authorization: Bearer <token>"` | Ruta: `userId`, que debe ser el del usuario autenticado. | `200` con la suscripción activa más reciente. | `404` si no tiene una suscripción activa; `403` si el `userId` es ajeno; `401`. |
| US-040 | GET | `curl "{BASE_URL}/api/v1/subscriptions/users/1/payments" -H "Authorization: Bearer <token>"` | Ruta: `userId`, el del usuario autenticado. | `200` con la lista de pagos. | `403` si el `userId` es ajeno; `401`. |
| TS-011 | GET | `curl "{BASE_URL}/api/v1/subscriptions/mobile-return/success?session_id=cs_test_..."` | Query: `session_id`. Es una página pública a la que Stripe devuelve al usuario; no figura en Swagger. | `200` con una página HTML que abre `anitec://subscriptions/success?session_id=...`. El identificador con caracteres inesperados se descarta. | — |
| TS-011 | GET | `curl "{BASE_URL}/api/v1/subscriptions/mobile-return/cancel"` | Ninguno. Página pública. | `200` con una página HTML que abre `anitec://subscriptions/cancel`. | — |

Los endpoints `POST`, `PUT` y `DELETE` de `/subscriptions` y de `/subscription-plans` y el pago simulado `POST /subscriptions/mock-checkout` siguen disponibles para el desarrollo, pero la aplicación no los usa y el pago simulado responde `404` en producción.

**Actividades** (`/farm-events`; Rancher y Veterinarian)

Ejemplo de `FarmActivityResource`: `{"id":1,"ownerId":1,"veterinarianId":2,"title":"Visita sanitaria Los Alamos","type":"Visita veterinaria","date":"2026-10-28","priority":"Alta","status":"Pendiente"}`. Un ganadero crea actividades propias; un veterinario las programa para un cliente suyo.

| Related story | HTTP | Call syntax | Parameters / body | Success response | Error responses |
|---|---|---|---|---|---|
| US-025 | GET | `curl "{BASE_URL}/api/v1/farm-events" -H "Authorization: Bearer <token>"` | Ninguno. | `200` con las actividades del usuario (las suyas y, para el veterinario, las de sus clientes). | `401`; `403`. |
| US-025 | GET | `curl "{BASE_URL}/api/v1/farm-events/1" -H "Authorization: Bearer <token>"` | Ruta: `id`. | `200` con el `FarmActivityResource`. | `404`; `401`; `403` si es ajena. |
| US-026 | POST | `curl -X POST "{BASE_URL}/api/v1/farm-events" -H "Authorization: Bearer <token>" -H "Content-Type: application/json" -d '{"ownerId":1,"veterinarianId":2,"title":"Visita sanitaria Los Alamos","type":"Visita veterinaria","date":"2026-10-28","priority":"Alta","status":"Pendiente"}'` | Body `CreateFarmActivityResource`: `ownerId`, `veterinarianId` (opcional), `title`, `type`, `date`, `priority` y `status`. | `201` con la actividad creada. | `400` datos inválidos; `401`; `403` si el ganadero crea una actividad para otra persona o el veterinario la programa para quien no es su cliente. |
| US-026 | PUT | `curl -X PUT "{BASE_URL}/api/v1/farm-events/1" -H "Authorization: Bearer <token>" -H "Content-Type: application/json" -d '{...}'` | Ruta: `id`. Body `CreateFarmActivityResource`. | `200` con la actividad actualizada. | `404`; `400`; `401`; `403`. |
| US-026 | DELETE | `curl -X DELETE "{BASE_URL}/api/v1/farm-events/1" -H "Authorization: Bearer <token>"` | Ruta: `id`. | `204` sin contenido. | `404`; `401`; `403`. |

**Movimientos financieros** (`/financial-records`; solo Rancher)

Ejemplo de `FinancialRecordResource`: `{"id":1,"ownerId":1,"type":"Ingreso","category":"Venta de leche","amount":4200.00,"date":"2026-08-06","description":"Venta semanal de leche"}`.

| Related story | HTTP | Call syntax | Parameters / body | Success response | Error responses |
|---|---|---|---|---|---|
| US-037 | GET | `curl "{BASE_URL}/api/v1/financial-records" -H "Authorization: Bearer <token>"` | Ninguno. | `200` con los movimientos del ganadero. | `401`; `403`. |
| US-037 | POST | `curl -X POST "{BASE_URL}/api/v1/financial-records" -H "Authorization: Bearer <token>" -H "Content-Type: application/json" -d '{"ownerId":1,"type":"Gasto","category":"Alimento","amount":850.50,"date":"2026-10-20","description":"Compra de alimento"}'` | Body `CreateFinancialRecordResource`: `ownerId`, `type` (`Ingreso` o `Gasto`), `category`, `amount`, `date` y `description`. | `201` con el movimiento creado. | `400` datos inválidos; `401`; `403` si `ownerId` es otra persona. |
| US-037 | PUT | `curl -X PUT "{BASE_URL}/api/v1/financial-records/1" -H "Authorization: Bearer <token>" -H "Content-Type: application/json" -d '{...}'` | Ruta: `id`. Body `CreateFinancialRecordResource`. | `200` con el movimiento actualizado. | `404`; `400`; `401`; `403`. |
| US-037 | DELETE | `curl -X DELETE "{BASE_URL}/api/v1/financial-records/1" -H "Authorization: Bearer <token>"` | Ruta: `id`. | `204` sin contenido. | `404`; `401`; `403`. |

**Dispositivos IoT y lecturas** (`/devices` y `/device-metrics`; escritura de dispositivos solo para Rancher)

Ejemplo de `DeviceResource`: `{"id":1,"name":"Balanza Los Alamos","type":"Scale","serialNumber":"SCL-001","status":"Online","herdId":1,"animalId":null}`. Ejemplo de `DeviceMetricResource`: `{"id":1,"deviceId":1,"type":"Weight","value":455.00,"unit":"kg","recordedAt":"2026-10-24T12:42:40"}`. Un dispositivo debe asignarse a una finca o a un animal que el usuario pueda ver.

| Related story | HTTP | Call syntax | Parameters / body | Success response | Error responses |
|---|---|---|---|---|---|
| Sin historia | GET | `curl "{BASE_URL}/api/v1/devices" -H "Authorization: Bearer <token>"` | Ninguno. | `200` con los dispositivos visibles para el usuario. | `401`; `403`. |
| Sin historia | POST | `curl -X POST "{BASE_URL}/api/v1/devices" -H "Authorization: Bearer <token>" -H "Content-Type: application/json" -d '{"name":"Balanza Los Alamos","type":"Scale","serialNumber":"SCL-001","status":"Online","herdId":1,"animalId":null}'` | Body `CreateDeviceResource`: `name`, `type`, `serialNumber`, `status`, `herdId` y `animalId` (uno de los dos). | `201` con el dispositivo creado. | `400` si no tiene una finca ni un animal asignados; `403` si la finca o el animal no son visibles para el usuario; `401`. |
| Sin historia | PUT / DELETE | `curl -X PUT "{BASE_URL}/api/v1/devices/1" ...` y `curl -X DELETE "{BASE_URL}/api/v1/devices/1" ...` | Ruta: `id`. | `200` con el dispositivo actualizado o `204`. | `404`; `400`; `401`; `403`. |
| Sin historia | GET | `curl "{BASE_URL}/api/v1/devices/1/metrics" -H "Authorization: Bearer <token>"` | Ruta: `id`. | `200` con las lecturas del dispositivo, la más reciente primero. | `404` si el dispositivo no existe; `401`; `403`. |
| Sin historia | GET | `curl "{BASE_URL}/api/v1/devices/1/latest-metric" -H "Authorization: Bearer <token>"` | Ruta: `id`. | `200` con la última lectura. | `404` si no existe el dispositivo o no tiene lecturas; `401`; `403`. |
| Sin historia | GET | `curl "{BASE_URL}/api/v1/device-metrics" -H "Authorization: Bearer <token>"` | Ninguno. | `200` con las lecturas de los dispositivos visibles para el usuario. | `401`; `403`. |

**Clientes del veterinario** (`/veterinarian`; solo Veterinarian, y solo sobre su propio identificador)

Ejemplo de cliente: `{"id":1,"veterinarianId":2,"rancherId":1,"rancherName":"Carlos Mendoza","status":"Active","herds":3,"animals":59}`.

| Related story | HTTP | Call syntax | Parameters / body | Success response | Error responses |
|---|---|---|---|---|---|
| US-023 | GET | `curl "{BASE_URL}/api/v1/veterinarian/2/clients" -H "Authorization: Bearer <token>"` | Ruta: `veterinarianId`, el del usuario. | `200` con los clientes del veterinario, con su número de fincas y animales. | `403` si el identificador es ajeno; `401`. |
| US-023 | GET | `curl "{BASE_URL}/api/v1/veterinarian/2/available-ranchers" -H "Authorization: Bearer <token>"` | Ruta: `veterinarianId`. | `200` con los ganaderos que aún no son sus clientes (`id`, `username`, `fullName`, `herds` y `animals`). | `403`; `401`. |
| US-023 | POST | `curl -X POST "{BASE_URL}/api/v1/veterinarian/2/clients/1" -H "Authorization: Bearer <token>"` | Ruta: `veterinarianId` y `rancherId`. | `201` con el vínculo creado. | `409` si ya es su cliente; `403`; `401`. |
| US-023 | DELETE | `curl -X DELETE "{BASE_URL}/api/v1/veterinarian/2/clients/1" -H "Authorization: Bearer <token>"` | Ruta: `veterinarianId` y `rancherId`. | `204` sin contenido; el veterinario deja de ver los datos de ese ganadero. | `404` si no es su cliente; `403`; `401`. |

**Paneles analíticos** (`/analytics`; Rancher y Veterinarian)

Los endpoints entregan indicadores calculados en el servidor. La aplicación Android calcula sus indicadores con los datos de su caché, por lo que estos endpoints quedan documentados para otros clientes.

| Related story | HTTP | Call syntax | Parameters / body | Success response | Error responses |
|---|---|---|---|---|---|
| US-035 | GET | `curl "{BASE_URL}/api/v1/analytics/ranchers/1/dashboard" -H "Authorization: Bearer <token>"` | Ruta: `rancherId`, el del usuario. | `200` con los totales del ganadero: `{"herds":...,"animals":...,"healthyAnimals":...,"healthEvents":...,"upcomingActivities":...,"devices":...,"income":...,"expenses":...,"balance":...}`. | `403` si el identificador es ajeno; `401`. |
| US-036 | GET | `curl "{BASE_URL}/api/v1/analytics/veterinarians/2/dashboard" -H "Authorization: Bearer <token>"` | Ruta: `veterinarianId`, el del usuario. | `200` con los totales del veterinario: `{"clients":...,"herds":...,"patients":...,"healthEvents":...,"upcomingVisits":...,"activeTreatments":...}`. | `403`; `401`. |
| US-035 | GET | `curl "{BASE_URL}/api/v1/analytics/ranchers/1/health-summary" -H "Authorization: Bearer <token>"` | Ruta: `rancherId`. Lo consulta el ganadero o su veterinario. | `200` con el total de registros y su distribución por tipo: `{"totalEvents":...,"byType":[{"label":"Vacuna","value":...}]}`. | `403`; `401`. |
| US-037 | GET | `curl "{BASE_URL}/api/v1/analytics/ranchers/1/financial-summary" -H "Authorization: Bearer <token>"` | Ruta: `rancherId`, el del ganadero. | `200` con `{"income":...,"expenses":...,"balance":...,"byCategory":[...]}`. | `403`; `401`. |

- **Web Services repository:** <https://github.com/ADM-1ACC0238-2620-13975-Grupo01/anitec-backend/tree/main>
- **Swagger:** <https://anitec-backend-android.onrender.com/swagger/index.html>
- **API publicada:** <https://anitec-backend-android.onrender.com>
- **Documentation commits:** pendiente de completar.
- **Interaction screenshots:** las capturas siguientes muestran llamadas con datos de muestra desde Swagger.

<div align="center">
  <img src="../../assets/chapter-4/captura-pendiente.svg" alt="Captura pendiente: Swagger UI del servicio publicado con los grupos Animals, Subscriptions, SubscriptionPlans, FarmActivities, FinancialRecords, Devices y VeterinarianClients desplegados" width="800">
  <p><i>Figura 4.2.2.7.1. Swagger UI con los endpoints del Sprint 2. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/captura-pendiente.svg" alt="Captura pendiente: en Swagger, PATCH /api/v1/animals/{id}/status con el cuerpo {&quot;status&quot;:&quot;Archivado&quot;}, un id de animal de muestra, y la respuesta 200 (hacerlo autorizado con el token del usuario ganadero)" width="800">
  <p><i>Figura 4.2.2.7.2. PATCH /animals/{id}/status para archivar un animal. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/captura-pendiente.svg" alt="Captura pendiente: en Swagger, GET /api/v1/subscription-plans autorizado con el token y la respuesta 200 con los tres planes" width="800">
  <p><i>Figura 4.2.2.7.3. GET /subscription-plans con los planes de suscripción. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/captura-pendiente.svg" alt="Captura pendiente: en Swagger, POST /api/v1/subscriptions/stripe-checkout con el cuerpo {&quot;planId&quot;:1,&quot;platform&quot;:&quot;android&quot;} y la respuesta 200 con el sessionId y la checkoutUrl (ocultar parte de la URL si lo prefieres)" width="800">
  <p><i>Figura 4.2.2.7.4. POST /subscriptions/stripe-checkout con la sesión de pago creada. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/captura-pendiente.svg" alt="Captura pendiente: en Swagger, GET /api/v1/farm-events o GET /api/v1/financial-records autorizado con el token y la respuesta 200 con datos de muestra" width="800">
  <p><i>Figura 4.2.2.7.5. Consulta de actividades o movimientos financieros con datos de muestra. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/captura-pendiente.svg" alt="Captura pendiente: en Swagger, autorizado con el token de un ganadero, GET /api/v1/animals/{id} con el id de un animal de otro ganadero (por ejemplo del usuario maria) y la respuesta 403" width="800">
  <p><i>Figura 4.2.2.7.6. Respuesta 403 al consultar un animal de otro ganadero. Fuente: elaboración propia.</i></p>
</div>

<a id="toc-4-2-2-8-software-deployment-evidence-for-sprint-review"></a>

### 4.2.2.8. Software Deployment Evidence for Sprint Review

Durante el Sprint 2 se desplegó la versión completa del backend, se cargaron en el servicio publicado los datos de demostración y se distribuyeron las dos aplicaciones móviles. Para la distribución se creó el proyecto de Firebase «AniTec», se registraron las aplicaciones Android y Flutter, se generaron los APK firmados y se publicaron en App Distribution con un grupo de evaluadores con vínculos de invitación. Los pasos detallados están en la sección 4.1.4.

| Product | Platform | Configuration performed | Version / Commit | Public URL or Release | Status |
|---|---|---|---|---|---|
| Landing Page | GitHub Pages | Sin cambios en el sprint. Queda pendiente reemplazar el botón de descarga de Android por el vínculo de invitación de Firebase (tarea T-061). | Pendiente | <https://adm-1acc0238-2620-13975-grupo01.github.io/anitec-landing-page/> | Publicada |
| Web Services | Render | Redespliegue del servicio con el backend completo, variable `SeedDemoData` para cargar los datos de demostración y límite de conexiones en la cadena de conexión. | Pendiente | API: <https://anitec-backend-android.onrender.com>. Swagger: <https://anitec-backend-android.onrender.com/swagger/index.html> | Publicado |
| Android | Firebase App Distribution | Proyecto «AniTec» (`anitec-17af9`), aplicación `com.anitec.platform`, APK `release` firmado con R8 (cerca de 25 MB), grupo «Equipo AniTec» y vínculos de invitación del grupo. | `versionName` `0.2.0` (`versionCode` 2); commit pendiente | Versión 0.2.0 (2) del 2026-10-25. Vínculos del grupo: <https://appdistribution.firebase.dev/i/417dc4e6d8ae3e32> y <https://appdistribution.firebase.dev/i/862507cca1d4abc6> | Publicada |
| Flutter | Firebase App Distribution | Aplicación `com.anitec.platform.flutter` en el mismo proyecto, APK `release` firmado con el mismo keystore (52 MB) y el mismo grupo, con los mismos vínculos de invitación. | Versión `1.0.0+1`; commit pendiente | Versión 1.0.0 (1) del 2026-10-25, en el mismo grupo | Publicada |

**Pasos ejecutados (Web Services):**

1. Integrar los cambios del sprint en la rama `main` de `anitec-backend`; el push inicia el despliegue automático en Render.
2. Cargar los datos de demostración en la base publicada, que ya contenía datos de una carga anterior: vaciar sus tablas desde el cliente web del proveedor con `DROP TABLE` (sin eliminar la base, para conservar sus credenciales), definir `SeedDemoData=true` en el panel **Environment** de Render y esperar el redespliegue, durante el cual la API crea las tablas con las migraciones y carga los datos. La base quedó con 7 usuarios, 11 fincas, 34 corrales y 182 animales, además de sus registros sanitarios, actividades, movimientos financieros, dispositivos, suscripciones y pagos.
3. Verificar el servicio publicado: iniciar sesión con el usuario `ganadero` devuelve `200` y sus listas de fincas, corrales y animales contienen sus datos (3 fincas, 10 corrales y 59 animales).
4. Corregir un fallo de carga: al abrir la aplicación en el teléfono aparecía «El servidor tuvo un problema». Las pruebas contra el servicio mostraron que cada petición respondía `200` por separado, pero que al pedir a la vez las ocho listas del inicio la mayoría respondía `500`, porque el plan gratuito de la base de datos limita las conexiones simultáneas. Se añadió `;Maximum Pool Size=2` al final de `ConnectionStrings__DefaultConnection`, con lo que las peticiones esperan turno, y la aplicación cargó sus datos correctamente.
5. Desactivar `SeedDemoData` (se retira de las variables o se pone en `false`) para que el servicio no intente cargar datos en los siguientes arranques.

<div align="center">
  <img src="../../assets/chapter-4/captura-pendiente.svg" alt="Captura pendiente: panel Environment del servicio anitec-backend-android en Render con las variables, incluida SeedDemoData, y todos los valores ocultos o tapados" width="800">
  <p><i>Figura 4.2.2.8.1. Variables de entorno del backend con la variable SeedDemoData (valores ocultos). Fuente: elaboración propia (captura de Render).</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/captura-pendiente.svg" alt="Captura pendiente: cliente web del proveedor de la base de datos (o MySQL Workbench) mostrando las 16 tablas con sus filas después de la carga de datos (por ejemplo animals 182, users 7), sin mostrar la contraseña" width="800">
  <p><i>Figura 4.2.2.8.2. Base de datos publicada con los datos de demostración cargados. Fuente: elaboración propia (captura del proveedor).</i></p>
</div>

**Pasos ejecutados (aplicaciones móviles):**

1. Crear el keystore con `keytool` y guardarlo fuera del repositorio, con una copia de respaldo; configurar `keystore.properties` en Android y `android/key.properties` en Flutter (ambos ignorados por git).
2. Generar el APK de Android con `./gradlew assembleRelease` (tras `./gradlew --stop`, para cerrar daemons iniciados con otro JDK) y el de Flutter con `flutter build apk --release`. La firma del APK de Flutter se comprobó con `apksigner verify --print-certs`.
3. Instalar el APK de Android en un dispositivo físico y comprobar que inicia sesión y carga los datos del backend publicado.
4. Crear el proyecto «AniTec» en Firebase Console, sin Gemini ni Google Analytics, y registrar las dos aplicaciones Android (Figura 4.1.4.4).
5. Subir los APK en App Distribution (Figuras 4.1.4.5 y 4.1.4.6), crear el grupo «Equipo AniTec» y distribuir cada versión.
6. Crear vínculos de invitación para el grupo «Equipo AniTec» (Figura 4.1.4.7), que la consola muestra desde las dos aplicaciones, y comprobar la instalación.

<div align="center">
  <img src="../../assets/chapter-4/captura-pendiente.svg" alt="Captura pendiente: terminal con el comando keytool -genkeypair terminado (sin mostrar contraseñas) o la salida de gradlew assembleRelease con BUILD SUCCESSFUL y la ruta de app-release.apk" width="800">
  <p><i>Figura 4.2.2.8.3. Generación del keystore y de la compilación release firmada. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/sprint2/fig-4-2-2-8-4-firebase-grupo-equipo-anitec.png" alt="App Distribution, pestaña Verificadores y grupos, con el grupo Equipo AniTec seleccionado y sus miembros" width="800">
  <p><i>Figura 4.2.2.8.4. Grupo de evaluadores «Equipo AniTec» en App Distribution. Fuente: elaboración propia (captura de Firebase).</i></p>
</div>

<a id="toc-4-2-2-9-team-collaboration-insights-during-sprint"></a>

### 4.2.2.9. Team Collaboration Insights during Sprint

Esta sección interpreta la participación del equipo a partir de las tareas del Sprint Backlog (sección 4.2.2.3), de los commits de los repositorios y de la colaboración por producto. Las métricas se analizan en contexto y no se usan de forma aislada para medir aporte. El Sprint 2 repartió las tareas en partes iguales: cada integrante tuvo 40 de las 200 horas estimadas.

| Integrante | Productos / aspectos | Contribución en el sprint | Evidencia | Reflexión |
|---|---|---|---|---|
| Sebastian Martin Beingolea Montalvo | Backend, aplicación Flutter (pruebas) y despliegue | Implementó el filtrado de los datos por usuario en el servidor, el retorno móvil de Stripe y la confirmación del pago, la carga de los planes de suscripción, el archivado de animales y el nombre base del alta masiva con los datos de demostración. Configuró el servicio publicado y escribió las pruebas de la aplicación Flutter. | Tareas T-031 a T-037. Commits: pendiente de completar. | Hacer que el servidor decida qué ve cada usuario me mostró que la seguridad no puede depender de la aplicación, y que cada regla debe tener su prueba de integración, incluida la de quien intenta ver lo ajeno. Con Stripe aprendí que el pago ocurre fuera de nuestro sistema y que lo importante es confirmarlo en el servidor. Al desplegar descubrí que un recurso gratuito, como el límite de conexiones de la base, puede romper lo que funciona en local, y que conviene probar con las mismas condiciones de uso real. |
| Josep Eliu Melgarejo Quiroz | Aplicación Android e informe | Implementó la vista del veterinario (clientes, pacientes e historial), el trabajo sin conexión con la cola de operaciones, las suscripciones con Stripe en Android, la corrección de la navegación inferior con su prueba y el permiso de red local para depurar. Mantiene la estructura del informe, ajustó el Product Backlog y documentó el sprint. | Tareas T-038 a T-043. Commits: pendiente de completar. | La corrección de la navegación inferior me enseñó a reproducir un error con una prueba antes de arreglarlo: así supe que la causa era la pila guardada y no otra, y quedó cubierta. Implementar la cola sin conexión me mostró que reintentar sin claves de idempotencia puede duplicar registros, algo que queda para el Sprint 3. Documentar el sprint contrastando cada historia con el código me obligó a reconocer cuáles quedaron parciales. |
| Saul Ortega Muñoz | Aplicación Android (escáner y dispositivos), Flutter, pruebas del backend y Landing Page | Implementó el escáner de códigos QR con ML Kit y la búsqueda manual, los dispositivos IoT, la arquitectura y el diseño del proyecto Flutter, las pruebas de integración y BDD del backend, y los mensajes de error y el idioma. Tiene pendiente la actualización de la Landing Page. | Tareas T-056 a T-061. Commits: pendiente de completar. | Integrar ML Kit con CameraX me enseñó a trabajar con un recurso del dispositivo que el emulador no puede probar: el permiso denegado, el código ilegible y la búsqueda manual deben resolverse sin la cámara, y la lectura real queda por comprobar en un teléfono. Crear el proyecto Flutter con la misma estructura por contextos que Android me mostró que una arquitectura clara se traslada entre tecnologías. |
| Luciana Celeste Sanchez Silva | Diseño UX/UI, aplicación Android (actividades y finanzas) y Flutter | Construyó las pantallas de actividades y de finanzas, el campo de nombre base del formulario de lotes, y en Flutter el inicio de sesión y el inicio del ganadero con su selector de finca, sus contadores y el cambio de idioma. Tiene pendientes los videos del AV2. | Tareas T-044 a T-049. Commits: pendiente de completar. | Llevar el mismo diseño del inicio a Flutter me mostró que los tokens de color y los estados de carga, vacío y error son lo que hace reconocible a una aplicación en cualquier tecnología. En finanzas aprendí que los montos exigen cuidar los decimales y el formato, y que un formulario solo debe mostrar errores después de un intento de guardado. |
| Giuseppe Villanueva Rodriguez | Aplicación Android (analítica y pruebas), compilación y distribución | Implementó la analítica del ganadero y del veterinario con gráficos propios, el archivado de animales en Android, la compilación firmada con R8, la distribución de las dos aplicaciones en Firebase y las pruebas unitarias e instrumentadas de Android. Tiene pendiente la verificación del QR y del pago de prueba en un dispositivo físico. | Tareas T-050 a T-055. Commits: pendiente de completar. | Firmar y distribuir las aplicaciones me enseñó pasos nuevos, como el keystore que no puede perderse, la firma que debe distinguir una versión de depuración de una de distribución y los vínculos de invitación. Escribir pruebas de los casos de uso de los contextos nuevos me confirmó que probar a la par de implementar evita errores cuando se añaden pantallas. |

Los repositorios del proyecto son:

- Informe: <https://github.com/ADM-1ACC0238-2620-13975-Grupo01/Informe>
- Landing Page: <https://github.com/ADM-1ACC0238-2620-13975-Grupo01/anitec-landing-page>
- Web Services: <https://github.com/ADM-1ACC0238-2620-13975-Grupo01/anitec-backend>
- Android: <https://github.com/ADM-1ACC0238-2620-13975-Grupo01/anitec-android>
- Flutter: <https://github.com/ADM-1ACC0238-2620-13975-Grupo01/anitec-flutter>

Las capturas siguientes muestran los analíticos de colaboración y de commits de GitHub (**Insights → Contributors** y **Insights → Commits**) de cada repositorio.

<div align="center">
  <img src="../../assets/chapter-4/captura-pendiente.svg" alt="Captura pendiente: GitHub del repositorio Informe, Insights → Contributors, mostrando los commits por integrante" width="800">
  <p><i>Figura 4.2.2.9.1. Analíticos de colaboración del repositorio Informe. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/captura-pendiente.svg" alt="Captura pendiente: GitHub del repositorio anitec-android, Insights → Contributors" width="800">
  <p><i>Figura 4.2.2.9.2. Analíticos de colaboración del repositorio anitec-android. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/captura-pendiente.svg" alt="Captura pendiente: GitHub del repositorio anitec-backend, Insights → Contributors" width="800">
  <p><i>Figura 4.2.2.9.3. Analíticos de colaboración del repositorio anitec-backend. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/captura-pendiente.svg" alt="Captura pendiente: GitHub del repositorio anitec-flutter, Insights → Contributors" width="800">
  <p><i>Figura 4.2.2.9.4. Analíticos de colaboración del repositorio anitec-flutter. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-4/captura-pendiente.svg" alt="Captura pendiente: GitHub del repositorio anitec-landing-page, Insights → Contributors (solo si hay commits en el Sprint 2)" width="800">
  <p><i>Figura 4.2.2.9.5. Analíticos de colaboración del repositorio anitec-landing-page. Fuente: elaboración propia.</i></p>
</div>

**Interpretación de los analíticos.** Los analíticos de GitHub se leen junto con las tareas del Sprint Backlog, porque el número de commits por autor no mide por sí solo el aporte de cada integrante. El trabajo se concentró en la aplicación Android, que reúne 106 de las 200 horas estimadas (53 %), seguida por el backend, con 40 horas (20 %), la aplicación Flutter, con 34 horas (17 %), y la distribución y la documentación, con 20 horas (10 %). Los cinco integrantes participaron en el desarrollo del backend o de las aplicaciones y cada uno lideró al menos un aspecto: Sebastian Beingolea lideró el backend y colaboró en las pruebas de Flutter, Josep Melgarejo lideró Android, Luciana Sanchez lideró el diseño y Flutter, Giuseppe Villanueva lideró las pruebas y la distribución, y Saul Ortega lideró la Landing Page y colaboró en Android, Flutter y el backend, como indica la matriz de la sección 4.2.2.2. El reparto por persona fue de 40 horas para cada integrante.

**Conclusión del trabajo en equipo.** Al cierre del Sprint 2 el equipo entregó el backend completo con 150 pruebas automatizadas, una aplicación Android con las funciones del ganadero y del veterinario, una primera versión de la aplicación Flutter y la distribución de las dos aplicaciones en Firebase App Distribution. De las 31 tareas, 25 quedaron en Done, 2 en To-Review (las suscripciones en Android y el escáner QR, que esperan su prueba en un dispositivo físico), 1 en In-Process (esta documentación) y 3 en Todo (los videos, la verificación en el dispositivo y la actualización de la Landing Page). De las 24 historias comprometidas, 14 se completaron y 10 quedaron parciales, y las historias del consentimiento veterinario, las notificaciones, la persistencia local en Flutter y la sincronización idempotente pasaron al Sprint 3. Como aprendizajes, el equipo destaca cerrar las historias parciales del sprint anterior, probar en las condiciones reales de uso, como las conexiones simultáneas de la base de datos publicada, y verificar en un dispositivo físico lo que el emulador no permite. Para el Sprint 3, el foco será el consentimiento del ganadero sobre el acceso veterinario, las notificaciones, el trabajo sin conexión con sincronización idempotente, la persistencia local en Flutter, la accesibilidad y la automatización de las pruebas de los flujos críticos.
