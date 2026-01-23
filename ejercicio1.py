#Ejercicio
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12

n  = int(input("Dame la cantidad :"))
cont = 1
cadena = ""
for j in range(n):
    for i in range(n):
        cadena = cadena + f"{cont}" + "\t"
        cont = cont + 1
    print(cadena + "\n")
    cadena = ""


