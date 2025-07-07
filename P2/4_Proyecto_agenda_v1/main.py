import agenda

def main():
    opcion = True
    agenda_contactos = {}  

    while opcion:
        agenda.borrarPantalla()
        opcion = agenda.menu_principal()
        
        if opcion == "1":
            agenda.agregar_contacto(agenda_contactos)
            agenda.esperarTecla()
        elif opcion == "2":
            agenda.mostrar_contactos(agenda_contactos)
            agenda.esperarTecla()
        elif opcion == "3":
            agenda.buscar_contactos(agenda_contactos)
            agenda.esperarTecla()
        elif opcion == "4":
            agenda.modificar_contacto(agenda_contactos)
            agenda.esperarTecla()
        elif opcion == "5":
            agenda.eliminar_contacto(agenda_contactos)
            agenda.esperarTecla()
        elif opcion == "6":
            opcion = False
            agenda.borrarPantalla()
            print("\n\t🚪 Terminaste la ejecución del SW 🚪")
        else:
            print("\n\t❌ Opción inválida.Vuelva a intentarlo")
            agenda.esperarTecla()

if __name__ == "__main__":
    main()