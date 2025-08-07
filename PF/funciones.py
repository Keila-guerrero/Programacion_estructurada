def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  input("\n\t\t ... ⚠️ Oprima cualquier tecla para continuar ⚠️ ...")

def menu_usurios():
   print("\n \t.:: Sistema administrativo ::.. \n\t\t1.-  Registro  \n\t\t2.-  Login \n\t\t3.- Salir ")
   opcion1=input("\t\t Elige una opción: ").upper().strip() 
   return opcion1

def menu_ventas():
  print("\n\t..:::🎉 CARNITAS DEL SEÑOR 🎉:::... \n..:::📝 Sistema administrativo para el personal 📝:::...\n 🔍1.- Agregar venta \n 🔍2.- Mostrar ventas \n 🔍3.- Calcular total de ventas en el día \n 💾4.- Exportar ventas a Excel \n 🚪5.- SALIR ")

  opcion=input("\t 📝Elige una opción (1-4):  ").upper().strip()
  return opcion