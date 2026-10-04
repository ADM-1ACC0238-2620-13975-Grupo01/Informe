<a id="toc-3-1-product-design"></a>

# 3.1. Product design

El diseño de AniTec traduce las necesidades de ganaderos y veterinarios en una experiencia coherente entre la Landing Page, la aplicación Android nativa y la aplicación multiplataforma. Se priorizan la consulta rápida en campo, el registro con pocos pasos, la legibilidad en exteriores y la continuidad ante una conexión inestable. Los artefactos mantienen trazabilidad con los User Personas, User Stories y bounded contexts del capítulo II.

<a id="toc-3-1-1-style-guidelines"></a>

## 3.1.1. Style Guidelines

Estas pautas establecen un lenguaje visual común para que las interfaces sean consistentes, reconocibles y accesibles en la Landing Page, Jetpack Compose y Flutter.

<a id="toc-3-1-1-1-general-style-guidelines"></a>

### 3.1.1.1. General Style Guidelines

**Identidad visual.** AniTec combina referencias al entorno ganadero con una presentación digital moderna. Los logotipos deben conservar sus proporciones, un área libre alrededor y suficiente contraste. No deben deformarse, rotarse ni recolorearse arbitrariamente.

<div align="center">
  <img src="../../assets/chapter-3/style-guidelines/logo-startup.png" alt="Logo de la startup Titan" width="220">
  <p><i>Figura 3.1.1.1. Logo de la startup Titan. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-3/style-guidelines/logo-producto.png" alt="Logo del producto AniTec" width="220">
  <p><i>Figura 3.1.1.2. Logo de AniTec. Fuente: elaboración propia.</i></p>
</div>

**Paleta de colores.** Los verdes representan salud, campo y crecimiento; los marrones conectan la interfaz con la actividad ganadera; y los tonos claros producen superficies legibles. Ningún estado dependerá únicamente del color: las alertas, confirmaciones y errores también usarán texto o iconografía.

<table>
  <thead><tr><th>Color</th><th>Código</th><th>Uso principal</th></tr></thead>
  <tbody>
    <tr><td>Verde principal</td><td>#79B267</td><td>Acciones principales, selección activa y marca.</td></tr>
    <tr><td>Marrón oscuro</td><td>#925930</td><td>Contraste de identidad y elementos ganaderos.</td></tr>
    <tr><td>Marrón medio</td><td>#A3794F</td><td>Acentos, ilustraciones y acciones secundarias.</td></tr>
    <tr><td>Verde suave</td><td>#A3C4A8</td><td>Estados secundarios y fondos de apoyo.</td></tr>
    <tr><td>Beige</td><td>#D1BFA5</td><td>Tarjetas, superficies y separadores.</td></tr>
    <tr><td>Crema</td><td>#F5F0E6</td><td>Fondo claro principal y descanso visual.</td></tr>
  </tbody>
</table>

<div align="center">
  <img src="../../assets/chapter-3/style-guidelines/79B267.png" alt="Color 79B267" width="105">
  <img src="../../assets/chapter-3/style-guidelines/925930.png" alt="Color 925930" width="105">
  <img src="../../assets/chapter-3/style-guidelines/A3794F.png" alt="Color A3794F" width="105">
  <img src="../../assets/chapter-3/style-guidelines/A3C4A8.png" alt="Color A3C4A8" width="105">
  <img src="../../assets/chapter-3/style-guidelines/D1BFA5.png" alt="Color D1BFA5" width="105">
  <img src="../../assets/chapter-3/style-guidelines/F5F0E6.png" alt="Color F5F0E6" width="105">
  <p><i>Figura 3.1.1.3. Paleta cromática de AniTec. Fuente: elaboración propia.</i></p>
</div>

**Tipografía.** AniTec utiliza Poppins por su lectura clara. Los encabezados emplean SemiBold o Bold y el cuerpo Regular o Medium. En móviles se respetará el escalado configurado por el usuario y se evitarán bloques extensos en mayúsculas.

| Uso | Peso recomendado | Tamaño móvil de referencia |
|---|---|---|
| Título principal | Bold | 28–32 sp |
| Título de pantalla | SemiBold | 22–24 sp |
| Subtítulo | SemiBold | 18–20 sp |
| Cuerpo | Regular | 16 sp |
| Etiqueta o ayuda | Medium / Regular | 14 sp |
| Texto auxiliar | Regular | 12 sp como mínimo |

<div align="center">
  <img src="../../assets/chapter-3/style-guidelines/poppins.png" alt="Muestra de Poppins" width="650">
  <p><i>Figura 3.1.1.4. Tipografía Poppins. Fuente: elaboración propia.</i></p>
</div>

**Espaciado, formas e iconografía.** Se usará una cuadrícula base de 8 unidades. Las tarjetas podrán utilizar radios de 8 a 16 dp y los controles táctiles mantendrán un área mínima de 48 × 48 dp. Los iconos tendrán etiquetas o descripciones accesibles cuando su significado no sea evidente.

<div align="center">
  <img src="../../assets/chapter-3/style-guidelines/icons.png" alt="Iconografía de AniTec" width="650">
  <p><i>Figura 3.1.1.5. Referencia de iconografía. Fuente: elaboración propia.</i></p>
</div>

**Tono de comunicación.** La comunicación será clara, respetuosa, serena y orientada a la acción. Usará términos conocidos por ganaderos y veterinarios, instrucciones breves y mensajes que indiquen cómo recuperarse de un problema.

| Situación | Redacción recomendada |
|---|---|
| Acción | “Registrar animal” |
| Confirmación | “El animal se registró correctamente.” |
| Error recuperable | “No pudimos guardar los cambios. Revisa tu conexión e inténtalo nuevamente.” |
| Sin resultados | “No se encontraron animales con esos filtros.” |
| Permiso | “AniTec necesita acceso a la cámara para leer el código del animal.” |

**Accesibilidad e internacionalización**

- Mantener contraste suficiente y no depender solo del color.
- Permitir el aumento de texto sin pérdida de contenido.
- Incluir descripciones accesibles en imágenes y controles.
- Centralizar textos para English (en_US) y Latin American Spanish (es_419), con inglés como idioma predeterminado.
- Formatear fechas, números y monedas según la región.
- Ofrecer una alternativa manual cuando la cámara no esté disponible.
- Usar etiquetas semánticas, foco visible y atributos ARIA en la Landing Page.

