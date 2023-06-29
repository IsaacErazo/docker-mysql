### DOCUMENTATION
### LAB INSTRUCTIONS

Este laboratorio será implementado con Debian 12 = https://www.debian.org/distrib/netinst

Instalar Docker = https://docs.docker.com/engine/install/debian/

Descargar la última versión de mysql = docker pull mysql

### GUIDE

### CONTAINER
Archivos y configuración de mysql deben almacenarse de forma persistente.

docker run -d -p 9000:3306 \
-v /root/mysql_data:/var/lib/mysql \
-v /root/mysql_config:/etc/mysql/conf.d \
--name mysql_kinder -e MYSQL_ROOT_PASSWORD=secret mysql:latest

