#Estructuras repetitivas

#Estructura "mientras"
'''
numero = 10
while numero >= 0:
    print(f"Este es el numero {numero}")
    numero = numero - 1
'''
#Sumatoria
'''
#1+2+3+4+5+6......
n = int(input("Dicte su numero para las operaciones sucesivas: \t"))

i = 1
sumatoria = 0
while i<=n: 
    sumatoria = sumatoria + i
    i = i + 1
    print(sumatoria)

print(f"La sumatoria es: {sumatoria}")

gauss = n*(n+1)/2
print(gauss)

if gauss == sumatoria:
    print("Coinciden ambas formulas")
else:
    print("No coinciden")

#Factorial
#1*2*3*4*5*6......
i = 1
factorial = 1
while i<=n: 
    factorial = factorial * i
    i = i + 1
    print(factorial)

print(f"El factorial es: {factorial}")
'''
#Funciones matemaricas
x = 1
while x<10:
    fx = x**2+x**3+x**4-12
    print(fx)
    x = x + 0.1