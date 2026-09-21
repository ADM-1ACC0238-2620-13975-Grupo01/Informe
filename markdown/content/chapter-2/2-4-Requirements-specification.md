# 2.4. Requirements specification

Esta sección especifica los requisitos de la solución móvil de AniTec a partir de las entrevistas, los User Personas, el Needfinding y los supuestos Lean UX. El alcance comprende la landing page estática, la API REST propia, una aplicación Android nativa desarrollada con Kotlin y Jetpack Compose, y una aplicación multiplataforma desarrollada con Flutter y Dart. Los requisitos también incluyen almacenamiento local, uso de la cámara, notificaciones, integración con Stripe como servicio externo y un feature de aprendizaje autónomo basado en Google ML Kit Barcode Scanning.

La priorización utiliza MoSCoW: **Must Have** identifica capacidades necesarias para cumplir el alcance o completar los flujos core; **Should Have** corresponde a capacidades importantes que admiten una implementación posterior dentro del proyecto; **Could Have** representa capacidades complementarias cuya inclusión depende de la capacidad disponible. Todo elemento incluido en el Product Backlog deberá implementarse antes de la entrega final o retirarse formalmente del alcance.

### To-Be Scenario Mapping

El To-Be Scenario Mapping representa cómo realizarán sus tareas Jorge Luis Rivas, del segmento ganadero, y Valeria Mendoza, del segmento veterinario, cuando utilicen AniTec. Los escenarios incorporan el uso en campo, la conectividad intermitente, la identificación mediante cámara, los recordatorios y el acceso veterinario autorizado.

#### To-Be Scenario Mapping: pequeño o mediano ganadero

**User Persona:** Jorge Luis Rivas
**Escenario:** Registro y seguimiento móvil de un animal durante el trabajo de campo.

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="background-color: #70AD47;">FASES</th>
    <th style="background-color: #70AD47;">Revisar actividades y seleccionar la finca</th>
    <th style="background-color: #70AD47;">Identificar al animal</th>
    <th style="background-color: #70AD47;">Registrar información en campo</th>
    <th style="background-color: #70AD47;">Programar el seguimiento</th>
    <th style="background-color: #70AD47;">Sincronizar y compartir el historial</th>
  </tr>
  <tr>
    <th style="background-color: #FFE699;">DOING</th>
    <td style="background-color: #DDEBF7;">Consulta sus actividades pendientes y los animales de la finca desde el teléfono.</td>
    <td style="background-color: #DDEBF7;">Escanea el código QR del animal o lo busca manualmente.</td>
    <td style="background-color: #DDEBF7;">Registra una incidencia, control o actualización; si no hay conexión, guarda el trabajo localmente.</td>
    <td style="background-color: #DDEBF7;">Define la próxima actividad y activa el recordatorio correspondiente.</td>
    <td style="background-color: #DDEBF7;">Revisa los cambios pendientes y permite que se sincronicen cuando vuelve la conexión.</td>
  </tr>
  <tr>
    <th style="background-color: #FFE699;">THINKING</th>
    <td style="background-color: #DDEBF7;">“Puedo saber qué debo atender antes de comenzar el recorrido”.</td>
    <td style="background-color: #DDEBF7;">“Necesito encontrar la ficha correcta sin perder tiempo”.</td>
    <td style="background-color: #DDEBF7;">“Quiero dejar el registro ahora para no olvidarlo después”.</td>
    <td style="background-color: #DDEBF7;">“El teléfono debe ayudarme a recordar la siguiente acción”.</td>
    <td style="background-color: #DDEBF7;">“Quiero confirmar que la información quedó guardada y disponible para el veterinario autorizado”.</td>
  </tr>
  <tr>
    <th style="background-color: #FFE699;">FEELING</th>
    <td style="background-color: #DDEBF7;">Orientado al tener una lista clara de pendientes.</td>
    <td style="background-color: #DDEBF7;">Confiado cuando identifica al animal correcto.</td>
    <td style="background-color: #DDEBF7;">Tranquilo al conservar el trabajo pese a la falta de conexión.</td>
    <td style="background-color: #DDEBF7;">Aliviado al delegar el recordatorio en la aplicación.</td>
    <td style="background-color: #DDEBF7;">Seguro cuando distingue los datos sincronizados de los pendientes.</td>
  </tr>
</table>

#### To-Be Scenario Mapping: veterinario de campo

**User Persona:** Valeria Mendoza
**Escenario:** Consulta de antecedentes, atención y seguimiento de un paciente autorizado.

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="background-color: #70AD47;">FASES</th>
    <th style="background-color: #70AD47;">Seleccionar un cliente autorizado</th>
    <th style="background-color: #70AD47;">Identificar al paciente</th>
    <th style="background-color: #70AD47;">Consultar antecedentes</th>
    <th style="background-color: #70AD47;">Registrar la atención</th>
    <th style="background-color: #70AD47;">Programar y sincronizar el seguimiento</th>
  </tr>
  <tr>
    <th style="background-color: #FFE699;">DOING</th>
    <td style="background-color: #DDEBF7;">Consulta los ganaderos que mantienen una autorización vigente.</td>
    <td style="background-color: #DDEBF7;">Escanea el código QR o busca al animal dentro de los pacientes del cliente.</td>
    <td style="background-color: #DDEBF7;">Revisa el historial sanitario disponible y su última sincronización.</td>
    <td style="background-color: #DDEBF7;">Registra diagnóstico, tratamiento y recomendaciones, incluso si la conexión se interrumpe.</td>
    <td style="background-color: #DDEBF7;">Programa el próximo control y verifica la sincronización de la atención.</td>
  </tr>
  <tr>
    <th style="background-color: #FFE699;">THINKING</th>
    <td style="background-color: #DDEBF7;">“Debo consultar únicamente los clientes que me autorizaron”.</td>
    <td style="background-color: #DDEBF7;">“Necesito confirmar que atenderé al paciente correcto”.</td>
    <td style="background-color: #DDEBF7;">“Los antecedentes me ayudarán a sustentar la decisión clínica”.</td>
    <td style="background-color: #DDEBF7;">“La atención debe quedar registrada con mi autoría”.</td>
    <td style="background-color: #DDEBF7;">“El ganadero debe poder consultar las indicaciones y la próxima fecha”.</td>
  </tr>
  <tr>
    <th style="background-color: #FFE699;">FEELING</th>
    <td style="background-color: #DDEBF7;">Seguro al reconocer el alcance de su autorización.</td>
    <td style="background-color: #DDEBF7;">Confiado al verificar la identidad del animal.</td>
    <td style="background-color: #DDEBF7;">Preparado al disponer de antecedentes ordenados.</td>
    <td style="background-color: #DDEBF7;">Responsable al dejar un registro trazable.</td>
    <td style="background-color: #DDEBF7;">Satisfecho al mantener continuidad entre visitas.</td>
  </tr>
</table>

## 2.4.1. User Stories

Las Epics y las historias siguientes describen resultados esperados para la landing page, las aplicaciones móviles y los servicios. Las User Stories evitan decisiones de interfaz en sus criterios de aceptación; las Technical Stories describen capacidades sin interacción directa y utilizan el rol Developer. Por otro lado, las Spike Stories delimitan investigaciones técnicas breves para reducir incertidumbre y comprobar la viabilidad de una alternativa antes de implementarla.
### Epics

<table>
  <thead><tr><th>Epic ID</th><th>Title</th><th>Description</th></tr></thead>
  <tbody>
    <tr><td>EP-001</td><td>Landing Page</td><td>Comunica la propuesta de valor, los segmentos atendidos y los canales de acceso a las aplicaciones móviles de AniTec.</td></tr>
    <tr><td>EP-002</td><td>Identity and Access Management</td><td>Gestiona el registro, la autenticación, la sesión y la autorización de ganaderos y veterinarios.</td></tr>
    <tr><td>EP-003</td><td>Farm and Livestock Management</td><td>Permite organizar fincas y registrar, consultar, actualizar y archivar animales desde las aplicaciones móviles.</td></tr>
    <tr><td>EP-004</td><td>Sanitary Management</td><td>Centraliza incidencias, diagnósticos, tratamientos, controles e historiales sanitarios de los animales.</td></tr>
    <tr><td>EP-005</td><td>Veterinary Collaboration</td><td>Gestiona la relación autorizada entre ganaderos y veterinarios para el seguimiento de clientes y pacientes.</td></tr>
    <tr><td>EP-006</td><td>Activities and Notifications</td><td>Organiza actividades ganaderas y sanitarias y genera recordatorios en los dispositivos móviles.</td></tr>
    <tr><td>EP-007</td><td>Offline Storage and Synchronization</td><td>Mantiene información esencial y trabajo pendiente en el dispositivo y lo sincroniza cuando vuelve la conexión.</td></tr>
    <tr><td>EP-008</td><td>Animal Identification and Autonomous Feature</td><td>Identifica animales mediante códigos QR y la cámara, incorporando una tecnología investigada de forma autónoma.</td></tr>
    <tr><td>EP-009</td><td>Analytics and Reports</td><td>Presenta indicadores sanitarios y operativos relevantes para ganaderos y veterinarios.</td></tr>
    <tr><td>EP-010</td><td>Financial and Subscription Management</td><td>Permite consultar finanzas, planes, pagos y el estado de la suscripción mediante un servicio externo.</td></tr>
    <tr><td>EP-011</td><td>Accessibility, Internationalization and Resilience</td><td>Asegura una experiencia comprensible, accesible, internacionalizada y tolerante a errores.</td></tr>
    <tr><td>EP-012</td><td>Mobile Platforms and Services</td><td>Agrupa la arquitectura y las integraciones técnicas de Android nativo, Flutter, API REST, almacenamiento y distribución.</td></tr>
  </tbody>
</table>

