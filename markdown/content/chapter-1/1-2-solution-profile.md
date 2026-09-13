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

## 1.2.2. Lean UX Process.

### 1.2.2.1. Lean UX Problem Statements.

**Problem Statement:**

El estado actual de la gestión ganadera para pequeños y medianos productores se ha centrado principalmente en controles manuales, registros en cuadernos y herramientas digitales improvisadas para administrar la información sanitaria, reproductiva y económica del hato.

Lo que los productos y servicios existentes no abordan es la necesidad de contar con una aplicación para Android sencilla, accesible y adaptada al trabajo de campo, que permita centralizar la información del ganado y mantener el registro de las actividades principales incluso cuando la conexión a Internet sea inestable.

Nuestro producto, AniTec, abordará esta brecha mediante una aplicación móvil para Android que permitirá registrar, organizar y consultar la información del ganado desde el teléfono. La solución incluirá recordatorios sanitarios, historiales por animal, reportes y almacenamiento local de información esencial para reducir errores, evitar la pérdida de datos y facilitar la toma de decisiones.

Nuestro enfoque inicial será pequeños y medianos ganaderos que actualmente dependen de registros manuales o sistemas poco organizados para gestionar su producción, junto con veterinarios que necesitan consultar información sanitaria y dar seguimiento a los animales de sus clientes desde un dispositivo Android.

Sabremos que hemos tenido éxito cuando observemos una reducción en el uso de registros manuales, un aumento en la frecuencia y precisión de los registros realizados desde la aplicación, una mejora en el cumplimiento de vacunaciones y tratamientos, y una consulta más rápida de los historiales sanitarios por parte de ganaderos y veterinarios.

### 1.2.2.2. Lean UX Assumptions.

### **Business Assumptions:**

1. **Creemos que nuestros usuarios necesitan** un método confiable y eficiente para registrar y supervisar desde el teléfono la salud, productividad y trazabilidad de su ganado.
2. **Creemos que esta necesidad puede satisfacerse** mediante una aplicación para Android que permita registrar información clave, conservar datos esenciales en el dispositivo, generar alertas y consultar reportes útiles para la toma de decisiones.
3. **Creemos que nuestros primeros usuarios serán** pequeños y medianos ganaderos que utilizan teléfonos Android, así como veterinarios y técnicos agropecuarios que asesoran directamente en el campo.
4. **Creemos que lo más importante para los clientes es** contar con un control ordenado y disponible durante sus actividades, evitando pérdidas de información y mejorando la trazabilidad del ganado.
5. **Creemos que los usuarios también recibirán** alertas sanitarias mediante notificaciones, reportes económicos, acceso al historial de cada animal y contenido educativo dentro de la aplicación.
6. **Creemos que conseguiremos clientes mediante** alianzas con asociaciones ganaderas, programas de desarrollo rural, recomendaciones de veterinarios y campañas digitales dirigidas a regiones con actividad ganadera.
7. **Creemos que los ingresos se generarán mediante** un modelo de suscripción con planes ajustados al tamaño del hato y licencias institucionales para asociaciones y entidades del sector agropecuario.
8. **Creemos que nuestra competencia incluye** aplicaciones genéricas de gestión ganadera, hojas de cálculo y métodos tradicionales de registro manual.
9. **Creemos que nuestra ventaja competitiva radica en** ofrecer una aplicación Android adaptada al contexto rural, fácil de usar y preparada para conservar el progreso cuando la conectividad sea limitada.
10. **Creemos que un riesgo importante es** que algunos ganaderos no adopten fácilmente la aplicación por falta de experiencia digital, conectividad inestable o limitaciones de sus dispositivos.
11. **Creemos que lo mitigaremos mediante** una interfaz intuitiva, tutoriales paso a paso, formularios breves, almacenamiento local y mensajes claros sobre el estado de sincronización.

### **User Assumptions:**

- **Creemos que** los principales usuarios son pequeños y medianos ganaderos, veterinarios y técnicos agropecuarios que utilizan dispositivos Android durante sus actividades. En etapas posteriores, la aplicación también podría apoyar a asociaciones, cooperativas y entidades vinculadas con la sanidad y trazabilidad del sector.

- **Creemos que** AniTec ayuda a organizar la información del hato desde el teléfono, evitando la pérdida de datos importantes y la falta de seguimiento de vacunas, partos, tratamientos y movimientos. Para los veterinarios, facilita la consulta de clientes, pacientes e historiales sanitarios durante una atención.

- **Creemos que** los usuarios valoran el registro individual de cada animal, las notificaciones sobre actividades pendientes, los reportes simples, el historial del hato y la posibilidad de conservar registros cuando la conexión sea inestable. También creemos que la facilidad de uso es esencial para su adopción.

- **Creemos que** AniTec se integra en la rutina del ganadero porque puede utilizarse en el campo cada vez que se registra un animal, tratamiento, parto, vacunación o cambio productivo. Los veterinarios pueden utilizarla antes, durante y después de una visita para consultar antecedentes y registrar la atención.

