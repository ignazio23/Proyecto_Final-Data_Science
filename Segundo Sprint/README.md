<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **SEGUNDO SPRINT** </h1>

## **Conceptos Básicos**

En estas semanas se plantea el realizar el ETL del proyecto seleccionado, en nuestro caso 'FOOD CRUSH' y de los datos que tengamos disponibles. Este análisis nos permitira no solo comprender a un nivel más profundo la funcionalidad de nuestros datos, sino también visualizar de manera más organizada nuestro objetivos con la intención de poder así ya comenzar a formular en conjunto con el equipo el dashboard final y la visual de nuestros datos a través del sitio web a diseñar.


### • **Objetivos**

Afrontar cambios planteados, modificaciones solicitadas o nuevas implementaciones fundamentadas en la documentación. Es decir, se documenta y desarrolla aquello que ha ido siendo trabajado y considerado necesario para la creación del proyecto. 
Realización y completitud de un ETL el cual nos permita realizar la validación de la totalidad de los datos seleccionados, los cuales se acoplen a las necesidades del desarrollo, y se comporten a la altura de una implementación seria, logrando incorporar un mecanismo de validación de los datos utilizados con el objetivo de asegurarnos que el proceso de ETL se haya ejecutado correctamente. 
Llevar a cabo el registro en un video de las correctas implementaciones y las ejecuciones del ETL, esto se realizará con el objetivo de conseguir un Backup, el cual nos sea de utilidad para comprobar el funcionamiento y paso a paso de lo desarrollado. 
Se continuará con la documentación de los realizado, siendo en este punto lo más destacable del tema, el apartado 'Ciclo de Vida' del proyecto donde esté buscará actualizar y registrar aquellos avances y conclusiones que vayamos obteniendo. 
Generar una completa idea del diseño de nuestro modelo de datos, esto para manera una visión clara de aquello a lo que apuntamos al momento de realizar el desarrollo de nuestro proyecto. 


### • **Alcance**

Deberemos delimitar el trabajo definiendo el correcto alcance y las tareas/desarrollos que se puedan considerar importantes para la integridad del proyecto por complejidad o tiempo.


### • **ETL y Plataforma WEB**

Realizamos de manera conjunta la evaluación de los datos actualmente trabajados, de manera tal que podamos acceder a los mismos y cargarlos en la plataforma seleccionada (en nuestro GCP) para su uso posterior y el correcto diseño con los mismo de un ETL Automatizado, el cual nos permita no solo evaluar, organizar y dejar preparados los datos para el uso de estos en el futuro Dashboard a realizar; sino también poder demostrar la capacidad de realización y desarrollo de un procesado automatizado el cual al recibir datos pueda evaluar de manera autonoma los mismos, y procesarlos para su posterior carga y utilización.


### • **Solución Presentada**

Se debe realizar una estimación de tiempo para cada tarea, contemplando los tiempos de ejecución globales y los hitos previstos para cada semana; y plasmar esta estimación en un diagrama de Gantt.

Nos organizamos de manera tal que el equipo en esta instancia pasa a ser un equipo unido de Data Engineers, los cuales nos dividimos en aquellos quienes van a analizar y filtrar los datos para el diseñado del ETL y sus implementación. Aquellos que investiguen y evaluen los modos de uso de la plataforma seleccionada, a su vez la posibilidad de una herramienta extra la cual se vincula al almacenado de los datos (Docker), y la posterior implementación de lo recabado, siendo los que esten a cargo de la carga de datos y del manejo de los mismos a nivel Web. Y por último aquel que realice la revisión y actualización de la documentación, el análisis y control del código implementado y los diferentes entornos de visualización (Github y Notion).

Finalmente, como en Data es muy importante trabajar con datos de calidad, deberán incluir en su informe un video de la implementación y ejecución del código (ETL) desarrollado, detallándolos lo más posible.


## Diccionario de Datos

### `review_estado`
| Dato | Descripción |
| --- | --- |
| **user_id** | Id de usuario en Google Maps. |
| **name** | Nombre de usuario en Google Maps. |
| **time** | Fecha y hora de registro del comentario o calificación. |
| **gmap_id** | Id de localización del establecimiento. |
| **rating** | Calificación hecha por el usuario. |
| **text** | Comentario hecho por el usuario. |
| **review** | Dato para ML. |

### `metadatos_restaurantes`
| Dato | Descripción |
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