### User Stories

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-001</td>
    <td>Visitante</td>
    <td>Must Have</td>
    <td>EP-001</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Comprender la propuesta de valor de AniTec</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como visitante, quiero conocer el problema que resuelve AniTec y sus beneficios para determinar si la solución se relaciona con mis necesidades.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Propuesta disponible</b><br><b>Given</b> el contenido público de AniTec está publicado<br><b>When</b> el visitante accede a la dirección de la landing page<br><b>Then</b> el sistema presenta la propuesta de valor y los beneficios principales para la gestión ganadera<br><br><b>Scenario 2: Contenido verificable</b><br><b>Given</b> la startup todavía no dispone de resultados comerciales validados<br><b>When</b> el visitante consulta cifras o testimonios<br><b>Then</b> el sistema diferencia las metas y testimonios reales de cualquier información todavía no validada</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-002</td>
    <td>Visitante</td>
    <td>Must Have</td>
    <td>EP-001</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Conocer las soluciones para cada segmento</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como visitante, quiero conocer cómo AniTec ayuda a ganaderos y veterinarios para identificar la aplicación móvil adecuada para mi perfil.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Información para ganaderos</b><br><b>Given</b> el visitante pertenece al segmento ganadero<br><b>When</b> el visitante consulta la información dirigida a su segmento<br><b>Then</b> el sistema explica las capacidades móviles destinadas a la gestión del hato<br><br><b>Scenario 2: Información para veterinarios</b><br><b>Given</b> el visitante pertenece al segmento veterinario<br><b>When</b> el visitante consulta la información dirigida a su segmento<br><b>Then</b> el sistema explica las capacidades de seguimiento de clientes y pacientes</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-003</td>
    <td>Visitante</td>
    <td>Should Have</td>
    <td>EP-001</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Acceder a una landing page adaptable e internacionalizada</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como visitante, quiero consultar la landing page desde distintos dispositivos y en un idioma disponible para comprender la información y acceder a los canales de contacto o descarga.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Adaptación al dispositivo</b><br><b>Given</b> el visitante utiliza un teléfono, una tableta o una computadora<br><b>When</b> el visitante accede a la landing page<br><b>Then</b> el contenido conserva su legibilidad y permite completar las acciones principales<br><br><b>Scenario 2: Idioma disponible</b><br><b>Given</b> la landing page ofrece más de un idioma<br><b>When</b> el visitante selecciona un idioma<br><b>Then</b> el sistema muestra el contenido traducido y conserva la preferencia durante la navegación</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-004</td>
    <td>Ganadero o veterinario</td>
    <td>Must Have</td>
    <td>EP-002</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Registrar una cuenta según el rol</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como ganadero o veterinario, quiero crear una cuenta con mi rol para acceder a las capacidades que corresponden a mi actividad.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Registro válido</b><br><b>Given</b> la persona proporciona datos válidos y selecciona un rol permitido<br><b>When</b> la persona solicita crear su cuenta<br><b>Then</b> el sistema registra la cuenta y asocia el rol seleccionado<br><br><b>Scenario 2: Datos duplicados o inválidos</b><br><b>Given</b> ya existe una cuenta con el mismo correo o los datos incumplen una regla<br><b>When</b> la persona solicita crear su cuenta<br><b>Then</b> el sistema rechaza el registro e informa la causa sin exponer información sensible</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-005</td>
    <td>Usuario registrado</td>
    <td>Must Have</td>
    <td>EP-002</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Iniciar sesión</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como usuario registrado, quiero autenticarme con mis credenciales para consultar de manera segura mi información en AniTec.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Credenciales válidas</b><br><b>Given</b> existe una cuenta activa con las credenciales proporcionadas<br><b>When</b> el usuario solicita iniciar sesión<br><b>Then</b> el sistema autentica al usuario y habilita las capacidades de su rol<br><br><b>Scenario 2: Credenciales inválidas</b><br><b>Given</b> las credenciales no corresponden a una cuenta activa<br><b>When</b> el usuario solicita iniciar sesión<br><b>Then</b> el sistema rechaza el acceso mediante un mensaje que no revela qué dato es incorrecto</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-006</td>
    <td>Usuario autenticado</td>
    <td>Must Have</td>
    <td>EP-002</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Mantener y finalizar la sesión móvil</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como usuario autenticado, quiero conservar mi sesión de manera segura y poder finalizarla para evitar accesos no autorizados a mis datos.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Sesión vigente</b><br><b>Given</b> el usuario tiene una sesión válida almacenada de forma segura<br><b>When</b> el usuario vuelve a abrir la aplicación<br><b>Then</b> el sistema recupera la sesión y valida su vigencia antes de entregar información protegida<br><br><b>Scenario 2: Cierre de sesión</b><br><b>Given</b> el usuario mantiene una sesión activa<br><b>When</b> el usuario solicita finalizarla<br><b>Then</b> el sistema elimina las credenciales locales y bloquea el acceso a la información protegida</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-007</td>
    <td>Usuario autenticado</td>
    <td>Must Have</td>
    <td>EP-002</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Acceder únicamente a información autorizada</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como usuario autenticado, quiero acceder solamente a los datos permitidos para mi rol y relaciones vigentes para proteger la información ganadera y clínica.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Acceso permitido</b><br><b>Given</b> el usuario posee el rol y la relación requeridos por una operación<br><b>When</b> el usuario solicita consultar o modificar información<br><b>Then</b> el sistema procesa la operación dentro del alcance autorizado<br><br><b>Scenario 2: Acceso denegado</b><br><b>Given</b> el usuario no posee el rol o la relación requeridos<br><b>When</b> el usuario solicita consultar o modificar información protegida<br><b>Then</b> el sistema rechaza la operación y registra el resultado de autorización</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-008</td>
    <td>Ganadero</td>
    <td>Must Have</td>
    <td>EP-003</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Consultar las fincas registradas</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como ganadero, quiero consultar mis fincas para organizar los animales según su unidad productiva.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Fincas existentes</b><br><b>Given</b> el ganadero tiene una o más fincas registradas<br><b>When</b> el ganadero consulta sus fincas<br><b>Then</b> el sistema devuelve únicamente las fincas que le pertenecen<br><br><b>Scenario 2: Sin fincas</b><br><b>Given</b> el ganadero todavía no registra fincas<br><b>When</b> el ganadero consulta sus fincas<br><b>Then</b> el sistema informa que no existen unidades productivas registradas</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-009</td>
    <td>Ganadero</td>
    <td>Must Have</td>
    <td>EP-003</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Registrar y actualizar una finca</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como ganadero, quiero registrar y mantener los datos de una finca para asociar correctamente mis animales y actividades.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Registro válido</b><br><b>Given</b> el ganadero proporciona los datos obligatorios de una nueva finca<br><b>When</b> el ganadero solicita registrarla<br><b>Then</b> el sistema crea la finca y la deja disponible para asociar animales<br><br><b>Scenario 2: Actualización válida</b><br><b>Given</b> existe una finca perteneciente al ganadero<br><b>When</b> el ganadero modifica información permitida<br><b>Then</b> el sistema conserva los cambios y la relación con sus animales</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-010</td>
    <td>Ganadero</td>
    <td>Must Have</td>
    <td>EP-003</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Consultar y buscar animales</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como ganadero, quiero consultar y buscar los animales de mis fincas para localizar rápidamente el registro que necesito.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Consulta autorizada</b><br><b>Given</b> el ganadero tiene animales registrados<br><b>When</b> el ganadero consulta sus animales<br><b>Then</b> el sistema devuelve únicamente animales asociados a sus fincas<br><br><b>Scenario 2: Búsqueda</b><br><b>Given</b> existen animales que coinciden con un código, nombre, especie o raza<br><b>When</b> el ganadero realiza una búsqueda<br><b>Then</b> el sistema devuelve los animales coincidentes</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-011</td>
    <td>Ganadero</td>
    <td>Must Have</td>
    <td>EP-003</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Registrar un animal</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como ganadero, quiero registrar un animal en una de mis fincas para iniciar su trazabilidad sanitaria y productiva.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Registro válido</b><br><b>Given</b> el ganadero tiene una finca y proporciona los datos obligatorios del animal<br><b>When</b> el ganadero solicita registrar el animal<br><b>Then</b> el sistema crea un identificador único y asocia el animal con la finca<br><br><b>Scenario 2: Código duplicado</b><br><b>Given</b> ya existe un animal del ganadero con el mismo código de identificación<br><b>When</b> el ganadero solicita registrar otro animal con ese código<br><b>Then</b> el sistema rechaza la operación e informa la duplicidad</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-012</td>
    <td>Ganadero</td>
    <td>Must Have</td>
    <td>EP-003</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Actualizar o archivar un animal</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como ganadero, quiero actualizar o archivar un animal para mantener vigente el inventario sin perder su historial.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Actualización válida</b><br><b>Given</b> el animal pertenece al ganadero<br><b>When</b> el ganadero modifica datos permitidos<br><b>Then</b> el sistema conserva los cambios y mantiene el historial asociado<br><br><b>Scenario 2: Archivado</b><br><b>Given</b> el animal ya no forma parte del hato activo<br><b>When</b> el ganadero solicita archivarlo<br><b>Then</b> el sistema lo excluye del inventario activo y conserva su historial para consulta</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-013</td>
    <td>Usuario autorizado</td>
    <td>Must Have</td>
    <td>EP-003</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Consultar el detalle de un animal</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como usuario autorizado, quiero consultar la ficha de un animal para conocer sus datos e historial relevante antes de realizar una acción.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Detalle autorizado</b><br><b>Given</b> el usuario está autorizado para consultar el animal<br><b>When</b> el usuario solicita su detalle<br><b>Then</b> el sistema devuelve los datos generales y las referencias a su historial<br><br><b>Scenario 2: Animal no autorizado</b><br><b>Given</b> el usuario no tiene relación autorizada con el animal<br><b>When</b> el usuario solicita su detalle<br><b>Then</b> el sistema rechaza la consulta sin revelar información del animal</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-014</td>
    <td>Usuario autorizado</td>
    <td>Must Have</td>
    <td>EP-004</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Consultar eventos sanitarios</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como usuario autorizado, quiero consultar los eventos sanitarios de los animales a mi alcance para conocer su situación de salud.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Eventos existentes</b><br><b>Given</b> existen eventos sanitarios de animales autorizados<br><b>When</b> el usuario consulta los eventos<br><b>Then</b> el sistema devuelve la fecha, el tipo, el animal y el responsable de cada registro<br><br><b>Scenario 2: Sin eventos</b><br><b>Given</b> no existen eventos sanitarios dentro del alcance autorizado<br><b>When</b> el usuario realiza la consulta<br><b>Then</b> el sistema informa que no existen registros disponibles</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-015</td>
    <td>Ganadero</td>
    <td>Must Have</td>
    <td>EP-004</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Registrar una incidencia sanitaria</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como ganadero, quiero registrar una incidencia observada en uno de mis animales para dejar evidencia y solicitar seguimiento oportuno.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Incidencia válida</b><br><b>Given</b> el animal pertenece al ganadero y los datos obligatorios están completos<br><b>When</b> el ganadero registra la incidencia<br><b>Then</b> el sistema incorpora el evento al historial del animal<br><br><b>Scenario 2: Animal ajeno</b><br><b>Given</b> el animal no pertenece al ganadero<br><b>When</b> el ganadero intenta registrar una incidencia<br><b>Then</b> el sistema rechaza la operación</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-016</td>
    <td>Veterinario</td>
    <td>Must Have</td>
    <td>EP-004</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Registrar diagnóstico y tratamiento</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como veterinario, quiero registrar el diagnóstico, tratamiento y recomendaciones de un paciente autorizado para documentar la atención realizada.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Atención autorizada</b><br><b>Given</b> el paciente pertenece a un cliente que autorizó al veterinario<br><b>When</b> el veterinario registra una atención con datos válidos<br><b>Then</b> el sistema incorpora el registro al historial e identifica al profesional responsable<br><br><b>Scenario 2: Atención no autorizada</b><br><b>Given</b> el veterinario no tiene acceso vigente al paciente<br><b>When</b> el veterinario intenta registrar una atención<br><b>Then</b> el sistema rechaza la operación</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-017</td>
    <td>Usuario autorizado</td>
    <td>Must Have</td>
    <td>EP-004</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Consultar el historial sanitario de un animal</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como usuario autorizado, quiero consultar cronológicamente el historial sanitario de un animal para tomar decisiones con base en sus antecedentes.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Historial disponible</b><br><b>Given</b> el animal tiene eventos sanitarios y el usuario posee acceso<br><b>When</b> el usuario consulta el historial<br><b>Then</b> el sistema devuelve los eventos ordenados y con su responsable<br><br><b>Scenario 2: Conectividad interrumpida</b><br><b>Given</b> existe una copia local vigente del historial autorizado<br><b>When</b> el usuario consulta el historial sin conexión<br><b>Then</b> el sistema entrega la información disponible e indica cuándo fue actualizada</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-018</td>
    <td>Autor de un registro sanitario</td>
    <td>Should Have</td>
    <td>EP-004</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Corregir un registro sanitario con trazabilidad</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como autor de un registro sanitario, quiero corregir información incorrecta dejando constancia del cambio para preservar la confiabilidad del historial.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Corrección permitida</b><br><b>Given</b> el usuario es autor del registro y proporciona el motivo<br><b>When</b> el usuario solicita corregir información permitida<br><b>Then</b> el sistema guarda la nueva versión e identifica la fecha, el autor y el motivo<br><br><b>Scenario 2: Eliminación no permitida</b><br><b>Given</b> el registro clínico ya forma parte del historial<br><b>When</b> el usuario intenta eliminarlo definitivamente<br><b>Then</b> el sistema conserva el registro y ofrece el mecanismo de corrección o anulación trazable</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-019</td>
    <td>Veterinario</td>
    <td>Should Have</td>
    <td>EP-004</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Programar un control sanitario posterior</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como veterinario, quiero programar el próximo control de un paciente para dar continuidad al tratamiento indicado.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Control programado</b><br><b>Given</b> el veterinario registra una atención autorizada<br><b>When</b> el veterinario establece una fecha futura de control<br><b>Then</b> el sistema crea la actividad asociada al paciente y al cliente<br><br><b>Scenario 2: Fecha inválida</b><br><b>Given</b> la fecha propuesta no es posterior a la atención<br><b>When</b> el veterinario solicita programar el control<br><b>Then</b> el sistema rechaza la programación e informa la regla incumplida</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-020</td>
    <td>Ganadero</td>
    <td>Must Have</td>
    <td>EP-005</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Recibir una solicitud de seguimiento veterinario</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como ganadero, quiero recibir solicitudes de veterinarios para decidir quién puede consultar y registrar información sanitaria de mis animales.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Solicitud válida</b><br><b>Given</b> un veterinario registrado solicita relacionarse con el ganadero<br><b>When</b> el sistema procesa la solicitud<br><b>Then</b> el ganadero recibe la solicitud con la identidad del profesional y su estado pendiente<br><br><b>Scenario 2: Solicitud duplicada</b><br><b>Given</b> ya existe una solicitud pendiente o una relación vigente<br><b>When</b> el mismo veterinario envía otra solicitud<br><b>Then</b> el sistema evita crear una relación duplicada</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-021</td>
    <td>Ganadero</td>
    <td>Must Have</td>
    <td>EP-005</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Aceptar o rechazar acceso veterinario</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como ganadero, quiero aceptar o rechazar una solicitud veterinaria para controlar el acceso a la información de mis animales.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Solicitud aceptada</b><br><b>Given</b> existe una solicitud pendiente<br><b>When</b> el ganadero la acepta<br><b>Then</b> el sistema activa la relación y autoriza al veterinario dentro del alcance definido<br><br><b>Scenario 2: Solicitud rechazada</b><br><b>Given</b> existe una solicitud pendiente<br><b>When</b> el ganadero la rechaza<br><b>Then</b> el sistema cierra la solicitud sin conceder acceso</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-022</td>
    <td>Ganadero</td>
    <td>Must Have</td>
    <td>EP-005</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Revocar el acceso de un veterinario</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como ganadero, quiero revocar una autorización veterinaria para impedir futuras consultas o registros sobre mis animales.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Revocación válida</b><br><b>Given</b> existe una relación veterinaria vigente<br><b>When</b> el ganadero revoca la autorización<br><b>Then</b> el sistema impide nuevas operaciones del veterinario y conserva la autoría de registros anteriores<br><br><b>Scenario 2: Relación inexistente</b><br><b>Given</b> no existe una relación vigente con el veterinario<br><b>When</b> el ganadero solicita revocarla<br><b>Then</b> el sistema informa que no existe acceso activo</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-023</td>
    <td>Veterinario</td>
    <td>Must Have</td>
    <td>EP-005</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Consultar clientes y pacientes autorizados</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como veterinario, quiero consultar mis clientes y sus pacientes autorizados para organizar las atenciones de campo.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Clientes autorizados</b><br><b>Given</b> el veterinario tiene relaciones vigentes<br><b>When</b> el veterinario consulta sus clientes<br><b>Then</b> el sistema devuelve únicamente los ganaderos y pacientes autorizados<br><br><b>Scenario 2: Sin clientes</b><br><b>Given</b> el veterinario no tiene relaciones vigentes<br><b>When</b> el veterinario consulta sus clientes<br><b>Then</b> el sistema informa que no existen clientes autorizados</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-024</td>
    <td>Veterinario</td>
    <td>Must Have</td>
    <td>EP-005</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Consultar antecedentes de un paciente autorizado</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como veterinario, quiero consultar los antecedentes de un paciente autorizado para sustentar el diagnóstico y seguimiento.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Acceso vigente</b><br><b>Given</b> el ganadero mantiene autorización vigente<br><b>When</b> el veterinario consulta los antecedentes del paciente<br><b>Then</b> el sistema devuelve la información sanitaria permitida<br><br><b>Scenario 2: Acceso revocado</b><br><b>Given</b> el ganadero revocó la autorización<br><b>When</b> el veterinario vuelve a solicitar los antecedentes<br><b>Then</b> el sistema rechaza la consulta</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-025</td>
    <td>Usuario autenticado</td>
    <td>Must Have</td>
    <td>EP-006</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Consultar actividades programadas</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como usuario autenticado, quiero consultar mis actividades ganaderas o sanitarias para organizar el trabajo pendiente.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Actividades existentes</b><br><b>Given</b> el usuario tiene actividades dentro de un periodo<br><b>When</b> el usuario consulta su programación<br><b>Then</b> el sistema devuelve las actividades ordenadas por fecha y prioridad<br><br><b>Scenario 2: Actividades por rol</b><br><b>Given</b> existen actividades de distintos propietarios o profesionales<br><b>When</b> el usuario realiza la consulta<br><b>Then</b> el sistema devuelve solamente las actividades dentro de su alcance</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-026</td>
    <td>Usuario autenticado</td>
    <td>Must Have</td>
    <td>EP-006</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Gestionar una actividad o recordatorio</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como usuario autenticado, quiero crear, actualizar o cancelar una actividad para mantener vigente mi planificación.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Actividad válida</b><br><b>Given</b> el usuario proporciona una fecha y datos válidos<br><b>When</b> el usuario guarda una actividad<br><b>Then</b> el sistema registra la actividad y programa el recordatorio cuando corresponde<br><br><b>Scenario 2: Cancelación</b><br><b>Given</b> existe una actividad pendiente perteneciente al usuario<br><b>When</b> el usuario solicita cancelarla<br><b>Then</b> el sistema cambia su estado y evita recordatorios posteriores</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-027</td>
    <td>Usuario autenticado</td>
    <td>Must Have</td>
    <td>EP-006</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Recibir una notificación de actividad</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como usuario autenticado, quiero recibir notificaciones de actividades próximas para reducir olvidos de controles y tareas importantes.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Permiso concedido</b><br><b>Given</b> existe una actividad pendiente y el dispositivo permite notificaciones<br><b>When</b> llega el momento configurado<br><b>Then</b> el sistema entrega una notificación relacionada con la actividad<br><br><b>Scenario 2: Permiso denegado</b><br><b>Given</b> el dispositivo no permite notificaciones<br><b>When</b> se aproxima una actividad<br><b>Then</b> el sistema conserva la actividad para consulta y comunica que las notificaciones están deshabilitadas</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-028</td>
    <td>Usuario autenticado</td>
    <td>Should Have</td>
    <td>EP-006</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Atender o reprogramar una actividad</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como usuario autenticado, quiero marcar una actividad como atendida o reprogramarla para mantener actualizado su seguimiento.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Actividad atendida</b><br><b>Given</b> existe una actividad pendiente<br><b>When</b> el usuario registra que fue atendida<br><b>Then</b> el sistema actualiza su estado y conserva la fecha de atención<br><br><b>Scenario 2: Actividad reprogramada</b><br><b>Given</b> existe una actividad pendiente<br><b>When</b> el usuario establece una nueva fecha válida<br><b>Then</b> el sistema actualiza la programación y reemplaza el recordatorio anterior</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-029</td>
    <td>Usuario autenticado</td>
    <td>Must Have</td>
    <td>EP-007</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Consultar información esencial sin conexión</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como usuario autenticado, quiero consultar información esencial previamente sincronizada cuando no tengo conexión para continuar mi trabajo en campo.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Datos locales disponibles</b><br><b>Given</b> el dispositivo conserva datos autorizados y no existe conexión<br><b>When</b> el usuario consulta fincas, animales, actividades o historiales disponibles<br><b>Then</b> el sistema entrega la copia local e informa su última sincronización<br><br><b>Scenario 2: Datos locales inexistentes</b><br><b>Given</b> no existe conexión ni una copia local de la información solicitada<br><b>When</b> el usuario realiza la consulta<br><b>Then</b> el sistema informa que los datos requieren una sincronización inicial</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-030</td>
    <td>Usuario autenticado</td>
    <td>Must Have</td>
    <td>EP-007</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Guardar trabajo pendiente sin conexión</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como usuario autenticado, quiero guardar localmente un registro pendiente cuando no tengo conexión para evitar perder la información ingresada.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Guardado local</b><br><b>Given</b> la conexión no está disponible y los datos cumplen las reglas locales<br><b>When</b> el usuario guarda un animal, incidencia, atención o actividad<br><b>Then</b> el sistema conserva la operación como pendiente de sincronización<br><br><b>Scenario 2: Datos inválidos</b><br><b>Given</b> los datos incumplen una regla que puede validarse localmente<br><b>When</b> el usuario intenta guardar la operación<br><b>Then</b> el sistema no la incorpora a la cola y explica la corrección necesaria</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-031</td>
    <td>Usuario autenticado</td>
    <td>Must Have</td>
    <td>EP-007</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Sincronizar operaciones pendientes</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como usuario autenticado, quiero sincronizar el trabajo pendiente al recuperar la conexión para mantener consistentes el dispositivo y el servidor.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Sincronización exitosa</b><br><b>Given</b> existen operaciones locales pendientes y la conexión vuelve a estar disponible<br><b>When</b> el sistema inicia la sincronización<br><b>Then</b> el servidor procesa cada operación una sola vez y el dispositivo actualiza su estado<br><br><b>Scenario 2: Sincronización parcial</b><br><b>Given</b> una operación es rechazada y otras son válidas<br><b>When</b> el sistema procesa la cola<br><b>Then</b> el sistema conserva como pendiente solo la operación rechazada e informa su causa</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-032</td>
    <td>Usuario autenticado</td>
    <td>Should Have</td>
    <td>EP-007</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Resolver errores o conflictos de sincronización</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como usuario autenticado, quiero conocer y resolver los conflictos de sincronización para evitar sobrescribir información válida.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Conflicto detectado</b><br><b>Given</b> el registro local y el remoto fueron modificados después de la última sincronización<br><b>When</b> el sistema intenta sincronizarlos<br><b>Then</b> el sistema conserva ambas referencias y solicita aplicar una regla de resolución válida<br><br><b>Scenario 2: Reintento seguro</b><br><b>Given</b> una operación falló por una causa temporal<br><b>When</b> el usuario o el sistema reintenta la sincronización<br><b>Then</b> el servidor evita duplicar la operación ya procesada</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-033</td>
    <td>Usuario autorizado</td>
    <td>Must Have</td>
    <td>EP-008</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Identificar un animal mediante código QR</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como usuario autorizado, quiero escanear el código QR de un animal con la cámara para abrir rápidamente su ficha.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Código reconocido</b><br><b>Given</b> el dispositivo concede acceso a la cámara y el código pertenece a un animal autorizado<br><b>When</b> el usuario realiza el escaneo<br><b>Then</b> el sistema identifica al animal y recupera su información disponible<br><br><b>Scenario 2: Código no autorizado</b><br><b>Given</b> el código corresponde a un animal fuera del alcance del usuario<br><b>When</b> el usuario realiza el escaneo<br><b>Then</b> el sistema rechaza la consulta sin revelar datos del animal</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-034</td>
    <td>Usuario autorizado</td>
    <td>Must Have</td>
    <td>EP-008</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Identificar un animal sin utilizar la cámara</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como usuario autorizado, quiero buscar manualmente un animal cuando la cámara o el código QR no estén disponibles para continuar la tarea.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Permiso de cámara denegado</b><br><b>Given</b> el dispositivo no concede acceso a la cámara<br><b>When</b> el usuario intenta iniciar la identificación<br><b>Then</b> el sistema mantiene disponible la búsqueda por código o nombre<br><br><b>Scenario 2: Código ilegible</b><br><b>Given</b> la cámara no reconoce un código válido<br><b>When</b> el usuario concluye el intento de escaneo<br><b>Then</b> el sistema informa el resultado y permite identificar el animal manualmente</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-035</td>
    <td>Ganadero</td>
    <td>Should Have</td>
    <td>EP-009</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Consultar indicadores del hato</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como ganadero, quiero consultar indicadores de mis animales, actividades y eventos sanitarios para priorizar decisiones de manejo.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Indicadores con datos</b><br><b>Given</b> el ganadero tiene información registrada<br><b>When</b> el ganadero consulta sus indicadores<br><b>Then</b> el sistema calcula resultados únicamente con datos de sus fincas y comunica el periodo considerado<br><br><b>Scenario 2: Indicadores sin datos suficientes</b><br><b>Given</b> no existen datos suficientes para calcular un indicador<br><b>When</b> el ganadero realiza la consulta<br><b>Then</b> el sistema informa la falta de información sin presentar resultados engañosos</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-036</td>
    <td>Veterinario</td>
    <td>Should Have</td>
    <td>EP-009</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Consultar indicadores sanitarios de clientes</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como veterinario, quiero consultar indicadores sanitarios de mis clientes autorizados para priorizar pacientes y controles pendientes.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Indicadores autorizados</b><br><b>Given</b> el veterinario tiene clientes vigentes con información sanitaria<br><b>When</b> el veterinario consulta los indicadores<br><b>Then</b> el sistema calcula resultados únicamente con los datos autorizados<br><br><b>Scenario 2: Autorización revocada</b><br><b>Given</b> un cliente deja de autorizar al veterinario<br><b>When</b> el veterinario actualiza la consulta<br><b>Then</b> el sistema excluye los datos de ese cliente</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-037</td>
    <td>Ganadero</td>
    <td>Could Have</td>
    <td>EP-010</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Registrar y consultar movimientos financieros</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como ganadero, quiero registrar ingresos y egresos y consultar mi balance para conocer el resultado económico de mi operación.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Movimiento válido</b><br><b>Given</b> el ganadero proporciona tipo, monto, categoría y fecha válidos<br><b>When</b> el ganadero registra el movimiento<br><b>Then</b> el sistema incorpora el movimiento y actualiza el balance correspondiente<br><br><b>Scenario 2: Consulta por periodo</b><br><b>Given</b> existen movimientos del ganadero en distintos periodos<br><b>When</b> el ganadero consulta un periodo<br><b>Then</b> el sistema calcula ingresos, egresos y balance únicamente con sus movimientos</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-038</td>
    <td>Usuario autenticado</td>
    <td>Must Have</td>
    <td>EP-010</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Consultar planes de suscripción</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como usuario autenticado, quiero comparar los planes vigentes para seleccionar una alternativa acorde con mi operación.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Planes disponibles</b><br><b>Given</b> existen planes activos definidos por AniTec<br><b>When</b> el usuario consulta las alternativas<br><b>Then</b> el sistema devuelve precio, moneda, periodicidad, límites y capacidades de cada plan<br><br><b>Scenario 2: Precio por validar</b><br><b>Given</b> la startup todavía no aprueba un precio comercial<br><b>When</b> el usuario consulta un entorno de validación<br><b>Then</b> el sistema identifica claramente la información como propuesta o prueba</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-039</td>
    <td>Usuario autenticado</td>
    <td>Must Have</td>
    <td>EP-010</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Iniciar un pago mediante un proveedor externo</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como usuario autenticado, quiero iniciar el pago de un plan mediante un proveedor externo para contratar una suscripción sin entregar datos bancarios directamente a AniTec.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Sesión de pago creada</b><br><b>Given</b> el usuario selecciona un plan activo<br><b>When</b> el usuario solicita continuar con el pago<br><b>Then</b> el sistema crea una sesión asociada al usuario y transfiere el proceso al proveedor externo<br><br><b>Scenario 2: Solicitud repetida</b><br><b>Given</b> ya existe una operación en proceso para la misma referencia<br><b>When</b> el usuario repite la solicitud<br><b>Then</b> el sistema evita registrar cobros duplicados</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-040</td>
    <td>Usuario autenticado</td>
    <td>Must Have</td>
    <td>EP-010</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Consultar el resultado del pago y la suscripción</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como usuario autenticado, quiero consultar el resultado de mis pagos y el estado de mi suscripción para conocer las capacidades disponibles en mi cuenta.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Pago confirmado</b><br><b>Given</b> el proveedor externo confirma una operación válida<br><b>When</b> el sistema procesa la confirmación<br><b>Then</b> el sistema activa o actualiza la suscripción una sola vez y conserva la referencia del pago<br><br><b>Scenario 2: Pago cancelado o fallido</b><br><b>Given</b> el proveedor externo no confirma la operación<br><b>When</b> el usuario vuelve a AniTec<br><b>Then</b> el sistema conserva la suscripción anterior e informa el estado sin registrar un pago exitoso</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-041</td>
    <td>Usuario</td>
    <td>Should Have</td>
    <td>EP-011</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Cambiar el idioma de la aplicación</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como usuario, quiero elegir un idioma disponible para comprender la información y realizar mis tareas con términos consistentes.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Cambio de idioma</b><br><b>Given</b> la aplicación dispone de las traducciones requeridas<br><b>When</b> el usuario selecciona otro idioma<br><b>Then</b> el sistema actualiza los textos y formatos localizables<br><br><b>Scenario 2: Preferencia conservada</b><br><b>Given</b> el usuario eligió un idioma<br><b>When</b> el usuario vuelve a abrir la aplicación<br><b>Then</b> el sistema aplica la preferencia almacenada</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-042</td>
    <td>Usuario</td>
    <td>Must Have</td>
    <td>EP-011</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Utilizar la aplicación con necesidades de accesibilidad</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como usuario con necesidades de accesibilidad, quiero percibir y comprender el contenido para completar las tareas principales de manera autónoma.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Escalado de texto</b><br><b>Given</b> el dispositivo utiliza un tamaño de fuente mayor<br><b>When</b> el usuario accede a una tarea principal<br><b>Then</b> el contenido mantiene su legibilidad y no oculta información necesaria<br><br><b>Scenario 2: Tecnología de asistencia</b><br><b>Given</b> el usuario utiliza un lector de pantalla<br><b>When</b> el usuario recorre la información y las acciones principales<br><b>Then</b> el sistema comunica nombres, estados y propósitos comprensibles</td>
  </tr>