**Criterios por producto.** La Landing Page tendrá jerarquía vertical, navegación superior y diseño responsive. Android aplicará los patrones de Material Design con Jetpack Compose. Flutter utilizará componentes equivalentes y conservará la misma identidad y orden de tareas. Ambas aplicaciones contemplarán carga, contenido, ausencia de datos, error, confirmación y operación sin conexión cuando corresponda.

<a id="toc-3-1-2-information-architecture"></a>

## 3.1.2. Information Architecture

La arquitectura de información organiza la Landing Page y las aplicaciones para que visitantes, ganaderos y veterinarios encuentren con rapidez las funciones relacionadas con sus objetivos. La propuesta reduce carga cognitiva mediante etiquetas breves, agrupación por tareas y navegación diferenciada por rol.

<a id="toc-3-1-2-1-organization-systems"></a>

### 3.1.2.1. Organization Systems

| Sistema | Aplicación en AniTec |
|---|---|
| Jerárquico | Los dashboards priorizan alertas, indicadores y acciones frecuentes. |
| Secuencial | Registro de cuenta, finca, animal y evento sanitario se resuelve en pasos ordenados. |
| Cronológico | Actividades, historial sanitario, pagos y operaciones pendientes se ordenan por fecha. |
| Por tópicos | Animales, fincas, sanidad, actividades, finanzas, colaboración, analíticas y suscripciones. |
| Por audiencia | La Landing Page y la navegación diferencian a ganaderos y veterinarios. |
| Matricial | Los reportes cruzan indicadores por finca, animal, categoría, estado o periodo. |

La Landing Page sigue un recorrido de descubrimiento: propuesta de valor, problema, beneficios, funciones por segmento, planes y llamada a la acción. En las aplicaciones, la autenticación conduce a un dashboard ajustado al rol.

<a id="toc-3-1-2-2-labelling-systems"></a>

### 3.1.2.2. Labelling Systems

Las etiquetas representan conceptos del dominio y evitan términos técnicos internos.

| Producto o rol | Etiqueta | Significado |
|---|---|---|
| Landing Page | Inicio | Propuesta principal de AniTec. |
| Landing Page | Beneficios | Valor ofrecido por el producto. |
| Landing Page | Ganaderos | Capacidades de gestión del hato. |
| Landing Page | Veterinarios | Capacidades de seguimiento clínico. |
| Landing Page | Planes | Alternativas de suscripción. |
| Ganadero | Inicio | Alertas, animales, actividades e indicadores. |
| Ganadero | Fincas | Unidades productivas. |
| Ganadero | Animales | Búsqueda, registro y consulta de animales. |
| Ganadero | Sanidad | Incidencias, visitas, tratamientos e historial. |
| Ganadero | Actividades | Tareas y recordatorios. |
| Ganadero | Finanzas | Ingresos, egresos y resúmenes. |
| Veterinario | Clientes | Ganaderos que autorizaron colaboración. |
| Veterinario | Pacientes | Animales autorizados por cada cliente. |
| Veterinario | Seguimiento | Información clínica autorizada. |
| Compartido | Reportes | Métricas y tendencias del rol. |
| Compartido | Plan | Suscripción y condiciones vigentes. |

Las acciones principales serán “Registrar”, “Guardar”, “Actualizar”, “Archivar”, “Buscar”, “Filtrar”, “Reintentar” y “Cancelar”. “Eliminar” se reservará para operaciones destructivas y requerirá confirmación.

<a id="toc-3-1-2-3-seo-tags-and-meta-tags"></a>

### 3.1.2.3. SEO Tags and Meta Tags

**Landing Page**

| Elemento | Valor propuesto |
|---|---|
| Title | AniTec – Gestión y trazabilidad inteligente para la ganadería |
| Description | AniTec ayuda a ganaderos y veterinarios a organizar animales, sanidad, actividades y decisiones de campo desde experiencias móviles conectadas. |
| Keywords | AniTec, gestión ganadera, trazabilidad animal, salud animal, veterinarios, aplicación ganadera, ganado, Perú |
| Author | AniTec |
| Open Graph title | AniTec – Información ganadera donde la necesitas |
| Open Graph description | Gestiona animales, registros sanitarios y actividades desde una experiencia diseñada para el trabajo de campo. |

**ASO de las aplicaciones móviles**

| Elemento | Android nativo | Aplicación Flutter |
|---|---|---|
| App title | AniTec Ganadería | AniTec Ganadería |
| Subtitle | Gestión del ganado en campo | Gestión ganadera multiplataforma |
| Keywords | ganado, animales, sanidad, trazabilidad, veterinario | ganado, animales, sanidad, trazabilidad, veterinario |
| Short description | Registra animales, controla su salud y organiza actividades desde el teléfono. | Consulta y gestiona la información esencial de AniTec desde dispositivos compatibles. |
| Full description | Aplicación para ganaderos y veterinarios que necesitan información organizada, alertas y trazabilidad en campo. | Experiencia multiplataforma para acceder a los flujos de AniTec mediante la misma API y reglas del producto. |

Los textos definitivos se ajustarán a las restricciones de longitud de cada tienda antes de la distribución.

<a id="toc-3-1-2-4-searching-systems"></a>

### 3.1.2.4. Searching Systems

| Datos | Búsqueda | Filtros | Presentación |
|---|---|---|---|
| Animales | Nombre o identificador | Finca, especie, raza y estado | Tarjetas con identificación, finca y estado. |
| Fincas | Nombre o ubicación | Estado y actividad | Lista con cantidad de animales. |
| Historial sanitario | Animal, diagnóstico o tratamiento | Tipo, fecha y profesional | Línea de tiempo cronológica. |
| Clientes | Nombre del ganadero | Autorización y estado | Lista con acceso disponible o pendiente. |
| Pacientes | Nombre o identificador | Cliente, especie y condición | Tarjetas con acceso al historial. |
| Actividades | Título o animal | Fecha, prioridad y estado | Lista por urgencia y fecha. |
| Finanzas | Concepto o categoría | Tipo, categoría y periodo | Resumen y lista de movimientos. |

Los resultados permitirán limpiar criterios y mostrarán un estado vacío cuando no existan coincidencias. Las búsquedas esenciales podrán consultar la caché local sin conexión.

<a id="toc-3-1-2-5-navigation-systems"></a>

### 3.1.2.5. Navigation Systems

