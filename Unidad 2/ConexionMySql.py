import mysql.connector
from mysql.connector import errorcode

try:
    cnx = mysql.connector.connect(user='root', password='',
        host='127.0.0.1',
        database='d_n2_p12_c1')

    print('Conexion MySql Establecida Correctamente!')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)



cnx.close()
#INSERT INTO TBL_AUTOS VALUES()
#SELECT * FROM TBL_AUTOS