</table>

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Story ID</th>
    <th style="text-align: center;">User</th>
    <th style="text-align: center;">Priority</th>
    <th style="text-align: center;">Epic</th>
  </tr>
  <tr>
    <td>US-043</td>
    <td>Usuario</td>
    <td>Must Have</td>
    <td>EP-011</td>
  </tr>
  <tr>
    <th style="text-align: center;">Title</th>
    <td colspan="3">Comprender errores y estados de conectividad</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como usuario, quiero recibir información clara ante errores o cambios de conectividad para decidir cómo continuar sin perder mi trabajo.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Error recuperable</b><br><b>Given</b> una operación falla por una causa temporal<br><b>When</b> el sistema recibe el error<br><b>Then</b> el sistema conserva el trabajo posible y comunica una acción de recuperación<br><br><b>Scenario 2: Cambio de conectividad</b><br><b>Given</b> el dispositivo pierde o recupera la conexión<br><b>When</b> el sistema detecta el cambio<br><b>Then</b> el sistema actualiza el estado de trabajo local y sincronización sin afirmar que una operación terminó antes de confirmarla</td>
  </tr>
</table>

### Technical Stories

<table>
  <tr>
    <th>Story ID</th>
    <th>User</th>
    <th>Priority</th>
    <th>Epic</th>
  </tr>
  <tr>
    <td>TS-001</td>
    <td>Developer</td>
    <td>Must Have</td>
    <td>EP-012</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3">Configurar la aplicación Android nativa</td>
  </tr>
  <tr>
    <th colspan="4">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como Developer, quiero configurar el proyecto Android con Kotlin y Jetpack Compose para implementar una aplicación nativa mantenible y ejecutable en dispositivos físicos.</td>
  </tr>
  <tr>
    <th colspan="4">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Proyecto reproducible</b><br><b>Given</b> el repositorio contiene la configuración documentada<br><b>When</b> el Developer compila el proyecto en un ambiente limpio<br><b>Then</b> el sistema genera una aplicación instalable sin depender de archivos locales no versionados<br><br><b>Scenario 2: Dispositivo físico</b><br><b>Given</b> existe una compilación de desarrollo válida<br><b>When</b> el Developer instala y ejecuta la aplicación en un dispositivo Android compatible<br><b>Then</b> las funciones base inician sin errores bloqueantes</td>
  </tr>
