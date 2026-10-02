<a id="toc-4-1-software-configuration-management"></a>

# 4.1. Software Configuration Management

La gestión de configuración de AniTec define las herramientas, repositorios, convenciones y procesos de publicación que permiten trabajar sobre la Landing Page, la API REST y las aplicaciones móviles de manera consistente y trazable.

<a id="toc-4-1-1-software-development-environment-configuration"></a>

## 4.1.1. Software Development Environment Configuration

Las herramientas se agrupan según la actividad que soportan. Todo integrante deberá utilizar versiones compatibles con los repositorios y registrar cualquier cambio de versión que afecte la compilación.

**Project and Requirements Management**

| Herramienta | Propósito | Referencia |
|---|---|---|
| Trello | Organizar Product Backlog, Sprint Backlog y estados de tareas. | <https://trello.com> |
| GitHub Issues / Projects | Dar trazabilidad a incidencias, cambios y trabajo del repositorio. | <https://github.com/features/issues> |
| Gherkin | Especificar criterios de aceptación y escenarios BDD. | <https://cucumber.io/docs/gherkin/> |
| Miro | Modelar EventStorming y flujos colaborativos. | <https://miro.com> |

**Product UX/UI Design**

| Herramienta | Propósito | Referencia |
|---|---|---|
| Figma | Elaborar wireframes, mock-ups, wireflows, user flows y prototipos. | <https://www.figma.com> |
| Canva | Preparar recursos visuales complementarios. | <https://www.canva.com> |
| Lucidchart | Modelar flujos y diagramas auxiliares. | <https://www.lucidchart.com> |

**Software Development**

| Herramienta o tecnología | Propósito | Versión / estado |
|---|---|---|
| Git y GitHub | Control de versiones y colaboración. | Versión estable compatible |
| Visual Studio Code | Landing Page, documentación y edición general. | Versión estable |
| Rider / Visual Studio | Desarrollo de la API ASP.NET Core. | Compatible con .NET SDK 10.0.x (SDK instalado: 10.0.401) |
| .NET SDK | Compilar y ejecutar el backend (`global.json`). | 10.0.0 (`rollForward: latestMajor`) |
| ASP.NET Core | Exponer servicios REST y OpenAPI (`TargetFramework`). | `net10.0` |
| Entity Framework Core | Persistencia y migraciones. | 10.0.8 |
| MySql.EntityFrameworkCore | Proveedor MySQL para EF Core. | 10.0.7 |
| Swashbuckle.AspNetCore | Documentación OpenAPI / Swagger UI. | 10.2.0 |
| System.IdentityModel.Tokens.Jwt / JwtBearer | Emisión y validación de JWT. | 8.18.0 / 10.0.8 |
| BCrypt.Net-Next | Hash de contraseñas. | 4.2.0 |
| Docker | Empaquetar y publicar la API en Render (`Dockerfile`). | Imágenes `mcr.microsoft.com/dotnet/sdk:10.0` y `aspnet:10.0` |
| Postman / Swagger UI | Probar contratos HTTP de la API. | Swagger UI del servicio desplegado |
| MySQL / MySQL Workbench | Persistencia central y administración de datos. | Compatible con MySql.EntityFrameworkCore 10.0.7 |
| Android Studio | Desarrollo, emulación y depuración Android. | Koala Feature Drop (2024.1.2) o superior |
| Kotlin | Implementar la aplicación Android nativa. | 2.0.0 |
| Jetpack Compose | Construir la interfaz Android. | Compose BOM 2024.06.00 |
| Flutter SDK y Dart | Implementar la aplicación multiplataforma. | Flutter 3.22.0 / Dart 3.4.0 |

**Software Testing**

| Producto | Herramientas previstas | Tipo de comprobación |
|---|---|---|
| Backend | xUnit, Swagger UI y cliente HTTP | Unitarias, contratos HTTP y ejecución exploratoria |
| Android | JUnit 4, Compose UI Test, KotlinX Coroutines Test y Android Emulator | Unitarias (ViewModels/UseCases) e interfaz/instrumentadas (Room DAOs) |
| Flutter | flutter_test e integration_test | Unitarias, widgets e integración |
| API | Swagger UI (Swashbuckle) y cliente HTTP controlado | Contratos y ejecución exploratoria |
| Landing Page | DevTools, Lighthouse y validadores web | Responsive, accesibilidad y desempeño |

**Deployment and Documentation**

