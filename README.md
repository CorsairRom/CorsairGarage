# CorsairGarage
Esta es una pagina creada para mi taller, donde actualmente presto servicios de reparacion de motocicletas

## Inicio

![App Screenshot](https://i.postimg.cc/6pVX090j/imagen-2023-04-25-011816140.png)

![App Screenshot](https://i.postimg.cc/T2BbgtL0/imagen-2022-12-21-180057857.png)

![App Screenshot](https://i.postimg.cc/tJ6YBHZ5/imagen-2022-12-21-180201325.png)

## Inicio
<p> La idea final de esta pagina es tener una aplicacion que permita agendar visitas al taller, como tambien crear cotizaciones para que el cliente,  </p>
<p> tenga una idea clara de cuanto es el costo de reparacion de su motocicleta.  </p>


## Inicio Sesion

<p>Podemos Dirigirnos al inicio sesion precionando en el icono de persona: </p>

![App Screenshot](https://i.postimg.cc/fbvr3yKs/imagen-2023-04-25-011513924.png)


<p>Ingresamos nuestras crendencias, iniciamos sesion y si nuestras credenciales son validas se nos redirigira al dashboard </p>

![App Screenshot](https://i.postimg.cc/NFZJhHg6/imagen-2023-04-25-011606475.png)

## Dashboard
<p>La pagina sigue avanzando esta ves agregandon un dashboard con distintas funcionalidades, como la de registrar clientes, motocicletas y fichas de ingreso.</p>

![App Screenshot](https://i.postimg.cc/J4KrN1W0/imagen-2023-02-21-183015187.png)


<p>Podemos consultar por el rut de un cliente para ver si se encuentra registrado, en el caso que no se encuentre en la base de datos un mensaje de alerta para registrarlo </p>

![App Screenshot](https://i.postimg.cc/xTVbN9VB/imagen-2023-02-21-183822095.png)

<p>Formulario de registro</p>

![App Screenshot](https://i.postimg.cc/Y060zmBZ/imagen-2023-02-21-183907170.png)

<p>En esta sección se pueden visualizar las motocicletas que reguistra cada cliente y generar una ficha de ingreso</p>

![App Screenshot](https://i.postimg.cc/KvsSs8cH/imagen-2023-02-21-184055913.png)

<p>En esta parte podemos agregar los servicios que se necesiten para la reparacion de la motocicleta, estos servicios se encuentran registrados en la base de datos</p>

![App Screenshot](https://i.postimg.cc/G2zS8XH5/imagen-2023-02-21-184412235.png)

<p>La misma pagina nos va agregando el precio ppor cada servicio y las horas necesarias, esta informacion es tomada de la base de datos donde se hace un calculo de horas segun el codigo de este y la cilindrada de la motocicleta, de esta forma se estima el precio justo para la reparacion de ese servicio en particular, al final se puede ver el subtotal el cual se le puede aplicar un descuento precionando el boton de descuento</p>

![App Screenshot](https://i.postimg.cc/W3p5v0X6/imagen-2023-02-21-184517060.png)

<p>Descuento</p>

![App Screenshot](https://i.postimg.cc/K8BbkyFp/imagen-2023-02-21-184742279.png)

<p>Por ultimo tenemos dos caminos, generar la orden de trabajo para esta ficha en particular, o imprimir la ficha actual en formato pdf.</p>

![App Screenshot](https://i.postimg.cc/qvsfBXX9/imagen-2023-02-21-184916365.png)

## Faltante:

<p>Estoy trabajando en una forma de generar un formulario el cual me permita regular válvulas de forma más rápida, me permita calcular cual es la pastilla de regulación que debo reemplazar para poder cumplir con la informacion del fabricante.</p>

<p>Tambien tengo que trabajar en la orden de trabajo, ya que la ficha de ingreso es temporal, durante la reparacion pueden aparecer mas servicios por aplicar las cuales no se detectan en la primera inspeccion de la motocicleta. Esta parte sera una herramienta para el mecanico a cargo de la reparacion el cual podra usar para agregar comentarios y horas realizadas de forma extra. Esta parte esta pensada que funcione mediante aplicacion movil y usar django como rest-api</p>

<p>Otro punto es mejorar la estetica, este punto lo dejare al final</p>