</table>

<table>
  <tr>
    <th>Story ID</th>
    <th>User</th>
    <th>Priority</th>
    <th>Epic</th>
  </tr>
  <tr>
    <td>TS-002</td>
    <td>Developer</td>
    <td>Must Have</td>
    <td>EP-012</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3">Configurar la aplicación multiplataforma con Flutter</td>
  </tr>
  <tr>
    <th colspan="4">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como Developer, quiero configurar un proyecto Flutter con Dart para entregar una experiencia multiplataforma coherente con la aplicación Android nativa.</td>
  </tr>
  <tr>
    <th colspan="4">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Proyecto reproducible</b><br><b>Given</b> el repositorio contiene las versiones y dependencias documentadas<br><b>When</b> el Developer ejecuta la compilación desde un ambiente limpio<br><b>Then</b> el sistema genera una aplicación para las plataformas objetivo definidas<br><br><b>Scenario 2: Consistencia funcional</b><br><b>Given</b> existe un flujo core implementado en Android nativo<br><b>When</b> el Developer implementa el mismo flujo en Flutter<br><b>Then</b> ambas aplicaciones aplican las mismas reglas de negocio y contrato de servicio</td>
  </tr>
</table>

<table>
  <tr>
    <th>Story ID</th>
    <th>User</th>
    <th>Priority</th>
    <th>Epic</th>
  </tr>
  <tr>
    <td>TS-003</td>
    <td>Developer</td>
    <td>Must Have</td>
    <td>EP-012</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3">Definir la arquitectura móvil por capas y bounded contexts</td>
  </tr>
  <tr>
    <th colspan="4">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como Developer, quiero definir una arquitectura móvil alineada con Domain-Driven Design para separar presentación, aplicación, dominio e infraestructura.</td>
  </tr>
  <tr>
    <th colspan="4">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Límites definidos</b><br><b>Given</b> se conocen los bounded contexts y dependencias permitidas<br><b>When</b> el equipo documenta la arquitectura móvil<br><b>Then</b> cada módulo identifica sus responsabilidades y evita dependencias contrarias a la dirección acordada<br><br><b>Scenario 2: Regla de dominio aislada</b><br><b>Given</b> existe una regla que no depende del sistema operativo<br><b>When</b> el Developer implementa y prueba la regla<br><b>Then</b> la regla se ejecuta sin requerir componentes de interfaz o infraestructura</td>
  </tr>
