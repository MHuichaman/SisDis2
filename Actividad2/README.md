En esta actividad de usa RabbitMQ


Para la ejecución:

$docker-compose build

$docker-compose up --scale client=2  #generará 2 clientes de forma inmediata con la configuración de docker


**Luego para ejecutar un cliente hacer:**

$docker exec -it actividad1_client_{numero_cliente} bash

**y luego ejecutar:

$python client.py


**Para incorporar nuevos clientes hacer

$docker build -t <nombre_temporal> .

$docker run -it --network=actividad1_default <nombre_temporal> bash

y realizar el mismo paso para ejecutar el archivo client.py

**Para obtener el listado de usuarios: 'list_users!'

**Para obtener el listado de mensajes: 'list_messages!'

**Para salirse: 'leave!'



Esperar al siguiente mensaje en consola:

*****    ... user 'guest' authenticated and granted access to vhost '/' *******

Luego para ejecutar un cliente hacer: docker exec -it actividad2_client_1 bash

Eso por ahora
