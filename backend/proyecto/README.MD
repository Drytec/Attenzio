
###  para probar la vista renderizados y funcionalidad
```
En la terminal abren la carpeta backend "cd backend"
siguiendo en la terminan escriben "python manage.py runserver"
ya con este comando pueden ver todo lo relacionado a las vistas y el servidor

```
### cambios a los modelos 
```
En la terminal abren la carpeta backend "cd backend"
En caso de que hagan alguna modificacion a algun modelo y corran el servidor 
les dara error, para que todo funcione correctamente tienen que escribir
en la terminal "python manage.py makemigrations" lo que hace es una especie
de commit de los cambios que realicen al modelo en la bd, aunque como
usaremos postgres es posible que no sea necesario cuando se implemente.
despues escriban "python manage.py migrate" que hara el "push" de los cambios
a la base de datos
```
### cambios que necesita el proyecto
```
Por ahora hace falta actualizar todo lo relacionado a "aula" por
sesion.
hay que cambiar los html usando react @esgore03 y arreglar la ruta
ya que se encuentran en un lugar poco conveniente las plantillas.
hay que implementar todo lo relacionado a la app mobile.
hay que implementar las preguntas tanto para profesor como estudiante.
hay que implementar la funcion de qr.
la verificacion de registro de usuario por el admin(ya esta casi implementado)
Las vistas por ahora solo renderizan los request que manda el servidor preferiblemente
hay que añadir el json a eso (aun hay que investigar)

``` 