La Landing Page navega hacia Inicio, Beneficios, Ganaderos, Veterinarios, Planes y Contacto. En pantallas pequeñas usará un menú condensado sin ocultar las llamadas a la acción.

| Rol | Destinos principales | Rutas secundarias |
|---|---|---|
| Ganadero | Inicio, Animales, Actividades, Reportes y Más | Fincas, sanidad, finanzas, plan, perfil y configuración. |
| Veterinario | Inicio, Clientes, Pacientes, Actividades y Más | Seguimiento, reportes, plan, perfil y configuración. |

El retorno conservará filtros y datos no enviados. Las notificaciones y enlaces profundos comprobarán autenticación y autorización antes de abrir un recurso; si no está disponible, mostrarán una explicación y una ruta segura hacia el inicio.

<a id="toc-3-1-3-landing-page-ui-design"></a>

## 3.1.3. Landing Page UI Design

La Landing Page comunica el problema, los beneficios para cada segmento y las opciones para conocer las aplicaciones. Aplica la identidad visual, la organización jerárquica y una estructura responsive.

**Enlace de diseño móvil:** 
https://www.figma.com/design/DvQjG8GIupLP7TBQNi5Hr6/LandingMovil_MockUp?node-id=0-1&t=qJgJhyhc97VCfTMW-1
https://www.figma.com/design/q7A10f5s09GjpeGGWNdsZG/LandingMovil_wireframe?node-id=0-1&t=FDHM5xffOJs1fj7Z-1

<a id="toc-3-1-3-1-landing-page-wireframe"></a>

### 3.1.3.1. Landing Page Wireframe

El wireframe de escritorio define la distribución del encabezado, propuesta de valor, beneficios, secciones por segmento, planes, testimonios y pie de página antes de aplicar el acabado visual.

<div align="center">
  <img src="../../assets/chapter-3/landing-page/landing-page-wireframe-desktop.png" alt="Wireframe de escritorio de la Landing Page" width="500">
  <p><i>Figura 3.1.3.1. Wireframe de escritorio de la Landing Page. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-3/landing-page/LandingMovil_wireframe1.png" alt="Wireframe de movil de la Landing Page" width="500">
  <p><i>Figura 3.1.3.1.2 Wireframe de movil de la Landing Page. Fuente: elaboración propia.</i></p>
</div>

Link del wireframe movil: https://www.figma.com/design/q7A10f5s09GjpeGGWNdsZG/LandingMovil_wireframe?node-id=0-1&t=FDHM5xffOJs1fj7Z-1 


<a id="toc-3-1-3-2-landing-page-mock-up"></a>

### 3.1.3.2. Landing Page Mock-up

El mock-up de escritorio incorpora la paleta, Poppins, imágenes, iconografía y llamadas a la acción para transmitir confianza y relación con el entorno agropecuario.

<div align="center">
  <img src="../../assets/chapter-3/landing-page/landing-page-mockup-desktop.png" alt="Mock-up de escritorio de la Landing Page" width="500">
  <p><i>Figura 3.1.3.2. Mock-up de escritorio de la Landing Page. Fuente: elaboración propia.</i></p>
</div>

<div align="center">
  <img src="../../assets/chapter-3/landing-page/LandingMovil_MockUp1.png" alt="Mock-up de movil de la Landing Page" width="500">
  <p><i>Figura 3.1.3.2.2 Mock-up de movil de la Landing Page. Fuente: elaboración propia.</i></p>
</div>

Link del MockUp: https://www.figma.com/design/DvQjG8GIupLP7TBQNi5Hr6/LandingMovil_MockUp?node-id=0-1&t=qJgJhyhc97VCfTMW-1 


<a id="toc-3-1-4-mobile-applications-ux-ui-design"></a>

## 3.1.4. Mobile Applications UX/UI Design

La propuesta comprende Android nativo con Kotlin y Jetpack Compose y una aplicación multiplataforma con Flutter y Dart. Ambas comparten objetivos, contratos, identidad y reglas de negocio, pero respetan los patrones de su plataforma. Los primeros flujos cubren autenticación, dashboard, registro y mantenimiento de animales, consulta del historial y registro sanitario.

<a id="toc-3-1-4-1-mobile-applications-wireframes"></a>

### 3.1.4.1. Mobile Applications Wireframes

Los wireframes representan la estructura funcional de cada pantalla de la aplicación móvil, definiendo la distribución de elementos y flujos de interacción básicos. Sirven como punto de partida para validar la organización visual y funcional del producto.



El diseño en Figma se encuentra en: https://www.figma.com/design/uRmjCeeukXUb2AnZ2kFQsA/Anitec-2026-2?node-id=1-2&t=GnQ9UR4xNp7TYaA1-1

#### Aplicación Flutter

##### IAM

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/wireframe-sheets/flutter-iam-01.jpg" alt="Wireframes Flutter del módulo IAM, lámina 1 de 1" width="650">
  <p><i>Figura 3.1.4.1.1. Wireframes Flutter del módulo IAM, lámina 1 de 1. Fuente: elaboración propia.</i></p>
</div>

##### Usuario rancher

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/wireframe-sheets/flutter-rancher-01.jpg" alt="Wireframes Flutter del usuario rancher, lámina 1 de 5" width="650">
  <p><i>Figura 3.1.4.1.2. Wireframes Flutter del usuario rancher, lámina 1 de 5. Fuente: elaboración propia.</i></p>
</div>

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/wireframe-sheets/flutter-rancher-02.jpg" alt="Wireframes Flutter del usuario rancher, lámina 2 de 5" width="650">
  <p><i>Figura 3.1.4.1.3. Wireframes Flutter del usuario rancher, lámina 2 de 5. Fuente: elaboración propia.</i></p>
</div>

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/wireframe-sheets/flutter-rancher-03.jpg" alt="Wireframes Flutter del usuario rancher, lámina 3 de 5" width="650">
  <p><i>Figura 3.1.4.1.4. Wireframes Flutter del usuario rancher, lámina 3 de 5. Fuente: elaboración propia.</i></p>
</div>

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/wireframe-sheets/flutter-rancher-04.jpg" alt="Wireframes Flutter del usuario rancher, lámina 4 de 5" width="650">
  <p><i>Figura 3.1.4.1.5. Wireframes Flutter del usuario rancher, lámina 4 de 5. Fuente: elaboración propia.</i></p>
