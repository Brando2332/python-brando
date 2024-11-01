import sqlite3
db = sqlite3.connect("mibd.sqlite3")
cursor = db.cursor()
cursor.execute("""DELETE FROM Estudiantes 
                 WHERE id=2""")

db.commit()