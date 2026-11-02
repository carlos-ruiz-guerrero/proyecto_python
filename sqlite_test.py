import sqlite3

conn = sqlite3.connect("empresa.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS empleados (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    salario REAL
)
""")

cursor.execute("""
INSERT INTO empleados (nombre, salario)
VALUES ('Juan', 30000)
""")

conn.commit()

for fila in cursor.execute("SELECT * FROM empleados"):
    print(fila)

conn.close()