</table>

<table>
  <tr>
    <th>Story ID</th>
    <th>User</th>
    <th>Priority</th>
    <th>Epic</th>
  </tr>
  <tr>
    <td>TS-004</td>
    <td>Developer</td>
    <td>Must Have</td>
    <td>EP-012</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3">Integrar las aplicaciones con la API REST interna</td>
  </tr>
  <tr>
    <th colspan="4">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como Developer, quiero implementar clientes HTTP autenticados en Android y Flutter para consumir de forma consistente la API REST de AniTec.</td>
  </tr>
  <tr>
    <th colspan="4">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Respuesta exitosa</b><br><b>Given</b> la API devuelve una respuesta válida<br><b>When</b> la aplicación solicita un recurso<br><b>Then</b> el cliente transforma la respuesta al modelo correspondiente sin exponer el formato de transporte al dominio<br><br><b>Scenario 2: Respuesta de error</b><br><b>Given</b> la API devuelve un código de error o no responde<br><b>When</b> la aplicación procesa la solicitud<br><b>Then</b> el cliente clasifica el resultado para que la aplicación pueda informar o reintentar de forma segura</td>
  </tr>
</table>

<table>
  <tr>
    <th>Story ID</th>
    <th>User</th>
    <th>Priority</th>
    <th>Epic</th>
  </tr>
  <tr>
    <td>TS-005</td>
    <td>Developer</td>
    <td>Must Have</td>
    <td>EP-007</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3">Implementar persistencia local segura en Android</td>
  </tr>
  <tr>
    <th colspan="4">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como Developer, quiero implementar persistencia local con Room para almacenar información esencial y operaciones pendientes en la aplicación Android.</td>
  </tr>
  <tr>
    <th colspan="4">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Persistencia</b><br><b>Given</b> la aplicación recibe información autorizada<br><b>When</b> el repositorio local la almacena<br><b>Then</b> los datos permanecen disponibles después de reiniciar la aplicación<br><br><b>Scenario 2: Protección y limpieza</b><br><b>Given</b> el usuario finaliza la sesión o cambia de cuenta<br><b>When</b> la aplicación procesa el cambio<br><b>Then</b> los datos protegidos que no deben compartirse se eliminan o aíslan según la política definida</td>
  </tr>
</table>

<table>
  <tr>
    <th>Story ID</th>
    <th>User</th>
    <th>Priority</th>
    <th>Epic</th>
  </tr>
  <tr>
    <td>TS-006</td>
    <td>Developer</td>
    <td>Must Have</td>
    <td>EP-007</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3">Implementar persistencia local en Flutter</td>
  </tr>
  <tr>
    <th colspan="4">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como Developer, quiero implementar una base local compatible con Flutter para ofrecer el mismo comportamiento offline en la aplicación multiplataforma.</td>
  </tr>
  <tr>
    <th colspan="4">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Esquema equivalente</b><br><b>Given</b> Android y Flutter comparten las reglas de datos offline<br><b>When</b> el Developer configura el almacenamiento local de Flutter<br><b>Then</b> los registros esenciales y operaciones pendientes conservan los campos necesarios para sincronizarse<br><br><b>Scenario 2: Migración local</b><br><b>Given</b> existe una versión anterior del esquema en el dispositivo<br><b>When</b> la aplicación se actualiza<br><b>Then</b> la migración conserva los datos compatibles sin bloquear el inicio</td>
  </tr>
</table>

<table>
  <tr>
    <th>Story ID</th>
    <th>User</th>
    <th>Priority</th>
    <th>Epic</th>
  </tr>
  <tr>
    <td>TS-007</td>
    <td>Developer</td>
    <td>Must Have</td>
    <td>EP-007</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3">Implementar sincronización idempotente</td>
  </tr>
  <tr>
    <th colspan="4">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como Developer, quiero implementar una cola de sincronización idempotente para enviar operaciones pendientes sin duplicarlas ni perderlas.</td>
  </tr>
  <tr>
    <th colspan="4">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Operación identificada</b><br><b>Given</b> una operación local pendiente posee un identificador único<br><b>When</b> el cliente la envía más de una vez por un fallo temporal<br><b>Then</b> el servidor produce un único efecto y devuelve el resultado correspondiente<br><br><b>Scenario 2: Conflicto</b><br><b>Given</b> el servidor detecta una versión incompatible<br><b>When</b> el cliente intenta sincronizar<br><b>Then</b> el sistema conserva el conflicto y aplica la estrategia documentada antes de reemplazar información</td>
  </tr>
</table>

<table>
  <tr>
    <th>Story ID</th>
    <th>User</th>
    <th>Priority</th>
    <th>Epic</th>
  </tr>
  <tr>
    <td>TS-008</td>
    <td>Developer</td>
    <td>Must Have</td>
    <td>EP-002</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3">Proteger credenciales y datos de sesión</td>
  </tr>
  <tr>
    <th colspan="4">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como Developer, quiero almacenar tokens mediante mecanismos seguros de cada plataforma para reducir la exposición de credenciales.</td>
  </tr>
  <tr>
    <th colspan="4">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Almacenamiento seguro</b><br><b>Given</b> el servidor entrega un token válido<br><b>When</b> la aplicación conserva la sesión<br><b>Then</b> el token se almacena mediante el mecanismo seguro definido para la plataforma<br><br><b>Scenario 2: Token vencido</b><br><b>Given</b> el servidor rechaza un token por expiración<br><b>When</b> el cliente recibe la respuesta<br><b>Then</b> la aplicación invalida la sesión o ejecuta la renovación autorizada sin reutilizar credenciales inválidas</td>
  </tr>
</table>

