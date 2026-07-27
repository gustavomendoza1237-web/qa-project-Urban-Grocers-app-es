# QA Project — Urban Grocers (API REST)

## Descripción

Proyecto de automatización de pruebas para la API REST de **Urban Grocers**, desarrollado como parte del bootcamp de QA Engineering de TripleTen.

El proyecto automatiza la lista de comprobación de creación de kits personales de usuario (`POST /api/v1/kits`), validando el comportamiento del campo `name` ante distintos casos límite: longitud de caracteres, caracteres especiales, espacios, tipos de datos incorrectos y parámetros faltantes.

## Fuente de documentación

La documentación oficial de la API se encuentra publicada mediante **apiDoc**, en el servidor de prácticas provisto por TripleTen (endpoint `/docs/`).

## Tecnologías y técnicas usadas

- **Python 3**
- **pytest** — framework de pruebas
- **requests** — librería para el envío de solicitudes HTTP
- Técnicas de diseño de pruebas: partición de equivalencia y análisis de valores límite (boundary value analysis)
- Arquitectura de tres capas: datos (`data.py`), configuración (`configuration.py`) y ejecución de solicitudes (`sender_stand_request.py`), separada de los archivos de prueba

## Estructura del proyecto

```
qa-project-Urban-Grocers-app-es/
├── configuration.py              # URL del servidor y rutas de los endpoints
├── data.py                       # Datos de prueba (cuerpos de solicitud)
├── sender_stand_request.py       # Funciones que envían las solicitudes HTTP
├── create_kit_name_kit_test.py   # Pruebas del checklist de creación de kit
├── README.md
└── .gitignore
```

## Cómo ejecutar las pruebas

1. Clona este repositorio y ábrelo en PyCharm (o tu editor de preferencia).
2. Crea un entorno virtual e instala las dependencias:
   ```
   pip install requests pytest
   ```
3. Lanza el servidor de prácticas Urban Grocers desde la plataforma de TripleTen.
4. Copia la nueva dirección del servidor y actualiza la variable `URL_SERVICE` en `configuration.py`.
5. Desde la terminal integrada, ejecuta todas las pruebas del proyecto:
   ```
   pytest
   ```
   O ejecuta únicamente el archivo del checklist de kits:
   ```
   pytest create_kit_name_kit_test.py
   ```

## Nota sobre los resultados

Algunas pruebas del checklist (por ejemplo, los casos de caracteres especiales y espacios) pueden devolver **FAILED** de forma esperada, ya que el comportamiento real de la API no siempre coincide con lo documentado en la lista de comprobación. Esto está documentado y es un resultado válido dentro del alcance de este proyecto.