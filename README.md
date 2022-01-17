# Prueba tecnica Foodin

Si se ejecuta en Windows, cambiar el tipo de salto de linea de CRLF a LF al archivo
>backend\django\entrypoint.sh

ya que genera el siguente error cuando se encuentra en CRLF

>standard_init_linux.go:228: exec user process caused: no such file or directory

Ejecutar 
> docker compose up

Para  inicializar las apps.

Ingresar a [http://localhost:7070/admin](http://localhost:7070/admin) para loguearse y posteriormente a [http://localhost:7070/api/v1/product](http://localhost:7070/api/v1/product) para consultar los endpoints.

Importar a Postman el archivo
> FoodinApi.postman_collection.json
