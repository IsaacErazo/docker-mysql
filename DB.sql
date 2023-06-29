DROP DATABASE demo;
create database demo;

use demo;
CREATE TABLE PROFESORES(
profesor_id INTEGER NOT NULL AUTO_INCREMENT,
nombre varchar(100),
nacionalidad varchar(100),
ingreso varchar(20),
telefono varchar(25),
PRIMARY KEY (profesor_id)
);

Create table PADRES(
padre_id INTEGER NOT NULL AUTO_INCREMENT,
nombre varchar(100),
nacionalidad VARCHAR(100),
direccion VARCHAR(100),
telefono varchar(25),
PRIMARY KEY (padre_id)
);

CREATE TABLE ESTUDIANTES(
estudiante_id INTEGER NOT NULL AUTO_INCREMENT,
nombre varchar(100),
nacionalidad VARCHAR(100),
fecha_nacimiento DATE,
padre_id INTEGER NOT NULL,
PRIMARY KEY (estudiante_id),
CONSTRAINT padre_id FOREIGN KEY (padre_id) REFERENCES PADRES(padre_id)
);

CREATE TABLE MATRICULAS(
matricula_id INTEGER NOT NULL AUTO_INCREMENT,
periodo INTEGER,
desempeño VARCHAR(50),
pago DECIMAL(6,2),
fk_estudiante_id INTEGER NOT NULL,
PRIMARY KEY (matricula_id),
CONSTRAINT fk_estudiante_id FOREIGN KEY (fk_estudiante_id) REFERENCES ESTUDIANTES(estudiante_id)
);

CREATE TABLE CALIFICACIONES(
fk_estudiante_id2 INTEGER,
lectura DECIMAL (2,1),
dibujo DECIMAL (2,1),
deporte DECIMAL (2,1),
idioma DECIMAL (2,1),
musica DECIMAL (2,1),
razonamiento DECIMAL (2,1),
asistencia DECIMAL (2,1),
CONSTRAINT fk_estudiante_id2 FOREIGN KEY (fk_estudiante_id2) REFERENCES ESTUDIANTES(estudiante_id)
);