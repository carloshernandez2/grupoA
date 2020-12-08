# Sistema de inventarios para cafetería

## Tabla de contenidos

* [Introducción al problema](##Introducción-al-problema)
* [Funcionalidades](##Funcionalidades)
* [Busqueda](##Busqueda)
* [Tecnologías](##Tecnologias)

## Introducción al problema

Actualmente nuestra problemática consiste en que ocasionalmente no contamos con
el estado real del inventario de la cafetería (bebidas, mekatos) en un momento dado,
lo cual genera interrupciones en la prestación de servicio del establecimiento, ya que
de forma inesperada queda sin stock, sobretodo de los productos más vendidos, esto
sin duda alguna genera malestar entre nuestros clientes, lo cual podría significar el
retiro de la clientela por los continuos faltantes que se presentan. Para resolver la
anterior problemática, requerimos de una aplicación web para la gestión del inventario
de los productos de nuestra tienda, la cual nos permita conocer en cualquier momento
el stock disponible en bodega y proyectarlo respecto a las ventas por dia.

## Funcionalidades

### Registro de usuarios

Este registro solo debe ser realizado por el usuario
administrador, el cual se supone que es una cuenta que existe desde el
despliegue de la aplicación. Para este registro, el administrador debe ingresar
a la plataforma y luego seleccionar la opción registrar, en donde debería
suministrar la siguiente información para registrar un nuevo usuario: nombre
de usuario, contraseña y correo electrónico. La aplicación debe enviar un e-mail al correo del nuevo usuario registrado con las credenciales asignadas.

### Portal de acceso

Proveer un portal de acceso, donde los usuario puedan acceder a la aplicación,
si se autentican, usando usuario y contraseñas, exitosamente. Esto debe
cumplir con los requerimientos mínimos de seguridad.

### Recuperar contraseña

Ofrecer la opción para recuperar la contraseña en caso de olvido para los
usuarios. Esta opción puede ser implementada, por ejemplo, por medio del
envío de un e-mail al correo electrónico registrado para el usuario

### Creación, actualización y eliminación de productos

Ofrecer la opción para la creación, actualización y eliminación de productos.
Esto solo debe ser realizado por el usuario administrador. Es decir, el usuario
administrador puede crear, actualizar y/o dar de baja a un producto. En la
creación de un artículo se debería ingresar referencia (un identificador para el
producto), nombre del producto, cantidad, y una imagen del producto.

## Busqueda

* Un usuario autenticado puede buscar una producto por caracteres en el
nombre y esta búsqueda mostrará una galería de imágenes que corresponda.
* Un usuario autenticado puede actualizar las cantidades de un producto
particular. Es decir, se debe permitir actualizar la cantidad de un producto
haciendo click en la respectiva imagen del producto.

## Tecnologías

1. Python 3.9.0
2. Flask 1.1.2
3. Bootstrap 4
