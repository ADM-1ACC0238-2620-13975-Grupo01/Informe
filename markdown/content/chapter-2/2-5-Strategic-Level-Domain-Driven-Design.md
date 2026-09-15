# 2.5. Strategic-Level Domain-Driven Design

El diseño estratégico de AniTec utiliza Domain-Driven Design para separar el dominio ganadero en modelos con responsabilidades, reglas y lenguaje propios. El proceso parte del Big Picture EventStorming de la sección 2.3.5, lo contrasta con los User Personas, entrevistas y requisitos de la sección 2.4, y concluye con bounded contexts y relaciones que pueden mantenerse de forma coherente en el backend y en las aplicaciones móviles.

La revisión recupera la evidencia del trabajo anterior —especialmente los pasos 4 al 10 del EventStorming, los canvases de Livestock, Sanitary, Financial y Analytics, y la estructura modular del backend— y la adapta al alcance actual: una aplicación Android nativa, una aplicación multiplataforma, operación offline, identificación QR, colaboración veterinaria, notificaciones y pagos mediante Stripe.

## 2.5.1. EventStorming

El equipo utilizó Miro para construir una narrativa compartida del dominio de AniTec. La sesión identificó actores, comandos, eventos de dominio, políticas, read models, sistemas externos, agregados, puntos problemáticos y eventos pivote. El análisis se organizó en bloques de trabajo acotados para evitar que la exploración se convirtiera en un inventario de funcionalidades sin secuencia de negocio.

<table>
  <thead>
    <tr><th>Dato de la sesión</th><th>Registro</th></tr>
  </thead>
  <tbody>
    <tr><td>Herramienta</td><td>Miro</td></tr>
    <tr><td>Participantes</td><td>Equipo de AniTec</td></tr>
    <tr><td>Fecha real</td><td><b>Placeholder:</b> completar con la fecha de la sesión registrada por el equipo.</td></tr>
    <tr><td>Duración real</td><td><b>Placeholder:</b> completar con la duración de la sesión; el time-box recomendado es de una a dos horas.</td></tr>
    <tr><td>Entradas</td><td>Entrevistas, User Personas, Needfinding, Ubiquitous Language y Product Backlog móvil.</td></tr>
    <tr><td>Resultados</td><td>Flujo actualizado del dominio, eventos pivote, nueve bounded contexts candidatos, Domain Stories y dependencias.</td></tr>
  </tbody>
</table>

### Convención visual

<table>
  <thead>
    <tr><th>Elemento</th><th>Color utilizado</th><th>Propósito</th></tr>
  </thead>
  <tbody>
    <tr><td>Domain Event</td><td>Naranja</td><td>Hecho relevante del negocio redactado en pasado.</td></tr>
    <tr><td>Command</td><td>Azul</td><td>Intención que puede producir un evento.</td></tr>
    <tr><td>Actor</td><td>Amarillo</td><td>Persona o rol que ejecuta una acción.</td></tr>
    <tr><td>Policy</td><td>Morado</td><td>Regla que reacciona ante un evento y puede generar otro comando.</td></tr>
    <tr><td>Read Model</td><td>Verde</td><td>Información que un actor consulta antes de tomar una decisión.</td></tr>
    <tr><td>External System</td><td>Rosado</td><td>Sistema ajeno a AniTec que participa en el flujo.</td></tr>
    <tr><td>Hotspot</td><td>Rojo o rosado intenso</td><td>Duda, riesgo, conflicto o decisión todavía abierta.</td></tr>
    <tr><td>Aggregate</td><td>Amarillo amplio</td><td>Frontera de consistencia que recibe comandos y produce eventos.</td></tr>
  </tbody>
</table>

### Proceso de exploración y refinamiento

**Paso 1 — Unstructured Exploration.** Los participantes registraron hechos relevantes sin imponer inicialmente una estructura. Se identificaron eventos relacionados con autenticación, fincas, animales, sanidad, finanzas, analítica, actividades y suscripciones.

<div align="center">
  <img src="../../assets/chapter-2/EventStormingPaso1.jpeg" alt="Paso 1 del EventStorming: exploración no estructurada" width="900">
  <p><i>Figura 2.5.1. Exploración no estructurada del dominio. Fuente: elaboración propia.</i></p>
</div>

**Paso 2 — Timeline.** Los eventos fueron ordenados para formar secuencias de negocio. El orden permitió distinguir el acceso al sistema, la gestión del hato, la atención sanitaria, el trabajo de campo y la obtención de indicadores.

<div align="center">
  <img src="../../assets/chapter-2/EventStormingPaso2.jpeg" alt="Paso 2 del EventStorming: línea de tiempo" width="900">
  <p><i>Figura 2.5.2. Línea de tiempo inicial. Fuente: elaboración propia.</i></p>
</div>

**Paso 3 — Pain Points.** Se marcaron problemas como credenciales inválidas, animales duplicados, detección tardía de enfermedades, registros financieros incompletos y fallos de notificación. Para el alcance móvil se añadieron conectividad intermitente, conflictos de sincronización, cámara no disponible, QR ilegible, autorización veterinaria vencida y pago no confirmado.

<div align="center">
  <img src="../../assets/chapter-2/EventStormingPaso3.jpeg" alt="Paso 3 del EventStorming: pain points" width="900">
  <p><i>Figura 2.5.3. Pain points identificados. Fuente: elaboración propia.</i></p>
</div>

