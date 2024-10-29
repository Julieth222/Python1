contactos = {}

def agregar_contacto(nombre, telefono):
    contactos[nombre] = telefono
    print(f"Contacto {nombre} agregado con éxito.")

def ver_contactos():
    if contactos:
        for nombre, telefono in contactos.items():
            print(f"{nombre}: {telefono}")
    else:
        print("No hay contactos.")

def eliminar_contacto(nombre):
    if nombre in contactos:
        del contactos[nombre]
        print(f"Contacto {nombre} eliminado.")
    else:
        print(f"Contacto {nombre} no encontrado.")

def main():
    print("Gestión de Contactos")
    print("1) Agregar contacto 2) Ver contactos 3) Eliminar contacto")
    
    while True:
        opcion = input("Selecciona una opción (1-3) o 'q' para salir: ")
        
        if opcion == 'q':
            break
        
        if opcion == '1':
            nombre = input("Nombre del contacto: ")
            telefono = input("Teléfono del contacto: ")
            agregar_contacto(nombre, telefono)
        elif opcion == '2':
            ver_contactos()
        elif opcion == '3':
            nombre = input("Nombre del contacto a eliminar: ")
            eliminar_contacto(nombre)
        else:
            print("Opción no válida.")
            
if __name__ == "__main__":
    main()
