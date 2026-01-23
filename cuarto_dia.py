
#Funciones
# d =   lim     f(x+h)-f(x)
#       h->0        h
'''
h = float(input("Cuanto va a ser el valor: \t"))
xme = float(input("Cuanto es el limite inferior: \t"))
xma =float(input("Cuanto es el limite superior: \t"))

#Funcion
x = xme
xs = x+h
while x<=xma:
    fx = (x)**2-1+(x)
    fhx = (xs)**2-1+(xs)
    #fx = (x)**2-1+(x)
    d = (fhx-fx)/h
    x = xs
    xs = xs + h 
    print(f"De la funcion {round(fx,4)} la derivada es: {round(d,4)}")
#print(f"La derivada de la funciones : {d}")
'''
'''
#Ciclo for
for i in range(6,10,2):
    print(f"La iteracion es :{i}")

#Concatenacion
palabra = "Hola"
nombre = "Jose Freddy"

union = palabra +" " + nombre
print(f"{palabra} {nombre} -  {union}")


#*
#* *
#* * *
#* * * *  n = 4
n = int(input("Escriba la cantidad de datos"))
linea = ""
for i in range(n):
    linea += "*"+"\t"
    #linea = linea + "*"
    print(linea)

'''

#Ejercicio 1  n=3
#1 2 3 
#4 5 6 
#7 8 9

#FUNCIONES 
#Funcion sin parametros - vacia
def funcion(v):
    x = v
    y = 2
    #print(f"La suma es : {x+y}")
    return x+y

#a = funcion(int(input("Dame el numero : ")))
#print("El valor de la funcion es: ",a)


def funcion(x):
    fx = (x)**2-1+(x)
    return fx

def derivada(x,h):
    fhx = funcion(x+h)
    fx = funcion(x)
    d = (fhx - fx) /h
    return d

h = float(input("Cuanto va ser el deltax: \t"))    #Delta de x == h
xme = float(input("Cuanto es el limite inferior: \t"))
xma =float(input("Cuanto es el limite superior: \t"))


while xme<=xma:
    print(f"La funcion es : {funcion(xme)} y la derivada es : {derivada(xme,h)}")
    xme = xme + h

