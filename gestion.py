import os  # Importamos el módulo os para manejar operaciones del sistema operativo
productos = []  # Lista para almacenar los productos

def añadir_producto():
    # Lógica para añadir un producto
    while True:
        nombre = input("Añada el producto: ").strip()  # Pedimos el nombre del producto y eliminamos espacios
        if not nombre:
            print("El nombre del producto no puede estar vacío. Intente nuevamente.")
            continue  # Si el nombre está vacío, volvemos a pedirlo

        try:
            precio = float(input("Agregue el precio: "))  # Pedimos el precio y lo convertimos a float
            if precio <= 0:
                print("El precio debe ser un número positivo. Intente nuevamente.")
                continue  # Si el precio es menor o igual a 0, volvemos a pedirlo
        except ValueError:
            print("Por favor, ingrese un número válido para el precio.")
            continue  # Si no se puede convertir a float, volvemos a pedirlo
        cantidad = int(input("Ingrese la cantidad de productos"))
        if cantidad < 0:
            print("La cantidad deber ser positiva")
            continue
        # Comprobar si el producto ya existe
        if any(p["nombre"] == nombre for p in productos):
            print("Ese producto ya existe. Intente con otro nombre.")
            continue  # Si el producto ya existe, volvemos a pedir el nombre

        # Agregamos el producto a la lista
        productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
        print("Producto añadido correctamente")
        print("-" * 20)
        break  # Salimos del bucle una vez que el producto ha sido añadido

def ver_productos():
    # Lógica para ver todos los productos
    if not productos:
        print("No hay productos")
        print("-" * 20)
        return  # Si no hay productos, salimos de la función
    for producto in productos:
        print("-" * 20)
        print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']},  Cantidad: {producto['cantidad']}")  # Mostramos el nombre y precio de cada producto


def actualizar_producto():
    # Lógica para actualizar un producto
    nombre = input("Ingrese el nombre del producto que desea actualizar: ").strip()  # Pedimos el nombre del producto
    hay_producto = False  # Bandera para verificar si el producto existe
    
    for producto in productos:
        if producto["nombre"] == nombre:
            hay_producto = True  # Marcamos que encontramos el producto
            while True:
                print("1. Para actualizar nombre")
                print("2. Para actualizar precio")
                print("3. Para actualizar cantidad")            
                print("4. Para salir")
                print("-" * 20)
                
                opcion = input("Seleccione una opción: ")  # Pedimos una opción para actualizar
                if opcion == "1": 
                    nuevo_nombre = input("Ingrese un nombre nuevo (en blanco para no actualizar): ").strip()
                    if any(p["nombre"] == nuevo_nombre for p in productos if p != producto):
                        print("Ese producto ya existe")
                        print("-" * 20)
                        continue  # Si el nuevo nombre ya existe, volvemos a pedirlo
                    producto["nombre"] = nuevo_nombre  # Actualizamos el nombre
                    print("Nombre actualizado")
                    print("-" * 20)
                elif opcion == "2":
                    nuevo_precio = float(input("Ingrese un precio nuevo: "))  # Pedimos el nuevo precio
                    if nuevo_precio <= 0:
                        print("El precio no puede ser menor o igual a 0")
                        continue  # Validamos que el precio sea positivo
                    producto["precio"] = nuevo_precio  # Actualizamos el precio
                    print("Precio actualizado")
                    print("-" * 20)
                elif opcion == "3":
                    nuevo_cantidad = int(input("Ingrese una cantidad nueva: "))  # Pedimos la nueva cantidad
                    if nuevo_cantidad <= 0:
                        print("La cantidad no puede ser menor o igual a 0")
                        continue  # Validamos que la cantidad sea psotiva
                    producto["cantidad"] = nuevo_cantidad  # Actualizamos la cantidad
                    print("Cantidad actualizada")
                    print("-" * 20)
                elif opcion == "4":
                    
                    break  # Salimos del bucle de actualización
                else:
                    print("Opción no válida")
                    print("-" * 20)
                guardar_datos()  # Guardamos los cambios
                break
        if not hay_producto:
            print(f"No se encontró el producto '{nombre}'")
            print("-" * 20)

def eliminar_producto():
    # Lógica para eliminar un producto
    nombre = input("Ingrese el nombre del producto que desea eliminar: ").strip()  # Pedimos el nombre del producto
    print("-" * 20)
    for producto in productos:
        if producto["nombre"] == nombre:
            productos.remove(producto)  # Eliminamos el producto de la lista
            print("Producto eliminado")
            guardar_datos()  # Guardamos los cambios
            return
    print("No se encontró el producto")
    print("-" * 20)

def guardar_datos():
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            # Modificamos el formato para que sea más consistente y fácil de separar
            archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("Datos guardados")
    print("-" * 20)

def cargar_datos():
    if os.path.exists("productos.txt"):
        productos.clear()  # Limpiamos la lista actual antes de cargar
        with open("productos.txt", "r") as archivo:
            for linea in archivo:
                try:
                    # Dividimos la línea por comas
                    nombre, precio, cantidad = linea.strip().split(",")
                    productos.append({
                        "nombre": nombre,
                        "precio": float(precio),
                        "cantidad": int(cantidad)
                    })
                except ValueError as e:
                    print(f"Error al procesar la línea: {linea.strip()}")
                    continue
        print("Datos cargados")
        print("-" * 20)
    else:
        print("No se encontraron datos")
        print("-" * 20)

def menu():
    cargar_datos()  # Cargamos los datos al iniciar
    while True:
        # Mostramos las opciones del menú
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")  # Pedimos la opción del usuario

        if opcion == '1':
            añadir_producto()  # Llamamos a la función para añadir un producto
        elif opcion == '2':
            ver_productos()  # Llamamos a la función para ver los productos
        elif opcion == '3':
            actualizar_producto()  # Llamamos a la función para actualizar un producto
        elif opcion == '4':
            eliminar_producto()  # Llamamos a la función para eliminar un producto
        elif opcion == '5':
            guardar_datos()  # Guardamos los datos y salimos
            break
        else:
            print("Por favor, selecciona una opción válida.")
            print("-" * 20)
            
if __name__ == "__main__":
    menu()  # Ejecutamos la función menu si el script se ejecuta directamente
