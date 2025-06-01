"""
Ejemlo 1:
Crear una lista de numeros e imrimir el contenido
"""
numeros = [1,2,3,4,5,6,7,8,9,10]
print(numeros)
 #1er forma
variables="["
for i in numeros:
    variable+=f"{i},"
print(f"{numeros}]")

#2da forma
variables="["
for i in range(0,len(numeros)):
    variable+=f"{i},"
print(f"{numeros}]")


"""
Ejemplo 2:
Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 
"""
import os 
os.system("cls")

lista_palabras = ["hola","hi","holis","hi","pato","pollo","pan","pescao"]
busqueda = input("¿Que palabra desea buscar?")
if busqueda in lista_palabras:
    print("Su palabra se encuentra en la lista")
else:
    print("Su palabra no esta en la lista ")

posiciones=[]
cuantas=0
encontro=False
for i in lista_palabras:
    if i==busqueda:
        encontro=True
        cuantas+=1
        posiciones.apped(lista_palabras.index(i))
if encontro:
    print("Su palabra se encuentra en la lista")
else:
    print("Su palabra no esta en la lista ")


posiciones=[]
cuantas=0
encontro=False
for i in range(0,len(lista_palabras)):
    if lista_palabras[i] == busqueda:
        encontro=True
        cuantas+=1
        posiciones.apped(lista_palabras.index(i))
if encontro:
    print("Su palabra se encuentra en la lista")
else:
    print("Su palabra no esta en la lista ")

encontro=False
for i in range(0,len(lista_palabras)):
    if lista_palabras[i] == busqueda:
        encontro=True
        posiciones.apped(lista_palabras.index(i))
if encontro:
    print("Su palabra se encuentra en la lista")
else:
    print("Su palabra no esta en la lista ")

"""
ejemplo 3:
añadir elementos a la lista
"""

lista_palabras.insert(1,"México")
print(lista_palabras)

"""
ejemplo 4:
crear una lista para almacenar numeros y nombres de personas (agenda)
"""
opcion = 1
agenda_num = []
agenda_name = []
while opcion == 1:
    os.system("cls")
    opcion = int(input("\t\t..::Bienvenido a su agenda::..\n\tSeleccione el numero de la opcion que desea:\n1.-Agregar persona\n2.-Buscar persona\n3.-Finalizar\nOpción: "))
    if opcion == 1:
        nombre1 = input("\tIngrese el nombre de la persona que desea agregar a su agenda: ")
        numero1 = input("\tIngrese el numero de la persona que desea agregar a su agenda: ")
        agenda_name.append(nombre1)
        agenda_num.append(numero1)
        opcion = 1
    elif opcion == 2:
        persona = input("Ingrese el nombre de la persona que busca: ")
        if persona in agenda_name:
            posicion = agenda_name.index(persona)
            print(f"Nombre: {agenda_name[posicion]}\tNúmero: {agenda_num[posicion]}")
        else:
            print("La persona no se encuentra en la agenda")
        opcion = 1
    elif opcion == 3:
        print("Programa finalizado")
    else:
        print("Opción no válida")
        opcion = 1


agenda=[
    ["Carlos",618156548],
    ["Carlos V",5654884896],
    ["Carlos VI",664879765],
]
print(agenda)
for i in agenda:
    print(i)

for r in range(0,3):
    for c in range(0,2):
        print(agenda[r][c])

for r in range(0,3):
    for c in range(0,2):
        listas+=f"{agenda[r][c]})"
        lista+="\n"
print(listas)