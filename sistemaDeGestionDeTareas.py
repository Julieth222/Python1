
tareas = {}

def agregar_tarea(tarea):
    tareas[tarea] = False
    print(f"Tarea '{tarea}' agregada.")

def ver_tareas():
    if tareas:
        for tarea, completada in tareas.items():
            estado = "Completada" if completada else "Pendiente"
            print(f"{tarea} - {estado}")
    else:
        print("No hay tareas.")

def completar_tarea(tarea):
    if tarea in tareas:
        tareas[tarea] = True
        print(f"Tarea '{tarea}' marcada como completada.")
    else:
        print(f"Tarea '{tarea}' no encontrada.")

def main():
    print("Sistema de Gestión de Tareas")
    print("1) Agregar tarea 2) Ver tareas 3) Completar tarea")
    
    while True:
        opcion = input("Selecciona una opción (1-3) o 'q' para salir: ")
        
        if opcion == 'q':
            break
        
        if opcion == '1':
            tarea = input("Descripción de la tarea: ")
            agregar_tarea(tarea)
        elif opcion == '2':
            ver_tareas()
        elif opcion == '3':
            tarea = input("Tarea a completar: ")
            completar_tarea(tarea)
        else:
            print("Opción no válida.")
            
if __name__ == "__main__":
    main()
