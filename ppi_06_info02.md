# MetroMap

## Herramientas/aplicativos
- [Metro de Seúl](https://www.seoulmetro.co.kr/en/cyberStation.do): El sistema de metro de Seúl consta de 23 líneas y ofrece varias características útiles para los usuarios:
  - Permite buscar estaciones específicas para facilitar su ubicación en el mapa
  - Las estaciones cuentan con información sobre la primera y última salida del metro para los días de la semana y los fines de semana.
  - Es posible calcular rutas entre estaciones y filtrarlas según los criterios de "menos transbordos", "más rápido" o "menos distancia".
  - Cada estación cuenta con una imagen que detalla la información de las rutas de evacuación en caso de emergencia.
  - El sistema de metro de Seúl también está integrado con Google Maps, lo que permite a los usuarios conocer los puntos de interés cercanos a cada estación.
- [Metro de Madrid](https://www.metromadrid.es/es): El metro de Madrid cuenta con cada linea detallada individualemte, cumple con el objetivo de indicar el estado de las lineas y sus estaciones. 
  - Es posible calcular rutas entre estaciones y filtrarlas según los criterios de "menos transbordos", "más rápido" o "menos distancia".
  - Una vez seleccionada una ruta, se muestra un mapa de Madrid con todas las estaciones, destacando el tramo seleccionado.
  - El mapa de las líneas y estaciones se superpone en un mapa detallado de Madrid que muestra direcciones y ubicaciones.
  - Madrid cuenta con un mapa estático detallado, similar al sistema de metro de Medellín, que está disponible en varias variaciones (cartográfico, de red, esquemático, etc.). 
  - Los horaios estan fijados para cada tramo.
- [Metro de Lima](https://www.lineauno.pe/estaciones/):El proyecto de metro más reciente actualmente cuenta con una sola línea en funcionamiento.
  - La congestión en la línea se muestra a través de un gradiente de colores, que va desde verde (de 0 a 10m) hasta roja (de mas de 60m)
  - Se proporcionan horarios de llegada y salida estimados.
  - El mapa dinámico de la línea de metro se superpone en un mapa estático de la ciudad que se divide en sectores.

## Software open source

- [Nextra](https://nextra.site/): Es de mucha utilidad ya que nos permite documentar nuestro proyecto a través de una página web atractiva que en el futuro pensamos será de utilidad para enseñar a otros desarroladores cómo implementar nuestra API. Entre sus principales ventajas encontramos:
  - Facilidad y rápida implementación.
  - Visuales atractivos.
  - Documentación accesible en múltiples dispositivos.
  - Alta capacidad para personalizar la apariencia de la documentación.
- [Django](https://www.djangoproject.com/): Consideramos que será el núcleo para el funcionamiento del backend de nuestra aplicación web. Sus principales ventajas, además de permitirnos desarrollar un backend robusto en python, son:
  - Múltiples opciones predesarrolladas que pueden ser usadas en nuestro proyecto.
  - Seguridad implementada por defecto.
  - Su documentación esta muy completa.
  - Es altamente escalable, y puede ser beneficioso a futuro cuando querramos implementar nuevas características a nuestro mapa interactivo.
- [Next.js](https://nextjs.org/) en conjunto con [React](https://es.reactjs.org/): Dos de los frameworks más prometedores para el desarrollo de frontend funcionando unidos, creemos que será de gran utilidad para la interactividad del mapa. Las principales ventajas son:
  - Renderizado en servidor o cliente.
  - Mejora la experiencia de usuario considerablemente con respecto a usar solo HTML, CSS y JS.
  - React nos permite un desarrollo más rápido y eficiente.
  - Existe mucha documentación al respecto.
- [Django REST Framework](https://www.django-rest-framework.org/): Basado en Django, mantiene una línea de aprendizaje similar, y nos permite implementar la API de mejor forma, entre sus principales ventajas encontramos:
  - Proporciona herramientas y utilidades para simplificar la creación de APIs web.
  - Genera documentación para las APIs creadas.
  - Es muy flexible y permite personalizar el comportamiento de las APIs de acuerdo a nuestras necesidades.
- [MySQL](https://www.mysql.com/): Un sistema de gestión de bases de datos muy conocido, que nos servirá para almacenar todos los datos recolectados por nuestra plataforma. Entre sus principales ventajas están:
  - Cuenta con una gran comunidad de desarrolladores y se encuentra en el top de sistemas de gestión de bases de datos.
  - Es muy fiable y estable.
  - Se puede conectar con múltiples lenguajes y sistemas operativos.
  - Es conocido por su alto rendimiento y velocidad en la gestión de bases de datos.

## Librerías disponibles

- [snscrape](https://github.com/JustAnotherArchivist/snscrape): es una librería que permite hacer web scraping de redes sociales. Sus características son: 
    - Su compatibilidad con varias redes sociales, entre las que se encuentran Twitter, Reddit,  Instagram y YouTube.
    - El hecho de que permite realizar búsquedas avanzadas en las redes sociales.
    - Su gran flexibilidad, ya que permite extraer los datos en diversos formatos como JSON o CSV.
    - La rapidez con la que puede llevar a cabo la extracción de grandes cantidades de datos
    - El poder llevar a cabo seguimiento en tiempo real de la red social que se quiera a través de su herramienta de streaming.
    - Por último, está su gran facilidad de uso gracias a la interfaz que tiene que lo vuelve fácil de usar para gente con diferentes conocimientos de programación.

- [re](https://docs.python.org/3/library/re.html): es una librería que se usa para trabajar con patrones de cadenas de texto. Entre sus características más relevantes encontramos: 
  - Permite buscar y reemplazar patrones
  - Permite encontrar patrones que coinciden con una expresión regular
  - Nos permite definir patrones complejos utilizando una sintaxis de expresiones regulares
  - Permite utilizar comodines y caracteres especiales
  - También nos permite agrupar y capturar patrones para su posterior uso en el código

- [pandas](https://pandas.pydata.org/): es una librería popular de Python utilizada para manipular y analizar datos. Sus principales características incluyen:
  - Estructuras de datos flexibles para manejar datos unidimensionales y bidimensionales. Posee numerosas funciones para la manipulación y transformación de datos.
  - Está integrada con otras bibliotecas de Python
  - Tiene la capacidad de leer y escribir datos en una amplia variedad de formatos
  - Nos da diversas funciones de agregación y análisis
  - Además, nos permite flexibilidad en la indexación. 