<table>
  <tr>
    <th>Story ID</th>
    <th>User</th>
    <th>Priority</th>
    <th>Epic</th>
  </tr>
  <tr>
    <td>TS-009</td>
    <td>Developer</td>
    <td>Must Have</td>
    <td>EP-006</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3">Implementar notificaciones móviles</td>
  </tr>
  <tr>
    <th colspan="4">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como Developer, quiero integrar notificaciones locales o push para entregar recordatorios sanitarios respetando los permisos del sistema operativo.</td>
  </tr>
  <tr>
    <th colspan="4">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Programación</b><br><b>Given</b> existe una actividad válida y el permiso correspondiente<br><b>When</b> la aplicación programa el recordatorio<br><b>Then</b> el sistema operativo recibe una notificación con una referencia válida a la actividad<br><br><b>Scenario 2: Permiso ausente</b><br><b>Given</b> el permiso no fue concedido<br><b>When</b> la aplicación procesa una actividad con recordatorio<br><b>Then</b> la actividad permanece registrada y la aplicación informa que no puede entregar la notificación</td>
  </tr>
</table>

<table>
  <tr>
    <th>Story ID</th>
    <th>User</th>
    <th>Priority</th>
    <th>Epic</th>
  </tr>
  <tr>
    <td>TS-010</td>
    <td>Developer</td>
    <td>Must Have</td>
    <td>EP-008</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3">Integrar identificación QR mediante Google ML Kit</td>
  </tr>
  <tr>
    <th colspan="4">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como Developer, quiero integrar Google ML Kit Barcode Scanning y una alternativa compatible en Flutter para identificar animales mediante códigos QR usando la cámara.</td>
  </tr>
  <tr>
    <th colspan="4">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Código compatible</b><br><b>Given</b> la cámara recibe un código QR válido<br><b>When</b> la biblioteca procesa la imagen<br><b>Then</b> la aplicación obtiene el identificador sin almacenar imágenes innecesarias<br><br><b>Scenario 2: Lectura fallida</b><br><b>Given</b> la biblioteca no reconoce un código válido<br><b>When</b> finaliza el intento configurado<br><b>Then</b> la aplicación devuelve un resultado controlado y conserva la alternativa manual</td>
  </tr>
</table>

<table>
  <tr>
    <th>Story ID</th>
    <th>User</th>
    <th>Priority</th>
    <th>Epic</th>
  </tr>
  <tr>
    <td>TS-011</td>
    <td>Developer</td>
    <td>Must Have</td>
    <td>EP-010</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3">Integrar el checkout externo de Stripe</td>
  </tr>
  <tr>
    <th colspan="4">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como Developer, quiero integrar el checkout de Stripe mediante el backend y enlaces seguros para procesar pagos de prueba desde las aplicaciones móviles.</td>
  </tr>
  <tr>
    <th colspan="4">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Creación de checkout</b><br><b>Given</b> el cliente solicita pagar un plan activo<br><b>When</b> el backend valida la solicitud<br><b>Then</b> el servicio crea una sesión de Stripe y devuelve una URL permitida<br><br><b>Scenario 2: Confirmación idempotente</b><br><b>Given</b> Stripe informa el resultado mediante el mecanismo configurado<br><b>When</b> el backend procesa el evento<br><b>Then</b> el pago y la suscripción se actualizan una sola vez</td>
  </tr>
</table>

<table>
  <tr>
    <th>Story ID</th>
    <th>User</th>
    <th>Priority</th>
    <th>Epic</th>
  </tr>
  <tr>
    <td>TS-012</td>
    <td>Developer</td>
    <td>Must Have</td>
    <td>EP-011</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3">Aplicar internacionalización y accesibilidad móvil</td>
  </tr>
  <tr>
    <th colspan="4">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como Developer, quiero centralizar recursos traducibles y aplicar prácticas de accesibilidad para mantener una experiencia coherente en Android y Flutter.</td>
  </tr>
  <tr>
    <th colspan="4">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Recursos traducibles</b><br><b>Given</b> existen idiomas soportados<br><b>When</b> el Developer agrega o modifica contenido<br><b>Then</b> los textos visibles provienen de recursos localizables y no quedan cadenas funcionales sin traducir<br><br><b>Scenario 2: Verificación accesible</b><br><b>Given</b> existen flujos core implementados<br><b>When</b> el equipo ejecuta verificaciones con escalado de texto y lector de pantalla<br><b>Then</b> los problemas encontrados se documentan y los bloqueantes se corrigen</td>
  </tr>
</table>

<table>
  <tr>
    <th>Story ID</th>
    <th>User</th>
    <th>Priority</th>
    <th>Epic</th>
  </tr>
  <tr>
    <td>TS-013</td>
    <td>Developer</td>
    <td>Must Have</td>
    <td>EP-012</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3">Adaptar y documentar los servicios backend para móviles</td>
  </tr>
  <tr>
    <th colspan="4">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como Developer, quiero adaptar los endpoints existentes y documentarlos con OpenAPI para soportar los flujos móviles y las reglas de autorización.</td>
  </tr>
  <tr>
    <th colspan="4">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Contrato documentado</b><br><b>Given</b> un endpoint forma parte del alcance móvil<br><b>When</b> el Developer publica la documentación OpenAPI<br><b>Then</b> el contrato describe autenticación, parámetros, respuestas exitosas y errores<br><br><b>Scenario 2: Autorización</b><br><b>Given</b> una solicitud autenticada intenta acceder a un recurso ajeno<br><b>When</b> la API evalúa el rol y la relación<br><b>Then</b> la API rechaza la operación mediante el código HTTP correspondiente</td>
  </tr>
</table>

<table>
  <tr>
    <th>Story ID</th>
    <th>User</th>
    <th>Priority</th>
    <th>Epic</th>
  </tr>
  <tr>
    <td>TS-014</td>
    <td>Developer</td>
    <td>Should Have</td>
    <td>EP-012</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3">Automatizar pruebas de los flujos móviles críticos</td>
  </tr>
  <tr>
    <th colspan="4">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como Developer, quiero automatizar pruebas unitarias y de integración para detectar regresiones en dominio, persistencia, sincronización y consumo de servicios.</td>
  </tr>
  <tr>
    <th colspan="4">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Pruebas de dominio</b><br><b>Given</b> existen reglas críticas de autorización, estado o sincronización<br><b>When</b> el equipo ejecuta la suite<br><b>Then</b> las pruebas verifican resultados exitosos y alternativos de manera determinista<br><br><b>Scenario 2: Integración controlada</b><br><b>Given</b> existen repositorios locales y clientes de servicio<br><b>When</b> el equipo ejecuta pruebas con dobles o ambientes controlados<br><b>Then</b> la suite comprueba persistencia, mapeo y tratamiento de errores</td>
  </tr>
</table>

<table>
  <tr>
    <th>Story ID</th>
    <th>User</th>
    <th>Priority</th>
    <th>Epic</th>
  </tr>
  <tr>
    <td>TS-015</td>
    <td>Developer</td>
    <td>Must Have</td>
    <td>EP-012</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3">Configurar compilación y distribución de versiones móviles</td>
  </tr>
  <tr>
    <th colspan="4">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como Developer, quiero automatizar compilaciones firmadas y distribuir versiones mediante Firebase App Distribution para probarlas en dispositivos físicos.</td>
  </tr>
  <tr>
    <th colspan="4">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Compilación versionada</b><br><b>Given</b> el repositorio alcanza un hito de entrega<br><b>When</b> el pipeline genera la versión<br><b>Then</b> el artefacto incluye un número de versión trazable y una configuración válida<br><br><b>Scenario 2: Distribución</b><br><b>Given</b> existe un artefacto aprobado para pruebas<br><b>When</b> el equipo publica la versión en Firebase App Distribution<br><b>Then</b> los evaluadores autorizados pueden instalarla y se registra la versión distribuida</td>
  </tr>
</table>

### Matriz de coherencia con el alcance móvil y los requisitos del curso

La siguiente matriz hace trazable cada condición tecnológica obligatoria con una decisión verificable y con los elementos del backlog que permiten implementarla. Ambas aplicaciones consumen el mismo dominio y la misma API REST, pero conservan implementaciones y pruebas propias para demostrar el desarrollo Android nativo y el desarrollo multiplataforma.

<table>
  <thead>
    <tr>
      <th>Aspecto requerido</th>
      <th>Decisión para AniTec</th>
      <th>Evidencia esperada</th>
      <th>Historias relacionadas</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Aplicación Android nativa</td><td>Kotlin y Jetpack Compose, con arquitectura por capas y funcionalidades core de ganaderos y veterinarios.</td><td>Proyecto Android compilable, ejecución y pruebas en un dispositivo Android físico.</td><td>TS-001, TS-003, TS-004 y US-004 a US-043.</td></tr>
    <tr><td>Aplicación multiplataforma</td><td>Flutter y Dart, con el mismo alcance funcional y contratos de servicio que la aplicación Android.</td><td>Proyecto Flutter compilable y comparación de los flujos core en las plataformas objetivo definidas por el equipo.</td><td>TS-002, TS-003, TS-004, TS-006 y US-004 a US-043.</td></tr>
    <tr><td>Almacenamiento local</td><td>Room en Android y una base de datos local compatible en Flutter para caché, operaciones pendientes y estado de sincronización.</td><td>Consulta y registro de información esencial sin conexión, seguidos por una sincronización idempotente.</td><td>US-029 a US-032 y TS-005 a TS-007.</td></tr>
    <tr><td>Recurso interno del dispositivo</td><td>Cámara del teléfono para leer el código QR que identifica al animal, con alternativa de búsqueda manual.</td><td>Prueba con permiso concedido, permiso denegado, código válido, código inválido y condiciones reales de iluminación.</td><td>US-033, US-034, TS-010 y SP-001.</td></tr>
    <tr><td>Servicio REST interno</td><td>API REST propia de AniTec, documentada con OpenAPI y protegida mediante autenticación y autorización por rol y relación.</td><td>Backend público al 70 % en Sprint 1 y al 100 % desde Sprint 2, con documentación accesible.</td><td>US-004 a US-040, TS-004, TS-008 y TS-013.</td></tr>
    <tr><td>Servicio externo</td><td>Stripe Checkout para iniciar pagos y confirmar el estado de la suscripción sin almacenar datos de tarjeta en AniTec.</td><td>Flujos de pago aprobado, rechazado o cancelado y validación del resultado desde el backend.</td><td>US-038 a US-040, SP-002 y TS-011.</td></tr>
    <tr><td>Feature de aprendizaje autónomo</td><td>Investigación, prototipo e integración de Google ML Kit Barcode Scanning para reconocer códigos QR en el dispositivo.</td><td>Informe del Spike, fuentes consultadas, alternativas, riesgos, prueba física y conclusión de viabilidad.</td><td>US-033, TS-010 y SP-001.</td></tr>
    <tr><td>Notificaciones móviles</td><td>Recordatorios locales o remotos asociados con actividades ganaderas y sanitarias.</td><td>Recepción, atención y reprogramación de recordatorios con permisos habilitados o denegados.</td><td>US-025 a US-028 y TS-009.</td></tr>
    <tr><td>Despliegue y validación física</td><td>Versiones firmadas y distribuidas mediante Firebase App Distribution o un servicio equivalente.</td><td>Instalación trazable en dispositivos físicos y registro de versión para la Release Review.</td><td>TS-014 y TS-015.</td></tr>
  </tbody>
