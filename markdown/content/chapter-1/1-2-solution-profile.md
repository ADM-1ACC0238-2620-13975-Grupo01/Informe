# 1.2. Solution Profile

## 1.2.1. Antecedentes y problemática

**Qué (What)**

_¿Cuál es la situación problemática?_

Los pequeños y medianos ganaderos suelen distribuir la información de sus animales entre cuadernos, hojas sueltas, archivos y mensajes. Esto dificulta mantener historiales completos, encontrar datos durante una atención, recordar actividades sanitarias y compartir información confiable con el veterinario. La aplicación web tomada como base centraliza parte de esos datos, pero no cubre por sí sola la necesidad de registrar y consultar información mientras el usuario se desplaza por el campo.

**Cuándo (When)**

_¿Cuándo ocurre el problema?_

El problema aparece durante todo el ciclo de manejo del animal: registro o nacimiento, vacunaciones, tratamientos, controles, reproducción, cambios productivos y venta. Se vuelve especialmente crítico cuando una actividad debe registrarse en el momento o cuando se necesita consultar el historial para decidir una atención.

**Dónde (Where)**

_¿Dónde se manifiesta y dónde se origina?_

Se manifiesta en unidades ganaderas rurales y semiurbanas, durante recorridos de campo y atenciones veterinarias. En estos entornos puede haber acceso limitado a una computadora y conectividad móvil intermitente, por lo que depender exclusivamente de una aplicación web o de una conexión constante interrumpe el flujo de trabajo.

**Quién (Who)**

_¿Quiénes participan y quiénes usarán la solución?_

Los usuarios principales serán pequeños y medianos ganaderos responsables del manejo cotidiano del hato y veterinarios de campo que necesitan consultar antecedentes y registrar atenciones. Asociaciones, cooperativas y entidades del sector son actores relacionados, pero no constituyen los segmentos de usuario priorizados para la primera versión.

**Por qué (Why)**

_¿Cuál es la causa principal del problema?_

Las herramientas disponibles no siempre se ajustan a la movilidad del trabajo ganadero, al nivel de experiencia digital de los usuarios ni a las restricciones de conectividad. Como consecuencia, el registro se posterga, la información queda incompleta o dispersa y la coordinación entre ganadero y veterinario depende de comunicaciones informales.

**Cómo (How)**

_¿Cómo se implementará la solución?_

AniTec extenderá el producto web existente con una aplicación nativa Android desarrollada con Kotlin y una aplicación multiplataforma cuya tecnología se elegirá mediante evaluación técnica. Las aplicaciones consumirán la API REST propia y permitirán registrar animales y eventos, consultar historiales, recibir notificaciones, utilizar la cámara, revisar indicadores y conservar temporalmente datos o borradores en el dispositivo.

_¿Cómo se logrará una experiencia útil en campo?_

Se diseñarán flujos breves, formularios con validación, estados claros de sincronización y alternativas manuales cuando una función del dispositivo no esté disponible. La solución considerará accesibilidad, internacionalización, seguridad de acceso y pruebas en dispositivos físicos bajo distintas condiciones de conectividad.

**Cuánto (How much)**

_¿Cuál es la magnitud del contexto?_

El IV Censo Nacional Agropecuario registró 2 199 243 productores agropecuarios como personas naturales y señaló que el 79,6 % tenía unidades de menos de cinco hectáreas (INEI, 2014). Además, durante el primer trimestre de 2025 solo el 20,5 % de los hogares rurales disponía de Internet en el hogar (INEI, 2025a). Estas cifras no cuantifican por sí solas el mercado de AniTec, pero muestran la escala de la pequeña producción agropecuaria y la necesidad de diseñar para un entorno de conectividad restringida.

### Descripción consolidada de los antecedentes y la problemática

AniTec parte de una aplicación web creada en un curso anterior. El reto actual consiste en adaptar y ampliar esa solución para el uso móvil, sin limitarse a reproducir sus pantallas. El teléfono debe convertirse en la herramienta de trabajo inmediata del ganadero y del veterinario: permitir el registro en el lugar donde ocurre el evento, presentar la información relevante con rapidez y tolerar interrupciones de red.

