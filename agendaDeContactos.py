import sqlite3
db = sqlite3.connect("agendaDeContactos.sqlite3")
cursor = db.cursor()

contacto = []



def BuscarContacto(venta):
    nombre = input("Ingresa el nombre que deseas buscar: ")

    cursor.execute("SELECT * FROM Contactos WHERE nombre LIKE ?% AND telefono = ?", (nombre,))
    contactos = cursor.fetchall()
    if len(contactos == 0):
        print("No se encorraron contactos")
    else:
        print("\nLista de contactos encontrados:")
        for contacto in contactos:
            id = contacto[0]
            nombre = contacto[1]
            numero = contacto[2]
            print(f"{id:<5} - {nombre:15} - {numero:12}")

def AgregarContacto():
    nombre = input("Ingrese el nombre del nuevo contacto: ")
    numero = input("Ingrese el numero de telefono del nuevo contacto: ")

    cursor.execute("INSERT INTO contactos (nombre, numero) VALUES (?, ?)", (nombre,numero))


def EliminarContacto():
    nombre = input("Ingresa el nombre del contacto que deseas eliminar: ")

    cursor.execute("SELECT * FROM Contactos WHERE nombre LIKE ?% AND telefono = ?", (nombre,))
    contactos = cursor.fetchall()
    if len(contactos == 0):
        print("No se encorraron contactos")
    
    elif len(contactos == 1):
        cursor.execute("DELETE FROM contactos WHERE nombre = ?" , (contactos[0][1],))
        db.commit
        print("Contacto eliminado exitosamente")
    
    else:
        print("\nLista de contactos encontrados:")
        for contacto in contactos:
            id = contacto[0]
            nombre = contacto[1]
            numero = contacto[2]
            print(f"{id:<5} - {nombre:15} - {numero:12}")
    
    id = int(input("Ingresa la id que desee eliminar: "))
    cursor.execute("DELETE FROM contactos WHERE id = ?" , (id,))
    db.commit
    print("Contacto eliminado exitosamente")
    

def EditarContacto():
    cursor.execute("SELECT * FROM contactos")
    contactos = cursor.fetchall()
    if len(contactos == 0):
        print("No se encorraron contactos")
    else:
        print("\nLista de contactos:")
        for contacto in contactos:
            id = contacto[0]
            nombre = contacto[1]
            numero = contacto[2]
            print(f"{id:<5} - {nombre:15} - {numero:12}")
    
        id = int(input("Ingresa la id que desee editar: "))
        opcion_editar = int(input("""Ingrese la opcion que desea editar: 
        [1] nombre
        [2] numero
        """))
        if opcion_editar == 1:
            nombre = input("Ingresa el nuevo nombre: ")
            cursor.execute("UPDATE contactos SET nombre = ? WHERE id = ?", (nombre,id))
        elif opcion_editar == 2:
            nombre = input("Ingresa el nuevo numero: ")
            cursor.execute("UPDATE contactos SET nombre = ? WHERE id = ?", (nombre,id))
        db.commit
        print("Contacto editado exitosamente")
    

def ListarContactos():
    cursor.execute("SELECT * FROM contactos")
    contactos = cursor.fetchall()
    if len(contactos == 0):
        print("No se encorraron contactos")
    else:
        print("\nLista de contactos:")
        for contacto in contactos:
            id = contacto[0]
            nombre = contacto[1]
            numero = contacto[2]
            print(f"{id:<5} - {nombre:15} - {numero:12}")
    

def principal():
    while True:
        opcion = int(input("""
        MENU REGISTRO DE CONTACTOS

        [1] Buscar Contacto
        [2] Agregar Contacto
        [3] Eliminar Contacto 
        [4] Editar Contacto
        [5] Listar Contactos 
        [6] Salir
                    
        """))
    
        if opcion == 1:
            BuscarContacto()
        elif opcion == 2:
            AgregarContacto()
        elif opcion == 3:
            EliminarContacto()
        elif opcion == 4:
            EditarContacto()
        elif opcion == 5:
            ListarContactos()
        elif opcion == 6:
            quit()

principal()