</div>

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/wireframe-sheets/flutter-rancher-05.jpg" alt="Wireframes Flutter del usuario rancher, lámina 5 de 5" width="650">
  <p><i>Figura 3.1.4.1.6. Wireframes Flutter del usuario rancher, lámina 5 de 5. Fuente: elaboración propia.</i></p>
</div>

##### Usuario veterinario

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/wireframe-sheets/flutter-vet-01.jpg" alt="Wireframes Flutter del usuario vet, lámina 1 de 5" width="650">
  <p><i>Figura 3.1.4.1.7. Wireframes Flutter del usuario vet, lámina 1 de 5. Fuente: elaboración propia.</i></p>
</div>

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/wireframe-sheets/flutter-vet-02.jpg" alt="Wireframes Flutter del usuario vet, lámina 2 de 5" width="650">
  <p><i>Figura 3.1.4.1.8. Wireframes Flutter del usuario vet, lámina 2 de 5. Fuente: elaboración propia.</i></p>
</div>

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/wireframe-sheets/flutter-vet-03.jpg" alt="Wireframes Flutter del usuario vet, lámina 3 de 5" width="650">
  <p><i>Figura 3.1.4.1.9. Wireframes Flutter del usuario vet, lámina 3 de 5. Fuente: elaboración propia.</i></p>
</div>

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/wireframe-sheets/flutter-vet-04.jpg" alt="Wireframes Flutter del usuario vet, lámina 4 de 5" width="650">
  <p><i>Figura 3.1.4.1.10. Wireframes Flutter del usuario vet, lámina 4 de 5. Fuente: elaboración propia.</i></p>
</div>

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/wireframe-sheets/flutter-vet-05.jpg" alt="Wireframes Flutter del usuario vet, lámina 5 de 5" width="650">
  <p><i>Figura 3.1.4.1.11. Wireframes Flutter del usuario vet, lámina 5 de 5. Fuente: elaboración propia.</i></p>
</div>

#### Aplicación Android

##### IAM

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/wireframe-sheets/android-iam-01.jpg" alt="Wireframes Android del módulo IAM, lámina 1 de 1" width="650">
  <p><i>Figura 3.1.4.1.12. Wireframes Android del módulo IAM, lámina 1 de 1. Fuente: elaboración propia.</i></p>
</div>

##### Usuario rancher

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/wireframe-sheets/android-rancher-01.jpg" alt="Wireframes Android del usuario rancher, lámina 1 de 5" width="650">
  <p><i>Figura 3.1.4.1.13. Wireframes Android del usuario rancher, lámina 1 de 5. Fuente: elaboración propia.</i></p>
</div>

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/wireframe-sheets/android-rancher-02.jpg" alt="Wireframes Android del usuario rancher, lámina 2 de 5" width="650">
  <p><i>Figura 3.1.4.1.14. Wireframes Android del usuario rancher, lámina 2 de 5. Fuente: elaboración propia.</i></p>
</div>

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/wireframe-sheets/android-rancher-03.jpg" alt="Wireframes Android del usuario rancher, lámina 3 de 5" width="650">
  <p><i>Figura 3.1.4.1.15. Wireframes Android del usuario rancher, lámina 3 de 5. Fuente: elaboración propia.</i></p>
</div>

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/wireframe-sheets/android-rancher-04.jpg" alt="Wireframes Android del usuario rancher, lámina 4 de 5" width="650">
  <p><i>Figura 3.1.4.1.16. Wireframes Android del usuario rancher, lámina 4 de 5. Fuente: elaboración propia.</i></p>
</div>

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/wireframe-sheets/android-rancher-05.jpg" alt="Wireframes Android del usuario rancher, lámina 5 de 5" width="650">
  <p><i>Figura 3.1.4.1.17. Wireframes Android del usuario rancher, lámina 5 de 5. Fuente: elaboración propia.</i></p>
</div>

##### Usuario veterinario

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/wireframe-sheets/android-vet-01.jpg" alt="Wireframes Android del usuario vet, lámina 1 de 5" width="650">
  <p><i>Figura 3.1.4.1.18. Wireframes Android del usuario vet, lámina 1 de 5. Fuente: elaboración propia.</i></p>
</div>

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/wireframe-sheets/android-vet-02.jpg" alt="Wireframes Android del usuario vet, lámina 2 de 5" width="650">
  <p><i>Figura 3.1.4.1.19. Wireframes Android del usuario vet, lámina 2 de 5. Fuente: elaboración propia.</i></p>
</div>

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/wireframe-sheets/android-vet-03.jpg" alt="Wireframes Android del usuario vet, lámina 3 de 5" width="650">
  <p><i>Figura 3.1.4.1.20. Wireframes Android del usuario vet, lámina 3 de 5. Fuente: elaboración propia.</i></p>
</div>

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/wireframe-sheets/android-vet-04.jpg" alt="Wireframes Android del usuario vet, lámina 4 de 5" width="650">
  <p><i>Figura 3.1.4.1.21. Wireframes Android del usuario vet, lámina 4 de 5. Fuente: elaboración propia.</i></p>
</div>

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/wireframe-sheets/android-vet-05.jpg" alt="Wireframes Android del usuario vet, lámina 5 de 5" width="650">
  <p><i>Figura 3.1.4.1.22. Wireframes Android del usuario vet, lámina 5 de 5. Fuente: elaboración propia.</i></p>
</div>

<a id="toc-3-1-4-2-mobile-applications-wireflow-diagrams"></a>

### 3.1.4.2. Mobile Applications Wireflow Diagrams

Cada wireflow muestra cómo cambia la interfaz después de una acción: La flecha continua representa el *happy path* y las flechas discontinuas rojas, las rutas alternativas (*unhappy paths*); cuando una alternativa no cuenta con una pantalla propia, se representa con un recuadro punteado. Se presenta un wireflow por cada user goal, y por perfil cuando el objetivo lo realizan tanto el ganadero como el veterinario. 

