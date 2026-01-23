
#BASE DE DATOS COLEGIO
#Nombre del personal docente
# Listas de informacion - Base de datos 
nombre_personal = ["Juan","Jose","Janneth","Luis","Ana"]
apellido_personal = ["Mamani","Casas","Huascar","Fernandez","Quispe"]
ci_personal = [32545545, 54354355,54545554, 54545222,65656777]
id_personal = [1, 2, 3, 4, 5]

x = 4
while x>3:
    print("ADMINISTRACION PARA BASE DE DATOS")
    print("1. Consultas")
    print("2. Agregar datos")
    print("3. Salir")
    op =  (input("Escoja su opcion: "))
    if op == "1":
        dato = input("Realice su consulta por nombre: ")
        for i in range(len(nombre_personal)):
            if dato == nombre_personal[i]:
                print(nombre_personal[i])
                print(f"El docente {nombre_personal[i]} {apellido_personal [i]} con CI {ci_personal[i]} de identicador {id_personal[i]}")
            else:
                #print("No existe el personal solicitado")
                pass
    elif op == "2":
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        ci = int(input("CI: "))
        id = int(len(id_personal)) + 1
        nombre_personal.append(nombre)
        apellido_personal.append(apellido)
        ci_personal.append(ci)
        id_personal.append(id)

    elif op == "3":
        x = 2
        print("PROGRAMA FINALIZADO")
    else:
        print("No esta colocado el valor correcto")


