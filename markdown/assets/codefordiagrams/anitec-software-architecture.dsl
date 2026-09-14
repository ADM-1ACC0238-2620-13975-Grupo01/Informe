workspace "AniTec - Software Architecture" "Modelo C4 de contexto, contenedores y despliegue para la solución móvil de AniTec." {

    model {
        visitor = person "Visitor" "Persona interesada que consulta la propuesta, beneficios y canales de acceso de AniTec."
        rancher = person "Rancher" "Gestiona fincas, animales, actividades, sanidad y finanzas desde una aplicación móvil."
        veterinarian = person "Veterinarian" "Atiende animales autorizados, registra información sanitaria y consulta sus clientes y pacientes."
        evaluator = person "Evaluator / Tester" "Instala versiones de prueba y valida la solución en un dispositivo físico."

        stripe = softwareSystem "Stripe" "Servicio externo para crear sesiones de checkout y confirmar pagos de suscripciones."
        notificationProvider = softwareSystem "Firebase Cloud Messaging" "Servicio externo que entrega notificaciones push a los dispositivos móviles."
        mlKit = softwareSystem "Google ML Kit" "SDK ejecutado en el dispositivo para reconocer códigos QR mediante la cámara."
        appDistribution = softwareSystem "Firebase App Distribution" "Servicio usado para distribuir versiones firmadas a evaluadores autorizados."

        anitec = softwareSystem "AniTec" "Solución móvil para la gestión ganadera y la colaboración entre ganaderos y veterinarios." {
            landingPage = container "Landing Page" "Comunica la propuesta de valor, segmentos, funcionalidades y canales de acceso al producto." "HTML, CSS y JavaScript"

            androidApp = container "Native Android Application" "Aplicación nativa para ganaderos y veterinarios. Presenta los flujos móviles, usa capacidades del dispositivo y sincroniza información con la API." "Kotlin y Jetpack Compose"
            androidDatabase = container "Android Local Database" "Mantiene caché, read models y operaciones pendientes para brindar continuidad con conectividad limitada." "Room sobre SQLite" "Database"

            flutterApp = container "Cross-Platform Mobile Application" "Aplicación multiplataforma con el mismo alcance funcional y los mismos contratos de servicio que la aplicación Android nativa." "Flutter y Dart"
            flutterDatabase = container "Flutter Local Database" "Mantiene caché, read models y operaciones pendientes de la aplicación multiplataforma." "SQLite compatible con Flutter" "Database"

            api = container "AniTec REST API" "Expone los contratos de IAM, Profiles, Livestock, Sanitary, Veterinary Collaboration, Activities, Financial, Subscriptions y Analytics; aplica autenticación, autorización y reglas de negocio." "C#, ASP.NET Core, Entity Framework Core, JWT y OpenAPI"
            database = container "AniTec Database" "Persiste identidades, perfiles, ganado, registros sanitarios, autorizaciones, actividades, finanzas, suscripciones y proyecciones analíticas." "MySQL" "Database"
        }

        visitor -> anitec "Consulta información del producto"
        rancher -> anitec "Gestiona su operación ganadera"
        veterinarian -> anitec "Colabora en la atención sanitaria autorizada"
        evaluator -> anitec "Instala y valida versiones móviles"
        anitec -> stripe "Procesa el checkout y confirma pagos" "HTTPS"
        anitec -> notificationProvider "Solicita la entrega de recordatorios" "HTTPS"
        anitec -> mlKit "Reconoce códigos QR en el dispositivo"
        anitec -> appDistribution "Publica versiones móviles firmadas"

        visitor -> landingPage "Consulta la propuesta de valor" "HTTPS"
        rancher -> androidApp "Usa los flujos nativos de gestión ganadera"
        rancher -> flutterApp "Usa los flujos multiplataforma de gestión ganadera"
        veterinarian -> androidApp "Consulta pacientes y registra atenciones autorizadas"
        veterinarian -> flutterApp "Consulta pacientes y registra atenciones autorizadas"
        evaluator -> appDistribution "Obtiene acceso a una versión autorizada" "HTTPS"
        appDistribution -> androidApp "Distribuye compilaciones firmadas"
        appDistribution -> flutterApp "Distribuye compilaciones firmadas"
        landingPage -> appDistribution "Dirige a los evaluadores al canal de distribución" "HTTPS"

        androidApp -> androidDatabase "Lee, escribe y mantiene operaciones pendientes"
        flutterApp -> flutterDatabase "Lee, escribe y mantiene operaciones pendientes"
        androidApp -> api "Consume servicios y sincroniza datos" "JSON/HTTPS + JWT"
        flutterApp -> api "Consume servicios y sincroniza datos" "JSON/HTTPS + JWT"
        androidApp -> mlKit "Escanea y decodifica códigos QR" "API en el dispositivo"
        flutterApp -> mlKit "Escanea y decodifica códigos QR mediante un adaptador compatible" "API en el dispositivo"
        api -> database "Lee y persiste información transaccional" "Entity Framework Core / SQL"
        api -> stripe "Crea y confirma sesiones de checkout" "Stripe API / HTTPS"
        api -> notificationProvider "Envía solicitudes de notificación" "FCM API / HTTPS"

        production = deploymentEnvironment "Production" {
            nativeDevice = deploymentNode "Physical Android Device" "Dispositivo físico usado por un ganadero, veterinario o evaluador." "Android" "Mobile Device" {
                nativeRuntime = deploymentNode "Android Runtime" "Entorno de ejecución de la aplicación nativa." "Android Runtime" {
                    containerInstance androidApp
                    containerInstance androidDatabase
                    nativeCamera = infrastructureNode "Camera" "Captura la imagen del código QR." "Android Camera API"
                    nativeMlRuntime = infrastructureNode "On-device QR Recognition" "Ejecuta el reconocimiento del QR sin incorporar reglas del dominio." "Google ML Kit Barcode Scanning"
                }
            }

            crossPlatformDevice = deploymentNode "Cross-Platform Target Device" "Dispositivo físico objetivo definido para validar la aplicación Flutter." "Android o iOS" "Mobile Device" {
                flutterRuntime = deploymentNode "Flutter Runtime" "Entorno de ejecución de la aplicación multiplataforma." "Flutter Engine" {
                    containerInstance flutterApp
                    containerInstance flutterDatabase
                    flutterCamera = infrastructureNode "Camera" "Captura la imagen del código QR." "Camera plugin"
                    flutterMlAdapter = infrastructureNode "QR Recognition Adapter" "Adapta el reconocimiento QR para la aplicación Flutter." "Plugin compatible con ML Kit"
                }
            }

            githubPages = deploymentNode "GitHub Pages" "Alojamiento público de la landing page." "Static Web Hosting" "Cloud Service" {
                containerInstance landingPage
            }

            render = deploymentNode "Render" "Servicio público que ejecuta el backend de AniTec." "Web Service" "Cloud Service" {
                apiRuntime = deploymentNode "ASP.NET Core Runtime" "Entorno administrado del servicio web." ".NET Runtime" {
                    containerInstance api
                }
            }

            filess = deploymentNode "Filess.io" "Servicio administrado de persistencia relacional utilizado por el backend." "Managed Database" "Cloud Service" {
                mysqlRuntime = deploymentNode "MySQL Server" "Motor que almacena los datos de AniTec." "MySQL" {
                    containerInstance database
                }
            }

            firebaseDistributionNode = deploymentNode "Firebase App Distribution" "Canal de distribución de builds firmadas para pruebas y release review." "Firebase" "External Service" {
                softwareSystemInstance appDistribution
            }

            notificationNode = deploymentNode "Firebase Cloud Messaging" "Infraestructura externa de entrega de notificaciones push." "Firebase" "External Service" {
                softwareSystemInstance notificationProvider
            }

            stripeNode = deploymentNode "Stripe Cloud" "Infraestructura externa para checkout y confirmación de pagos." "Stripe" "External Service" {
                softwareSystemInstance stripe
            }
        }
    }

    views {
        systemContext anitec "AniTec-SystemContext" "Actores y sistemas externos que interactúan con AniTec." {
            include *
            autoLayout lr
        }

        container anitec "AniTec-Containers" "Contenedores de la solución móvil AniTec y sus dependencias externas." {
            include *
            autoLayout lr
        }

        deployment anitec production "AniTec-Deployment" "Despliegue objetivo de AniTec para la entrega y validación del producto móvil." {
            include *
            autoLayout tb
        }

        styles {
            element "Person" {
                shape person
                background #084C61
                color #FFFFFF
            }
            element "Software System" {
                background #177E89
                color #FFFFFF
            }
            element "Container" {
                background #2A9D8F
                color #FFFFFF
            }
            element "Database" {
                shape cylinder
                background #5C6B73
                color #FFFFFF
            }
            element "Mobile Device" {
                shape mobileDevicePortrait
                background #E9C46A
                color #1F2933
            }
            element "Cloud Service" {
                shape roundedBox
                background #A8DADC
                color #1D3557
            }
            element "External Service" {
                shape roundedBox
                background #F4A261
                color #1F2933
            }
            element "Infrastructure Node" {
                background #E5E7EB
                color #1F2933
            }
            relationship "Relationship" {
                color #52616B
                routing orthogonal
            }
        }

        terminology {
            person "Actor"
            softwareSystem "Software System"
            container "Container"
            deploymentNode "Deployment Node"
        }
    }

    configuration {
        scope softwaresystem
    }
}