**Paso 4 — Pivotal Events.** Se buscaron hechos que cambian el estado o la responsabilidad del proceso. Los principales eventos pivote son `UserRegistered`, `AnimalRegistered`, `AnimalIdentified`, `VeterinaryAccessGranted`, `HealthEventRecorded`, `DataSynchronized`, `PaymentConfirmed` y `SubscriptionActivated`. Estos eventos ayudaron a proponer límites entre modelos.

<div align="center">
  <img src="../../assets/chapter-2/EventStormingPaso4.jpeg" alt="Paso 4 del EventStorming: pivotal events" width="900">
  <p><i>Figura 2.5.4. Identificación de eventos pivote. Fuente: elaboración propia.</i></p>
</div>

**Paso 5 — Commands and Actors.** Cada evento se relacionó con el comando que lo origina y con el actor correspondiente. Por ejemplo, el ganadero ejecuta `RegisterAnimal`, mientras que el veterinario ejecuta `RecordVeterinaryCare` únicamente cuando existe una autorización vigente.

<div align="center">
  <img src="../../assets/chapter-2/EventStormingPaso5.jpeg" alt="Paso 5 del EventStorming: comandos y actores" width="900">
  <p><i>Figura 2.5.5. Incorporación de comandos y actores. Fuente: elaboración propia.</i></p>
</div>

**Paso 6 — Policies.** Se representaron reglas reactivas. Cuando una atención requiere seguimiento, se solicita programar una actividad; cuando la conexión vuelve, se solicita sincronizar operaciones pendientes; cuando Stripe confirma un pago válido, se solicita activar la suscripción.

<div align="center">
  <img src="../../assets/chapter-2/EventStormingPaso6.jpeg" alt="Paso 6 del EventStorming: políticas" width="900">
  <p><i>Figura 2.5.6. Políticas y automatizaciones. Fuente: elaboración propia.</i></p>
</div>

**Paso 7 — Read Models.** Se incorporó la información necesaria para decidir: lista de fincas, ficha del animal, historial sanitario, clientes autorizados, actividades pendientes, resumen financiero, indicadores y estado de suscripción. En la aplicación móvil, cada read model debe indicar si procede del servidor o de una copia local y cuándo fue actualizado.

<div align="center">
  <img src="../../assets/chapter-2/EventStormingPaso7.jpeg" alt="Paso 7 del EventStorming: read models" width="900">
  <p><i>Figura 2.5.7. Read models del dominio. Fuente: elaboración propia.</i></p>
</div>

**Paso 8 — External Systems.** Stripe participa en el checkout y la confirmación de pagos. El proveedor de notificaciones entrega recordatorios cuando se utiliza notificación remota. Google ML Kit se trata como una dependencia técnica ejecutada en el dispositivo para decodificar el QR y no como parte del modelo de negocio.

<div align="center">
  <img src="../../assets/chapter-2/EventStormingPaso8.jpeg" alt="Paso 8 del EventStorming: sistemas externos" width="900">
  <p><i>Figura 2.5.8. Sistemas externos. Fuente: elaboración propia.</i></p>
</div>

**Paso 9 — Aggregates.** Los comandos y eventos se agruparon alrededor de agregados con consistencia propia: `User`, `Profile`, `Farm`, `Animal`, `HealthHistory`, `VeterinaryAuthorization`, `FarmActivity`, `FinancialRecord`, `Subscription` y las proyecciones de analítica.

<div align="center">
  <img src="../../assets/chapter-2/EventStormingPaso9.jpeg" alt="Paso 9 del EventStorming: agregados" width="900">
  <p><i>Figura 2.5.9. Agregados candidatos. Fuente: elaboración propia.</i></p>
</div>

La siguiente síntesis actualiza el resultado anterior con las capacidades móviles del Product Backlog. Su propósito es mantener visibles los cambios de estado del negocio sin convertir Room, Flutter, Android, sincronización o ML Kit en conceptos del dominio.

![EventStorming móvil actualizado de AniTec](../../assets/chapter-2/strategic-ddd/eventstorming-mobile-overview.svg)

<p align="center"><i>Figura 2.5.10. Síntesis actualizada del EventStorming móvil. Fuente: elaboración propia.</i></p>

**Enlace del tablero de trabajo:** https://tinyurl.com/EventSorming

El equipo debe actualizar en ese tablero las notas correspondientes a QR, autorización veterinaria, offline, sincronización, Stripe y aplicaciones móviles para que la evidencia pública coincida con esta versión del informe.

### Decisiones derivadas del EventStorming

- La gestión del hato, la sanidad y la colaboración veterinaria concentran el valor diferencial y se clasifican como Core Domain.
- La autorización veterinaria posee reglas y ciclo de vida propios, por lo que no se modela como un simple atributo del perfil.
- La suscripción y los movimientos financieros representan conceptos distintos: una suscripción controla el acceso a un plan; un movimiento financiero describe la operación económica del ganadero.
- La analítica consume información de otros contextos mediante proyecciones y no modifica sus agregados.
- La sincronización offline pertenece a la infraestructura móvil. El contexto propietario mantiene las reglas para aceptar, rechazar o detectar conflictos.
- La lectura QR es una forma de identificar un animal; el dominio continúa trabajando con `AnimalId` y `AnimalCode` aunque cambie la tecnología de escaneo.

### 2.5.1.1. Candidate Context Discovery

El Candidate Context Discovery aplicó dos técnicas complementarias. **Start-with-Value** permitió separar las capacidades que generan el valor principal para ganaderos y veterinarios. **Look-for-Pivotal-Events** permitió ubicar cambios de estado y de responsabilidad en la línea de tiempo. Después se contrastaron los candidatos con el Ubiquitous Language, el Product Backlog y los módulos existentes del backend.