| User goal | Actor | Punto inicial | Pasos principales | Alternativas | Resultado |
|---|---|---|---|---|---|
| Registrarse e iniciar sesión | Ganadero / Veterinario | Bienvenida | Seleccionar rol, ingresar datos y autenticar | Cuenta existente, datos inválidos, error de red | Dashboard del rol |
| Consultar dashboard | Ambos roles | Sesión autenticada | Cargar resumen y abrir módulo | Sin datos, sin conexión o acceso no autorizado | Recurso seleccionado |
| Registrar animal | Ganadero | Lista de animales | Completar datos y guardar | Datos incompletos, duplicado u operación offline | Animal registrado o pendiente |
| Consultar o actualizar animal | Ganadero | Lista o búsqueda | Abrir detalle, revisar y editar | Sin autorización, archivado o error | Información actualizada |
| Consultar historial sanitario | Usuario autorizado | Detalle del animal | Abrir sanidad, filtrar y revisar | Historial vacío o permiso insuficiente | Evento consultado |
| Registrar evento sanitario | Usuario autorizado | Historial | Seleccionar tipo, completar y guardar | Validación, falta de permiso o sin conexión | Evento registrado o pendiente |


##### Wireflow 1. Registrarse e iniciar sesión

**User goal:** Crear mi cuenta con el rol que me corresponde e ingresar a AniTec para llegar a mi dashboard.  
**User Persona:** Jorge Luis Rivas (ganadero) y Valeria Mendoza (médica veterinaria)

El usuario recorre el onboarding de tres pantallas, llega a Registration, elige el tipo de cuenta (Rancher o Veterinarian), completa los datos y accede al dashboard de su rol. Si los datos son inválidos se muestran errores en línea y permanece en el formulario; si ya tiene cuenta, pasa a Sign in; si falla la red, se informa el error y se permite reintentar.

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/wireflow-diagrams/flutter-wireflow-01-registro-e-inicio-de-sesion.png" alt="Wireflow Flutter - Registrarse e iniciar sesión" width="650">
  <p><i>Figura 3.1.4.2.1. Wireflow del user goal «Registrarse e iniciar sesión». Fuente: elaboración propia.</i></p>
</div>

##### Wireflow 2. Consultar dashboard

**User goal:** Ver de un vistazo el estado de mi hato, mis actividades y mis alertas (en el caso de la veterinaria, mis clientes y seguimientos pendientes) y entrar al módulo que necesito.  
**User Persona:** Jorge Luis Rivas (ganadero) y Valeria Mendoza (médica veterinaria)

Con la sesión autenticada, el ganadero llega a su dashboard (animales, actividades y alertas) y abre un módulo desde la barra inferior; el veterinario llega al suyo (clientes y seguimientos) y abre Clients. Las alternativas cubren el primer uso sin datos, la carga del resumen, el trabajo sin conexión (banner offline y acceso al estado de sincronización), la sesión vencida, el servicio no disponible y el acceso no autorizado.

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/wireflow-diagrams/flutter-wireflow-02-consultar-dashboard.png" alt="Wireflow Flutter - Consultar dashboard" width="526">
  <p><i>Figura 3.1.4.2.2. Wireflow del user goal «Consultar dashboard». Fuente: elaboración propia.</i></p>
</div>

##### Wireflow 3. Registrar animal

**User goal:** Registrar un animal nuevo en pocos pasos, incluso cuando estoy en el campo sin conexión.  
**User Persona:** Jorge Luis Rivas (ganadero)

Desde la lista de animales, el ganadero abre el formulario New animal, completa los datos y guarda; el resultado es el detalle del animal registrado. Si la lista está vacía se ofrece crear el primer animal; los campos incompletos o un tag duplicado se señalan en línea; sin conexión el registro se guarda en el dispositivo y queda pendiente de sincronizar; también puede cambiarse a registro masivo (Bulk).

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/wireflow-diagrams/flutter-wireflow-03-registrar-animal.png" alt="Wireflow Flutter - Registrar animal" width="650">
  <p><i>Figura 3.1.4.2.3. Wireflow del user goal «Registrar animal». Fuente: elaboración propia.</i></p>
</div>

##### Wireflow 4. Consultar o actualizar animal

**User goal:** Encontrar un animal, revisar su información y mantenerla actualizada.  
**User Persona:** Jorge Luis Rivas (ganadero)

El ganadero busca o selecciona un animal, revisa su detalle, entra a Edit animal, modifica los datos y guarda; el detalle refleja la información actualizada. Una búsqueda sin coincidencias muestra el estado sin resultados; la falta de autorización o un animal archivado dejan el detalle en solo lectura; los datos inválidos se corrigen antes de guardar y un conflicto de sincronización se resuelve en Sync status (Keep mine / Use server).

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/wireflow-diagrams/flutter-wireflow-04-consultar-o-actualizar-animal.png" alt="Wireflow Flutter - Consultar o actualizar animal" width="650">
  <p><i>Figura 3.1.4.2.4. Wireflow del user goal «Consultar o actualizar animal». Fuente: elaboración propia.</i></p>
</div>

##### Wireflow 5. Consultar historial sanitario

**User goal:** Revisar qué vacunas, tratamientos y controles ha recibido un animal para decidir qué hacer a continuación.  
**User Persona:** Jorge Luis Rivas (ganadero) y Valeria Mendoza (médica veterinaria)

El usuario autorizado abre el historial sanitario del animal (el ganadero desde el detalle del animal; el veterinario desde el detalle del cliente y de su paciente) y revisa el detalle de un registro. Las alternativas son el historial vacío, el animal sin registros, el permiso insuficiente, la copia local sin conexión y el acceso revocado o finalizado por el ganadero.

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/wireflow-diagrams/flutter-wireflow-05-historial-sanitario.png" alt="Wireflow Flutter - Consultar historial sanitario" width="526">
  <p><i>Figura 3.1.4.2.5. Wireflow del user goal «Consultar historial sanitario». Fuente: elaboración propia.</i></p>
</div>

##### Wireflow 6. Registrar evento sanitario

**User goal:** Dejar constancia de un evento de salud: reportar un problema (ganadero) o registrar la visita y su seguimiento (veterinaria).  
**User Persona:** Jorge Luis Rivas (ganadero) y Valeria Mendoza (médica veterinaria)

El ganadero reporta un evento desde el detalle del animal (Report health issue) y el veterinario registra una visita desde el historial del paciente (Record visit); en ambos casos se completa el formulario, se guarda y el evento queda visible en el historial. Los campos obligatorios vacíos se señalan en línea; sin conexión el evento queda guardado localmente y pendiente de sincronizar; sin permiso o con el acceso revocado no se puede registrar; el veterinario puede además programar un seguimiento o descartar los cambios sin guardar.

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/wireflow-diagrams/flutter-wireflow-06-registro-sanitario.png" alt="Wireflow Flutter - Registrar evento sanitario" width="503">
  <p><i>Figura 3.1.4.2.6. Wireflow del user goal «Registrar evento sanitario». Fuente: elaboración propia.</i></p>
