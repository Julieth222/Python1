1

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def main():
    print("Calculadora")
    print("Operaciones: 1) Sumar 2) Restar 3) Multiplicar 4) Dividir")
    
    while True:
        opcion = input("Selecciona una operación (1-4) o 'q' para salir: ")
        
        if opcion == 'q':
            break
        
        if opcion in ['1', '2', '3', '4']:
            try:
                a = float(input("Ingresa el primer número: "))
                b = float(input("Ingresa el segundo número: "))
                
                if opcion == '1':
                    print("Resultado:", sumar(a, b))
                elif opcion == '2':
                    print("Resultado:", restar(a, b))
                elif opcion == '3':
                    print("Resultado:", multiplicar(a, b))
                elif opcion == '4':
                    print("Resultado:", dividir(a, b))
            except ValueError:
                print("Error: Ingresa números válidos.")
        else:
            print("Opción no válida.")
            
if __name__ == "__main__":
    main()