![Candidate Context Discovery de AniTec](../../assets/chapter-2/strategic-ddd/candidate-context-discovery.svg)

<p align="center"><i>Figura 2.5.11. Clasificación de los bounded contexts candidatos. Fuente: elaboración propia.</i></p>

<table>
  <thead>
    <tr><th>Bounded Context</th><th>Clasificación</th><th>Responsabilidad y eventos pivote</th><th>Correspondencia técnica actual</th></tr>
  </thead>
  <tbody>
    <tr><td>Identity and Access Management</td><td>Generic</td><td>Identidad, credenciales, sesiones y roles. `UserRegistered`, `SessionIssued`.</td><td><code>Iam</code></td></tr>
    <tr><td>Profile Management</td><td>Supporting</td><td>Datos personales y profesionales. `ProfileCreated`, `ProfileUpdated`.</td><td><code>Profiles</code></td></tr>
    <tr><td>Livestock Management</td><td>Core</td><td>Fincas, hatos, animales e identificación. `AnimalRegistered`, `AnimalIdentified`.</td><td><code>Livestock</code></td></tr>
    <tr><td>Sanitary Management</td><td>Core</td><td>Incidencias, diagnósticos, tratamientos e historial. `HealthEventRecorded`, `VeterinaryCareRecorded`.</td><td><code>Sanitary</code></td></tr>
    <tr><td>Veterinary Collaboration</td><td>Core</td><td>Solicitudes y autorizaciones entre ganaderos y veterinarios. `VeterinaryAccessGranted`, `VeterinaryAccessRevoked`.</td><td><code>Clients</code>, que deberá adoptar el lenguaje de colaboración.</td></tr>
    <tr><td>Activity Management</td><td>Supporting</td><td>Actividades, controles y recordatorios. `ActivityScheduled`, `ReminderDue`.</td><td><code>Activities</code></td></tr>
    <tr><td>Financial Management</td><td>Supporting</td><td>Ingresos, egresos y resumen financiero. `FinancialMovementRecorded`.</td><td><code>Financial</code></td></tr>
    <tr><td>Subscription Management</td><td>Supporting</td><td>Planes, checkout, pago confirmado y suscripción. `PaymentConfirmed`, `SubscriptionActivated`.</td><td><code>Subscriptions</code></td></tr>
    <tr><td>Analytics and Reporting</td><td>Supporting</td><td>Indicadores y read models para cada rol. `IndicatorsGenerated`.</td><td><code>Analytics</code></td></tr>
  </tbody>
</table>

#### Decisiones sobre los límites

<table>
  <thead>
    <tr><th>Elemento analizado</th><th>Decisión</th><th>Justificación</th></tr>
  </thead>
  <tbody>
    <tr><td>Offline Storage and Synchronization</td><td>No constituye bounded context.</td><td>Es una capacidad técnica de Android y Flutter. Cada operación sigue perteneciendo al contexto que define sus reglas.</td></tr>
    <tr><td>Animal Identification con QR</td><td>Capability de Livestock Management.</td><td>ML Kit traduce una imagen a un código; Livestock resuelve el animal y verifica autorización.</td></tr>
    <tr><td>Notifications</td><td>Capability técnica de Activity Management.</td><td>Activities decide cuándo existe un recordatorio; el proveedor solo lo entrega.</td></tr>
    <tr><td>Landing Page</td><td>Producto informativo, no bounded context.</td><td>No contiene reglas relevantes del dominio ganadero.</td></tr>
    <tr><td>Shared</td><td>Infraestructura compartida, no subdominio.</td><td>Repositorio base, Unit of Work y manejo de errores son mecanismos técnicos.</td></tr>
    <tr><td>Devices y Metrics</td><td>Fuera del alcance actual.</td><td>Pertenecen a la propuesta IoT anterior y no están respaldados por el Product Backlog móvil vigente.</td></tr>
  </tbody>
</table>

El resultado corrige la diferencia existente entre la lista anterior de cinco contextos, los cuatro canvases históricos y los contextos adicionales utilizados en los Domain Stories. Los nueve contextos seleccionados serán la referencia única para Context Mapping, Software Architecture y Tactical-Level DDD.

### 2.5.1.2. Domain Message Flows Modeling

Los Domain Message Flows aplican Domain Storytelling para mostrar cómo los actores, aplicaciones móviles y bounded contexts colaboran en los escenarios principales. Cada historia identifica quién inicia el flujo, qué comando se transmite, quién aplica las reglas y qué evento informa el resultado. Los términos Android, Flutter, base local y ML Kit aparecen únicamente cuando explican el transporte o la interacción con el dispositivo.

<table>
  <thead>
    <tr><th>Domain Story</th><th>Objetivo</th><th>Requisitos relacionados</th></tr>
  </thead>
  <tbody>
    <tr><td>DS-01</td><td>Registrar un animal con conectividad disponible o interrumpida.</td><td>US-008 a US-013, US-029 a US-031, TS-005 a TS-007.</td></tr>
    <tr><td>DS-02</td><td>Identificar un animal mediante QR y conservar búsqueda manual.</td><td>US-033, US-034, TS-010 y SP-001.</td></tr>
    <tr><td>DS-03</td><td>Registrar una incidencia y programar seguimiento.</td><td>US-014 a US-019 y US-025 a US-028.</td></tr>
    <tr><td>DS-04</td><td>Autorizar al veterinario y registrar una atención trazable.</td><td>US-016 a US-024.</td></tr>
    <tr><td>DS-05</td><td>Sincronizar operaciones idempotentes y comunicar conflictos.</td><td>US-029 a US-032 y TS-007.</td></tr>
    <tr><td>DS-06</td><td>Procesar una suscripción mediante Stripe.</td><td>US-038 a US-040 y TS-011.</td></tr>
  </tbody>
