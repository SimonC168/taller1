frutas = []  # Lista para almacenar las frutas

# Ingreso de frutas
print("Registro de Frutas para el Salpicón")
for i in range(10):
    nombre = input(f"Ingrese el nombre de la fruta {i + 1}: ")
    precio_input = input(f"Ingrese el precio de {nombre}: ")

    if precio_input.replace(".", "", 1).isdigit():  # Validación de número
        precio = float(precio_input)
        frutas.append({"nombre": nombre, "precio": precio})
    else:
        print("Error: El precio debe ser un número válido.")
        break  # Si hay un error, se detiene el ingreso

# Ordenamiento Burbuja de mayor a menor
n = len(frutas)
for i in range(n - 1):
    for j in range(n - i - 1):
        if frutas[j]["precio"] < frutas[j + 1]["precio"]:  # Comparación
            frutas[j], frutas[j + 1] = frutas[j + 1], frutas[j]  # Intercambio

# Mostrar la lista ordenada
print("\nFrutas ordenadas de mayor a menor precio:")
for fruta in frutas:
    print(f"Nombre: {fruta['nombre']}, Precio: ${fruta['precio']:.2f}")