</div>


<a id="toc-3-1-4-3-mobile-applications-mock-ups"></a>

### 3.1.4.3. Mobile Applications Mock-ups

Los mock-ups presentan la propuesta visual de las aplicaciones móviles de AniTec y aplican el Design System definido en la sección 3.1.1 a la estructura validada mediante los wireframes. Las pantallas muestran contenido representativo, controles táctiles, navegación y estados de la interfaz para IAM, el usuario rancher y el usuario veterinario. Para facilitar su revisión se organizan por tecnología y perfil funcional.


El diseño editable y completo de pantallas se encuentran en https://www.figma.com/design/uRmjCeeukXUb2AnZ2kFQsA/Anitec-2026-2?node-id=1-2&t=GnQ9UR4xNp7TYaA1-1 

#### Aplicación Flutter

##### IAM

Este conjunto presenta el onboarding, el registro y el inicio de sesión compartidos por los usuarios de la aplicación. La secuencia progresiva reduce la cantidad de información mostrada en cada paso; los formularios emplean etiquetas visibles, jerarquía tipográfica y una acción primaria destacada. 

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/mock-up-sheets/flutter-iam-01.jpg" alt="Mock-ups Flutter del módulo IAM" width="650">
  <p><i>Figura 3.1.4.3.1. Mock-ups Flutter del módulo IAM. Fuente: elaboración propia.</i></p>
</div>

##### Usuario rancher

Las siguientes láminas recorren la experiencia del ganadero: dashboard, animales, actividades, veterinarios, escaneo QR, finanzas, suscripción, configuración y los estados asociados a estas operaciones. El dashboard aplica jerarquía visual para priorizar alertas, indicadores y accesos frecuentes; la navegación agrupa las funciones por tareas del dominio; y las listas combinan etiquetas, búsqueda, filtros y estados.

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/mock-up-sheets/flutter-rancher-01.jpg" alt="Mock-ups Flutter del usuario rancher, lámina 1" width="650">
  <p><i>Figura 3.1.4.3.2. Mock-ups Flutter del usuario rancher, lámina 1 de 5. Fuente: elaboración propia.</i></p>
</div>

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/mock-up-sheets/flutter-rancher-02.jpg" alt="Mock-ups Flutter del usuario rancher, lámina 2" width="650">
  <p><i>Figura 3.1.4.3.3. Mock-ups Flutter del usuario rancher, lámina 2 de 5. Fuente: elaboración propia.</i></p>
</div>

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/mock-up-sheets/flutter-rancher-03.jpg" alt="Mock-ups Flutter del usuario rancher, lámina 3" width="650">
  <p><i>Figura 3.1.4.3.4. Mock-ups Flutter del usuario rancher, lámina 3 de 5. Fuente: elaboración propia.</i></p>
</div>

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/mock-up-sheets/flutter-rancher-04.jpg" alt="Mock-ups Flutter del usuario rancher, lámina 4" width="650">
  <p><i>Figura 3.1.4.3.5. Mock-ups Flutter del usuario rancher, lámina 4 de 5. Fuente: elaboración propia.</i></p>
</div>

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/mock-up-sheets/flutter-rancher-05.jpg" alt="Mock-ups Flutter del usuario rancher, lámina 5" width="650">
  <p><i>Figura 3.1.4.3.6. Mock-ups Flutter del usuario rancher, lámina 5 de 5. Fuente: elaboración propia.</i></p>
</div>

##### Usuario veterinario

Las pantallas del veterinario cubren el dashboard profesional, la gestión de clientes, el historial clínico, el registro y corrección de visitas, el seguimiento, las actividades, los indicadores y la configuración. La arquitectura por audiencia presenta solamente la información autorizada para este rol; los clientes y pacientes se organizan mediante búsqueda, filtros y orden cronológico



<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/mock-up-sheets/flutter-vet-01.jpg" alt="Mock-ups Flutter del usuario vet, lámina 1" width="650">
  <p><i>Figura 3.1.4.3.7. Mock-ups Flutter del usuario vet, lámina 1 de 4. Fuente: elaboración propia.</i></p>
</div>

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/mock-up-sheets/flutter-vet-02.jpg" alt="Mock-ups Flutter del usuario vet, lámina 2" width="650">
  <p><i>Figura 3.1.4.3.8. Mock-ups Flutter del usuario vet, lámina 2 de 4. Fuente: elaboración propia.</i></p>
</div>

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/mock-up-sheets/flutter-vet-03.jpg" alt="Mock-ups Flutter del usuario vet, lámina 3" width="650">
  <p><i>Figura 3.1.4.3.9. Mock-ups Flutter del usuario vet, lámina 3 de 4. Fuente: elaboración propia.</i></p>
</div>

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/mock-up-sheets/flutter-vet-04.jpg" alt="Mock-ups Flutter del usuario vet, lámina 4" width="650">
  <p><i>Figura 3.1.4.3.10. Mock-ups Flutter del usuario vet, lámina 4 de 4. Fuente: elaboración propia.</i></p>
</div>

#### Aplicación Android

##### IAM

La versión Android conserva el mismo alcance funcional del acceso y adapta la presentación a los patrones visuales de Material Design. Mantiene la identidad de AniTec, la jerarquía y las etiquetas del flujo Flutter, pero ajusta campos, botones y controles de navegación a las convenciones de Android para conservar familiaridad y consistencia externa.

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/mock-up-sheets/android-iam-01.jpg" alt="Mock-ups Android del módulo IAM" width="650">
  <p><i>Figura 3.1.4.3.11. Mock-ups Android del módulo IAM. Fuente: elaboración propia.</i></p>
</div>

##### Usuario rancher

Las láminas Android mantienen la secuencia funcional del usuario rancher e incluyen vistas principales, formularios, estados vacíos, confirmaciones, errores y sincronización. La misma arquitectura por tareas permite cambiar de plataforma sin reaprender el producto: Inicio resume la situación del hato, Animals concentra la gestión del ganado, Activities organiza el trabajo y More agrupa funciones de menor frecuencia. Los formularios conservan etiquetas persistentes, acciones principales visibles y mensajes que explican cómo corregir o reintentar.

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/mock-up-sheets/android-rancher-01.jpg" alt="Mock-ups Android del usuario rancher, lámina 1" width="650">
  <p><i>Figura 3.1.4.3.12. Mock-ups Android del usuario rancher, lámina 1 de 5. Fuente: elaboración propia.</i></p>
