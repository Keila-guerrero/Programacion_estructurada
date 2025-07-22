"""
crear un poryecto que perminta administrar peliculas; 
colocar un menu de opciones para gregar, eliminar, modificar, consultar, buscar peliculas.

notas.
1.-Utilizar funciones y mandar a llamar desde otro archivo. 
2.-Utilizar diccionarios para almacenar los atributos o caracteristicas (nombre,categoria,clasificacion,genero,idioma) de las peliculas.
3.-Utilizar e implementar una BD relacional en MySQL
"""
import os 
os.system("cls")
opcion = "SI"
nombre_peli = []
import peliculas
peliculas.borrarPantalla()
while opcion == "SI":
    accion = input("\t\t\t.::CINEPOLIS CLON ::..\n\t\t..::BIENVENIDO A ADMINISTRADOR DE PELICULAS::..\n\t\#Escoja la accion que quiera realizar\n1.-Crear \n2.-Borrar \n3.-Mostrar \n4.-Buscar\n5.-Modificar\n6.-salir")
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
            peliculas.buscarPeliculas() 
            peliculas.esperarTecla()
        case "5": 
            peliculas.modificarPeliculas()
            peliculas.esperarTecla()
        case "6": 
            opcion="NO"    
            print("\n\t\tTerminaste la ejecucion del SW")
        case _: 
            input("Opción invalida vuelva a intentarlo ... por favor")
            


        

