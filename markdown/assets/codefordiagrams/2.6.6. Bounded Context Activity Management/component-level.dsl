workspace "AniTec - Activity Management Components" "Vistas C4 de componentes del bounded context Activity Management." {
    model {
        user = person "Authenticated Mobile User" "Ganadero o veterinario autorizado para usar las capacidades del contexto."
        external1 = softwareSystem "Livestock Context" "Dependencia externa de Activity Management."
        external2 = softwareSystem "Sanitary Context" "Dependencia externa de Activity Management."
        external3 = softwareSystem "Firebase Cloud Messaging" "Dependencia externa de Activity Management."

        anitec = softwareSystem "AniTec" "Solución móvil para gestión ganadera." {
            api = container "AniTec REST API" "Backend y fuente autoritativa de reglas de negocio." "C# y ASP.NET Core" {
                apiController = component "REST Interface" "Controladores: FarmActivitiesController." "ASP.NET Core Controllers"
                apiAssembler = component "Resource Assemblers" "Traduce resources y comandos sin exponer entidades." "C#"
                apiApplication = component "Application Services and Handlers" "Servicios existentes: FarmActivityCommandService, FarmActivityQueryService. Incluye command handlers y event handlers como diseño objetivo." "C# Application Services"
                apiDomain = component "Activity Management Domain Model" "FarmActivity; reglas, value objects y puertos del contexto." "C# Domain Model"
                repositoryPort = component "Repository Ports" "Interfaces de repositorio definidas desde el dominio." "C# Interfaces"
                repositoryAdapter = component "Persistence Adapters" "FarmActivityRepository." "Entity Framework Core"
            }
            android = container "Native Android Application" "Cliente Android nativo." "Kotlin y Jetpack Compose" {
                androidUi = component "Activity Management Compose UI" "Pantallas y componentes visuales del contexto." "Jetpack Compose"
                androidViewModel = component "ViewModel and UI State" "Mantiene estado de presentación y procesa intenciones." "Kotlin ViewModel"
                androidUseCases = component "Mobile Use Cases" "Casos de uso de programación, reprogramación, finalización y recordatorios." "Kotlin"
                androidRepository = component "Repository Implementation" "Coordina fuentes remota y local." "Kotlin"
                androidRemote = component "REST Data Source" "Consume los endpoints del contexto." "Retrofit/OkHttp"
                androidLocal = component "Room Data Source" "Mantiene caché y outbox local." "Room"
                androidSync = component "Synchronization Worker" "Reintenta operaciones pendientes de forma idempotente." "WorkManager"
            }
            flutter = container "Cross-Platform Mobile Application" "Cliente móvil multiplataforma." "Flutter y Dart" {
                flutterUi = component "Activity Management Widgets" "Páginas y widgets del contexto." "Flutter"
                flutterState = component "State Controller" "Mantiene estado de presentación y procesa intenciones." "Dart"
                flutterUseCases = component "Mobile Use Cases" "Casos de uso equivalentes a Android." "Dart"
                flutterRepository = component "Repository Implementation" "Coordina fuentes remota y local." "Dart"
                flutterRemote = component "REST Data Source" "Consume los endpoints del contexto." "Dio"
                flutterLocal = component "SQLite Data Source" "Mantiene caché y outbox local." "SQLite"
                flutterSync = component "Synchronization Coordinator" "Reintenta operaciones pendientes de forma idempotente." "Dart"
            }
            mysql = container "AniTec Database" "Persistencia autoritativa del contexto." "MySQL" "Database"
            room = container "Android Local Database" "Caché y outbox del contexto en Android." "Room/SQLite" "Database"
            flutterDb = container "Flutter Local Database" "Caché y outbox del contexto en Flutter." "SQLite" "Database"
        }

        user -> androidUi "Usa"
        user -> flutterUi "Usa"
        androidUi -> androidViewModel "Envía intenciones y observa estado"
        androidViewModel -> androidUseCases "Invoca"
        androidUseCases -> androidRepository "Usa el puerto"
        androidRepository -> androidRemote "Consulta o sincroniza"
        androidRepository -> androidLocal "Lee y escribe"
        androidSync -> androidRepository "Procesa operaciones pendientes"
        androidRemote -> apiController "Consume" "JSON/HTTPS + JWT"
        androidLocal -> room "Persiste" "Room"

        flutterUi -> flutterState "Envía intenciones y observa estado"
        flutterState -> flutterUseCases "Invoca"
        flutterUseCases -> flutterRepository "Usa el puerto"
        flutterRepository -> flutterRemote "Consulta o sincroniza"
        flutterRepository -> flutterLocal "Lee y escribe"
        flutterSync -> flutterRepository "Procesa operaciones pendientes"
        flutterRemote -> apiController "Consume" "JSON/HTTPS + JWT"
        flutterLocal -> flutterDb "Persiste" "SQLite"

        apiController -> apiAssembler "Traduce requests y responses"
        apiAssembler -> apiApplication "Entrega comandos y consultas"
        apiApplication -> apiDomain "Ejecuta reglas"
        apiApplication -> repositoryPort "Depende del puerto"
        repositoryAdapter -> repositoryPort "Implementa"
        repositoryAdapter -> mysql "Lee y escribe" "Entity Framework Core / SQL"
        apiApplication -> external1 "Consulta o publica información mediante un contrato explícito"
        apiApplication -> external2 "Consulta o publica información mediante un contrato explícito"
        apiApplication -> external3 "Consulta o publica información mediante un contrato explícito"
    }

    views {
        component api "BC6-ApiComponents" "Componentes backend de Activity Management." {
            include *
            autoLayout lr
        }
        component android "BC6-AndroidComponents" "Componentes Android de Activity Management." {
            include *
            autoLayout lr
        }
        component flutter "BC6-FlutterComponents" "Componentes Flutter de Activity Management." {
            include *
            autoLayout lr
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
            element "Component" {
                background #457B9D
                color #FFFFFF
            }
            element "Database" {
                shape cylinder
                background #5C6B73
                color #FFFFFF
            }
            relationship "Relationship" {
                color #52616B
                routing orthogonal
            }
        }
    }
    configuration {
        scope softwaresystem
    }
}
