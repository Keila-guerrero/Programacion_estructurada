"""
crear un poryecto que perminta administrar peliculas; 
colocar un menu de opciones para gregar, eliminar, modificar, consultar, buscar, vaciar pelicuals y salir del sistema.

notas.
1.-Utilizar funciones y mandar a llamar desde otro archivo. 
2.-Utilizar listas para almacenar los nombres de las peliculas.
 
"""
import os 
os.system("cls")
opcion = "SI"
nombre_peli = []
import peliculas
peliculas.limpiarPantalla()
while opcion == "SI":
    accion = input("\t\t\t..::BIENVENIDO A ADMINISTRADOR DE PELICULAS::..\n\t\#Escpja la accion que quiera realizar\n1.-Agregar peli\n2.-Eliminar peli\n3.-Modificar peli\n4.-consultar peli\n5.-Buscar peli\n6.-Vaciar peli\7.-salir")
    match accion:
        case "1":
            peliculas.agregarPeliculas()
            peliculas.esperarTecla()
        case "2":
            peliculas.eliminarPeliculas()
            peliculas.esperarTecla()
        case "3":
            peliculas.modificarPeliculas()
            peliculas.esperarTecla()  
        case "4":
            peliculas.consultarPeliculas() 
            peliculas.esperarTecla()
        case "5": 
            peliculas.buscarPeliculas()
            peliculas.esperarTecla()
        case "6": 
            peliculas.vaciarPeliculas()
            peliculas.esperarTecla()
        case "7":
            opcion="NO"    
            print("Terminaste la ejecucion del SW")
        case _: 
            input("Opción invalida vuelva a intentarlo ... por favor")
            


        

