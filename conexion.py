
#BASE DE DATOS COLEGIO
#Nombre del personal docente
nombre_personal1 = "Juan"
nombre_personal2 = "Jose"
nombre_personal3 = "Janneth"
nombre_personal4 = "Luis"
nombre_personal5 = "Ana"

apellido_personal1 = "Mamani"
apellido_personal2 = "Huascar"
apellido_personal3 = "Casas"
apellido_personal4 = "Fernandez"
apellido_personal5 = "Quispe"

ci_personal1 = 32545545
ci_personal2 = 54354355
ci_personal3 = 54545554
ci_personal4 = 54545222
ci_personal5 = 65656777

id_personal1 = 1
id_personal2 = 2
id_personal3 = 3
id_personal4 = 4
id_personal5 = 5


print("ADMINISTRACION PARA BASE DE DATOS")
print("1. Consultas")
print("2. Escribir datos")
print("3. Salir")

op =  (input("Escoja su opcion: "))
if op == "1":
    dato = input("Realice su consulta por nombre: ")
    if dato == nombre_personal1 or dato == nombre_personal2 or dato == nombre_personal3 or dato == nombre_personal4 or dato == nombre_personal5:
        print("Existe el personal")
        if dato == nombre_personal1:
            print(f"El docente {nombre_personal1} {apellido_personal1} de carnet {ci_personal1} tiene un identificador de {id_personal1}")
        if dato == nombre_personal2:
            print(f"El docente {nombre_personal2} {apellido_personal2} de carnet {ci_personal2} tiene un identificador de {id_personal2}")
        if dato == nombre_personal3:
            print(f"El docente {nombre_personal3} {apellido_personal3} de carnet {ci_personal3} tiene un identificador de {id_personal3}")
        if dato == nombre_personal4:
            print(f"El docente {nombre_personal4} {apellido_personal4} de carnet {ci_personal4} tiene un identificador de {id_personal4}")
        if dato == nombre_personal5:
            print(f"El docente {nombre_personal5} {apellido_personal5} de carnet {ci_personal5} tiene un identificador de {id_personal5}")
    else: 
        print("No existe el personal docente")
elif op == "2":
    pass
else:
    print("No esta colocado el valor correcto")


