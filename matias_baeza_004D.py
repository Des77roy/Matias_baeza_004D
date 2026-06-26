# ==========================================
# Sistema de gestion de inventario :D
# Una breve explicaion de la estructura de mi programa
# primero el programa valida con las funciones (validar_nombre, stock y precio) que hace que los datos ingresados sean los correctos antes de guardarlos
# la parte de menu y control usan funciones (mostrar_menu o leer_opcion) que hacen que se mantenga un ciclo de interacciones con el usuario y evitan errores de entrada :D
# El programa pincipar: agregar_producto crea un diccionario con la informacion y lo suma a la lista
# buscar_producto: recorre la lista para encontrar la posicion de un item
# actualizar_disponibilidad: cambia el estado true o false segun el stock
# mostrar_productos imprime en pantalla toda la base de datos formateada
# el programa pincipal osea main es el encargado que unifica todo usando el bucle "while" para repetir el menu hasta que el usuario decida salir :D 
# ==========================================

def validar_nombre(nombre):
    """Retorna True si el nombre no está vacío ni contiene solo espacios en blanco."""
    if nombre.strip() != "":
        return True
    return False

def validar_stock(stock_str):
    """Retorna True y el entero si el stock es un número >= 0, de lo contrario False y -1."""
    try:
        stock = int(stock_str)
        if stock >= 0:
            return True, stock
        return False, -1
    except ValueError:
        return False, -1

def validar_precio(precio_str):
    """Retorna True y el float si el precio es un número > 0, de lo contrario False y -1.0."""
    try:
        precio = float(precio_str)
        if precio > 0:
            return True, precio
        return False, -1.0
    except ValueError:
        return False, -1.0

# ============================
# Funciones de Menú y Control
# ============================
def mostrar_menu():
    """Muestra las opciones del menú principal en pantalla."""
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Eliminar producto")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar productos")
    print("6. Salir")
    print("=====================================")

def leer_opcion():
    """Lee y retorna la opción elegida por el usuario validando que sea un número."""
    while True:
        try:
            opcion = int(input("Seleccione una opción (1-6): "))
            return opcion
        except ValueError:
            print("Error: Por favor ingrese un número válido.")

# ==========================================
# Funciones de Operación
# ==========================================
def agregar_producto(lista_productos):
    """Solicita datos, valida y agrega un nuevo producto a la lista."""
    nombre = input("Ingrese el nombre del producto: ")
    stock_str = input("Ingrese el stock disponible: ")
    precio_str = input("Ingrese el precio del producto: ")

    es_valido_nom = validar_nombre(nombre)
    es_valido_stock, stock = validar_stock(stock_str)
    es_valido_precio, precio = validar_precio(precio_str)

    # Los mensajes de error se muestran aquí, no dentro de las validaciones
    if not es_valido_nom:
        print("Error: El nombre no puede estar vacío ni ser solo espacios en blanco.")
    elif not es_valido_stock:
        print("Error: El stock debe ser un número entero mayor o igual que cero.")
    elif not es_valido_precio:
        print("Error: El precio debe ser un número decimal mayor que cero.")
    else:
        producto = {
            "nombre": nombre,
            "stock": stock,
            "precio": precio,
            "disponible": False  #Se asigna automáticamente al registrar
        }
        lista_productos.append(producto)
        print("Producto agregado exitosamente.")

def buscar_producto(lista_productos, nombre_buscado):
    """Recorre la lista buscando un producto por coincidencia exacta de nombre. 
       Retorna la posición o -1 si no existe."""
    for i in range(len(lista_productos)):
        if lista_productos[i]["nombre"] == nombre_buscado:
            return i
    return -1

def actualizar_disponibilidad(lista_productos):
    """Actualiza el campo 'disponible' a True si stock > 0, o False si es 0."""
    for producto in lista_productos:
        if producto["stock"] > 0:
            producto["disponible"] = True
        else:
            producto["disponible"] = False

def mostrar_productos(lista_productos):
    """Actualiza disponibilidad y muestra todos los productos con el formato requerido."""
    actualizar_disponibilidad(lista_productos)
    print("\n=== LISTA DE PRODUCTOS ===")
    if not lista_productos:
        print("No hay productos registrados en el sistema.")
    else:
        for producto in lista_productos:
            print(f"Nombre: {producto['nombre']}")
            print(f"Stock: {producto['stock']}")
            print(f"Precio: {producto['precio']}")
            
            estado = "DISPONIBLE" if producto["disponible"] else "SIN STOCK"
            print(f"Estado: {estado}")
            print("********************************************")

# ==========================================
# Programa principal. cada uso que pide que tenga el programa :3
# ==========================================
def main():
    productos = []  # La colección debe existir desde que inicia y estar disponible.
    
    while True:
        mostrar_menu()
        opcion = leer_opcion()
        
        if opcion == 1:
            agregar_producto(productos)
            
        elif opcion == 2:
            nombre = input("Ingrese el nombre del producto a buscar: ")
            posicion = buscar_producto(productos, nombre)
            if posicion != -1:
                p = productos[posicion]
                print(f"\n--- Producto Encontrado en posición {posicion} ---")
                print(f"Nombre: {p['nombre']}, Stock: {p['stock']}, Precio: {p['precio']}, Disponible: {p['disponible']}")
            else:
                print("Producto no encontrado.")
                
        elif opcion == 3:
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            posicion = buscar_producto(productos, nombre)
            if posicion != -1:
                del productos[posicion]
                print("Producto eliminado exitosamente.")
            else:
                print(f"El producto '{nombre}' no se encuentra registrado.")
                
        elif opcion == 4:
            actualizar_disponibilidad(productos)
            print("Disponibilidad actualizada para todos los registros.")
            
        elif opcion == 5:
            mostrar_productos(productos)
            
        elif opcion == 6:
            print("Gracias por usar el sistema. Vuelva Pronto")
            break
            
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()