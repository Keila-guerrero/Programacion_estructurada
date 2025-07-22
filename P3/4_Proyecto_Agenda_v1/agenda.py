agenda_contactos = {
    "RUBEN": ["6181234567", "ruben@example.com"] 
}

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\tOprima cualquier tecla para continuar...\n\t")

def menu_principal(): 
    print("\n\t\t 💾..::: Sistema de Gestión de Agenda de Contactos :::..💾 \n\n\t\t1️⃣  Agregar contacto\n\t\t2️⃣  Mostrar contactos\n\t\t3️⃣  Buscar contacto\n\t\t4️⃣  Modificar contacto\n\t\t5️⃣  Eliminar contacto\n\t\t6️⃣  SALIR")
    opcion = input("\n\t\t👉 Elige una opción (1-6): ")
    return opcion

def agregar_contacto(agenda):
    borrarPantalla()
    print("\n\t\t📥 ..::AGREGAR CONTACTO::..📥 ")
    nombre = input("\n\tNombre: ").upper()
    if nombre in agenda:
        print("\n\t❌ El contacto ya existe.")
        esperarTecla()
    else:
        telefono = input("\tTeléfono: ")
        email = input("\tEmail: ")
        agenda[nombre] = [telefono, email]
        print("\n\t✅ Contacto agregado con éxito.")
        esperarTecla()

def mostrar_contactos(agenda):
    borrarPantalla()
    print("\n\t\t📋 ..::LISTA DE CONTACTOS::.. 📋 ")
    if not agenda:
        print("\n\t❌ No hay contactos registrados.")
        esperarTecla()
    else:
        print("-"*60)
        print(f"{'Nombre':<15}{'Teléfono':<15}{'Email':<15}")
        print("-"*60)
        for nombre, datos in agenda.items():
            print(f"{nombre:<20}{datos[0]:<15}{datos[1]:<15}")
        print("-"*60)
        esperarTecla()


def buscar_contactos(agenda):
    borrarPantalla()
    print("\n\t\t🔍 ..::BUSCAR CONTACTO::.. 🔍")
    if not agenda:
        print("\n\t❌ No hay contactos.")
        esperarTecla()
    else:
        nombre = input("\n\tNombre a buscar: ").upper().strip()
        if nombre in agenda:
            print("-"*60)
            print(f"{'Nombre':<15}{'Teléfono':<15}{'Email':<15}")
            print("-"*60)
            print(f"{nombre:<15}{agenda[nombre][0]:<15}{agenda[nombre][1]:<15}")
            print("-"*60)
            esperarTecla()
        else:
            print("\n\t❌ Contacto no encontrado.")
            esperarTecla()


def modificar_contacto(agenda):
    borrarPantalla()
    print("\n\t\t✏️ ..::MODIFICAR CONTACTO::..✏️")
    nombre = input("\n\tNombre del contacto a modificar: ").upper().strip()
    if nombre in agenda:
        print("\n\tDatos actuales:")
        print(f"\tTeléfono: {agenda[nombre][0]}")
        print(f"\tEmail: {agenda[nombre][1]}")
        nuevo_telefono = input("\n\tNuevo teléfono (dejar vacío para no cambiar): ")
        nuevo_email = input("\tNuevo email (dejar vacío para no cambiar): ")
        if nuevo_telefono:
            agenda[nombre][0] = nuevo_telefono
        if nuevo_email:
            agenda[nombre][1] = nuevo_email
        print("\n\t✅ Contacto modificado con éxito.")
        
    else:
        print("\n\t❌ Contacto no encontrado.")
        esperarTecla()

def eliminar_contacto(agenda):
    borrarPantalla()
    print("\n\t\t🗑️ ..::ELIMINAR CONTACTO::..🗑️")
    nombre = input("\n\tNombre del contacto a eliminar: ").upper().strip()
    if nombre in agenda:
        del agenda[nombre]
        print("\n\t✅ Contacto eliminado con éxito.")
        esperarTecla()
    else:
        print("\n\t❌ Contacto no encontrado.")
        esperarTecla()