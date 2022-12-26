import pymysql


class DBservices:
    def connect_db():
        pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="prueba_tp",
)