</table>

#### DS-01. Registro móvil de un animal

El ganadero registra un animal en la finca seleccionada. La aplicación guarda un comando identificado de forma única. Con conexión, el comando se envía inmediatamente; sin conexión, permanece pendiente. Livestock Management valida la propiedad de la finca y la unicidad del código antes de producir `AnimalRegistered`.

![Domain Story 1: registro móvil de un animal](../../assets/chapter-2/strategic-ddd/domain-flow-01-register-animal.svg)

<p align="center"><i>Figura 2.5.12. Domain Story del registro móvil de un animal. Fuente: elaboración propia.</i></p>

#### DS-02. Identificación mediante QR

La cámara proporciona la imagen y ML Kit decodifica el QR dentro del dispositivo. El código resultante se envía a Livestock Management, que resuelve `AnimalId` y comprueba que el usuario pueda consultar la ficha. Si no se obtiene un código válido, la búsqueda manual mantiene el resultado de negocio disponible.

![Domain Story 2: identificación mediante QR](../../assets/chapter-2/strategic-ddd/domain-flow-02-identify-qr.svg)

<p align="center"><i>Figura 2.5.13. Domain Story de identificación mediante QR. Fuente: elaboración propia.</i></p>

#### DS-03. Incidencia y seguimiento sanitario

Sanitary Management incorpora la incidencia al historial del animal. Cuando el evento requiere seguimiento, publica `FollowUpRequired`; Activity Management lo transforma en una actividad con fecha y produce `ReminderScheduled` para que el mecanismo móvil correspondiente programe la notificación.

![Domain Story 3: incidencia y seguimiento sanitario](../../assets/chapter-2/strategic-ddd/domain-flow-03-health-follow-up.svg)

<p align="center"><i>Figura 2.5.14. Domain Story de incidencia y seguimiento sanitario. Fuente: elaboración propia.</i></p>

#### DS-04. Autorización y atención veterinaria

Veterinary Collaboration administra la relación entre el ganadero y el veterinario. Sanitary Management consulta ese contrato antes de exponer antecedentes o registrar una atención. El evento final conserva la identidad profesional para asegurar trazabilidad.

![Domain Story 4: autorización y atención veterinaria](../../assets/chapter-2/strategic-ddd/domain-flow-04-veterinary-care.svg)

<p align="center"><i>Figura 2.5.15. Domain Story de autorización y atención veterinaria. Fuente: elaboración propia.</i></p>

#### DS-05. Sincronización y resolución de conflictos

La base local y el Sync Worker pertenecen a la infraestructura móvil. El comando conserva `CommandId`, versión y fecha. El contexto propietario comprueba idempotencia y concurrencia y responde con `Synced`, `Rejected` o `Conflict`; la aplicación muestra el estado sin duplicar la operación.

![Domain Story 5: sincronización y resolución de conflictos](../../assets/chapter-2/strategic-ddd/domain-flow-05-offline-sync.svg)

<p align="center"><i>Figura 2.5.16. Domain Story de sincronización y resolución de conflictos. Fuente: elaboración propia.</i></p>

#### DS-06. Suscripción mediante Stripe

Subscription Management crea el checkout para el plan seleccionado. La Anti-Corruption Layer transforma el modelo interno al contrato de Stripe y valida la respuesta. La suscripción solo cambia a activa después de que el backend comprueba el pago; una redirección del cliente por sí sola no confirma la operación.

![Domain Story 6: suscripción mediante Stripe](../../assets/chapter-2/strategic-ddd/domain-flow-06-subscription.svg)

<p align="center"><i>Figura 2.5.17. Domain Story de suscripción mediante Stripe. Fuente: elaboración propia.</i></p>

#### Tipos de colaboración identificados

- Las consultas directas desde Android y Flutter utilizan JSON sobre HTTPS mediante la API REST.
- Los eventos como `AnimalRegistered`, `HealthEventRecorded` o `FollowUpRequired` representan mensajes del dominio y permiten desacoplar consumidores.
- Los comandos offline se procesan con idempotencia para que una retransmisión no genere duplicados.
- Analytics utiliza read models y no consulta ni modifica directamente los agregados de otros contextos.
- Stripe y el proveedor de notificaciones se aíslan mediante Anti-Corruption Layers.

### 2.5.1.3. Bounded Context Canvases

Los canvases de Livestock Management, Animal Health, Financial Control y Analytics del trabajo anterior se utilizaron como punto de partida. La revisión actual normaliza sus nombres, actualiza reglas según el Product Backlog y agrega los contextos ausentes. Cada canvas se elaboró siguiendo este ciclo:

1. **Context Overview Definition:** propósito y clasificación estratégica.
2. **Business Rules Distillation and Ubiquitous Language Capture:** reglas y términos exclusivos.
3. **Capability Analysis:** comandos, consultas y eventos principales.
4. **Capability Layering:** distinción entre dominio, soporte e infraestructura.
5. **Dependencies Capture:** comunicaciones entrantes, salientes y contextos relacionados.
6. **Design Critique:** supuestos, métricas, preguntas abiertas y revisión de límites.

