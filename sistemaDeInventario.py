inventario = {}

def agregar_producto(nombre, cantidad):
    inventario[nombre] = inventario.get(nombre, 0) + cantidad
    print(f"Producto {nombre} actualizado. Cantidad: {inventario[nombre]}")

def ver_inventario():
    if inventario:
        for producto, cantidad in inventario.items():
            print(f"{producto}: {cantidad} unidades")
    else:
        print("El inventario está vacío.")

def eliminar_producto(nombre):
    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto {nombre} eliminado del inventario.")
    else:
        print(f"Producto {nombre} no encontrado en el inventario.")

def main():
    print("Sistema de Inventario")
    print("1) Agregar producto 2) Ver inventario 3) Eliminar producto")
    
    while True:
        opcion = input("Selecciona una opción (1-3) o 'q' para salir: ")
        
        if opcion == 'q':
            break
        
        if opcion == '1':
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            agregar_producto(nombre, cantidad)
        elif opcion == '2':
            ver_inventario()
        elif opcion == '3':
            nombre = input("Nombre del producto a eliminar: ")
            eliminar_producto(nombre)
        else:
            print("Opción no válida.")
            
if __name__ == "__main__":
    main()