| Herramienta | Propósito | Referencia |
|---|---|---|
| GitHub Pages | Publicar la Landing Page. | <https://pages.github.com> |
| Render | Publicar la API REST. | <https://render.com> |
| Firebase App Distribution | Distribuir builds móviles para validación. | <https://firebase.google.com/docs/app-distribution> |
| Swagger / OpenAPI | Documentar y probar endpoints. | <https://swagger.io/specification/> |
| Structurizr | Mantener los diagramas C4. | <https://structurizr.com> |
| PlantUML | Mantener diagramas de clases. | <https://plantuml.com> |

<a id="toc-4-1-2-source-code-management"></a>

## 4.1.2. Source Code Management

GitHub es la plataforma central de versionado. Los repositorios vigentes son:

| Producto | Repositorio |
|---|---|
| Informe | <https://github.com/ADM-1ACC0238-2620-13975-Grupo01/Informe> |
| Landing Page | <https://github.com/ADM-1ACC0238-2620-13975-Grupo01/anitec-landing-page> |
| Web Services | <https://github.com/ADM-1ACC0238-2620-13975-Grupo01/anitec-backend> |
| Android nativo | **Pendiente de completar:** URL del repositorio Android |
| Aplicación Flutter | **Pendiente de completar:** URL del repositorio Flutter |

**GitFlow**

- `main`: versiones estables y entregables.
- `develop`: integración del trabajo aprobado para la siguiente versión.
- `feature/<scope>-<description>`: desarrollo de una funcionalidad o artefacto.
- `release/<version>`: estabilización de una versión candidata.
- `hotfix/<description>`: corrección urgente originada desde `main`.

Cada Pull Request indicará propósito, cambios, evidencia de verificación y User Story relacionada. La integración requerirá revisión y comprobaciones correspondientes al producto.

**Semantic Versioning.** Las versiones seguirán `MAJOR.MINOR.PATCH`: MAJOR para cambios incompatibles, MINOR para funcionalidad compatible y PATCH para correcciones compatibles.

**Conventional Commits.** Se utilizará `type(scope): description`, con descripciones breves en inglés. Tipos principales: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `build`, `ci` y `chore`.

<a id="toc-4-1-3-source-code-style-guide-conventions"></a>

## 4.1.3. Source Code Style Guide & Conventions

El código fuente, nombres técnicos, rutas y mensajes de commit se redactarán en inglés. Las clases y funciones tendrán responsabilidades claras y se mantendrá la separación por capas y bounded contexts definida en el capítulo II.

| Tecnología | Convenciones principales |
|---|---|
| HTML y CSS | HTML semántico, atributos de accesibilidad, indentación de dos espacios y clases `kebab-case`. |
| JavaScript | Variables y funciones `camelCase`, constantes descriptivas, módulos pequeños y uso de `async/await`. |
| Kotlin | Google Kotlin Style Guide; tipos y composables `PascalCase`, funciones y propiedades `camelCase`, paquetes en minúsculas. |
| Jetpack Compose | Composables pequeños, estado elevado cuando corresponda, previews representativas y recursos fuera del código. |
| Dart | Effective Dart; tipos `UpperCamelCase`, miembros `lowerCamelCase`, archivos `lowercase_with_underscores`. |
| Flutter | Widgets pequeños, separación de presentación y estado, temas centralizados y textos localizables. |
| C# | Convenciones Microsoft ([C# Coding Conventions](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions)); tipos, métodos y propiedades `PascalCase`, parámetros `camelCase` y campos privados `_camelCase`. Controllers: `*Controller` en `Interfaces/Rest`. Resources (DTOs): `*Resource` y assemblers `*FromResourceAssembler` / `*FromEntityAssembler`. Commands y Queries: `Create*Command`, `Get*Query` en `Domain/Model`. Rutas en minúsculas bajo `api/v1/...` (p. ej. `api/v1/authentication/sign-in`, `api/v1/animals`). Estructura por bounded context (`Iam`, `Livestock`, `Sanitary`, …) con capas `Domain`, `Application`, `Infrastructure` e `Interfaces`. Errores HTTP vía Problem Details y validaciones en controllers/services. |
| REST / OpenAPI | Sustantivos plurales en rutas, verbos HTTP correctos, resources/DTOs, códigos de estado y respuestas de error consistentes. Documentación con Swashbuckle (`AddSwaggerGen`, anotaciones `[SwaggerOperation]` / `[SwaggerResponse]`) y esquema Bearer JWT. |
| Gherkin | Features y escenarios ligados a User Stories, pasos declarativos y estructura Given–When–Then. |

**Reglas compartidas**

- No incluir secretos, tokens ni cadenas de conexión en el repositorio.
- Centralizar textos para i18n en lugar de escribirlos directamente en vistas.
- Documentar interfaces públicas y decisiones no evidentes.
- Evitar duplicar reglas de negocio entre UI y API; el backend conserva las reglas autoritativas.
- Incluir pruebas para reglas o flujos incorporados durante el sprint.

