# docker-mysql

Este laboratorio será implementado con Debian 12 = https://www.debian.org/distrib/netinst


docker run -d -p 9000:3306 \
-v /root/mysql_data:/var/lib/mysql \
-v /root/mysql_config:/etc/mysql/conf.d \
--name mysql_kinder -e MYSQL_ROOT_PASSWORD=secret mysql:latest

