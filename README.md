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

#### f. Módulo de promociones

link: http://localhost:8000/api/promociones/

g. Modulo de gamificacion 
link: http://localhost:8000/api/insignias/
link: http://localhost:8000/api/desafios/
link: http://localhost:8000/api/progresos/

j. Modulo de dashboard
http://localhost:8000/api/dashboard-analitico/