</table>

### Spike Stories

<table>
  <tr>
    <th>Story ID</th>
    <th>User</th>
    <th>Priority</th>
    <th>Epic</th>
  </tr>
  <tr>
    <td>SP-001</td>
    <td>Developer</td>
    <td>Must Have</td>
    <td>EP-008</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3">Investigar identificación de animales con Google ML Kit</td>
  </tr>
  <tr>
    <th colspan="4">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como equipo de desarrollo móvil, queremos investigar y prototipar Google ML Kit Barcode Scanning en Android y una alternativa compatible en Flutter para comprender su viabilidad, riesgos y esfuerzo antes de implementar la identificación de animales mediante cámara.</td>
  </tr>
  <tr>
    <th colspan="4">Research Objective</th>
  </tr>
  <tr>
    <td colspan="4">Determinar si la lectura de códigos QR puede funcionar de manera confiable en Android y Flutter, incluso sin conexión, respetando permisos, privacidad y restricciones de dispositivos de gama media utilizados en el contexto peruano.</td>
  </tr>
  <tr>
    <th>Timebox</th>
    <td colspan="3">Entre 8 y 16 horas dentro del Sprint 1.</td>
  </tr>
  <tr>
    <th colspan="4">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Investigación documentada</b><br><b>Given</b> el equipo necesita identificar animales mediante códigos QR en Android y Flutter<br><b>When</b> el Developer revisa documentación oficial y compara compatibilidad, permisos, operación offline, licencias y privacidad<br><b>Then</b> el informe del spike registra fuentes, alternativas, riesgos y criterios de selección<br><br><b>Scenario 2: Prototipo en dispositivo físico</b><br><b>Given</b> existen códigos válidos e inválidos y al menos un dispositivo Android físico de gama media<br><b>When</b> el Developer ejecuta el prototipo con distintas condiciones de iluminación y conectividad<br><b>Then</b> el prototipo registra resultados de lectura, fallos, tiempos observados y comportamiento sin conexión<br><br><b>Scenario 3: Comparación entre plataformas</b><br><b>Given</b> Android utiliza Kotlin y la estrategia multiplataforma utiliza Flutter<br><b>When</b> el Developer evalúa la integración prevista para ambas aplicaciones<br><b>Then</b> el informe identifica dependencias, diferencias de implementación y una alternativa manual para los casos no compatibles<br><br><b>Scenario 4: Conclusión técnica</b><br><b>Given</b> la investigación y las pruebas han terminado<br><b>When</b> el equipo revisa los hallazgos<br><b>Then</b> el informe concluye si la solución es viable, recomienda un enfoque y estima el esfuerzo de implementación</td>
  </tr>
  <tr>
    <th colspan="4">Definition of Done</th>
  </tr>
  <tr>
    <td colspan="4">El informe del spike contiene fuentes, resultados, riesgos, comparación entre plataformas y conclusión técnica; el código del prototipo está registrado en una rama o repositorio identificable; y los hallazgos han sido revisados por el equipo para refinar TS-010 y las historias relacionadas.</td>
  </tr>
</table>

<table>
  <tr>
    <th>Story ID</th>
    <th>User</th>
    <th>Priority</th>
    <th>Epic</th>
  </tr>
  <tr>
    <td>SP-002</td>
    <td>Developer</td>
    <td>Must Have</td>
    <td>EP-010</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3">Investigar la integración de Stripe para suscripciones móviles</td>
  </tr>
  <tr>
    <th colspan="4">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como equipo de desarrollo móvil y backend, queremos investigar y prototipar la integración de Stripe con Android, Flutter y la API ASP.NET Core de AniTec para comprender el flujo recomendado, los riesgos de seguridad y el esfuerzo requerido antes de implementar pagos y suscripciones.</td>
  </tr>
  <tr>
    <th colspan="4">Research Objective</th>
  </tr>
  <tr>
    <td colspan="4">Determinar si Stripe Checkout en modo de prueba permite iniciar pagos desde ambas aplicaciones móviles, confirmar el resultado en el backend mediante webhooks e impedir cobros o activaciones duplicadas sin almacenar datos de tarjeta en AniTec.</td>
  </tr>
  <tr>
    <th>Timebox</th>
    <td colspan="3">Entre 8 y 16 horas durante el Sprint 2, antes de iniciar TS-011.</td>
  </tr>
  <tr>
    <th colspan="4">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><b>Scenario 1: Evaluación del flujo y dependencias</b><br><b>Given</b> AniTec necesita procesar suscripciones desde Android y Flutter<br><b>When</b> el Developer revisa la documentación oficial y compara Stripe Checkout con un flujo personalizado<br><b>Then</b> el informe identifica el enfoque recomendado, dependencias, configuración, costos de referencia y restricciones para las aplicaciones y el backend<br><br><b>Scenario 2: Seguridad y cumplimiento</b><br><b>Given</b> AniTec no debe almacenar datos de tarjeta<br><b>When</b> el Developer analiza redirecciones, claves, firmas de webhooks, idempotencia y responsabilidades PCI<br><b>Then</b> el informe documenta riesgos, medidas de mitigación y datos que pueden conservarse de forma segura<br><br><b>Scenario 3: Prototipo de pago</b><br><b>Given</b> existe una cuenta de prueba de Stripe y un plan de prueba<br><b>When</b> una aplicación móvil solicita una sesión al backend y completa o cancela el checkout<br><b>Then</b> el prototipo registra el resultado, valida la firma del webhook y evita procesar dos veces el mismo evento<br><br><b>Scenario 4: Conclusión y estimación</b><br><b>Given</b> la investigación y el prototipo han terminado<br><b>When</b> el equipo revisa los resultados<br><b>Then</b> el informe presenta ventajas, limitaciones, bloqueadores, enfoque recomendado y una estimación para implementar US-039, US-040 y TS-011</td>
  </tr>
  <tr>
    <th colspan="4">Definition of Done</th>
  </tr>
  <tr>
    <td colspan="4">El prototipo funciona únicamente en modo de prueba y su código está registrado; el informe documenta arquitectura, seguridad, dependencias, costos de referencia, resultados y recomendación; y los hallazgos han sido revisados por el equipo para refinar las historias de pago sin afirmar que Stripe ya está implementado en producción.</td>
  </tr>
</table>

## 2.4.2. Impact Mapping

El Impact Mapping conecta objetivos SMART del piloto con los User Personas, los cambios de comportamiento esperados, los entregables y las historias que los habilitan. Los objetivos se medirán con analítica de uso, registros de sincronización y pruebas moderadas antes de concluir el Sprint 3.

<table>
  <thead>
    <tr>
      <th>Business Goal</th>
      <th>Actor / User Persona</th>
      <th>Impact</th>
      <th>Deliverable</th>
      <th>User Stories</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2"><b>BG-01:</b> Lograr que al menos 8 de 10 ganaderos participantes registren tres animales y dos eventos desde una aplicación móvil durante un piloto de cuatro semanas, antes del cierre del Sprint 3.</td>
      <td>Jorge Luis Rivas — Ganadero</td>
      <td>Registra la información en el lugar donde ocurre y deja de postergarla por falta de una computadora.</td>
      <td>Gestión móvil de fincas y animales.</td>
      <td>Como ganadero, deseo registrar y consultar mis animales desde el teléfono para mantener su trazabilidad. US-008 a US-013.</td>
    </tr>
    <tr>
      <td>Jorge Luis Rivas — Ganadero</td>
      <td>Continúa trabajando durante interrupciones de red y confirma después la sincronización.</td>
      <td>Persistencia local, cola de operaciones y estados de sincronización.</td>
      <td>Como ganadero, deseo guardar y sincronizar registros sin repetirlos para trabajar con conectividad intermitente. US-029 a US-032.</td>
    </tr>
    <tr>
      <td rowspan="2"><b>BG-02:</b> Conseguir que al menos el 70 % de los recordatorios sanitarios creados durante el piloto se marquen como atendidos o reprogramados dentro de su plazo, antes del cierre del Sprint 3.</td>
      <td>Jorge Luis Rivas — Ganadero</td>
      <td>Registra incidencias y consulta actividades pendientes con mayor frecuencia.</td>
      <td>Historial sanitario, calendario y notificaciones móviles.</td>
      <td>Como ganadero, deseo registrar incidencias y recibir recordatorios para cumplir actividades sanitarias. US-014, US-015 y US-025 a US-028.</td>
    </tr>
    <tr>
      <td>Valeria Mendoza — Veterinaria</td>
      <td>Programa el control posterior como parte de la atención.</td>
      <td>Registro clínico trazable y actividad de seguimiento.</td>
      <td>Como veterinaria, deseo registrar tratamientos y próximos controles para mantener continuidad clínica. US-016 a US-019.</td>
    </tr>
    <tr>
      <td rowspan="2"><b>BG-03:</b> Lograr que al menos 4 de 5 veterinarios participantes consulten antecedentes y registren una atención autorizada en menos de cinco minutos y sin ayuda, durante la validación previa al cierre del Sprint 3.</td>
      <td>Valeria Mendoza — Veterinaria</td>
      <td>Consulta únicamente clientes y pacientes autorizados antes de atenderlos.</td>
      <td>Gestión de relaciones, clientes, pacientes e historiales.</td>
      <td>Como veterinaria, deseo consultar clientes y pacientes autorizados para preparar y documentar la atención. US-023 y US-024.</td>
    </tr>
    <tr>
      <td>Jorge Luis Rivas — Ganadero</td>
      <td>Controla quién puede consultar y registrar información sanitaria.</td>
      <td>Solicitudes, aceptación y revocación de acceso.</td>
      <td>Como ganadero, deseo conceder o revocar acceso veterinario para proteger los datos de mis animales. US-020 a US-022.</td>
    </tr>
    <tr>
      <td><b>BG-04:</b> Conseguir que al menos el 80 % de los participantes identifique correctamente un animal mediante QR o la alternativa manual en menos de 30 segundos, durante las pruebas del Sprint 2.</td>
      <td>Jorge Luis Rivas y Valeria Mendoza</td>
      <td>Localizan la ficha correcta con menos tiempo y mantienen una alternativa cuando la cámara falla.</td>
      <td>Escaneo QR con Google ML Kit y búsqueda manual.</td>
      <td>Como usuario autorizado, deseo identificar un animal mediante cámara o búsqueda para acceder rápidamente a su ficha. US-033 y US-034.</td>
    </tr>
  </tbody>
