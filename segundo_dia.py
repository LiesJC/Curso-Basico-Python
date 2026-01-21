
# Sobreescritura
a = 2           #  a = 2
b = 3           #  a = 2 ; b = 3
b = 2           #  a = 2 ; b = 2 
# Estructuras de control 
#if()        #Palabra reservada 
#print()     #Funcion   Programcion modular
#type()      #Objetos   POO

#Operador comparador
# >< >= <= ==

a = input("Escribe un numero: ")
b = input("Escriba su segundo numero: ")

# a codificado 010101010 == 010101010
# A codificado 000001111
# b codificado 000000011

if a == b:
    print("Es verdad")
else:
    print("Es falso")

if a == "Verde":
    print("El color es verde")
elif a =="Rojo":
    print(" El color es rojo")
elif a == "Amarillo":
    print("El color es amarillo")
else:
    print("No existe el color")

#Condicionales anidadas

#Identifique que un numero este en el rango de valores 1-10:
#5-6

numero = int(input("Coloque su numero: "))
'''
if numero <=10 :
    if numero >=1:
        print("Esta en el rango de valores")
    else:
        print("El numero no esta en el rango de valores")
else:
    print("El numero no esta en el rango de valores")

#Conectores Logicos 
#Conectivo Y (AND)
#       a   b    a&b
#       1   1     1
#       1   0     0
#       0   1     0
#       0   0     0  
'''
if numero <=10 and numero >=1:
    print("Esta en el rango de valores")
else:
    print("El numero no esta en el rango de valores")

#Conectivo O (OR)
#       a   b    a&b
#       1   1     1
#       1   0     1
#       0   1     1
#       0   0     0  

#Identifique que un numero este en el rango de valores -infito-1   :  10-infinito  

if numero <1 or numero >10:
    print("Esta en el segundo rango de valores")
else:
    print("El numero no esta en el segundo rango de valores")


# ----  PROGRAMA DE ADMINISTRACION DE UN TALLER MECANICO   -----
print("ADMINISTRACION DEL TALLER MECANICO")
print("1. Velocidad del carro")
print("2. Estado el carro")
print("3. Piezas")
print("4. Salir")
opcion = int(input("Ingresamos datos: "))

if opcion == 1:
    print("MODULO DE VELOCIDAD DEL CARRO")
    tiempo = int(input("Escriba el tiempo de recorrido del carro: \t"))
    distancia = int(input("Escriba la distancia del recorrido: \t"))
    velocidad = distancia/tiempo
    print(f"La velocidad es {velocidad} [m/s]")

elif opcion ==2:
    print("MODULO DE ESTADO DEL CARRO")
    estado = int(input("Estado de rodamientos en 1 - 100:\t"))
    if estado>=1 and estado<=100:
        print("Esta es un un buen estado")
    elif estado>=101 and  estado<=150:
        print("El estado del rodamiento es critico")
    else:
        print("El estado del rodamiento esta defectuoso")    

elif opcion ==3:
    #INVENTARIO     Base de datos
    pieza1 = "Broca"
    pieza2 = "Tornillos"
    pieza3 = "Clavos"
    pieza4 = "Pintura"

    #Consulta
    print("PREGUNTE POR SU PIEZA")
    x = input("Pieza: ")
    #print(type(x))      --- Para ver el tipo de dato de entrada
    if x == pieza1 or x == pieza2 or x == pieza3 or x == pieza4:
        print("Tenemos esa pieza en el taller mecanico")
    else :
        print("No tenemos esa pieza en el taller mecanico")
elif opcion ==4:
    pass
else:
    print("Escoja un dato correcto")