<table>
  <thead>
    <tr><th>Bounded Context</th><th>Resultado de la revisión</th></tr>
  </thead>
  <tbody>
    <tr><td>IAM</td><td>Se separaron credenciales y sesiones de los datos del perfil.</td></tr>
    <tr><td>Profiles</td><td>Se delimitó la identidad descriptiva de ganaderos y veterinarios.</td></tr>
    <tr><td>Livestock</td><td>Se incorporaron finca, identificación QR y alternativa manual.</td></tr>
    <tr><td>Sanitary</td><td>Se añadieron autorización, autoría y correcciones trazables.</td></tr>
    <tr><td>Veterinary Collaboration</td><td>Se formalizó como modelo con ciclo de vida propio.</td></tr>
    <tr><td>Activities</td><td>Se relacionaron controles, estados y recordatorios.</td></tr>
    <tr><td>Financial</td><td>Se separó la operación financiera de los pagos de suscripción.</td></tr>
    <tr><td>Subscriptions</td><td>Se reemplazó el pago simulado por Stripe y una ACL.</td></tr>
    <tr><td>Analytics</td><td>Se limitó a indicadores respaldados por historias vigentes.</td></tr>
  </tbody>
</table>

#### Capability Analysis and Layering

La revisión separa capacidades del dominio de mecanismos de aplicación e infraestructura. Esta separación evita crear bounded contexts para cada librería, pantalla o recurso del dispositivo.

<table>
  <thead>
    <tr><th>Bounded Context</th><th>Capacidades del dominio</th><th>Capacidades de aplicación o infraestructura</th></tr>
  </thead>
  <tbody>
    <tr><td>IAM</td><td>Registro, autenticación, sesión y autorización.</td><td>JWT, BCrypt y almacenamiento seguro del token.</td></tr>
    <tr><td>Profiles</td><td>Creación y actualización de datos personales y profesionales.</td><td>Validación, localización y exposición REST del perfil.</td></tr>
    <tr><td>Livestock</td><td>Fincas, animales, códigos e identificación.</td><td>Cámara, ML Kit, caché local y adaptadores REST.</td></tr>
    <tr><td>Sanitary</td><td>Historial, incidencia, atención, tratamiento y corrección.</td><td>Persistencia local, sincronización y control de versiones.</td></tr>
    <tr><td>Veterinary Collaboration</td><td>Solicitud, concesión, alcance y revocación del acceso.</td><td>Consulta REST y aplicación de políticas de autorización.</td></tr>
    <tr><td>Activities</td><td>Programación, atención y reprogramación.</td><td>Scheduler y adaptador del proveedor de notificaciones.</td></tr>
    <tr><td>Financial</td><td>Ingresos, egresos, categorías y balance.</td><td>Caché local y exposición REST.</td></tr>
    <tr><td>Subscriptions</td><td>Planes, estado de suscripción y confirmación de pago.</td><td>Stripe Checkout y Anti-Corruption Layer.</td></tr>
    <tr><td>Analytics</td><td>Definición de indicadores por rol y periodo.</td><td>Proyecciones, agregación y caché de read models.</td></tr>
  </tbody>
</table>

#### Identity and Access Management

Gestiona cuentas, credenciales, sesiones y autorización. Publica un identificador estable y el rol; no administra los datos personales del perfil.

![Bounded Context Canvas de IAM](../../assets/chapter-2/strategic-ddd/bounded-context-canvas-iam.svg)

<p align="center"><i>Figura 2.5.18. Bounded Context Canvas de IAM. Fuente: elaboración propia.</i></p>

#### Profile Management

Mantiene la información personal y profesional asociada con la identidad. Su separación evita que los cambios del perfil alteren el modelo de autenticación.

![Bounded Context Canvas de Profiles](../../assets/chapter-2/strategic-ddd/bounded-context-canvas-profiles.svg)

<p align="center"><i>Figura 2.5.19. Bounded Context Canvas de Profile Management. Fuente: elaboración propia.</i></p>

#### Livestock Management

Concentra el registro de fincas, hatos y animales. El QR es un medio de identificación y no sustituye el identificador estable del animal.

![Bounded Context Canvas de Livestock](../../assets/chapter-2/strategic-ddd/bounded-context-canvas-livestock.svg)

<p align="center"><i>Figura 2.5.20. Bounded Context Canvas de Livestock Management. Fuente: elaboración propia.</i></p>

#### Sanitary Management

Mantiene el historial sanitario, las atenciones y la trazabilidad clínica. Depende de Livestock para reconocer el animal y de Veterinary Collaboration para validar al profesional.

![Bounded Context Canvas de Sanitary](../../assets/chapter-2/strategic-ddd/bounded-context-canvas-sanitary.svg)

<p align="center"><i>Figura 2.5.21. Bounded Context Canvas de Sanitary Management. Fuente: elaboración propia.</i></p>

#### Veterinary Collaboration

Define solicitudes, autorizaciones, revocaciones, clientes y pacientes. La autorización es temporal y delimita qué información puede consultar o modificar el veterinario.

![Bounded Context Canvas de Veterinary Collaboration](../../assets/chapter-2/strategic-ddd/bounded-context-canvas-collaboration.svg)

<p align="center"><i>Figura 2.5.22. Bounded Context Canvas de Veterinary Collaboration. Fuente: elaboración propia.</i></p>

#### Activity Management

Administra actividades, fechas, responsables, estados y reprogramaciones. El mecanismo de notificación ejecuta la entrega, mientras Activity Management conserva la decisión de negocio sobre cuándo corresponde recordar.

