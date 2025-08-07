lista=[]
from funciones import *
from conexionBD import *
from precio import precios

#precios
precios.cargar_precios()
carnitas = precios.carnitasKg_precio
taco = precios.tacos_precio
torta = precios.torta_precio
cueritos = precios.cueritosKg_precio


#parte nueva (maenejo de archivos)
import openpyxl
from conexionBD import cursor

def exportar_ventas_excel(nombre_archivo="ventas_exportadas.xlsx"):
    try:
        cursor.execute("SELECT * FROM ventas")
        ventas = cursor.fetchall()

        if not ventas:
            print("⚠️ No hay ventas para exportar.")
            return

        # Crear archivo Excel
        wb = openpyxl.Workbook()
        hoja = wb.active
        hoja.title = "Ventas"

        # Encabezados
        encabezados = ["ID Usuario", "KG Carne", "Tacos", "Tortas", "Cueritos"]
        hoja.append(encabezados)

        # Agregar datos
        for venta in ventas:
            hoja.append(list(venta))

        # Guardar el archivo
        wb.save(nombre_archivo)
        print(f"✅ Ventas exportadas a {nombre_archivo}")
        
    except Exception as e:
        print(f"❌ Error al exportar: {e}")







def agregar_ventas(lista):
    borrarPantalla()
    print("\n.:: 💾 AGREGAR VENTA NUEVA 💾 ::.\n")
    

    bandera = True
    while bandera:
        try:
            kilos = float(input("📝 ¿Cuántos kilos desea? ($230 por kilo): "))
            if kilos >= 0:
                bandera = False
            else:
                print("❌ No se aceptan números negativos...❌")
        except ValueError:
            print("❌ Ingresa un número válido...❌")

    bandera = True
    while bandera:
        try:
            tacos = float(input("📝 ¿Cuántos tacos desea? ($20 c/u): "))
            if tacos >= 0:
                bandera = False
            else:
                print("❌ No se aceptan números negativos...❌")
        except ValueError:
            print("❌ Ingresa un número válido...❌")

    bandera = True
    while bandera:
        try:
            tortas = float(input("📝 ¿Cuántas tortas desea? ($65 c/u): "))
            if tortas >= 0:
                bandera = False
            else:
                print("❌ No se aceptan números negativos...❌")
        except ValueError:
            print("❌ Ingresa un número válido...❌")

    bandera = True
    while bandera:
        try:
            cueritos = float(input("📝 ¿Cuántos kilos de cuerito desea? ($150 por kilo): "))
            if cueritos >= 0:
                bandera = False
            else:
                print("❌ No se aceptan números negativos...❌")
        except ValueError:
            print("❌ Ingresa un número válido...❌")


    venta = [kilos, tacos, tortas, cueritos]
    lista.append(venta)

    try: 
        cursor.execute("INSERT INTO ventas (kilogramos_carne, Tacos, Tortas, Cueritos) VALUES (%s, %s, %s, %s);", 
                    (kilos, tacos, tortas, cueritos))
        conexion.commit()
        print("\n✅ Venta registrada con éxito ✅")
    except Exception as e:
        print(f"\n❌ Error al registrar la venta: {e}")

   



    
    
def mostrar_ventas():
    borrarPantalla()
    print("\n.::📂 VENTAS REGISTRADAS 📂::.\n")

    try:
        cursor.execute("SELECT * FROM ventas")
        registros = cursor.fetchall()

        if registros:
            print(f"{'ID':<5}{'KG':<10}{'TACOS':<10}{'TORTAS':<10}{'CUERITO':<10}")
            print("-" * 50)
            for venta in registros:
                # venta[0] = id_cliente, venta[1] = kilos, venta[2] = tacos, etc.
                print(f"{venta[0]:<5}{venta[1]:<10}{venta[2]:<10}{venta[3]:<10}{venta[4]:<10}")
        else:
            print("⚠️❌ No hay ventas registradas en la base de datos. ❌⚠️")
    except Exception as e:
        print(f"❌ Error al mostrar ventas: {e}")



def calcular_total():
    borrarPantalla()
    print("\n.:: 📂CÁLCULO DE TOTAL DE VENTAS 📂::.\n")
    total = 0

    try:
        cursor.execute("SELECT * FROM ventas")
        ventas = cursor.fetchall()


        if ventas:
            print(f"{'ID':<5}{'KG':<10}{'TACOS':<10}{'TORTAS':<10}{'CUERITOS':<10}{'TOTAL':<10}")
            print("-" * 65)
            for venta in ventas:
                id_cliente = venta[0]
                kg = venta[1]
                tacos = venta[2]
                tortas = venta[3]
                cuerito = venta[4]

                total_cliente = (kg * carnitas) + (tacos * taco) + (tortas * torta) + (cuerito * cueritos)
                print(f"{id_cliente:<5}{kg:<10}{tacos:<10}{tortas:<10}{cuerito:<10}${total_cliente:<10.2f}")
                total += total_cliente

            print("\n-----------------------------------------------")
            print(f"💰 Total general de ventas: ${total:.2f}")
        else:
            print("⚠️❌ No hay ventas para calcular. ❌⚠️")
    except Exception as e:
        print(f"❌ Error al calcular total: {e}")

