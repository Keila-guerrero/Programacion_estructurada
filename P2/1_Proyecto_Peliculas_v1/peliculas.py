peliculas = []

def limpiarPantalla():
    import os 
    os.system("cls")


def esperarTecla():
    input()

def agregarPeliculas():
    print("\t\t..::AGREGAR PELICULAS::..")
    peliculas.append(input("Ingrese la pelicula: ").upper().strip())
    print("\n\t\t:: LA OPERAICIÓN SE REALIZÓ CON EXITO :::")

def consultarPeliculas():
    limpiarPantalla()
    print("\t\t..::CONSULTAR TODAS LAS PERLICULAS::..")
    if len(peliculas) != 0:
        for i in range (1,len(peliculas)):
            print(f"{i+1} : {peliculas[i]}")
    else:
        input("..::No hay peliculas en el sistema::..")

def vaciarPeliculas ():
    limpiarPantalla()
    print("\t\t..::LIMPIAR O BORRAR TODOS LOS ELEMENTOS TODAS LAS PELICULAS::..")
    resp = input("Estas seguro de borrar todas las peliculas? (si/no): ").lower
    if resp == "si":
        peliculas.clear()
        print("\n\t\t:: LA OPERAICIÓN SE REALIZÓ CON EXITO :::")

def buscarPeliculas():
    limpiarPantalla()
    print("\t\t..::BUSCAR PELICUALS EN ESPECIFICO::..")
    peli = input("ingrese la pelicula que que busca: ").upper().strip()
    if peli in peliculas:
        print("si se encuentra la pelicula ")
        for i in range (1,len(peliculas)):
            if peli == peliculas[i]:
                print(f"La {peli} se encuentra en el casillero: {i + 1}")
                econtro += 1
        print(f"tenemos {econtro} veces la pelicula {peli}")
    else:
        print("No se encuentra la pelicula")  

    print("Precione cualquier tecla para continuar")  



def modificarPeliculas():
    limpiarPantalla()
    print("\t\t..::MODIFICAR PELICUALS EN ESPECIFICO::..")
    peli = input("ingrese la pelicula que quiere modificar: ").upper().strip()
    if peli in peliculas:
        resp = input("¿Deseas modificar la pelicula? (si/no): ").lower().strip()
        if resp == "si":
            for i in range (1,len(peliculas)):
                if peli == peliculas[i]:
                    peliculas[i] = input("Ingrese el nuevo nombre de la pelicula: ")
                    print(f"Ahora la pelicula se llama {peliculas[i]} y la tenermos en el casillero : {i + 1}")
        
    print("\n\t\t:: LA OPERAICIÓN SE REALIZÓ CON EXITO :::")
    






##..::EXAMEN::..##
# agregar toy, toy, debe decir cual peli borro , y de que casillo lo borro 
def eliminarPeliculas():
    limpiarPantalla
    peliBorrar = input("Ingrese el nombre de la pelicula que queire borrar: ")
    if peliBorrar in peliculas:
        for i in range (1,len(peliculas)):
            if peliBorrar == peliculas[i]:
                resp = print(f"Seguro que queieres borrar {peliculas[i]}? (si/no)").lower().strip()
                if resp == "si":
                    peliculas.remove(peliBorrar)
                else:
                        print("babay")
