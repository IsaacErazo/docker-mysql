from faker import Faker
from mysql.connector import Error
import mysql.connector

fake = Faker()
# data = []
# for _ in range(100):
#     data.append((_, fake.name(), fake.company(), fake.job()))



try:
    connection = mysql.connector.connect(
        host='192.168.1.19',
        port=9000,
        user='root',
        password='secret',
        db='demo'
    )

    # if connection.is_connected():
    #     cursor = connection.cursor()
    #     cursor.executemany("""INSERT INTO PROFESORES (nombre, nacionalidad,ingreso) 
    #                             VALUES (%s, %s, %s)""", data)
    #     if (len(data) == cursor.rowcount):
    #         connection.commit()
    #         print("{} rows inserted.".format(len(data)))
    #     else:
    #         connection.rollback()
except Error as ex:
    print("Error during connection: {}".format(ex))
# finally:
#     if connection.is_connected():
#         connection.close()
#         print("Connection closed.")

if connection.is_connected():    
    cursor = connection.cursor()

    for _ in range(100):
        query = 'INSERT INTO PROFESORES (nombre, nacionalidad,ingreso,telefono) VALUES (%s, %s, %s, %s)'
        values = (fake.name(), fake.country(), fake.date(), fake.phone_number())     
        cursor.execute(query,values)
        connection.commit()
    print("Profesores done")
    # if (len(data) == cursor.rowcount):
    #     connection.commit()
    #     print("{} rows inserted.".format(len(data)))
    # else:
    #     connection.rollback()

    for _ in range(100):
        query = 'INSERT INTO PADRES (nombre, nacionalidad, direccion, telefono) VALUES (%s, %s, %s, %s)'
        values = (fake.name(), fake.country(), fake.address(), fake.phone_number())     
        cursor.execute(query,values)
        connection.commit()
    print("Padres done")

    for _ in range(100):
        query = 'INSERT INTO ESTUDIANTES (nombre, nacionalidad, fecha_nacimiento, padre_id) VALUES (%s, %s, %s, %s)'
        values = (fake.name(), fake.country(), fake.date(), _+1)     
        cursor.execute(query,values)
        connection.commit()
    print("Estudiantes done")

    for _ in range(100):
        query = 'INSERT INTO MATRICULAS (periodo,desempeño,pago,fk_estudiante_id) VALUES (%s, %s, %s, %s)'
        values = (fake.year(),'bueno', fake.pyfloat(right_digits=2, positive=True, min_value=1000, max_value=2000), _+1)     
        cursor.execute(query,values)
        connection.commit()
    print("Matriculas done")

    for _ in range(100):
        query = 'INSERT INTO CALIFICACIONES (fk_estudiante_id2, lectura, dibujo, deporte, idioma, musica, razonamiento, asistencia) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
        values = (_+1,
                  fake.pyfloat(right_digits=1, positive=True, min_value=5, max_value=10),
                  fake.pyfloat(right_digits=1, positive=True, min_value=5, max_value=10),
                  fake.pyfloat(right_digits=1, positive=True, min_value=5, max_value=10),
                  fake.pyfloat(right_digits=1, positive=True, min_value=5, max_value=10),
                  fake.pyfloat(right_digits=1, positive=True, min_value=5, max_value=10),
                  fake.pyfloat(right_digits=1, positive=True, min_value=5, max_value=10),
                  fake.pyfloat(right_digits=1, positive=True, min_value=5, max_value=10))
        cursor.execute(query,values)
        connection.commit()
    print("Calificaciones done")

connection.close()
print("Connection closed.")
