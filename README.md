Proyecto blog para coderhouse

Nuestra aplicacion consta de Registrar un usuario que lo guardaria en la BD.
Una vez registrado ingresaria en la parte de Logearse(iniciar sesion),  para luego poder realizar un Post.
El Post puede ser visto en el Feed, tanto del propio usuario y de los usuarios que hallan realizado un Post.
El usuario tambien cuenta con un Perfil propio y luego de logear al usuario se abre una funcion donde puede registrar "ejercicios" para realizar y luego es guardado.

1. Herencia de HTML:
Se encuentra dentro de una carpeta "templates", donde LOS HTML padres son:
-layout.html, que lo heredan feet.html y profile.htl
-formulariobase.html, que lo heredan todos los formularios.
2. Por lo menos 3 clases en models.
Las clases estan dentro de la carpeta de la App, donde se encuentran:
-class Perfil
-class Posteado
-class Ejercicio
3. Un formulario para insertar datos a todas las clases de tu models.
Los formularios los puedes ver en view.py y forms.py, estos son:
-class Registrousuario (localhost/ingreso)
-class EjercioForm(localhost/nuevoejercicio)
-class Nuevopost(localhost/newpost)
4. Un formulario para buscar algo en la BD
este formulario se encuentra en:
-localhost/ingreso, se realizo con ayuda de un función interna de django que es LoginView y con el html ingreso.html.
Este formulario busca en la BD y valida que el usuario este registrado dentro de la misma.

