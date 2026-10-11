import sqlite3

conn = sqlite3.connect("gastos.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS gastos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT NOT NULL,
        descripcion TEXT NOT NULL,
        categoria TEXT NOT NULL,
        monto INTEGER NOT NULL
    )
""")
conn.commit()
conn.close()
print("Base de datos lista")