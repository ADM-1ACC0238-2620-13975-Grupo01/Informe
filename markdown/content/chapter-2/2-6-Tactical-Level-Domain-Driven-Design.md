<a id="toc-2-6-tactical-level-domain-driven-design"></a>

# 2.6. Tactical-Level Domain-Driven Design

Esta sección describe cómo los nueve bounded contexts identificados en el diseño estratégico se materializan en clases, capas, componentes y estructuras de persistencia. La propuesta utiliza un enfoque híbrido trazable: conserva nombres y responsabilidades del backend heredado y marca como no implementados los elementos requeridos para Android, Flutter y la evolución del dominio que todavía no existen en el código.

Para todos los contextos se aplican las siguientes convenciones:

- La **Domain Layer** mantiene entidades, aggregates, value objects, servicios de dominio e interfaces de repositorio.
- La **Application Layer** orquesta comandos, consultas, eventos y casos de uso sin depender de frameworks de presentación.
- La **Interface Layer** traduce HTTP o acciones de la interfaz móvil hacia los casos de uso.
- La **Infrastructure Layer** implementa persistencia, red, seguridad, sincronización e integraciones externas.
- MySQL es la fuente autoritativa; Room y SQLite mantienen caché y un outbox idempotente.
- Las reglas de negocio permanecen en la API y el dominio; Android y Flutter reutilizan los mismos contratos y lenguaje ubicuo.

Para mantener el informe legible, las fichas individuales se reservan para aggregates, entidades, servicios, handlers, controladores y adaptadores que explican decisiones relevantes de arquitectura. Los DTO, resources, mappers, comandos simples, configuraciones y adaptadores repetitivos se omiten del diccionario detallado y permanecen representados en el código o en los diagramas correspondientes cuando resulta necesario.

<table>
  <thead>
    <tr><th>Sección</th><th>Bounded Context</th><th>Módulo heredado</th><th>Propósito</th></tr>
  </thead>
  <tbody>
    <tr><td>2.6.1</td><td><a href="./2-6-1-Bounded-Context-Identity-and-Access-Management.md">Identity and Access Management</a></td><td>Iam</td><td>Administrar identidades, credenciales, roles y sesiones para que cada operación de AniTec se ejecute con una identidad autenticada y autorizada.</td></tr>
    <tr><td>2.6.2</td><td><a href="./2-6-2-Bounded-Context-Profile-Management.md">Profile Management</a></td><td>Profiles</td><td>Mantener la información personal y de contacto asociada con una identidad sin mezclarla con credenciales o reglas de autenticación.</td></tr>
    <tr><td>2.6.3</td><td><a href="./2-6-3-Bounded-Context-Livestock-Management.md">Livestock Management</a></td><td>Livestock</td><td>Gestionar fincas, hatos, animales e identificadores QR como fuente de referencia para los demás procesos ganaderos.</td></tr>
    <tr><td>2.6.4</td><td><a href="./2-6-4-Bounded-Context-Sanitary-Management.md">Sanitary Management</a></td><td>Sanitary</td><td>Conservar la historia sanitaria del animal y controlar el registro de diagnósticos, tratamientos, prescripciones y seguimientos autorizados.</td></tr>
    <tr><td>2.6.5</td><td><a href="./2-6-5-Bounded-Context-Veterinary-Collaboration.md">Veterinary Collaboration</a></td><td>Clients</td><td>Administrar solicitudes y autorizaciones entre ganaderos y veterinarios, delimitando clientes, pacientes y alcance de acceso.</td></tr>
    <tr><td>2.6.6</td><td><a href="./2-6-6-Bounded-Context-Activity-Management.md">Activity Management</a></td><td>Activities</td><td>Planificar actividades ganaderas y sanitarias, controlar su estado y decidir cuándo corresponde generar un recordatorio.</td></tr>
    <tr><td>2.6.7</td><td><a href="./2-6-7-Bounded-Context-Financial-Management.md">Financial Management</a></td><td>Financial</td><td>Registrar ingresos y egresos operativos y producir resúmenes económicos básicos para apoyar decisiones del ganadero.</td></tr>
    <tr><td>2.6.8</td><td><a href="./2-6-8-Bounded-Context-Subscription-Management.md">Subscription Management</a></td><td>Subscriptions</td><td>Administrar planes, vigencia de suscripciones y pagos confirmados sin introducir conceptos propios de Stripe en el dominio.</td></tr>
    <tr><td>2.6.9</td><td><a href="./2-6-9-Bounded-Context-Analytics-and-Reporting.md">Analytics and Reporting</a></td><td>Analytics</td><td>Construir proyecciones y métricas de consulta para los dashboards sin adquirir propiedad sobre los registros de los contextos fuente.</td></tr>
  </tbody>
</table>
