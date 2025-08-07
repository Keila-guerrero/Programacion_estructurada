from ventas import ventas
import funciones
import conexionBD
from usuarios import usuario
import getpass


def main ():
    opcion=True
    while opcion:
        funciones.borrarPantalla()
        opcion=funciones.menu_usurios()

        if opcion=="1" or opcion=="REGISTRO":
            funciones.borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre=input("\t ¿Cual es tu nombre?: ").upper().strip()
            gmail=input("\t Ingresa tu email: ").lower().strip()
            # password=input("\t Ingresa tu contraseña: ").strip()
            contraseña=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            #Agregar codigo
            regresar=usuario.registrar(nombre,gmail,contraseña)
            if regresar:
                print(f"{nombre} se registro correctamente con el e-mail: {gmail}")
            else:
                print(f"Por favor intentelo de nuevo ... no fue posible realizar el registro en este momento ...")    
            funciones.esperarTecla()
        elif opcion=="2" or opcion=="LOGIN": 
            funciones.borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::.. ")     
            email=input("\t Ingresa tu E-mail: ").lower().strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            #Agregar codigo 
            lista_usuario=usuario.iniciar_sesion(email,password)
            if lista_usuario:
               menu_ventas()
            else:
                print(f"...El E-mail y/o contraseña son incorrectos ... por favor intentalo nuevamente")
                funciones.esperarTecla()       
        elif opcion=="3" or opcion=="SALIR": 
            print("Termino la Ejecución del Sistema")
            opcion=False
            funciones.esperarTecla()  
        else:
            print("Opcion no valida")
            opcion=True
            funciones.esperarTecla() 

def menu_ventas():
    conexion = conexionBD
    if conexion:
        continuar = True
        datos=[]
        
        

        while continuar:
            funciones.borrarPantalla()
            opcion=funciones.menu_ventas()

            match opcion:
                case "1":
                    ventas.agregar_ventas(datos)
                    ventas.esperarTecla()
                case "2":
                    ventas.mostrar_ventas()
                    ventas.esperarTecla()
                case "3":
                    ventas.calcular_total()
                    ventas.esperarTecla()
                case "4":
                    ventas.exportar_ventas_excel()
                    ventas.esperarTecla()
                case "5":
                    continuar = False
                    ventas.borrarPantalla()
                    print("🎉 Gracias por usar el sistema administrativo... 🎉")
                case _:
                    input("⚠️ Opción inválida... Intente de nuevo por favor! ⚠️")
                    ventas.esperarTecla()


if __name__ == "__main__":
    main()
