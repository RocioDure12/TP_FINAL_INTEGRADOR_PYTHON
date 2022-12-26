import pymysql
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="prueba_tp",
)

cursor = connection.cursor()

class Participante():
    def __init__(self, nombre, apellido, dni, temperatura, id=None):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.temperatura = temperatura
        self.id=id

def insertar_info(p):
    sql = f"INSERT INTO participantes(nombre,apellido,dni,temperatura) VALUES('{p.nombre}','{p.apellido}', '{p.dni}', {p.temperatura})"
    cursor.execute(sql)
    connection.commit()
    
def lista_resultados(consulta):
    query = consulta
    cursor.execute(query)
    resultados = cursor.fetchall()
    participantes=[]
    for fila in resultados:
        participante = Participante(fila[1], fila[2], fila[3], fila[4], fila[0])
        participantes.append(fila)
    return participantes

def mostrar_menu():
    print("1. Cargar nuevo participante ")
    print("2. Editar participante")
    print("3. Eliminar participante")
    print("4. Listado partipantes ")
    print("5. Listar participantes con sintomas")
    print("6. Listar participantes sin sintomas")
    print("7. Salir ")


opcion = 0
while opcion != 7:
    mostrar_menu()
    opcion = int(input("Ingrese opcion: "))
    if opcion == 1:
        nombre = (input("Ingrese su nombre: "))
        apellido = (input("Ingrese su apellido: "))
        dni = input("Ingrese su dni: ")
        temperatura = input("Temperatura: ")
        participante = Participante(nombre, apellido, dni, float(temperatura))
        insertar_info(participante)
    elif opcion == 2:
        id=int(input("Ingrese el id del participante a editar: "))
        nombre = (input("Ingrese su nombre: "))
        apellido = (input("Ingrese su apellido: "))
        dni = input("Ingrese su dni: ")
        temperatura = input("Temperatura: ")
        participante = Participante(nombre, apellido, dni, float(temperatura))
        cursor.execute("UPDATE participantes SET nombre = %s,apellido = %s, dni=%s, temperatura=%s WHERE id = %s", ({nombre},{apellido},{dni},{temperatura}, (id)))
        connection.commit()
    elif opcion == 3:
        id=int(input("Ingrese el id del participante a eliminar:"))
        cursor.execute("DELETE FROM participantes WHERE id = %s", (id,))
        connection.commit()
    elif opcion == 4:
        lista_de_participantes=lista_resultados('SELECT * from participantes')
        for tupla in lista_de_participantes:
            print(tupla, end="\n")
    elif opcion == 5:
        invitados_temperatura_alta=lista_resultados('SELECT * FROM participantes WHERE temperatura > 37')
        for tupla in invitados_temperatura_alta:
            print(tupla, end="\n")
    elif opcion == 6:
        invitados_temperatura_normal=lista_resultados('SELECT * FROM participantes WHERE temperatura <=37')
        for tupla in invitados_temperatura_normal:
            print(tupla, end="\n")
    elif opcion == 7:
        print("has elegido salir")
    else:
        print("opcion invalida")
