import sqlite3


db = sqlite3.connect ("db_usuarios.sqlite3", check_same_thread=False)
cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nombre TEXT,
clave TEXT,
rol TEXT)""")

def crear_usuario_db(nombre, clave, rol):
    cursor.execute("""INSERT INTO usuarios(
    nombre, clave, rol) VALUES(?, ?, ?)
    """,(nombre, clave, rol))
    db.commit()

def verificar_usuario_db(nombre, clave):
    cursor.execute("""SELECT nombre, clave, rol FROM usuarios
    WHERE nombre=?
    """,(nombre,))
    data = cursor.fetchall()
    if len(data)==0:
        return("usuario no encontrado")
    elif data[0][1] == clave:
        return(f"bienvenido {nombre}\n rol:{data[0][2]}")
    elif data [0][1] != clave:
        return("clave invalida")