La propuesta comprenderá una landing page, una API REST propia, una aplicación Android nativa y una experiencia multiplataforma. El alcance inicial priorizará la gestión de animales e historiales sanitarios, el trabajo local y la posterior sincronización, las notificaciones, el uso de cámara, los indicadores de seguimiento y la colaboración autorizada con veterinarios. Las integraciones complementarias, como pagos o una capacidad autónoma basada en una tecnología nueva para el equipo, se incorporarán después de validar su viabilidad y su aporte al usuario.

El objetivo del proyecto es reducir la pérdida y fragmentación de información, facilitar el cumplimiento de actividades sanitarias y mejorar el acceso al historial del animal durante el trabajo de campo. La solución deberá mantener coherencia entre plataformas, proteger los datos, comunicar los estados de conexión y funcionar de manera comprensible para usuarios con distintos niveles de experiencia digital.

## 1.2.2. Lean UX Process

Las siguientes declaraciones representan supuestos que deberán comprobarse mediante entrevistas, prototipos, pruebas de usabilidad y evidencia de uso. Los porcentajes y tiempos indicados son criterios preliminares de validación y no resultados alcanzados.

### 1.2.2.1. Lean UX Problem Statements

**Problem Statement**

Los pequeños y medianos ganaderos y los veterinarios de campo necesitan registrar y consultar información confiable de los animales mientras realizan sus actividades, porque los apuntes dispersos y una solución dependiente de una computadora o de conexión continua dificultan actualizar historiales, recordar tareas sanitarias y coordinar el seguimiento. AniTec abordará esta necesidad mediante aplicaciones móviles simples, accesibles y conectadas con su API, con soporte para almacenamiento local, notificaciones y capacidades del dispositivo.

El enfoque inicial estará en los flujos de registro y consulta de animales, historial sanitario, recordatorios y seguimiento veterinario. Consideraremos validado el problema si, durante un piloto de cuatro semanas, al menos el 70 % de los participantes utiliza semanalmente los flujos principales, al menos el 80 % completa las tareas esenciales sin ayuda y el tiempo promedio para encontrar un antecedente sanitario disminuye en un 30 % frente a su método actual.

### 1.2.2.2. Lean UX Assumptions

#### Business Assumptions

1. Creemos que existe una necesidad por una herramienta móvil que centralice la información del ganado y pueda utilizarse durante el trabajo de campo.
2. Creemos que los primeros usuarios serán pequeños y medianos ganaderos y veterinarios que actualmente usan registros manuales o información digital dispersa.
3. Creemos que podremos llegar a ellos mediante asociaciones ganaderas, redes de profesionales veterinarios, demostraciones de campo y la landing page.
4. Creemos que un modelo de planes podrá sostener el servicio si las funciones pagadas ofrecen un beneficio comprobable y el proceso de pago inspira confianza.
5. Creemos que los principales riesgos de adopción son la conectividad inestable, la poca experiencia digital, el esfuerzo inicial de registrar animales y la preocupación por la privacidad de los datos.

#### Business Outcome Assumptions

1. Esperamos aumentar la activación de usuarios que completan el registro de su primer animal.
2. Esperamos lograr uso semanal recurrente de los flujos de animales, historial y recordatorios.
3. Esperamos reducir el abandono causado por errores de conexión o formularios extensos.
4. Esperamos que ganaderos y veterinarios encuentren suficiente valor para recomendar AniTec.
5. Esperamos identificar, mediante la validación de planes y pagos, qué capacidades justifican una suscripción.

#### User Assumptions

1. Los ganaderos llevan el teléfono durante parte de sus actividades y pueden usarlo para registrar un evento breve.
2. Los ganaderos necesitan identificar con rapidez al animal y consultar su historial.
3. Los veterinarios atienden a más de un cliente y requieren acceso autorizado a información actualizada.
4. Ambos segmentos tienen distintos niveles de experiencia digital y necesitan lenguaje directo, navegación consistente y ayuda contextual.
5. Parte de los usuarios trabaja con conectividad intermitente y necesita conservar el progreso hasta recuperar la conexión.

#### User Outcome and Benefit Assumptions

