Para la ejecución:

$docker-compose build
$docker-compose up --scale client=2  #generará 2 clientes de forma inmediata con la configuración ya provista


Esperar al siguietne mensaje:

*****    ... user 'guest' authenticated and granted access to vhost '/' *******

Luego para ejecutar un cliente hacer: docker exec -it actividad2_client_1 bash

Eso por ahora