![Bounded Context Canvas de Activities](../../assets/chapter-2/strategic-ddd/bounded-context-canvas-activities.svg)

<p align="center"><i>Figura 2.5.23. Bounded Context Canvas de Activity Management. Fuente: elaboración propia.</i></p>

#### Financial Management

Registra ingresos y egresos operativos del ganadero. Su alcance inicial proporciona visibilidad económica básica y no reemplaza un sistema contable o tributario.

![Bounded Context Canvas de Financial](../../assets/chapter-2/strategic-ddd/bounded-context-canvas-financial.svg)

<p align="center"><i>Figura 2.5.24. Bounded Context Canvas de Financial Management. Fuente: elaboración propia.</i></p>

#### Subscription Management

Administra planes, checkout, pagos confirmados y estado de suscripción. Stripe permanece fuera del modelo y se traduce mediante una Anti-Corruption Layer.

![Bounded Context Canvas de Subscriptions](../../assets/chapter-2/strategic-ddd/bounded-context-canvas-subscriptions.svg)

<p align="center"><i>Figura 2.5.25. Bounded Context Canvas de Subscription Management. Fuente: elaboración propia.</i></p>

#### Analytics and Reporting

Construye read models para indicadores de ganaderos y veterinarios. Consume información publicada por los contextos fuente y no adquiere propiedad sobre sus reglas o registros.

![Bounded Context Canvas de Analytics](../../assets/chapter-2/strategic-ddd/bounded-context-canvas-analytics.svg)

<p align="center"><i>Figura 2.5.26. Bounded Context Canvas de Analytics and Reporting. Fuente: elaboración propia.</i></p>

Las preguntas abiertas de cada canvas forman parte del Design Critique y deberán resolverse durante los sprints sin modificar silenciosamente el lenguaje o los límites. Cualquier decisión que cambie responsabilidades deberá reflejarse primero en el Context Map y después en el diseño táctico.

## 2.5.2. Context Mapping

El Context Mapping compara las relaciones estructurales entre los bounded contexts y explicita qué modelo actúa como proveedor, qué modelo consume sus contratos y qué patrón reduce el acoplamiento. Antes de seleccionar el mapa final se evaluaron tres alternativas.

<table>
  <thead>
    <tr><th>Alternativa</th><th>Descripción</th><th>Evaluación</th></tr>
  </thead>
  <tbody>
    <tr><td>A. Contextos amplios</td><td>Unir perfiles, colaboración, sanidad y actividades dentro de un único contexto de gestión ganadera.</td><td>Rechazada porque mezcla ciclos de vida, vocabularios y reglas de autorización; también dificulta la evolución independiente.</td></tr>
    <tr><td>B. Replicar todos los módulos anteriores</td><td>Considerar como contextos todos los módulos del backend, incluidos Devices, Metrics y Shared.</td><td>Rechazada porque confunde infraestructura con subdominios y conserva capacidades IoT fuera del backlog actual.</td></tr>
    <tr><td>C. Nueve contextos alineados con valor</td><td>Separar IAM, Profiles, Livestock, Sanitary, Veterinary Collaboration, Activities, Financial, Subscriptions y Analytics.</td><td>Seleccionada porque mantiene reglas cohesivas, coincide con el alcance móvil y aprovecha la modularidad existente del backend.</td></tr>
  </tbody>
</table>

![Context Mapping de AniTec](../../assets/chapter-2/strategic-ddd/context-map-anitec.svg)

<p align="center"><i>Figura 2.5.27. Context Map seleccionado para AniTec. Fuente: elaboración propia.</i></p>

### Relaciones entre bounded contexts

<table>
  <thead>
    <tr><th>Upstream / proveedor</th><th>Downstream / consumidor</th><th>Patrón</th><th>Contrato principal</th></tr>
  </thead>
  <tbody>
    <tr><td>IAM</td><td>Profiles</td><td>Customer/Supplier y Published Language</td><td><code>UserId</code>, <code>Role</code>, <code>UserRegistered</code>.</td></tr>
    <tr><td>IAM</td><td>Subscription Management</td><td>Open Host Service</td><td>Identidad y sesión autenticada.</td></tr>
    <tr><td>Profile Management</td><td>Livestock Management</td><td>Open Host Service y Published Language</td><td>Resumen del propietario.</td></tr>
    <tr><td>Profile Management</td><td>Veterinary Collaboration</td><td>Open Host Service y Published Language</td><td>Identidad y rol de las partes.</td></tr>
    <tr><td>Livestock Management</td><td>Veterinary Collaboration</td><td>Customer/Supplier y Published Language</td><td>Propietario, finca y animales.</td></tr>
    <tr><td>Livestock Management</td><td>Sanitary Management</td><td>Customer/Supplier y Published Language</td><td><code>AnimalId</code>, estado y propiedad.</td></tr>
    <tr><td>Veterinary Collaboration</td><td>Sanitary Management</td><td>Customer/Supplier</td><td>Estado y alcance de la autorización.</td></tr>
    <tr><td>Livestock Management</td><td>Activity Management</td><td>Published Language</td><td>Referencia de animal y finca.</td></tr>
    <tr><td>Sanitary Management</td><td>Activity Management</td><td>Published Language</td><td><code>FollowUpRequired</code>.</td></tr>
    <tr><td>Livestock, Sanitary, Activities y Financial</td><td>Analytics and Reporting</td><td>Conformist read models</td><td>Eventos y resúmenes publicados para proyecciones.</td></tr>
    <tr><td>Stripe</td><td>Subscription Management</td><td>Anti-Corruption Layer</td><td>Checkout Session y resultado de pago traducidos al modelo interno.</td></tr>
    <tr><td>Notification Provider</td><td>Activity Management</td><td>Anti-Corruption Layer</td><td>Solicitud de entrega y resultado de notificación.</td></tr>
  </tbody>
