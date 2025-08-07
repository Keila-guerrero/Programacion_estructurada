from conexionBD import cursor

# Diccionario general para almacenar todos los precios
PRECIOS = {}

# Variables individuales para cada producto
carnitasKg_precio = 0
tacos_precio = 0
torta_precio = 0
cueritosKg_precio = 0

def cargar_precios():
    global PRECIOS, carnitasKg_precio, tacos_precio, torta_precio, cueritosKg_precio

    try:
        cursor.execute("SELECT productos, precio FROM precios")
        resultados = cursor.fetchall()

        for producto, precio in resultados:
            PRECIOS[producto] = float(precio)

        # Asignar a variables específicas si existen
        carnitasKg_precio = PRECIOS.get("carnitasKg", 0)
        tacos_precio = PRECIOS.get("tacos", 0)
        torta_precio = PRECIOS.get("torta", 0)
        cueritosKg_precio = PRECIOS.get("cueritosKg", 0)

    except Exception as e:
        print(f"❌ Error al cargar precios: {e}")

# Cargar automáticamente los precios al importar el módulo




