#AGENDA CONTACTOS

#Conexion a la Base de Datos
import sqlite3
db = sqlite3.connect("cb_contactos.sqlite3")
cursor = db.cursor()

#Creacion tabla base de datos
cursor.execute("""
CREATE TABLE IF NOT EXISTS Contactos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    numero TEXT  
)
""")

#Creación del Menú y las funciones
def buscarContacto():
    nombre = input("Ingresa el nombre que deseas buscar: ")

    cursor.execute("SELECT * FROM Contactos WHERE nombre LIKE ?", (f'%{nombre}%',))
    contactos = cursor.fetchall()
    if len(contactos) == 0:
        print("No se encontraron contactos")
    else:
        print("\nLista de Contactos Encontrados:")
        for contacto in contactos:
            id = contacto[0]
            nombre = contacto[1]
            numero = contacto[2]

            print(f"{id:<5} - {nombre:15} - {numero:14}")

def listarContactos():
    cursor.execute("SELECT * FROM Contactos")
    contactos = cursor.fetchall()
    if len(contactos) == 0:
        print("No se encontraron contactos")
    else:
        print("\nLista de Contactos:")
        for contacto in contactos:
            id = contacto[0]
            nombre = contacto[1]
            numero = contacto[2]

            print(f"{id:<5} - {nombre:15} - {numero:14}")

def agregarContacto():
    nombre = input("Ingresa el nombre del nuevo contacto: ")
    numero = input("Ingresa el numero del nuevo contacto: ")

    cursor.execute("INSERT INTO Contactos (nombre, numero) VALUES(?, ?)", (nombre, numero))
    
    db.commit()

    print("Contacto agregado exitosamente\n")

def editarContacto():
    cursor.execute("SELECT * FROM Contactos")
    contactos = cursor.fetchall()
    print("\nLista de Contactos:")
    for contacto in contactos:
        id = contacto[0]
        nombre = contacto[1]
        numero = contacto[2]

        print(f"{id:<5} - {nombre:15} - {numero:14}")

    id = int(input("Ingresa el id del contacto que deseas editar: "))
    opcion_editar = int(input("""Ingresa la opcion que deseas editar:
[1] Nombre
[2] Numero
"""))
    if opcion_editar == 1:
        nombre = input("Ingresa el nuevo nombre: ")
        cursor.execute("UPDATE Contactos SET nombre = ? WHERE id = ?", (nombre, id))
    elif opcion_editar == 2:
        nombre = input("Ingresa el nuevo numero: ")
        cursor.execute("UPDATE Contactos SET numero = ? WHERE id = ?", (numero, id))

    db.commit()
    print("Contacto editado exitosamente")


def eliminarContacto():
    nombre = input("Ingresa el nombre del contacto que deseas eliminar: ")
    cursor.execute("SELECT * FROM Contactos WHERE nombre LIKE ?", (f'%{nombre}%',))
    contactos = cursor.fetchall()
    if len(contactos) == 0:
        print("No se encontraron contactos")
    elif len(contactos) == 1:
        cursor.execute("DELETE FROM Contactos WHERE nombre = ?", (contactos[0][1],))
        db.commit()
        print("Contacto eliminado exitosamente")
    else:
        print("\nLista de Contactos Encontrados:")
        for contacto in contactos:
            id = contacto[0]
            nombre = contacto[1]
            numero = contacto[2]

            print(f"{id:<5} - {nombre:15} - {numero:14}")

        id = int(input("Ingresa el id del contacto que deseas eliminar: "))

        cursor.execute("DELETE FROM Contactos WHERE id = ?", (id,))
        db.commit()
        print("Contacto eliminado exitosamente")

def principal():
    while True:
        opcion = int(input("""
[1] Buscar Contacto
[2] Listar Contactos
[3] Agregar Contacto
[4] Eliminar Contacto
[5] Editar Contacto 
[6] Salir
"""))
        
        if opcion == 1:
            buscarContacto()
        elif opcion == 2:
            listarContactos()
        elif opcion == 3:
            agregarContacto()
        elif opcion == 4:
            eliminarContacto()
        elif opcion == 5:
            editarContacto()
        elif opcion == 6:
            quit()
        
principal()