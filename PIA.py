import sqlite3
import pandas as pd
from sqlite3 import Error
import sys
import datetime
import re
import openpyxl
import os

# Conectar a la base de datos
try:
    with sqlite3.connect("Zara.db") as conn:
        mi_cursor = conn.cursor()

    # Crear las tablas
       

        mi_cursor.execute('''CREATE TABLE IF NOT EXISTS servicios (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nombre TEXT NOT NULL,
                            costo REAL NOT NULL
                        )''')

       
except Error as e:
    print(e)
except Exception:
    print(f"Se produjo un problema:{sys.int_info()[0]}")
finally:
        # Guardar los cambios
        conn.commit()

def agregar_servicio(nombre, costo):
    if not nombre or nombre.isspace():
        print("El nombre no puede estar vacío.")
        return

    if costo <= 0:
        print("El costo debe ser superior a 0.00.")
        return

    mi_cursor.execute("INSERT INTO servicios (nombre, costo) VALUES (?, ?)",
                   (nombre, costo))

    conn.commit()

    import sqlite3
import datetime

# Conectar a la base de datos SQLite
conn = sqlite3.connect("Zara.db")
cursor = conn.cursor()

# Crear la tabla de servicios si no existe
cursor.execute("""
    CREATE TABLE IF NOT EXISTS servicios (
        clave INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        costo REAL NOT NULL
    )
""")
conn.commit()

def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    costo = float(input("Ingrese el costo del producto: "))
    
    if costo <= 0:
        print("Los datos proporcionados no cumplen con las condiciones.")
        return
    
    cursor.execute("INSERT INTO servicios (nombre, costo) VALUES (?, ?)", (nombre, costo))
    conn.commit()
    print("Producto agregado con éxito.")

def buscar_por_clave():
        cursor.execute("SELECT * FROM servicios ")
        servicios = cursor.fetchall()
    
        for servicio in servicios:
            print(f"Id: {servicio[0]} |   Nombre: {servicio[1]}")
            print("-----------------------------------------------")

        clave = input("Ingrese el clave del servicio a buscar: ")
        cursor.execute("SELECT * FROM servicios WHERE (id) = (?)", (clave,))
        servicios = cursor.fetchall()
        
        if servicios:
            for servicio in servicios:
                print(f"Id: {servicio[0]} | Nombre: {servicio[1]} | Costo: ${servicio[2]} ")
                print("-----------------------------------------------------------------------")
        else:
            print("No se encontraron servicios con ese nombre.")

def buscar_por_nombre():
    nombre = input("Ingrese el nombre del servicio a buscar: ")
    cursor.execute("SELECT * FROM servicios WHERE UPPER(nombre) = UPPER(?)", (nombre,))
    servicios = cursor.fetchall()
    
    if servicios:
        for servicio in servicios:
            print(f"Id: {servicio[0] } | Nombre:      {servicio[1]} |  Costo: ${servicio[2]} ")
            print("-----------------------------------------------------------------------")
         
    else:
        print("No se encontraron servicios con ese nombre.")

def lista_clave():
        cursor.execute("SELECT * FROM servicios")
        servicios = cursor.fetchall()
        for servicio in servicios:
            print(f"Id: {servicio[0]} |  Nombre: {servicio[1]}| Costo: ${servicio[2]} ")
            print("-----------------------------------------------------------------------")
                

def lista_nombre():
    cursor.execute("SELECT * FROM servicios ORDER BY nombre")
    servicios = cursor.fetchall()
    for servicio in servicios:
        print(f"Nombre: {servicio[1]}  | Id: {servicio[0]}  | Costo: ${servicio[2]} ")
        print("-----------------------------------------------------------------------")
                
def obtener_datos():
    cursor.execute("SELECT * FROM servicios")
    datos = cursor.fetchall()
    return datos

def excel():
    datos = obtener_datos()
    if not datos:
        print("No hay datos disponibles para exportar.")
        return

    df = pd.DataFrame(datos)

    archivo = input("Ingrese el nombre del archivo Excel (sin extensión): ")
    archivo += ".xlsx"

    try:
        df.to_excel(archivo, index=False)
        print(f"Los datos se han exportado correctamente a {archivo}")
        ruta_completa = os.path.abspath(archivo)
        print(f"El archivo se encuentra en: {ruta_completa}")
    except Exception as e:
        print(f"Ocurrió un error al exportar a Excel: {e}")

def main():
    while True:
        print("Almacen Zara\n")
        print ("1. Agregar un producto")
        print ("2. Consultas y reportes")
        print ("3. Exportar a archivo .XLSX")
        print ("4. Volver al menu principal")
        opcserv = int(input("Elige una opción: "))
        if opcserv == 1:
            agregar_producto()
        elif opcserv == 2:
            print("Consultas y reportes")
            print("1. Busqueda por clave de servicio")
            print("2. Busqueda por nombre de servicio")
            print("3. Listado de servicios ordenados por clave")
            print("4. Listado de servicios ordenados por nombre")
            opcconsultas= int(input("Seleccione la opcion que desea: "))
            if opcconsultas == 1 :
                buscar_por_clave()
            elif opcconsultas == 2:
                buscar_por_nombre()
            elif opcconsultas == 3:
                lista_clave()
            elif opcconsultas == 4:
                lista_nombre()
            else : print ("Caracter invalido")        
        elif opcserv ==3: 
            excel()
if _name_ == "_main_":
    main()