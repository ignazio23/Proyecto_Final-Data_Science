<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PRIMER SPRINT** </h1>

## **Conceptos Básicos**

En esta semana deben realizar un análisis del proyecto seleccionado y los datos disponibles. En base al entendimiento que logren de la temática, deben proponer como encararla, brindando una solución o herramientas desarrolladas por ellos mismos para acercarse a dicha solución.


### • **Objetivos**

De la misma manera evaluamos las posibles herramientas a utilizar y llevamos a discusión las cualidades, posibilidades y usos que podemos darles para lograr poder tomar una decisión sobre cual sería la herramienta correcta a implementar. Podemos proceder a evaluar y categorizar las tareas a realizar por cada integrante en calidad de prioridad, complejidad y severidad. Planteamiento de un sistema de documentación de lo realizado y sus actualizaciones, inicio de la generación de un modelo organizacional mediante le uso de la herramienta Notion y adquisición de un orden específico de quienes llevarán a cabo que tareas (designación de roles). Registro y generación de los KPI que buscaremos implementar para poder fundamentar lo desarrollado y que estén alineados con las necesidades de lo solicitado. Se da comienzo a la generación del ciclo de vida del proyecto. Realización y completitud de un EDA completo, los cuales se acoplen a las necesidades del desarrollo, donde este análisis de calidad nos brinde el filtrado de data librándonos de data posiblemente sucia o corrupta que pueda modificar o truncar los resultados de procesos futuros.


### • **Alcance**

Deberemos delimitar el trabajo definiendo el correcto alcance y las tareas/desarrollos que se puedan considerar importantes para la integridad del proyecto por complejidad o tiempo.


### • **Objetivos y KPIs Asociados**

