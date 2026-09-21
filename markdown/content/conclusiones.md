<div style="page-break-before: always;"></div>

# Conclusiones

## Conclusiones y recomendaciones

### Conclusiones

El proyecto AniTec permitió validar la necesidad de una solución digital orientada a ganaderos y veterinarios, debido a que ambos segmentos requieren mayor orden, trazabilidad y disponibilidad de información sobre animales, fincas, actividades, sanidad y gastos. Las entrevistas y validaciones realizadas confirmaron que el problema identificado es real y que una plataforma web puede aportar valor si mantiene una experiencia simple, clara y cercana al contexto ganadero.

El diseño del sistema basado en Domain-Driven Design permitió organizar AniTec mediante bounded contexts como IAM, Profiles, Livestock, Sanitary, Financial, Activities, Analytics, Clients, Devices, Metrics y Subscriptions. Esta separación favorece la mantenibilidad del sistema, facilita la asignación de responsabilidades dentro del equipo y permite que cada módulo evolucione sin afectar innecesariamente al resto de la aplicación.

Durante el Sprint 1 se logró establecer la presencia digital del producto mediante una landing page funcional desplegada en GitHub Pages. Este avance permitió comunicar la propuesta de valor de AniTec, presentar los beneficios principales para ganaderos y veterinarios, y generar una primera base de validación frente a usuarios potenciales.

Durante el Sprint 2 se implementó la aplicación web frontend con Vue, organizada por bounded contexts y conectada inicialmente a datos de prueba mediante my-json-server. Este sprint permitió construir las principales vistas funcionales de la plataforma, validar flujos de navegación y preparar la estructura necesaria para reemplazar progresivamente los datos mock por servicios reales.

Durante el Sprint 3 se desarrolló el backend real de AniTec con ASP.NET Core, Entity Framework Core y MySQL. La API implementa autenticación con JWT, gestión de usuarios, perfiles, hatos, animales, eventos sanitarios, actividades, registros financieros, clientes veterinarios, analíticas, planes, suscripciones y pagos mock. Con ello, el proyecto dejó de depender solamente de datos simulados y pasó a contar con una base de servicios persistentes.

La documentación de servicios mediante Swagger/OpenAPI permitió verificar los endpoints implementados y facilitar las pruebas manuales del backend. Asimismo, las migraciones de Entity Framework Core permitieron mantener alineada la estructura de la base de datos con las entidades del dominio, reduciendo errores en la configuración y mejorando la trazabilidad técnica del sistema.

El despliegue del backend en Render representa un avance importante para el proyecto, ya que la API queda disponible desde internet y puede ser consumida por el frontend desplegado. Esto permite validar AniTec en un entorno más cercano a producción, comprobar la disponibilidad pública del servicio y preparar futuras pruebas de integración entre frontend, backend y base de datos.

En relación con el Student Outcome, el equipo evidenció trabajo colaborativo y liderazgo conjunto durante los tres avances. Cada integrante asumió responsabilidades claras por módulo o artefacto, participó en la planificación de tareas, colaboró en la integración del sistema y aportó a la documentación del producto. Esto permitió cumplir los objetivos de cada sprint de forma progresiva y mantener coherencia entre la propuesta, el diseño, el frontend, el backend y el despliegue.

**Contraste con Lean UX y validaciones:**

El Problem Statement se mantiene vigente, ya que las validaciones confirmaron que ganaderos y veterinarios siguen enfrentando problemas de desorden, registros manuales y falta de trazabilidad. AniTec responde a una necesidad real al centralizar información sanitaria, productiva, económica y operativa en una sola plataforma.

Las Business Assumptions fueron validadas de forma general, debido a que los usuarios reconocieron valor en contar con una solución web para registrar animales, eventos sanitarios, actividades, finanzas y clientes veterinarios. Sin embargo, todavía se requiere reforzar reportes, alertas y campos específicos para aumentar la utilidad percibida.

