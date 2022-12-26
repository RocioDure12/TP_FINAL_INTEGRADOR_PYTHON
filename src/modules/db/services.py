import pymysql

class DBservices:
    #se establece la conexion
    def connect_db(self)-> pymysql.Connection:
       return pymysql.connect(
            host='localhost',
            port=8306,
            user='root',
            password='123456',
            database='python-backend-concepts',
            cursorclass=pymysql.cursors.DictCursor
)
    
    def execute_db(self, sql:str):
        #conexion a la base de datos
        connection=self.connect_db()
        #crea un cursor para ejecutar consultas SQL
        cursor = connection.cursor()
        #ejecuta una consulta para traer informacion de la tabla participantes
        cursor.execute(sql)
        #cierro cursor
        cursor.close()
        #cierro conexion
        connection.close()    
    
    def query_db(self, sql:str):
         #conexion a la base de datos
        connection=self.connect_db()
        #crea un cursor para ejecutar consultas SQL
        cursor = connection.cursor()
        #ejecuta una consulta para traer informacion de la tabla participantes
        cursor.execute(sql)
        results=cursor.fetchall()
        #cierro cursor
        cursor.close()
        #cierro conexion
        connection.close()   
        return results
        
        