**Para la ejecución:

$docker-compose build 

$docker-compose up 


**Luego para ejecutar un cliente hacer:

$docker exec -it actividad1_client_{numero_cliente} bash

**y luego ejecutar:

$python client.py

inicialmente son 2 clientes,

**Para incorporar nuevos clientes hacer

$docker build -t <nombre_temporal> .

$docker run -it --network=actividad1_default <nombre_temporal> bash

y realizar el mismo paso para ejecutar el archivo client.py


**Para obtener el listado de usuarios: 'list_users!'

**Para obtener el listado de mensajes: 'list_messages!'

**Para salirse: 'leave!'


Referencias:

https://www.semantics3.com/blog/a-simplified-guide-to-grpc-in-python-6c4e25f0c506/

https://rancher.com/learning-paths/how-to-build-and-run-your-own-container-images/

https://giovannicortes.com/entrar-a-un-contenedor-docker-con-bash/

https://github.com/salesforce/reactive-grpc/issues/55 (timestamp protobuf)


