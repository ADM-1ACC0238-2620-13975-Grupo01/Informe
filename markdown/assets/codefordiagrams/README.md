# Diagramas C4 de AniTec

El archivo `anitec-software-architecture.dsl` contiene un único modelo consistente y tres vistas exportables:

| Vista en Structurizr | Sección del informe | Nombre esperado del archivo exportado |
|---|---|---|
| `AniTec-SystemContext` | 2.5.3.1 | `SoftwareArchitectureContextLevelDiagram.png` |
| `AniTec-Containers` | 2.5.3.2 | `SoftwareArchitectureContainerLevelDiagram.png` |
| `AniTec-Deployment` | 2.5.3.3 | `SoftwareArchitectureDeploymentDiagram.png` |

## Visualización y exportación

1. Abrir Structurizr Lite, Structurizr Cloud o una herramienta compatible con Structurizr DSL.
2. Importar `anitec-software-architecture.dsl`.
3. Revisar las tres vistas indicadas en la tabla.
4. Exportarlas como PNG con los nombres esperados.
5. Copiar los PNG a `Informe/markdown/assets/chapter-2/`.

Los bloques `<img>` del informe ya apuntan a esas rutas y funcionarán cuando se agreguen los archivos exportados.

## Diagramas tácticos de bounded contexts

Cada carpeta contiene un workspace C4 con tres vistas, un UML del dominio y los modelos de persistencia de MySQL, Android Room y Flutter SQLite.

| Bounded Context | C4 Components | Domain UML | Database Designs |
|---|---|---|---|
| 2.6.1 Identity and Access Management | `2.6.1. Bounded Context Identity and Access Management/component-level.dsl` | `2.6.1. Bounded Context Identity and Access Management/domain-layer-class-diagram.puml` | Tres archivos `.erd` |
| 2.6.2 Profile Management | `2.6.2. Bounded Context Profile Management/component-level.dsl` | `2.6.2. Bounded Context Profile Management/domain-layer-class-diagram.puml` | Tres archivos `.erd` |
| 2.6.3 Livestock Management | `2.6.3. Bounded Context Livestock Management/component-level.dsl` | `2.6.3. Bounded Context Livestock Management/domain-layer-class-diagram.puml` | Tres archivos `.erd` |
| 2.6.4 Sanitary Management | `2.6.4. Bounded Context Sanitary Management/component-level.dsl` | `2.6.4. Bounded Context Sanitary Management/domain-layer-class-diagram.puml` | Tres archivos `.erd` |
| 2.6.5 Veterinary Collaboration | `2.6.5. Bounded Context Veterinary Collaboration/component-level.dsl` | `2.6.5. Bounded Context Veterinary Collaboration/domain-layer-class-diagram.puml` | Tres archivos `.erd` |
| 2.6.6 Activity Management | `2.6.6. Bounded Context Activity Management/component-level.dsl` | `2.6.6. Bounded Context Activity Management/domain-layer-class-diagram.puml` | Tres archivos `.erd` |
| 2.6.7 Financial Management | `2.6.7. Bounded Context Financial Management/component-level.dsl` | `2.6.7. Bounded Context Financial Management/domain-layer-class-diagram.puml` | Tres archivos `.erd` |
| 2.6.8 Subscription Management | `2.6.8. Bounded Context Subscription Management/component-level.dsl` | `2.6.8. Bounded Context Subscription Management/domain-layer-class-diagram.puml` | Tres archivos `.erd` |
| 2.6.9 Analytics and Reporting | `2.6.9. Bounded Context Analytics and Reporting/component-level.dsl` | `2.6.9. Bounded Context Analytics and Reporting/domain-layer-class-diagram.puml` | Tres archivos `.erd` |

### Convenciones de exportación

- Los `.dsl` se validan y exportan con Structurizr; cada archivo declara vistas para API, Android y Flutter.
- Los `.puml` se renderizan con PlantUML.
- Los `.erd` contienen sintaxis Mermaid `erDiagram`; cada PNG renderizado se guarda junto a su archivo fuente.
- Los nombres exactos de los PNG esperados aparecen en los placeholders de cada Markdown de 2.6.
