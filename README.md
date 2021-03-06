# API_JOOPbox

 ## Lenguaje de programación (Python):

    He escogido Python como lenguaje para programar esta API, ya que coincide en que en este momento en las clases de Programación estamos viendo como crear una, y así poder reutilizar código en el caso de que lo necesite y aplicar tanto metodologías como las buenas prácticas que nos están enseñando.

 ## Enunciado:

<ul>
    <li>
        Hemos recibido una lista de contactos que viene de una transformación de datos procedente de un antiguo CSV.
    </li>
    <li>
        Para integrar estos contactos a nuestra aplicación de gestión, necesitamos que cada uno de ellos siga un esquema definido para la base de datos, pero ha habido problemas al importar los datos que nos indica que el proceso de transformación al formato JSON no ha sido correcto.
    </li>
    <li>
        Necesitamos poder filtrar aquellos que estén bien definidos para agregar a nuestra cartera de contactos, y separar aquellos que causan errores para analizarlos posteriormente.
    </li>
</ul>

 ## Objetivo:

Diseñar una API que analiza un bloque de datos que llegan en el archivo `data.json`,
para filtrar aquellos elementos que siguen un esquema definido con la llamada GET /list y aquellos que no con GET /failed.

 ### Estructura (json-schema):

```json
{
  "type": "object",
  "properties": {
    "name":     { "type": "string" },
    "id":       { "type": "string" },
    "phone_number": { "type": "number" },
    "street_name":  { "type": "string" },
    "street_type":  {
      "type": "string",
      "enum": ["Street", "Avenue", "Boulevard","Square", "Other"]
    },
    "birth_date":  { "type": "string" },
    "email":  { "type": "string" },
    "interests": {
      "type": "array",
      "items": { "type": "string" }
    }
  },
  "required": ["name","id","phone_number"],
  "additionalProperties":false
}

```

 ## Proyecto:

 - Crea el directorio y sitúate en él:

    ```bash
    $ mkdir API_JOOPbox
    $ cd API_JOOPbox
    ```

- Clona el projecto:

    `git clone https://github.com/gasparnovel/API_JOOPbox/tree/develop`

- Inicializa el entorno virtual y actívalo.

    ```bash
    $ python -m venv venv
    $ .\venv\Scripts\activate
    ```

- Instala el proyecto:

  `$ pip3 install API_JOOPbox-0.0.1-py3-none-any.whl`

 - Sitúate en el directorio y ejecuta flask:

    ```bash
    $ cd src
    $ flask run
    ```

 ## Código externo:

Guía de la estructura de directorios para la contrucción de la API:

\-[David Gelpi API](https://github.com/dfleta/api-rest-gildedrose/blob/master/README.md)

\-[David Gelpi tdd](https://github.com/dfleta/kata_tdd_pytest)

 ## Librerias:

https://palletsprojects.com/p/flask/

https://flask-restful.readthedocs.io/en/latest/

https://pypi.org/project/jsonschema/