<a id="toc-4-1-4-software-deployment-configuration"></a>

## 4.1.4. Software Deployment Configuration

Cada producto se configura y publica de manera independiente, pero las aplicaciones móviles consumen la misma API mediante HTTPS y contratos documentados en OpenAPI.

**Landing Page — GitHub Pages**

1. Integrar el contenido aprobado en `main`.
2. Ejecutar las comprobaciones y el proceso de construcción si corresponde.
3. Configurar GitHub Pages con la rama o workflow definido.
4. verificar navegación, recursos, responsive, i18n y accesibilidad desde la URL pública.

**Web Services — Render**

El backend se publica desde el repositorio <https://github.com/ADM-1ACC0238-2620-13975-Grupo01/anitec-backend> mediante Docker. El `Dockerfile` en la raíz del repo:

1. Construir con la imagen `mcr.microsoft.com/dotnet/sdk:10.0`, restaurar y publicar `Anitec.Platform/Anitec.Platform.csproj` en Release.
2. Ejecutar con la imagen `mcr.microsoft.com/dotnet/aspnet:10.0`, exponer el puerto `8080` y definir `ASPNETCORE_URLS=http://0.0.0.0:8080`.
3. En Render, conectar el repositorio, seleccionar despliegue por Docker (o build equivalente) y mapear el puerto del servicio.
4. Configurar variables de entorno / secretos (valores no publicados en el informe):
   - `ConnectionStrings__DefaultConnection` (o `ANITEC_CONNECTION_STRING` para migraciones)
   - `TokenSettings__Secret`
   - `StripeSettings__SecretKey`, `StripeSettings__WebhookSecret`, `StripeSettings__SuccessUrl`, `StripeSettings__CancelUrl` (si aplica el módulo de suscripciones)
   - `ASPNETCORE_ENVIRONMENT` (p. ej. `Production`)
5. Verificar salud del servicio, persistencia MySQL y documentación en `/swagger`.

**Android y Flutter — Firebase App Distribution**

1. Crear o vincular el proyecto Firebase y registrar cada aplicación.
2. Configurar identificadores, firma de builds y variables de ambiente.
3. Generar un artefacto instalable de prueba desde una versión trazable.
4. Publicar el build para el grupo autorizado de testers.
5. Registrar versión, commit, fecha, notas y resultados de instalación.

| Producto | Entorno / servicio | URL o identificador | Estado |
|---|---|---|---|
| Landing Page | GitHub Pages | **Pendiente de confirmar:** URL vigente | Pendiente de evidencia TB1 |
| Web Services | Render | API: <https://anitec-backend.onrender.com> · Swagger: <https://anitec-backend.onrender.com/swagger/index.html> | Live — evidencia en figuras 4.1.4.2 y 4.1.4.3 |
| Android | Firebase App Distribution | **Pendiente:** App ID, release y grupo de testers | Pendiente |
| Flutter | Firebase App Distribution | **Pendiente:** App ID, plataformas y release | Pendiente |

El diagrama de despliegue muestra los dispositivos, productos, servicios externos y relaciones necesarias para ejecutar AniTec.

<div align="center">
  <img src="../../assets/chapter-2/AniTec-Deployment.svg" alt="Diagrama C4 de despliegue de AniTec" width="900">
  <p><i>Figura 4.1.4.1. Software Architecture Deployment Diagram. Fuente: elaboración propia con Structurizr DSL.</i></p>
</div>

La evidencia siguiente corresponde al Web Service publicado en Render. Las variables se muestran con valores ocultos; no se incluyen secretos en el informe.

<div align="center">
  <img src="../../assets/chapter-4/backend/render-backend-live.png" width="800">
  <p><i>Figura 4.1.4.2. Servicio anitec-backend en Render con estado Live y URL pública. Fuente: elaboración propia (captura de Render).</i></p>
</div>

La captura confirma el despliegue Docker del backend, el plan Free y la disponibilidad en `https://anitec-backend.onrender.com`.

<div align="center">
  <img src="../../assets/chapter-4/backend/render-backend-environment.png" width="800">
  <p><i>Figura 4.1.4.3. Variables de entorno del backend en Render (valores ocultos): ASPNETCORE_ENVIRONMENT, ConnectionStrings__DefaultConnection, TokenSettings__Secret y StripeSettings. Fuente: elaboración propia (captura de Render).</i></p>
</div>

La configuración de secretos se mantiene fuera del repositorio GitHub y se administra en el panel Environment de Render.

> **Pendiente de completar:** capturas de Landing Page, Android y Flutter por parte de sus responsables.