</div>

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/mock-up-sheets/android-rancher-02.jpg" alt="Mock-ups Android del usuario rancher, lámina 2" width="650">
  <p><i>Figura 3.1.4.3.13. Mock-ups Android del usuario rancher, lámina 2 de 5. Fuente: elaboración propia.</i></p>
</div>

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/mock-up-sheets/android-rancher-03.jpg" alt="Mock-ups Android del usuario rancher, lámina 3" width="650">
  <p><i>Figura 3.1.4.3.14. Mock-ups Android del usuario rancher, lámina 3 de 5. Fuente: elaboración propia.</i></p>
</div>

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/mock-up-sheets/android-rancher-04.jpg" alt="Mock-ups Android del usuario rancher, lámina 4" width="650">
  <p><i>Figura 3.1.4.3.15. Mock-ups Android del usuario rancher, lámina 4 de 5. Fuente: elaboración propia.</i></p>
</div>

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/mock-up-sheets/android-rancher-05.jpg" alt="Mock-ups Android del usuario rancher, lámina 5" width="650">
  <p><i>Figura 3.1.4.3.16. Mock-ups Android del usuario rancher, lámina 5 de 5. Fuente: elaboración propia.</i></p>
</div>

##### Usuario veterinario

La versión Android del perfil veterinario documenta la gestión de clientes y visitas, los estados operativos, los indicadores, el escaneo, las notificaciones y las opciones de cuenta. El dashboard prioriza clientes, visitas y seguimientos; los historiales siguen una organización cronológica; y las pantallas de autorización, validación y estados vacíos combinan iconografía, texto y acciones de recuperación. Así, la adaptación a Android conserva tanto el Design System como los criterios de inclusión y arquitectura de información definidos para AniTec.

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/mock-up-sheets/android-vet-01.jpg" alt="Mock-ups Android del usuario vet, lámina 1" width="650">
  <p><i>Figura 3.1.4.3.17. Mock-ups Android del usuario vet, lámina 1 de 4. Fuente: elaboración propia.</i></p>
</div>

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/mock-up-sheets/android-vet-02.jpg" alt="Mock-ups Android del usuario vet, lámina 2" width="650">
  <p><i>Figura 3.1.4.3.18. Mock-ups Android del usuario vet, lámina 2 de 4. Fuente: elaboración propia.</i></p>
</div>

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/mock-up-sheets/android-vet-03.jpg" alt="Mock-ups Android del usuario vet, lámina 3" width="650">
  <p><i>Figura 3.1.4.3.19. Mock-ups Android del usuario vet, lámina 3 de 4. Fuente: elaboración propia.</i></p>
</div>

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/mock-up-sheets/android-vet-04.jpg" alt="Mock-ups Android del usuario vet, lámina 4" width="650">
  <p><i>Figura 3.1.4.3.20. Mock-ups Android del usuario vet, lámina 4 de 4. Fuente: elaboración propia.</i></p>
</div>

<a id="toc-3-1-4-4-mobile-applications-user-flow-diagrams"></a>

### 3.1.4.4. Mobile Applications User Flow Diagrams

Los User Flow Diagrams presentan la navegación propuesta para alcanzar cada user goal definido. Se establece un único flujo estándar por objetivo, aplicable tanto a Android como a Flutter, porque ambas implementaciones comparten la misma arquitectura de información, las mismas acciones esenciales y las mismas condiciones de recuperación. Los diagramas se derivan de los wireflows y emplean mock-ups representativos de las vistas involucradas. Para conservar la legibilidad, cada lámina resume el recorrido en tres pantallas principales y concentra las condiciones secundarias en bloques breves; su explicación detallada se mantiene en el texto. La línea verde continua representa el *happy path*; la línea roja discontinua representa los *unhappy paths* que requieren corrección, reintento o recuperación; y la línea ámbar discontinua identifica una ruta alternativa válida que no constituye un error.

| User goal | Happy path | Unhappy paths | Relación |
|---|---|---|---|
| Registro e inicio de sesión | Datos válidos y dashboard | Datos inválidos, cuenta existente, credenciales incorrectas y sin red | US-004, US-005, US-006 |
| Dashboard | Resumen disponible y acceso a módulo | Sin datos, sesión vencida y error del servicio | US-007 y flujos del rol |
| Registro de animal | Formulario válido y confirmación | Campos faltantes, duplicado, servidor y guardado offline | US-011, TS-004, TS-005 |
| Consulta y actualización | Recurso autorizado y actualización | Sin permiso, inexistente y conflicto de sincronización | US-010, US-012, US-013 |
| Historial sanitario | Historial disponible | Historial vacío, filtro sin resultados y acceso denegado | US-014 |
| Registro sanitario | Datos válidos y confirmación | Validación, permiso insuficiente y sin conexión | US-015 |

#### User Flow 1. Registrarse e iniciar sesión

**User goal:** Crear mi cuenta con el rol que me corresponde e ingresar a AniTec para llegar a mi dashboard.  
**User Persona:** Jorge Luis Rivas (ganadero) y Valeria Mendoza (médica veterinaria).

Este flujo se deriva del Wireflow 1. En el *happy path*, la persona recorre el onboarding, elige crear una cuenta o iniciar sesión, completa los datos requeridos y llega al dashboard correspondiente a su rol. Si el registro contiene datos inválidos, se mantienen los valores ingresados y se señalan los campos por corregir. Una cuenta existente conduce a Sign in como ruta alternativa válida. Las credenciales incorrectas permiten reintentar y un fallo de conexión conserva el contexto antes de volver a enviar la solicitud.


<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/user-flow-diagrams/user-flow-01-registro-inicio-sesion.png" alt="User Flow estándar para registrarse e iniciar sesión" width="650">
  <p><i>Figura 3.1.4.4.1. User Flow para registrarse e iniciar sesión. Fuente: elaboración propia.</i></p>
</div>

#### User Flow 2. Consultar dashboard