</table>

## 2.4.3. Product Backlog

El Product Backlog contiene todas las User Stories, Technical Stories y Spike Stories definidas en esta sección. El orden comienza con la landing page, como exige el statement, y continúa con incrementos verticales de valor móvil. Las historias técnicas se ubican cerca del resultado que habilitan y todas las estimaciones utilizan la escala 1, 2, 3, 5 u 8.

La distribución considera los hitos del curso:

- **Sprint 1 — TB1, semana 7:** landing page desplegada, backend al 70 %, bases de Android y Flutter y pantallas core de acceso y gestión de animales.
- **Sprint 2 — AV2, semana 12:** backend al 100 % y principales funciones core de sanidad, colaboración veterinaria, notificaciones, trabajo offline e identificación mediante cámara.
- **Sprint 3 — TB2, semana 15:** cierre de trazabilidad sanitaria y sincronización, reportes, pagos, accesibilidad, pruebas, distribución y aplicación completa según el backlog.

<table>
  <thead>
    <tr>
      <th># Orden</th>
      <th>User Story Id</th>
      <th>Título</th>
      <th>Story Points (1 / 2 / 3 / 5 / 8)</th>
      <th>Sprint</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>1</td><td>US-001</td><td>Comprender la propuesta de valor de AniTec</td><td>3</td><td>Sprint 1</td></tr>
    <tr><td>2</td><td>US-002</td><td>Conocer las soluciones para cada segmento</td><td>3</td><td>Sprint 1</td></tr>
    <tr><td>3</td><td>US-003</td><td>Acceder a una landing page adaptable e internacionalizada</td><td>5</td><td>Sprint 1</td></tr>
    <tr><td>4</td><td>TS-001</td><td>Configurar la aplicación Android nativa</td><td>5</td><td>Sprint 1</td></tr>
    <tr><td>5</td><td>TS-002</td><td>Configurar la aplicación multiplataforma con Flutter</td><td>5</td><td>Sprint 1</td></tr>
    <tr><td>6</td><td>TS-003</td><td>Definir la arquitectura móvil por capas y bounded contexts</td><td>5</td><td>Sprint 1</td></tr>
    <tr><td>7</td><td>TS-013</td><td>Adaptar y documentar los servicios backend para móviles</td><td>8</td><td>Sprint 1</td></tr>
    <tr><td>8</td><td>US-004</td><td>Registrar una cuenta según el rol</td><td>5</td><td>Sprint 1</td></tr>
    <tr><td>9</td><td>US-005</td><td>Iniciar sesión</td><td>3</td><td>Sprint 1</td></tr>
    <tr><td>10</td><td>US-006</td><td>Mantener y finalizar la sesión móvil</td><td>3</td><td>Sprint 1</td></tr>
    <tr><td>11</td><td>US-007</td><td>Acceder únicamente a información autorizada</td><td>5</td><td>Sprint 1</td></tr>
    <tr><td>12</td><td>TS-008</td><td>Proteger credenciales y datos de sesión</td><td>5</td><td>Sprint 1</td></tr>
    <tr><td>13</td><td>US-008</td><td>Consultar las fincas registradas</td><td>3</td><td>Sprint 1</td></tr>
    <tr><td>14</td><td>US-009</td><td>Registrar y actualizar una finca</td><td>5</td><td>Sprint 1</td></tr>
    <tr><td>15</td><td>US-010</td><td>Consultar y buscar animales</td><td>5</td><td>Sprint 1</td></tr>
    <tr><td>16</td><td>US-011</td><td>Registrar un animal</td><td>5</td><td>Sprint 1</td></tr>
    <tr><td>17</td><td>US-012</td><td>Actualizar o archivar un animal</td><td>5</td><td>Sprint 1</td></tr>
    <tr><td>18</td><td>US-013</td><td>Consultar el detalle de un animal</td><td>3</td><td>Sprint 1</td></tr>
    <tr><td>19</td><td>TS-004</td><td>Integrar las aplicaciones con la API REST interna</td><td>5</td><td>Sprint 1</td></tr>
    <tr><td>20</td><td>TS-005</td><td>Implementar persistencia local segura en Android</td><td>5</td><td>Sprint 1</td></tr>
    <tr><td>21</td><td>TS-006</td><td>Implementar persistencia local en Flutter</td><td>5</td><td>Sprint 2</td></tr>
    <tr><td>22</td><td>SP-001</td><td>Investigar identificación de animales con Google ML Kit</td><td>5</td><td>Sprint 1</td></tr>
    <tr><td>23</td><td>US-014</td><td>Consultar eventos sanitarios</td><td>3</td><td>Sprint 2</td></tr>
    <tr><td>24</td><td>US-015</td><td>Registrar una incidencia sanitaria</td><td>5</td><td>Sprint 2</td></tr>
    <tr><td>25</td><td>US-016</td><td>Registrar diagnóstico y tratamiento</td><td>5</td><td>Sprint 2</td></tr>
    <tr><td>26</td><td>US-017</td><td>Consultar el historial sanitario de un animal</td><td>5</td><td>Sprint 2</td></tr>
    <tr><td>27</td><td>US-018</td><td>Corregir un registro sanitario con trazabilidad</td><td>5</td><td>Sprint 3</td></tr>
    <tr><td>28</td><td>US-019</td><td>Programar un control sanitario posterior</td><td>3</td><td>Sprint 3</td></tr>
    <tr><td>29</td><td>US-020</td><td>Recibir una solicitud de seguimiento veterinario</td><td>3</td><td>Sprint 2</td></tr>
    <tr><td>30</td><td>US-021</td><td>Aceptar o rechazar acceso veterinario</td><td>3</td><td>Sprint 2</td></tr>
    <tr><td>31</td><td>US-022</td><td>Revocar el acceso de un veterinario</td><td>3</td><td>Sprint 2</td></tr>
    <tr><td>32</td><td>US-023</td><td>Consultar clientes y pacientes autorizados</td><td>5</td><td>Sprint 2</td></tr>
    <tr><td>33</td><td>US-024</td><td>Consultar antecedentes de un paciente autorizado</td><td>3</td><td>Sprint 2</td></tr>
    <tr><td>34</td><td>US-025</td><td>Consultar actividades programadas</td><td>3</td><td>Sprint 2</td></tr>
    <tr><td>35</td><td>US-026</td><td>Gestionar una actividad o recordatorio</td><td>5</td><td>Sprint 2</td></tr>
    <tr><td>36</td><td>US-027</td><td>Recibir una notificación de actividad</td><td>5</td><td>Sprint 2</td></tr>
    <tr><td>37</td><td>US-028</td><td>Atender o reprogramar una actividad</td><td>3</td><td>Sprint 3</td></tr>
    <tr><td>38</td><td>TS-009</td><td>Implementar notificaciones móviles</td><td>5</td><td>Sprint 2</td></tr>
    <tr><td>39</td><td>US-029</td><td>Consultar información esencial sin conexión</td><td>5</td><td>Sprint 2</td></tr>
    <tr><td>40</td><td>US-030</td><td>Guardar trabajo pendiente sin conexión</td><td>5</td><td>Sprint 2</td></tr>
    <tr><td>41</td><td>US-031</td><td>Sincronizar operaciones pendientes</td><td>8</td><td>Sprint 2</td></tr>
    <tr><td>42</td><td>US-032</td><td>Resolver errores o conflictos de sincronización</td><td>8</td><td>Sprint 3</td></tr>
    <tr><td>43</td><td>TS-007</td><td>Implementar sincronización idempotente</td><td>8</td><td>Sprint 2</td></tr>
    <tr><td>44</td><td>US-033</td><td>Identificar un animal mediante código QR</td><td>5</td><td>Sprint 2</td></tr>
    <tr><td>45</td><td>US-034</td><td>Identificar un animal sin utilizar la cámara</td><td>3</td><td>Sprint 2</td></tr>
    <tr><td>46</td><td>TS-010</td><td>Integrar identificación QR mediante Google ML Kit</td><td>5</td><td>Sprint 2</td></tr>
    <tr><td>47</td><td>US-035</td><td>Consultar indicadores del hato</td><td>5</td><td>Sprint 3</td></tr>
    <tr><td>48</td><td>US-036</td><td>Consultar indicadores sanitarios de clientes</td><td>5</td><td>Sprint 3</td></tr>
    <tr><td>49</td><td>US-037</td><td>Registrar y consultar movimientos financieros</td><td>5</td><td>Sprint 3</td></tr>
    <tr><td>50</td><td>SP-002</td><td>Investigar la integración de Stripe para suscripciones móviles</td><td>5</td><td>Sprint 2</td></tr>
    <tr><td>51</td><td>US-038</td><td>Consultar planes de suscripción</td><td>3</td><td>Sprint 3</td></tr>
    <tr><td>52</td><td>US-039</td><td>Iniciar un pago mediante un proveedor externo</td><td>5</td><td>Sprint 3</td></tr>
    <tr><td>53</td><td>US-040</td><td>Consultar el resultado del pago y la suscripción</td><td>5</td><td>Sprint 3</td></tr>
    <tr><td>54</td><td>TS-011</td><td>Integrar el checkout externo de Stripe</td><td>8</td><td>Sprint 3</td></tr>
    <tr><td>55</td><td>US-041</td><td>Cambiar el idioma de la aplicación</td><td>3</td><td>Sprint 3</td></tr>
    <tr><td>56</td><td>US-042</td><td>Utilizar la aplicación con necesidades de accesibilidad</td><td>5</td><td>Sprint 3</td></tr>
    <tr><td>57</td><td>US-043</td><td>Comprender errores y estados de conectividad</td><td>3</td><td>Sprint 3</td></tr>
    <tr><td>58</td><td>TS-012</td><td>Aplicar internacionalización y accesibilidad móvil</td><td>5</td><td>Sprint 3</td></tr>
    <tr><td>59</td><td>TS-014</td><td>Automatizar pruebas de los flujos móviles críticos</td><td>8</td><td>Sprint 3</td></tr>
    <tr><td>60</td><td>TS-015</td><td>Configurar compilación y distribución de versiones móviles</td><td>5</td><td>Sprint 3</td></tr>
  </tbody>
</table>
