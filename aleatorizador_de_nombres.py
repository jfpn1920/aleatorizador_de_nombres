import random
ids = []
nombres = []
apellidos = []
generos = []
edades = []
ciudades = []
observaciones = []
#---------------------------------------------#
#--|menu_principal_aleatorizador_de_nombres|--#
#---------------------------------------------#
while True:
    print("menu principal aleatorizador de nombres")
    print("1) crear nombre")
    print("2) editar nombre")
    print("3) eliminar nombre")
    print("4) buscar nombre")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #------------------#
    #--|crear_nombre|--#
    #------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_nombre = 1
        else:
            id_nombre = ids[-1] + 1
        nombre = input("nombre: ")
        apellido = input("apellido: ")
        genero = input("género: ")
        edad = int(input("edad: "))
        ciudad = input("ciudad: ")
        observacion = input("observación: ")
        ids.append(id_nombre)
        nombres.append(nombre)
        apellidos.append(apellido)
        generos.append(genero)
        edades.append(edad)
        ciudades.append(ciudad)
        observaciones.append(observacion)
        print("nombre registrado correctamente.")
        print("id:", id_nombre)
    #-------------------#
    #--|editar_nombre|--#
    #-------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("editar nombre")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {apellidos[i]} | {generos[i]} | {edades[i]} | {ciudades[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {nombres[posicion]} | {apellidos[posicion]} | {generos[posicion]} | {edades[posicion]} | {ciudades[posicion]} | {observaciones[posicion]}")
                nombres[posicion] = input("nuevo nombre: ")
                apellidos[posicion] = input("nuevo apellido: ")
                generos[posicion] = input("nuevo género: ")
                edades[posicion] = int(input("nueva edad: "))
                ciudades[posicion] = input("nueva ciudad: ")
                observaciones[posicion] = input("nueva observación: ")
                print("registro actualizado correctamente.")
            else:
                print("id no encontrada.")
    #---------------------#
    #--|eliminar_nombre|--#
    #---------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("eliminar nombre")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {apellidos[i]} | {generos[i]} | {edades[i]} | {ciudades[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {nombres[posicion]} | {apellidos[posicion]} | {generos[posicion]} | {edades[posicion]} | {ciudades[posicion]} | {observaciones[posicion]}")
                respuesta = input("¿desea eliminar este registro? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    nombres.pop(posicion)
                    apellidos.pop(posicion)
                    generos.pop(posicion)
                    edades.pop(posicion)
                    ciudades.pop(posicion)
                    observaciones.pop(posicion)
                    print("registro eliminado correctamente.")
                else:
                    print("el registro no fue eliminado.")
            else:
                print("id no encontrada.")
    #-------------------#
    #--|buscar_nombre|--#
    #-------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("buscar nombre")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {nombres[posicion]} | {apellidos[posicion]} | {generos[posicion]} | {edades[posicion]} | {ciudades[posicion]} | {observaciones[posicion]}")
            else:
                print("id no encontrada.")
    #-----------------#
    #--|lista_datos|--#
    #-----------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            suma_edades = 0
            mayor = edades[0]
            menor = edades[0]
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {apellidos[i]} | {generos[i]} | {edades[i]} | {ciudades[i]} | {observaciones[i]}")
                suma_edades += edades[i]
                if edades[i] > mayor:
                    mayor = edades[i]
                if edades[i] < menor:
                    menor = edades[i]
            promedio = suma_edades / len(ids)
            print("estadísticas aleatorizador de nombres")
            print("cantidad de personas:", len(ids))
            print("edad promedio:", round(promedio, 2))
            print("mayor edad:", mayor)
            print("menor edad:", menor)
            posicion = random.randint(0, len(ids) - 1)
            print("nombre seleccionado aleatoriamente")
            print(f"{ids[posicion]} | {nombres[posicion]} | {apellidos[posicion]} | {generos[posicion]} | {edades[posicion]} | {ciudades[posicion]} | {observaciones[posicion]}")
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el aleatorizador de nombres.")
        break
    else:
        print("opción no válida.")