**User goal:** Ver de un vistazo el estado de mi hato, mis actividades y mis alertas o, para la veterinaria, mis clientes y seguimientos pendientes, y entrar al módulo que necesito.  
**User Persona:** Jorge Luis Rivas (ganadero) y Valeria Mendoza (médica veterinaria).

Este flujo se deriva del Wireflow 2. El *happy path* parte de una sesión autenticada, carga el dashboard ajustado al rol y continúa al módulo elegido desde la navegación. En el primer uso se muestra una llamada a crear la primera finca o agregar el primer cliente; durante la carga se conservan estructuras que anticipan el contenido. Sin conexión se informa el uso de datos locales; una sesión vencida solicita autenticación y los errores de servicio o autorización ofrecen reintento o recuperación de acceso.

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/user-flow-diagrams/user-flow-02-consultar-dashboard.png" alt="User Flow estándar para consultar el dashboard" width="650">
  <p><i>Figura 3.1.4.4.2. User Flow para consultar el dashboard. Fuente: elaboración propia.</i></p>
</div>


#### User Flow 3. Registrar animal

**User goal:** Registrar un animal nuevo en pocos pasos, incluso cuando estoy en el campo sin conexión.  
**User Persona:** Jorge Luis Rivas (ganadero).

Este flujo se deriva del Wireflow 3. En la ruta esperada, Jorge abre Animals, toca la acción de nuevo registro, completa el formulario, guarda y revisa el detalle creado. Si la lista está vacía se ofrece registrar el primer animal. Los campos incompletos o un tag duplicado mantienen el formulario abierto con mensajes de corrección; sin conexión el registro queda pendiente en Sync status. El formulario Bulk constituye una alternativa válida cuando necesita registrar varios animales.

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/user-flow-diagrams/user-flow-03-registrar-animal.png" alt="User Flow estándar para registrar un animal" width="650">
  <p><i>Figura 3.1.4.4.3. User Flow para registrar un animal. Fuente: elaboración propia.</i></p>
</div>

#### User Flow 4. Consultar o actualizar animal

**User goal:** Encontrar un animal, revisar su información y mantenerla actualizada.  
**User Persona:** Jorge Luis Rivas (ganadero).

Este flujo se deriva del Wireflow 4. El *happy path* comienza con la búsqueda o selección de un animal, continúa con la revisión del detalle y la edición y termina mostrando los datos actualizados. Una búsqueda sin coincidencias permite limpiar los filtros; la falta de autorización o el estado archivado mantienen el recurso en solo lectura. Los datos inválidos se corrigen antes de guardar y los conflictos de sincronización se resuelven eligiendo entre la versión local y la versión del servidor.

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/user-flow-diagrams/user-flow-04-consultar-actualizar-animal.png" alt="User Flow estándar para consultar o actualizar un animal" width="650">
  <p><i>Figura 3.1.4.4.4. User Flow para consultar o actualizar un animal. Fuente: elaboración propia.</i></p>
</div>

#### User Flow 5. Consultar historial sanitario

**User goal:** Revisar qué vacunas, tratamientos y controles ha recibido un animal para decidir qué hacer a continuación.  
**User Persona:** Jorge Luis Rivas (ganadero) y Valeria Mendoza (médica veterinaria).

Este flujo se deriva del Wireflow 5 y muestra los puntos de entrada de ambos perfiles. Jorge parte del detalle del animal y Valeria del cliente o paciente autorizado; ambos abren Health history y seleccionan un registro. Si no existen antecedentes, se ofrece crear el primero; si una búsqueda no devuelve resultados, se modifican sus criterios. El contenido protegido no se muestra sin permiso, la copia local se identifica como potencialmente desactualizada y un acceso revocado finaliza la consulta indicando cómo solicitar una nueva autorización.

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/user-flow-diagrams/user-flow-05-historial-sanitario.png" alt="User Flow estándar para consultar el historial sanitario" width="650">
  <p><i>Figura 3.1.4.4.5. User Flow para consultar el historial sanitario. Fuente: elaboración propia.</i></p>
</div>

#### User Flow 6. Registrar evento sanitario

**User goal:** Dejar constancia de un evento de salud: reportar un problema como ganadero o registrar la visita y su seguimiento como veterinaria.  
**User Persona:** Jorge Luis Rivas (ganadero) y Valeria Mendoza (médica veterinaria).

Este flujo se deriva del Wireflow 6. Jorge utiliza Report health issue desde el detalle del animal y Valeria utiliza Record visit desde el historial del paciente; ambos completan los datos, guardan y comprueban que el evento aparezca en el historial. Los campos obligatorios vacíos mantienen el formulario abierto, el trabajo sin conexión guarda una copia pendiente y un permiso revocado bloquea el registro. Antes de salir sin guardar se solicita confirmación. Como ruta alternativa válida, Valeria puede programar un seguimiento posterior a la visita.

<div align="center" style="page-break-inside: avoid;">
  <img src="../../assets/chapter-3/user-flow-diagrams/user-flow-06-registrar-evento-sanitario.png" alt="User Flow estándar para registrar un evento sanitario" width="650">
  <p><i>Figura 3.1.4.4.6. User Flow para registrar un evento sanitario. Fuente: elaboración propia.</i></p>
</div>

<a id="toc-3-1-4-5-mobile-applications-prototyping"></a>

### 3.1.4.5. Mobile Applications Prototyping

Los prototipos simularán la navegación de los User Flow Diagrams y permitirán comprobar etiquetas, acciones, retroalimentación, recuperación ante errores y consistencia.

| Usuario | Prototipo Evidencia | Captura del video | Video en Microsoft Stream |
|---|---|---|---|
| Ganadero | <img src="../../assets/chapter-3/prototypingFigmaEvidence.png" width="650">| <img src="../../assets/chapter-3/prototyping.png" width="650">  | https://upcedupe-my.sharepoint.com/:v:/g/personal/u202215979_upc_edu_pe/IQAoOjKIja11SZkyivBWNnFHAfqWrhmYFjAEtX8G3aZOCPE?e=nkIv3O | 
| Veterinario | <img src="../../assets/chapter-3/prototypingFigmaEvidenceVet.png" width="650"> | <img src="../../assets/chapter-3/prototypingVet.png" width="650"> | https://upcedupe-my.sharepoint.com/:v:/g/personal/u202215979_upc_edu_pe/IQC1i57fMYVmS5YQVocXyarQAfhuAk37q3v1QPCuDFJ7Yyw?e=KRkjwP | 

