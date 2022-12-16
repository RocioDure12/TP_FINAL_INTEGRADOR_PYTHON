"""El gobierno de la Ciudad de Buenos Aires necesita implementar un control de covid en un encuentro
de programadores. Para esto necesita pedir la temperatura de cada persona, el nombre y dni.
El resultado del control debe listar a todas las personas que ingresaron (temperatura menor a 37
grados) y también listar las personas que no pudieron ingresar, indicando un mensaje que fue
derivado a un hospital. Calcular el número de personas que ingresaron y el número de personas que
no ingresar por presentar síntomas de covid.
Para la implementación utilizar lenguaje de programación Python. Aplicar lo visto en clase: listas,
diccionarios, funciones, librerías (opcional gráficas), base de datos

El modo de trabajo puede ser individual o grupal, en la última clase de la semana del 12 al 16 de
diciembre de 2022 exponen los que quieran compartir sus resoluciones
"""
"""
Datos de entrada: temperatura de c/persona, nombre, dni
Datos de salida: resultado de control (todos)
Variables: temperatura, nombre, dni etc

Problema 1 pedir temperaturas y agruparlas (todos)
Problema 2 agrupar o listar los que tienen mas de 37° indicando con un mensaje que fue derivado a un hospital
Problema 3 calcular el n° de personas que ingresaron
Problema 4 calcular el numero de personas que no pudieron ingresar por presentar sintomas

IDEAS SOBRE EL PROBLEMA
CLASE INVITADO/PARTICIPANTE/PERSONA
ATRIBUTOS DNI, NOMBRE, TEMPERATURA

GUARDAR EN BASE DE DATOS TABLA CON INFORMACION DE LOS PARTICIPANTES
"""
# Crea una conexión a la base de datos
import pymysql
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="prueba_tp",
)

# crea un cursor para ejecutar consultas SQL
cursor = connection.cursor()


class Participante():
    def __init__(self, nombre, apellido, dni, temperatura, id=None):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.temperatura = temperatura
        self.id=id


nombre = (input("Ingrese su nombre: "))
apellido = (input("Ingrese su apellido: "))
dni = input("Ingrese su dni: ")
temperatura = input("Temperatura: ")


def insertar_info(p):

    sql = f"INSERT INTO participantes(nombre,apellido,dni,temperatura) VALUES('{p.nombre}','{p.apellido}', '{p.dni}', {p.temperatura})"
    cursor.execute(sql)
    connection.commit()


# instanciar un objeto
participante = Participante(nombre, apellido, dni, float(temperatura))

insertar_info(participante)

"""
Funcion que haga la consulta a la base de datos y traiga los participantes
parametro opcional para poder filtrar por temperatura minima
"""


def lista_resultados(consulta):
    # ejecuta una consulta para traer informacion de la tabla participantes
    query = consulta
    cursor.execute(query)
    # obtiene todos los resultados de la consulta
    resultados = cursor.fetchall()
    # recorre los resultados 
    participantes=[]
    for fila in resultados:
        participante = Participante(fila[1], fila[2], fila[3], fila[4], fila[0])
        participantes.append(fila)
    return participantes
    # cierra el cursor y la conexion a la base de datos
    #cursor.close()
    #connection.close()


lista_de_participantes=lista_resultados('SELECT * from participantes')
invitados_temperatura_alta=lista_resultados('SELECT * FROM participantes WHERE temperatura > 37')



print("La cantidad de invitados que ingresaron en el evento es:",len(lista_de_participantes)-len(invitados_temperatura_alta))
print("La cantidad de personas que no pudieron ingresar al evento por sintomas y fueron derivados a un hospital es de:", len(invitados_temperatura_alta))