1. Los ganaderos reducirán el tiempo dedicado a buscar información de un animal.
2. Los recordatorios les ayudarán a cumplir actividades sanitarias pendientes.
3. El almacenamiento local evitará repetir registros cuando falle la conexión.
4. Los resúmenes visuales les permitirán detectar pendientes y cambios relevantes.
5. Los veterinarios podrán brindar continuidad a la atención al consultar antecedentes y registrar eventos autorizados.

#### Feature Assumptions

1. Un registro móvil centralizado de animales e historiales reducirá la dispersión de información.
2. El almacenamiento local de datos esenciales y borradores permitirá continuar tareas con conectividad inestable.
3. Las notificaciones programadas ayudarán a recordar vacunaciones, tratamientos y controles.
4. La identificación asistida por cámara, acompañada de búsqueda manual, reducirá el tiempo para localizar un animal.
5. Los resúmenes visuales facilitarán la interpretación del estado sanitario y productivo.
6. Un espacio de seguimiento veterinario con permisos explícitos mejorará la coordinación con el ganadero.
7. Un flujo de planes conectado con un servicio externo de pagos permitirá validar la disposición de pago sin almacenar información bancaria sensible en AniTec.

### 1.2.2.3. Lean UX Hypothesis Statements

**Hypothesis Statement 01: registro móvil centralizado**

Creemos que lograremos que al menos el 70 % de los participantes registre o consulte información cada semana si los pequeños y medianos ganaderos pueden gestionar animales e historiales mediante flujos móviles breves. Lo comprobaremos durante un piloto de cuatro semanas mediante analítica de uso y entrevistas de seguimiento.

**Hypothesis Statement 02: continuidad con conectividad inestable**

Creemos que reduciremos en al menos un 50 % las tareas abandonadas por problemas de red si los usuarios pueden guardar localmente datos esenciales o borradores y sincronizarlos después. Lo comprobaremos con pruebas en condiciones de conexión estable, lenta e interrumpida.

**Hypothesis Statement 03: recordatorios**

Creemos que aumentaremos el cumplimiento de actividades sanitarias si los ganaderos reciben notificaciones claras y oportunas. Lo comprobaremos si al menos el 70 % de los recordatorios del piloto se marca como atendido o reprogramado y los participantes declaran que la alerta fue útil.

**Hypothesis Statement 04: identificación asistida por cámara**

Creemos que reduciremos en un 30 % el tiempo necesario para encontrar la ficha de un animal si el usuario puede iniciar su identificación con la cámara y dispone de búsqueda manual cuando esta opción no funciona. Lo comprobaremos comparando tiempos y errores en pruebas de tareas.

**Hypothesis Statement 05: resúmenes visuales**

Creemos que mejoraremos la comprensión del estado del hato si los ganaderos reciben indicadores simples y accionables. Lo comprobaremos si al menos el 80 % interpreta correctamente los indicadores principales en pruebas de usabilidad.

**Hypothesis Statement 06: seguimiento veterinario autorizado**

Creemos que reduciremos el tiempo de consulta de antecedentes y mejoraremos la continuidad de la atención si los veterinarios acceden, con autorización, al historial de los animales de sus clientes. Lo comprobaremos si al menos el 80 % completa la consulta y el registro de una atención sin ayuda.

**Hypothesis Statement 07: planes y pago externo**

Creemos que podremos validar un modelo de suscripción si los usuarios comprenden las diferencias entre planes y completan un flujo seguro con un proveedor externo. Lo comprobaremos mediante pruebas de comprensión y la tasa de finalización del flujo; el umbral comercial se definirá después de entrevistar a los segmentos y evaluar su disposición de pago.

### 1.2.2.4. Lean UX Canvas.

El Lean UX Canvas es una herramienta utilizada en el marco del diseño centrado en el usuario (UX) y la metodología Lean, cuyo objetivo es apoyar la creación y mejora de productos de manera ágil y eficiente. Su propósito principal es proporcionar una estructura organizada que fomente la colaboración entre equipos multidisciplinarios. A continuación, se presenta el Lean UX Canvas elaborado por el equipo utilizando la plataforma digital Mural.

![Lean UX Canvas](../../assets/chapter-1/lean_ux_canvas.png)
Enlace para acceder al Lean UX Canvas en Mural:  https://tinyurl.com/LeanUxCanvasMural