</table>

### Design Critique del Context Map

- **Coherencia con el negocio:** cada contexto contiene conceptos que cambian por las mismas reglas y razones.
- **Protección del Core Domain:** Livestock, Sanitary y Veterinary Collaboration no dependen del modelo externo de Stripe ni del proveedor de notificaciones.
- **Autonomía de Analytics:** sus proyecciones pueden reconstruirse sin modificar los datos fuente.
- **Movilidad:** Android y Flutter consumen contratos publicados por la API; no introducen un segundo modelo del dominio.
- **Offline:** los clientes almacenan comandos y read models locales, mientras las reglas de aceptación siguen en el contexto propietario.
- **Evolución:** reemplazar ML Kit, Stripe o el proveedor de notificaciones no obliga a cambiar el Ubiquitous Language.
- **Trazabilidad:** los mismos nueve contextos deberán utilizarse en el capítulo 2.6 y en los futuros diagramas C4.

El mapa seleccionado será la base de 2.5.3 Software Architecture. En esa sección se representarán la landing page, Android, Flutter, almacenamiento local, API REST, MySQL, Stripe, ML Kit, notificaciones y Firebase App Distribution sin convertir los contenedores técnicos en bounded contexts adicionales.

## 2.5.3. Software Architecture

La arquitectura de AniTec se documenta con el modelo C4 para representar la solución con distintos niveles de detalle. Las tres vistas se construyen desde un único modelo en Structurizr DSL, de modo que los actores, dependencias, tecnologías y relaciones conserven el mismo significado. El archivo fuente se encuentra en [`anitec-software-architecture.dsl`](../../assets/codefordiagrams/anitec-software-architecture.dsl).

La solución reutiliza la API REST y la persistencia desarrolladas en el proyecto anterior, pero reemplaza el frontend web como canal operativo por una aplicación Android nativa y una aplicación multiplataforma. La landing page mantiene una función informativa. Los nueve bounded contexts definidos en las secciones anteriores pertenecen al backend y no se modelan como contenedores independientes en este nivel; su estructura interna se desarrollará en el diseño táctico del punto 2.6.

### 2.5.3.1. Software Architecture Context Level Diagrams

El Context Level Diagram delimita a AniTec como un único sistema de software y muestra quién lo usa y de qué servicios externos depende. El **Rancher** administra su operación ganadera; el **Veterinarian** consulta pacientes autorizados y registra atenciones; el **Visitor** conoce la propuesta mediante la landing page; y el **Evaluator / Tester** instala las versiones móviles distribuidas para la validación del curso.

Stripe procesa el checkout de las suscripciones, Firebase Cloud Messaging entrega notificaciones push, Google ML Kit reconoce códigos QR en el dispositivo y Firebase App Distribution distribuye compilaciones firmadas. Estos servicios permanecen fuera del límite de AniTec y se integran mediante contratos que evitan trasladar sus modelos al dominio.

<table>
  <thead>
    <tr><th>Elemento externo</th><th>Relación con AniTec</th><th>Resultado esperado</th></tr>
  </thead>
  <tbody>
    <tr><td>Visitor</td><td>Consulta la landing page.</td><td>Comprende la propuesta de valor y encuentra el canal de acceso al producto.</td></tr>
    <tr><td>Rancher</td><td>Usa las aplicaciones móviles.</td><td>Gestiona fincas, animales, sanidad, actividades y finanzas.</td></tr>
    <tr><td>Veterinarian</td><td>Usa las aplicaciones móviles con autorización del ganadero.</td><td>Consulta clientes y pacientes y mantiene la trazabilidad sanitaria permitida.</td></tr>
    <tr><td>Evaluator / Tester</td><td>Recibe e instala builds mediante Firebase App Distribution.</td><td>Valida la aplicación en un dispositivo físico y una versión identificable.</td></tr>
    <tr><td>Stripe</td><td>Recibe solicitudes de checkout y devuelve resultados de pago.</td><td>AniTec activa o conserva la suscripción según una confirmación válida.</td></tr>
    <tr><td>Firebase Cloud Messaging</td><td>Recibe solicitudes de entrega de notificaciones.</td><td>El dispositivo presenta recordatorios definidos por Activity Management.</td></tr>
    <tr><td>Google ML Kit</td><td>Procesa imágenes de la cámara localmente.</td><td>La aplicación obtiene el código que Livestock Management resuelve como un animal.</td></tr>
    <tr><td>Firebase App Distribution</td><td>Publica builds firmadas para usuarios autorizados.</td><td>Las versiones de prueba y entrega se distribuyen con trazabilidad.</td></tr>
  </tbody>
</table>

<div align="center">
  <img src="../../assets/chapter-2/AniTec-SystemContext.svg" alt="Software Architecture Context Level Diagram de AniTec" width="900">
  <p><i>Figura 2.5.28. Software Architecture Context Level Diagram de AniTec. Fuente: elaboración propia con Structurizr DSL.</i></p>
</div>

### 2.5.3.2. Software Architecture Container Level Diagrams

El Container Level Diagram descompone AniTec en unidades ejecutables o de almacenamiento. La landing page comunica el producto; las dos aplicaciones móviles implementan la experiencia de los roles; cada cliente mantiene almacenamiento local para caché y operaciones pendientes; la API centraliza autenticación, autorización y reglas de negocio; y MySQL conserva la fuente de verdad compartida.