Las User Assumptions se confirmaron parcialmente, porque los entrevistados comprendieron la navegación por roles y consideraron útiles los dashboards y módulos principales. Aun así, la experiencia debe seguir simplificándose, especialmente en formularios y mensajes de error.

Las Feature Assumptions resultaron pertinentes para una primera versión del producto, ya que los usuarios identificaron valor en el registro de animales, historial sanitario, actividades, finanzas y seguimiento veterinario. Como mejora futura, se deben ampliar los campos clínicos, datos del animal y métricas disponibles para apoyar mejores decisiones.

Las Hypothesis Statements fueron parcialmente validadas. Existe interés inicial y una percepción positiva sobre la utilidad de AniTec, especialmente por la centralización de información; no obstante, la adopción dependerá de fortalecer la confianza, mejorar recordatorios, optimizar reportes y facilitar el uso continuo de la plataforma.

Los criterios de éxito quedan planteados como metas para una siguiente etapa de validación con uso real de la aplicación desplegada. Las entrevistas permiten confirmar intención de uso y valor percibido, pero aún falta medir reducción de errores, mejora en precisión de registros y apoyo efectivo a decisiones basadas en datos.

### Recomendaciones

**Corto plazo:** Se recomienda continuar con la integración completa entre el frontend desplegado en GitHub Pages y el backend desplegado en Render, asegurando que las variables de entorno del frontend apunten a la API real y que los flujos principales funcionen sin depender de my-json-server.

**Corto plazo:** Se recomienda fortalecer la autenticación y autorización del sistema, definiendo permisos por rol para ganaderos, veterinarios y administradores. Esto permitiría proteger los endpoints sensibles y asegurar que cada usuario solo acceda a la información correspondiente a su perfil.

**Mediano plazo:** Se recomienda continuar la validación con ganaderos y veterinarios usando la aplicación desplegada, no solo prototipos. Esto permitirá identificar problemas reales de uso, comprensión del lenguaje, dificultad en formularios, utilidad de dashboards y necesidades adicionales en los módulos de sanidad, actividades y finanzas.

**Mediano plazo:** Se recomienda mejorar la experiencia de usuario del frontend en una siguiente iteración, priorizando claridad en dashboards, simplificación de formularios y mejor organización del flujo veterinario por clientes asignados.

**Mediano plazo:** Se recomienda completar y fortalecer las pruebas del backend, incluyendo pruebas de endpoints, validación de reglas de negocio, manejo de errores y pruebas de integración con la base de datos. Esto ayudará a asegurar mayor estabilidad antes de seguir ampliando funcionalidades.

**Futuro roadmap:** Se recomienda mantener actualizada la documentación técnica, incluyendo endpoints, migraciones, evidencias de despliegue, diagramas C4 y decisiones de arquitectura. A medida que AniTec crezca, esta documentación será clave para sostener la colaboración del equipo y facilitar futuras mejoras del producto.

---

## Video About The Team

El video About The Team presenta la participación de los integrantes del equipo Titan Team 4 durante el desarrollo de AniTec, destacando las actividades realizadas, los logros alcanzados en el curso y el desarrollo de competencias asociadas al trabajo colaborativo, liderazgo conjunto, planificación de tareas y cumplimiento de objetivos.

**Datos del video:**

| Elemento | Información |
| -------- | ----------- |
| Título | Video About The Team - AniTec |
| Duración | |
| Público objetivo | Docente del curso, visitantes del landing page e interesados en conocer el proceso de trabajo del equipo |
| URL publicado en Microsoft Stream |  |
| URL publicado en YouTube |  |
| Uso en landing page | El video de YouTube se utiliza como evidencia pública del proceso de trabajo del equipo. |

**URL del video publicado en Microsoft Stream:**


**URL del video publicado en YouTube:**


<div align="center">
    <img src="../assets/chapter-5/" width="700">
    <p><i><b>Fuente</b>: Elaboración propia.</i></p>
</div>

