# MetroMap

Mapa interactivo del Metro de Medellín disponible en [metromap.online](https://metromap.online).

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/metromap)

Nuestra plataforma proporciona en tiempo real el estado actual de las líneas del Metro de Medellín a través de un mapa interactivo en línea y otras herramientas cómo APIs para que el público en general pueda planificar sus viajes de manera efectiva, evitando sorpresas y contratiempos. Además, ofrecemos un espacio para que los usuarios puedan presentar reportes del estado de los servicios, lo que nos ayuda a mantener la información actualizada y mejorar continuamente nuestra plataforma.

## Dominios

### Sitio Principal

En este [sitio](https://metromap.online) encontrarás ejemplos de uso y la documentación oficial para implementar nuestros servicios en tu propia aplicación.

### Api

Puedes acceder a cualquiera de nuestras APIs a través de <https://api.metromap.online/> y utilizando las siguientes rutas. Ten en cuenta que necesitarás incluir una secret_key en la cabecera de la petición para poder acceder a ellas:

```bash
v1
├── status
├────[linea]
├──────[estacion]
├── data
├────[linea]
├──────[estacion]
├── incident
├────[linea]
└──────[estacion]
```

Ejemplo:

```curl
curl --location 'https://api.metromap.online/v1/status/A/san_antonio' \
--header 'secret_key: example'
```

### Mapa

Para acceder a los mapas disponibles, dirígete a <https://embed.metromap.online/> y utiliza cualquiera de las siguientes URLs. Ten en cuenta que deberás incluir una public_key como parámetro GET en tu solicitud.

```bash
v1
└── map
```

Ejemplo:

```curl
curl --location 'https://embed.metromap.online/v1/map?public_key=example'
```


## Guía de Instalación

Descargo de responsabilidad: Este proyecto incluye variables secretas, ya sean propias de la aplicación o utilizadas para conectarse con servicios externos, las cuales no se suben al repositorio GitHub por razones de seguridad. Si bien se proporcionan instrucciones para la instalación y configuración del proyecto, no podemos garantizar que el código funcione correctamente en su entorno local, ya que se necesitan las variables secretas para el funcionamiento correcto del mismo.

- Clonar el repositorio de GitHub.

    ```bash
    git clone https://github.com/danielcgiraldo/ppi_06.git
    ```

A partir de aquí, tienes dos aplicaciones web diferentes para ejecutar, el [Sitio Oficial](https://metromap.online)
y el core de nuestro servicio que contiene la [API](https://api.metromap.online) y el [mapa](https://embed.metromap.online).

### Sitio Oficial

- Dirigirse a la carpeta `site`.

    ```bash
    cd site
    ```

- Instalar las dependencias para correr el proyecto.

    ```bash
    pnpm install
    ```

- Ejecutar el servidor local en modo desarrollo.

    ```bash
    pnpm run dev
    ```

### Core

- Dirigirse a la carpeta `core`.

    ```bash
    cd core
    ```

- Instalar las dependencias para correr el proyecto usando el archivo "requirements.txt".

    ```bash
    pip install -r requirements.txt
    ```

## Autores

| Universidad Nacional de Colombia | 2023-1S |
| --- | --- |
| **Asignatura:** | Programación para Ingeniería |
| **Profesor:** | Gabriel Awad Aubad |
| **Integrante 1:** | [Jesús Porto López](https://github.com/JPortoL) |
| **Correo:** | jporto@unal.edu.co |
| **Integrante 2:** | [Daniel Castillo Giraldo](https://github.com/danielcgiraldo)  |
| **Correo:** | dcastillogi@unal.edu.co |
| **Integrante 3:** | [Santiago Rivera Mejía](https://github.com/SRCrimson)  |
| **Correo:** | sriverame@unal.edu.co |

## Biblografía

- <https://docs.djangoproject.com/>

> Reconocimiento especial a [Chat GPT](https://chat.openai.com/).