Android y Flutter consumen los mismos contratos JSON sobre HTTPS y se autentican con JWT. La persistencia local mejora la continuidad ante conectividad limitada, pero las reglas de aceptación continúan bajo el bounded context propietario en la API. La cámara y ML Kit actúan como capacidades del dispositivo: decodifican un QR, mientras Livestock Management determina qué animal representa y si el usuario puede consultarlo.

<table>
  <thead>
    <tr><th>Contenedor</th><th>Responsabilidad</th><th>Tecnología</th></tr>
  </thead>
  <tbody>
    <tr><td>Landing Page</td><td>Presenta la propuesta de valor, segmentos, características y acceso a versiones autorizadas.</td><td>HTML, CSS y JavaScript.</td></tr>
    <tr><td>Native Android Application</td><td>Implementa los flujos móviles nativos, utiliza cámara y notificaciones y sincroniza datos.</td><td>Kotlin y Jetpack Compose.</td></tr>
    <tr><td>Android Local Database</td><td>Almacena caché, read models y operaciones pendientes de sincronización.</td><td>Room sobre SQLite.</td></tr>
    <tr><td>Cross-Platform Mobile Application</td><td>Implementa el mismo alcance funcional mediante una base de código multiplataforma.</td><td>Flutter y Dart.</td></tr>
    <tr><td>Flutter Local Database</td><td>Proporciona persistencia local equivalente para la aplicación multiplataforma.</td><td>SQLite mediante una biblioteca compatible con Flutter.</td></tr>
    <tr><td>AniTec REST API</td><td>Expone casos de uso, aplica reglas de negocio y autorización y coordina integraciones externas.</td><td>C#, ASP.NET Core, Entity Framework Core, JWT y OpenAPI.</td></tr>
    <tr><td>AniTec Database</td><td>Persiste la información transaccional y las proyecciones de los bounded contexts.</td><td>MySQL.</td></tr>
  </tbody>
</table>

<div align="center">
  <img src="../../assets/chapter-2/AniTec-Containers.svg" alt="Software Architecture Container Level Diagram de AniTec" width="900">
  <p><i>Figura 2.5.29. Software Architecture Container Level Diagram de AniTec. Fuente: elaboración propia con Structurizr DSL.</i></p>
</div>

### 2.5.3.3. Software Architecture Deployment Diagrams

El Deployment Diagram representa la topología objetivo para las entregas del curso. La aplicación Android nativa se instala en un dispositivo Android físico y conserva su base Room dentro del mismo dispositivo. La aplicación Flutter se instala en el dispositivo físico correspondiente a la plataforma objetivo definida por el equipo y mantiene su propia base SQLite local. En ambos casos, la cámara y el reconocimiento QR se ejecutan dentro del dispositivo.

La landing page se publica como contenido estático en GitHub Pages. La API ASP.NET Core se ejecuta como Web Service en Render y accede a MySQL administrado en Filess.io, destinos recuperados del despliegue funcional del proyecto anterior. Stripe, Firebase Cloud Messaging y Firebase App Distribution se mantienen como servicios externos. Esta topología deberá actualizarse si durante los sprints cambia algún proveedor, sin alterar las responsabilidades de los contenedores.

<table>
  <thead>
    <tr><th>Nodo de despliegue</th><th>Artefacto o instancia</th><th>Comunicación principal</th></tr>
  </thead>
  <tbody>
    <tr><td>Physical Android Device</td><td>Native Android Application, Room/SQLite, cámara y ML Kit.</td><td>HTTPS con la API; almacenamiento y reconocimiento local.</td></tr>
    <tr><td>Cross-Platform Target Device</td><td>Flutter Application, SQLite, cámara y adaptador de reconocimiento QR.</td><td>HTTPS con la API; almacenamiento y reconocimiento local.</td></tr>
    <tr><td>GitHub Pages</td><td>Landing Page.</td><td>HTTPS con visitantes y acceso al canal de distribución.</td></tr>
    <tr><td>Render</td><td>AniTec REST API sobre el runtime de .NET.</td><td>JSON/HTTPS con clientes móviles; SQL con MySQL; HTTPS con servicios externos.</td></tr>
    <tr><td>Filess.io</td><td>AniTec Database sobre MySQL.</td><td>Conexión restringida desde la API.</td></tr>
    <tr><td>Firebase App Distribution</td><td>Builds móviles firmadas y versionadas.</td><td>Distribución a evaluadores autorizados.</td></tr>
    <tr><td>Firebase Cloud Messaging</td><td>Servicio de entrega de notificaciones.</td><td>Solicitudes desde el backend y entrega al dispositivo.</td></tr>
    <tr><td>Stripe Cloud</td><td>Checkout y confirmación de pago.</td><td>Stripe API sobre HTTPS.</td></tr>
  </tbody>
</table>

<div align="center">
  <img src="../../assets/chapter-2/AniTec-Deployment.svg" alt="Software Architecture Deployment Diagram de AniTec" width="900">
  <p><i>Figura 2.5.30. Software Architecture Deployment Diagram de AniTec. Fuente: elaboración propia con Structurizr DSL.</i></p>
</div>

Las tres imágenes deben exportarse desde el mismo archivo DSL. Los nombres y rutas requeridos se detallan en [`codefordiagrams/README.md`](../../assets/codefordiagrams/README.md), de modo que al copiar los PNG exportados los placeholders del informe se resuelvan sin modificar nuevamente el contenido.
