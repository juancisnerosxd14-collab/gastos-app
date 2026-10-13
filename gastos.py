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

import sqlite3
from datetime import date

def conectar():
    conn = sqlite3.connect("gastos.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS gastos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            categoria TEXT NOT NULL,
            monto INTEGER NOT NULL
        )
    """)
    return conn

def agregar_gasto():
    descripcion = input("Descripción: ")
    categoria = input("Categoría: ")
    monto = int(input("Monto: "))
    fecha = date.today().isoformat()

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO gastos (fecha, descripcion, categoria, monto)
        VALUES (?, ?, ?, ?)
    """, (fecha, descripcion, categoria, monto))
    conn.commit()
    conn.close()
    print("Gasto guardado")
    print((fecha, descripcion, categoria, monto))

agregar_gasto()

def ver_gastos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM gastos ORDER BY fecha DESC")
    filas = cursor.fetchall()
    conn.close()

    if not filas:
        print("No hay gastos registrados")
        return

    for id, fecha, descripcion, categoria, monto in filas:
        print(f"{id}. {fecha} | {descripcion} ({categoria}): ${monto}")

opcion = input("1. Agregar gasto  2. Ver gastos: ")
if opcion == "1":
    agregar_gasto()
elif opcion == "2":
    ver_gastos()

def menu():
    while True:
        print("\n--- Registro de gastos ---")
        print("1. Agregar gasto")
        print("2. Ver gastos")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_gasto()
        elif opcion == "2":
            ver_gastos()
        elif opcion == "3":
            print("Hasta luego")
            break
        else:
            print("Opción no válida")

menu()