helados = []  # Lista para almacenar los helados
contador_id = 1  # Contador para asignar IDs únicos

while True:
    print("\nGestión de Helados")
    print("1. Agregar un helado")
    print("2. Ver lista de helados")
    print("3. Modificar un helado")
    print("4. Eliminar un helado")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":  # Agregar un helado
        nombre = input("Ingrese el nombre del helado: ")
        descripcion = input("Ingrese la descripción del helado: ")
        precio_input = input("Ingrese el precio del helado: ")

        if precio_input.replace(".", "", 1).isdigit():  # Permite números con decimales
            precio = float(precio_input)
            helado = {"id": contador_id, "nombre": nombre, "descripcion": descripcion, "precio": precio}
            helados.append(helado)
            contador_id += 1
            print("Helado agregado correctamente.")
        else:
            print("Error: El precio debe ser un número válido.")

    elif opcion == "2":  # Ver lista de helados
        if not helados:
            print("No hay helados registrados.")
        else:
            print("\nLista de Helados:")
            for helado in helados:
                print(f"ID: {helado['id']}, Nombre: {helado['nombre']}, Descripción: {helado['descripcion']}, Precio: ${helado['precio']:.2f}")

    elif opcion == "3":  # Modificar un helado
        id_modificar = input("Ingrese el ID del helado a modificar: ")

        if id_modificar.isdigit():
            id_modificar = int(id_modificar)
            encontrado = False

            for helado in helados:
                if helado["id"] == id_modificar:
                    nuevo_nombre = input(f"Nuevo nombre ({helado['nombre']}): ") or helado["nombre"]
                    nueva_descripcion = input(f"Nueva descripción ({helado['descripcion']}): ") or helado["descripcion"]
                    nuevo_precio = input(f"Nuevo precio ({helado['precio']}): ")

                    if nuevo_precio.replace(".", "", 1).isdigit():
                        helado["precio"] = float(nuevo_precio)
                    
                    helado["nombre"] = nuevo_nombre
                    helado["descripcion"] = nueva_descripcion
                    
                    print("Helado modificado correctamente.")
                    encontrado = True
                    break

            if not encontrado:
                print("Error: No se encontró un helado con ese ID.")
        else:
            print("Error: El ID debe ser un número.")

    elif opcion == "4":  # Eliminar un helado
        id_eliminar = input("Ingrese el ID del helado a eliminar: ")

        if id_eliminar.isdigit():
            id_eliminar = int(id_eliminar)
            for helado in helados:
                if helado["id"] == id_eliminar:
                    helados.remove(helado)
                    print("Helado eliminado correctamente.")
                    break
            else:
                print("Error: No se encontró un helado con ese ID.")
        else:
            print("Error: El ID debe ser un número.")

    elif opcion == "5":  # Salir
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida, intente nuevamente.")