- **Creemos que** AniTec debe ofrecer una experiencia Android intuitiva, legible y estable, pensada para usuarios con distintos niveles de experiencia tecnológica. También debe proteger los datos, comunicar los errores de conexión y permitir recuperar el trabajo pendiente.

### Feature Assumptions:

**Feature Assumption 01**

**Creemos que** una funcionalidad de registro móvil centralizado permitirá a los pequeños y medianos ganaderos gestionar la información sanitaria, reproductiva y económica de sus animales desde un dispositivo Android.

**Sabremos que esta funcionalidad es valiosa cuando** la mayoría de los usuarios registre y actualice periódicamente la información de sus animales mediante la aplicación.

**Feature Assumption 02**

**Creemos que** un sistema de notificaciones para vacunaciones, tratamientos y eventos reproductivos ayudará a los ganaderos a recordar actividades importantes y reducir los descuidos en el manejo del hato.

**Sabremos que esta funcionalidad es valiosa cuando** los usuarios atiendan o reprogramen los recordatorios recibidos en sus dispositivos Android.

**Feature Assumption 03**

**Creemos que** un módulo de reportes visuales e historial de cada animal facilitará la interpretación de la información y permitirá tomar mejores decisiones productivas, reproductivas y económicas.

**Sabremos que esta funcionalidad es valiosa cuando** los usuarios consulten los reportes y antecedentes antes de realizar acciones relacionadas con la gestión del ganado.

**Feature Assumption 04**

**Creemos que** el almacenamiento local de información esencial y borradores permitirá que los usuarios continúen registrando actividades cuando la conexión a Internet sea inestable.

**Sabremos que esta funcionalidad es valiosa cuando** los usuarios puedan recuperar y sincronizar sus registros sin repetir la información ingresada.

**Feature Assumption 05**

**Creemos que** un módulo para veterinarios con acceso autorizado a clientes, historiales y eventos sanitarios facilitará el seguimiento de los animales y mejorará la colaboración con los ganaderos.

**Sabremos que esta funcionalidad es valiosa cuando** los veterinarios utilicen la aplicación Android para registrar y consultar la información sanitaria de los animales atendidos.

### 1.2.2.3. Lean UX Hypothesis Statements.

- **Hypothesis Statement 01:**

  **Creemos que lograremos** una mayor adopción y un uso continuo de AniTec

  **Si** los pequeños y medianos ganaderos

  **Obtienen** una forma sencilla de registrar y consultar la información sanitaria, reproductiva y económica de sus animales desde el teléfono

  **Con** una aplicación para Android que centralice y organice la información del hato.


- **Hypothesis Statement 02:**

  **Creemos que lograremos** mejorar la gestión sanitaria del hato y reducir actividades olvidadas

  **Si** los pequeños y medianos ganaderos

  **Obtienen** recordatorios oportunos sobre vacunaciones, tratamientos y eventos reproductivos

  **Con** un sistema de alertas y notificaciones integrado en la aplicación Android.

- **Hypothesis Statement 03:**

  **Creemos que lograremos** una mejor toma de decisiones sobre el manejo del ganado

  **Si** los pequeños y medianos ganaderos

  **Obtienen** acceso desde el teléfono a reportes visuales y al historial de cada animal

  **Con** un módulo móvil de reportes e historiales organizado y fácil de interpretar.


- **Hypothesis Statement 04:**

  **Creemos que lograremos** reducir la pérdida de información causada por problemas de conectividad

  **Si** los pequeños y medianos ganaderos y veterinarios

  **Obtienen** la posibilidad de conservar el progreso cuando no dispongan de una conexión estable

  **Con** almacenamiento local y sincronización posterior dentro de la aplicación Android.


- **Hypothesis Statement 05:**

  **Creemos que lograremos** una mejor colaboración entre ganaderos y veterinarios y un seguimiento sanitario más eficiente

  **Si** los veterinarios

  **Obtienen** acceso autorizado a los clientes asignados, al historial de los animales y al registro de eventos sanitarios

  **Con** un módulo para veterinarios integrado en la aplicación Android de AniTec.

### 1.2.2.4. Lean UX Canvas.

El Lean UX Canvas es una herramienta utilizada en el marco del diseño centrado en el usuario (UX) y la metodología Lean, cuyo objetivo es apoyar la creación y mejora de productos de manera ágil y eficiente. Su propósito principal es proporcionar una estructura organizada que fomente la colaboración entre equipos multidisciplinarios. A continuación, se presenta el Lean UX Canvas elaborado por el equipo utilizando la plataforma digital Mural.

![Lean UX Canvas](../../assets/chapter-1/lean_ux_canvas.png)
Enlace para acceder al Lean UX Canvas en Mural:  https://tinyurl.com/LeanUxCanvasMural
