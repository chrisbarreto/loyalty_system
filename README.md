# Examen Final

# Arquitectura Web

## ENUNCIADO 1: SISTEMA DE FIDELIZACIÓN DE CLIENTES

### Integrantes:

- Agustín Escobar Giménez
- Mariela Monserrat Fernández González
- Dafne Aylen Torrez Vera
- Christian David Barreto Barrios

#### a. Segmentación de Clientes:

Para probar correctamente se debe crear primero el o los cliente/s:

link: http://127.0.0.1:8000/api/clientes/

Luego de crear el cliente, se debe crear el o los criterios para la segmentación, está configurado para que sea por rango de edad. Para ello se solicita una descripción, la edad mínima y máxima:

link: http://127.0.0.1:8000/api/segmentacion/criterios/

Para que se identifiquen los clientes cargados que van en cada segmentación o rango de edad, se carga en la tabla de segmentaciones...utilizando el siguiente método (se puede probar desde el shell de python: python manage.py shell):

from segmentacion.models import Segmentacion

Segmentacion.segmentar_por_edad()

Con dicho método se completará automáticamente la tabla

Para la carga de los beneficios que obtiene cada rango de edad o criterio, se cargan en:

link: http://127.0.0.1:8000/api/segmentacion/beneficios/

#### b. Niveles de Fidelización:

link: http://localhost:8000/api/niveles/

El método para determinar el nivel actual del cliente se encuentra en:
Loyalty_system/clientes/models.py

```[python]
    def nivel(self)
        ....
```

Los beneficios se pueden crear con el módulo 'beneficios'
de forma simple

link: http://localhost:8000/api/beneficios/

O con el módulo 'promociones' correspondiente al ítem 'f'

link: http://localhost:8000/api/promociones/

**Pruebas**

link: https://www.postman.com/mission-administrator-12973138/workspace/pruebas-final

- Ejecutar la colección niveles

- Ejecutar la colección clientes

- Modificar las id de clientes en la colección bolsaPuntos y ejecutar

- Ejecutar la colección beneficios

#### d. Integración con Plataformas de Pago:

Pasos para prueba:
Paso 1 : Crear cliente(POST)

http://127.0.0.1:8000/api/clientes/

Ejemplo:
{
"nombre": “juan”,
"apellido": “Perez”,
"numero_documento": “123456-1”,
"tipo_documento": "RUC",
"nacionalidad": "Paraguaya",
"email": “juanperez@mail.com",
"fecha_nacimiento": "1990-01-30"
}

http://127.0.0.1:8000/api/reglas/

Paso 2 : Crear Regla(POST)

{
"limite_inferior": 50000,
"limite_superior": 100000,
"monto": 60000
}

http://127.0.0.1:8000/api/realizar_pago/

Paso 3 : Crear Regla(POST)

{
"cliente_id": 3,
"monto": 100000,
"metodo_pago": “paypal”
}

Paso adicional: Ver bolsa de Puntos(GET)

http://127.0.0.1:8000/api/bolsapuntos/

#### e. API

link: http://localhost:8000/api/niveles/

link: http://127.0.0.1:8000/api/clientes/

link: http://localhost:8000/api/beneficios/

**Pruebas**

link: https://www.postman.com/mission-administrator-12973138/pruebas-final

Si no existen registros:

- Ejecutar la colección Niveles

- Ejecutar la colección Beneficios

- Ejecutar la colección Clientes

Para probar la API: Ejecutar la colección API

#### f. Módulo de promociones

link: http://localhost:8000/api/promociones/

**Pruebas**

Ejecutar la colección Niveles

Ejecutar la colección Promociones

#### g. Modulo de gamificacion

link: http://localhost:8000/api/insignias/
ejemplo
{
     "id": 1,
     "nombre": "Primera Compra",
     "descripcion": "Otorgada por realizar la primera compra",
     "imagen": "ruta_imagen",
     "puntos_requeridos": 100,
     "creado_en": "2024-01-01T10:00:00Z"
}


link: http://localhost:8000/api/desafios/
ejemplo
{
    "titulo": "Meta Semanal",
    "descripcion": "Acumula 500 puntos esta semana",
    "meta_puntos": 500,
    "fecha_inicio": "2024-01-01T00:00:00Z",
    "fecha_fin": "2024-01-07T23:59:59Z"
}


link: http://localhost:8000/api/progresos/
ejemplo
{
    "usuario": 1,  # ID del usuario
    "desafio": 1,  # ID del desafío
    "puntos_acumulados": 150,
    "completado": false
}


#### h. Sistema de Referidos

Pasos para prueba

Crear un cliente(POST) con el id de cliente referido(debe ser un cliente ya creado en el sistema)

http://localhost:8000/api/clientes/

Ejemplo
{
"nombre": "lidia",
"apellido": "martinez",
"numero_documento": "744332",
"tipo_documento": "CI",
"nacionalidad": "Paraguaya",
"email": "lidiatr@mail.com",
"telefono": "098222312",
"fecha_nacimiento": "1970-05-10",
"referido_por": 2  
}

Ver Bolsa de puntos(GET) para ver los puntos asignados a cliente nuevo y al referido

http://localhost:8000/api/bolsapuntos/

#### j. Modulo de dashboard

http://localhost:8000/api/dashboard-analitico/ 


