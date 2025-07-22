"""
crear un poryecto que perminta administrar peliculas; 
colocar un menu de opciones para gregar, eliminar, modificar, consultar, buscar, vaciar pelicuals y salir del sistema.

notas.
1.-Utilizar funciones y mandar a llamar desde otro archivo. 
2.-Utilizar diccionarios para almacenar los atributos o caracteristicas (nombre,categoria,clasificacion,genero,idioma) de las peliculas.
 
"""
import os 
os.system("cls")
opcion = "SI"
nombre_peli = []
import peliculas
peliculas.borrarPantalla()
while opcion == "SI":
    accion = input("\t\t\t..::BIENVENIDO A ADMINISTRADOR DE PELICULAS::..\n\t\#Escpja la accion que quiera realizar\n1.-Crear peli\n2.-Borrar peli\n3.-Mostrar peli\n4.-Agregar Características\n5.-Modificar\n6.-Borrar caracteristicas\7.-salir")
    match accion:
        case "1":
            peliculas.crearPeliculas()

            peliculas.esperarTecla()
        case "2":
            peliculas.borrarPeliculas()
            peliculas.esperarTecla()
        case "3":
            peliculas.mostrarPeliculas()
            peliculas.esperarTecla()  
        case "4":
            peliculas.agregarCaracteristicaPeliculas() 
            peliculas.esperarTecla()
        case "5": 
            peliculas.modificarCaracteristicaPeliculas()
            peliculas.esperarTecla()
        case "6": 
            peliculas.borrarCaracteristicaPeliculas()
            peliculas.esperarTecla()
        case "7":
            opcion="NO"    
            print("Terminaste la ejecucion del SW")
        case _: 
            input("Opción invalida vuelva a intentarlo ... por favor")
            


        

