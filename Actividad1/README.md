Para la ejecución:

$docker-compose build 

$docker-compose up 


Luego para ejecutar un cliente hacer:

$docker exec -it actividad1_client_{numero_cliente} bash

y luego ejecutar:

$python client.py

inicialmente son 2 clientes,

Para incorporar nuevos clientes hacer

$docker build -t <nombre_temporal> .

$docker run -it --network=actividad1_default <nombre_temporal> bash

y realizar el mismo paso para ejecutar el archivo client.py


Referencias:

https://www.semantics3.com/blog/a-simplified-guide-to-grpc-in-python-6c4e25f0c506/

