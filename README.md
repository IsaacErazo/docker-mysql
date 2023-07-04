### Requerimientos para el laboratorio

Este laboratorio será implementado con Debian 12, descargar la imagen desde su oficial = https://www.debian.org/distrib/netinst

Instalar Docker desde su sitio oficial = https://docs.docker.com/engine/install/debian/

Descargar mysql contenerizada = docker pull 0xdani/mysql

En la máquina host se deberá descargar python y el módulo faker.

### Contenedor

Ejecutar el siguiente comando para inicializar la instancia del contenedor de MySQL.
Se deben crear los siguientes directorios para almacenar la información y la configuración de la base de datos de forma persistente. /root/mysql_data, /root/mysql_config.

docker run -d -p 9002:3306 \
-v /root/mysql_data:/var/lib/mysql \
-v /root/mysql_config:/etc/mysql/conf.d \
-e MYSQL_ROOT_PASSWORD=secret 0xdani/mysql:1.0

### Base de datos

Ejecutar los comandos de DB.sql para crear la base de datos y las tablas

Ejecutar Privileges.sql para crear roles y asignarlos a usuarios

En python ejecutar random_data.py para agregar información a las tablas de la base de datos.
