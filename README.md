# Teclados
Teclados Twitterbot

Bot de Twitter con ChatGPT
Este proyecto es un bot de Twitter que utiliza la API gratuita de ChatGPT para generar tweets.

Características
El código se ejecuta en un contenedor Docker
El contenedor se arranca mediante `docker-compose`
La aplicación está escrita en Python
Utiliza la API gratuita de ChatGPT para generar tweets
Requisitos previos
Instalar `docker` y `docker-compose` en tu sistema operativo
Crear un entorno virtual de Python (`venv`) y activarlo
Instalar las dependencias necesarias mediante pip: `flask`, `requests`, `chatgpt`
Configuración del proyecto
Clona este repositorio a tu sistema operativo.
Activá el entorno virtual de Python (`venv`).
Crea un archivo llamado `.env` en la raíz del proyecto y agrega tu clave de API de ChatGPT (free version) al siguiente formato: `CHATGPT_API_KEY="TU_CLAVE_DE_API"`.
Ejecuta `docker-compose build` para construir el contenedor.
Ejeuta `docker-compose up -d` para arrancar el contenedor.
Uso del proyecto
Ingresa al contenedor mediante `docker exec -it twitterbot /bin/bash`.
Entra a la carpeta `/app` y ejecuta `python app.py` para arrancar la aplicación.
Puedes enviar un request POST con el cuerpo JSON `{ "prompt": "TU_PROMPT" }` al puerto 5000 del contenedor (http://localhost:5000) para generar un tweet.
Contribución
Si deseas contribuir a este proyecto, por favor abre una Issue en este repositorio. Los cambios pueden ser enviados mediante Pull Request.

Licencia
Este proyecto se distribuye bajo la licencia MIT.