Del entendimiento de la problemática surgirán cuestiones que se buscarán resolver con el trabajo o las herramientas desarrolladas. Estas cuestiones, formuladas como objetivos, admitirán la creación de [KPIs](https://www.google.com/url?q=https://docs.google.com/document/d/e/2PACX-1vRmmx8r3a7YzHbIClAcVEQkzqGeEstItZSZ2e1HaycWHGblIuGE1frhQNbumSPcEe2RMgZ-u9gu4Iac/pub&sa=D&source=editors&ust=1706660402738041&usg=AOvVaw0jw64ofDxcvg_BSW5CNaRk) para evaluar su cumplimiento. 
Es una tarea muy abarcativa y a la vez muy específica en torno tanto a la problemática como al enfoque elegido.

Los KPI definidos posterior a su debido análisis y resolución por parte del equipo, son:
 + Mejorar el porcentaje de reseñas positivas en un 10 % respecto del año anterior.
 + Reducir el tiempo de espera de platillos en un 5% respecto al mes anterior.
 + Incrementar un 15% la clientela respecto del año anterior.
 + Medir si se cumple en un 80% el mejor plato servido, en el restaurante determinado.


### • **Repositorio Github y Documentación en Notion**

Armado de un repositorio de Github para trabajar colaborativamente con todo el grupo. Debe ser público para que lo pueda ver tanto el mentor como el Product Owner.
A su vez se realiza documentación de todo lo realizado en la herramienta Notion, con la intención de dejar registro y guía de lo que se fue desarrollando y a su vez, el como y el porque de ello.
Github: https://github.com/ignazio23/Proyecto_Final-Data_Science
Notion por otra parte se podrá visualizar de la siguiente forma:
  + Inicio - https://violet-sawfish-2e4.notion.site/9fd44a5c7d7a42e08f67ad4983f087b6?v=be746f1482a747548d851808b19c5b49&pvs=4
  + Ciclo de Vida - https://violet-sawfish-2e4.notion.site/Ciclo-de-Vida-a736b27fb9a34eb6ba929ad6c831372f?pvs=4
  + Especificaciones - https://violet-sawfish-2e4.notion.site/Especificaciones-0779e431232145e59b0cb251813c54ea?pvs=4
  + A su vez también contamos con instancias como 'Brainstorming' y 'Rollbacks' pero concideramos que las mismas son de uso único del equipo de trabajo y su publicación es irrelevante para comprender el contexto de lo implementado. De la misma forma contamos con otras instancias, de la misma forma irrelevantes para el seguimiento de lo desarrollado, tales como, 'Reuniones', 'Tareas', entre otras.


### • **Solución Presentada**

Se debe realizar una estimación de tiempo para cada tarea, contemplando los tiempos de ejecución globales y los hitos previstos para cada semana; y plasmar esta estimación en un diagrama de Gantt.

Una parte muy importante de la solución propuesta, es presentar con qué herramientas (**stack tecnológico**) se fue realizando la arquitectura del proyecto. Para esto, lo que van a tener que hacer es seleccionar una pequeña porción de los datos que disponen y realizar un proceso de limpieza y transformación utilizando las herramientas que planean implementar. Esto les dará una idea de cómo funcionarán en el proyecto completo y les permitirá tener un mejor abordaje para futuras tareas. Hay que tener en cuenta que, como este ítem va a ser una presentación previa de lo que van a trabajar en el segundo sprint, el PO puede dar el OK o determinar cuál es el mejor camino para que tomen. Esto les va a permitir adelantar trabajo de la segunda semana, ya que no se va a tener que esperar hasta la segunda demo para verificar si la arquitectura cumple con los requisitos solicitados.

Finalmente, como en Data es muy importante trabajar con datos de calidad, deberán incluir en su informe un análisis sobre los datos con los que van a trabajar, detallándolos lo más posible.

### • **Stack Tecnológico**

Tomamos la decisión en base al análisis realizado de trabajar con las siguientes herramientas y tecnologías -
 + Python y Jupyter Notebooks como principales fuentes de escritura de código.
 + Notion y Github para la generación de documentación, donde Github será enfocada al registro del código desarrollado, mientras Notion, tendrá documentación acorde a objetivos, presentación de integrantes, ciclo de vida, entre otras cosa.
 + Para la realización del EDA y en futuras instancias, para cualquier interacción con el código desarrollado, utilizaremos Google Colab y Visual Studio Code.
 + A su vez ya generamos un avance en la toma de decisiones, y optamos por la utilización de Google Cloud, Spark y Polars como implementación para el manejo de la data a utilizar, Power BI para la generación del Dashboard final, y por último, OpenIA y Bard como las herramientas de Inteligencia Artificial utilizadas.


## Diccionario de Datos

### `review_estado`
| Fila | Descripción |
| --- | --- |
| **user_id** | Id de usuario en Google Maps. |
| **name** | Nombre de usuario en Google Maps. |
| **time** | Fecha y hora de registro del comentario o calificación. |
| **gmap_id** | Id de localización del establecimiento. |
| **rating** | Calificación hecha por el usuario. |
| **text** | Comentario hecho por el usuario. |
| **review** | Dato para ML. |

### `metadatos_restaurantes`
| Fila | Descripción |
| --- | --- |
| **address** | Ubicación. |
| **avg_rating** | Promedio de todas las puntuaciones recibidas. |
| **category** | Categorías con las que está registrado. |
| **gmap_id** | ID de localización del establecimiento proporcionado por google maps. |
| **latitude** | Latitud de la coordenada. |
| **longitude** | Longitud de la coordenada. |
| **name** | Nombre del establecimiento. |
| **num_of_reviews** | Cantidad de reseñas recibidas por usuarios. |
| **Accessibility** | Características de los tipos de acceso al establecimiento. |
| **Amenities** | Servicios que ofrece el establecimiento. |
| **Atmosphere** | Tipo de entorno que ofrece el establecimiento. |
| **Crowd** | Tipos de multitud que es admitida |
| **Dining_options** | Opciones gastronómicas |
| **Highlights** | Servicios destacados |
| **Offerings** | Ofertas |
| **Payments** | Métodos de pago |
| **Planning** | Opciones en planificación |
| **Popular_for** | Público objetivo del establecimiento |
| **Service_options** | Opciones de servicios |
| **Popular_for** | Público objetivo del restaurante |
| **Service_options** | Opciones de servicios |
