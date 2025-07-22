import mysql.connector
from mysql.connector import Error

"""
dict u objeto para almacenar los atributos (nombre, categoria, clasificacion, genero, idioma)
pelicula = {
    "nombre": "",
    "categoria": "",
    "clasificacion": "",
    "genero": "",
    "idioma": ""
}
"""

pelicula = {}

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\tOprima cualquier tecla para continuar...\n\t")
   
def conectar ():
    try:
        conexion=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_peliculas"
        )
        return conexion
    except Error as e:
        print(f"El error que se preseto es: {e}")
        return None
    
def crearPeliculas():
    borrarPantalla()
    print("\n\t.:: Alta de Películas ::.\n")
    pelicula.update({"nombre": input("Ingresa el nombre: ").upper().strip()})
    pelicula.update({"categoria": input("Ingresa la categoría: ").upper().strip()})
    pelicula.update({"clasificacion": input("Ingresa la clasificación: ").upper().strip()})
    pelicula.update({"genero": input("Ingresa el género: ").upper().strip()})
    pelicula.update({"idioma": input("Ingresa el idioma: ").upper().strip()})
    
    
    
    
    
    
    
    input("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")

def mostrarPeliculas():
    borrarPantalla()
    print("\n\t.:: Consultar o Mostrar la Película ::.\n")
    if len(pelicula) > 0:
        for i in pelicula:
            print(f"\t{i}: {pelicula[i]}")
    else:
        print("\t..:: No hay películas en el sistema ::..\n")

def borrarPeliculas():
    borrarPantalla()
    print("\n\t.:: Borrar o Quitar TODAS las Películas ::.\n")
    resp = input("¿Deseas quitar o borrar todas las películas del sistema? (Si/No): ").lower().strip()
    if resp == "si":
        pelicula.clear()
        input("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")

