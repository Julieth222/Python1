
print(menu)
opcion = input('Digita una opción entre 1 y 3: ')
if opcion == '1':
    nombre = input('Digita tu nombre: ')
    edad = input('digitar edad')
    print("tu nombre es:" + nombre)
    print("tu nombre es:", nombre)
    print('Tu nombre es {}'.format(nombre), 'tu edad es{}.'.format(edad))
elif opcion == '2':
    edad = input('Digita tu edad: ')
    print('Tu edad es:' + edad)
    print('Tu edad es:', edad)
    print('Tu edad es {}'.format(edad))
elif opcion == '3':
    email = input('Digita tu email: ')
    print('tu email es: ' + email)
    print('tu email es: ', email)
    print(f'tu email es: {email}')
else:
    print('Debes digitar un numero entre 1 y 3')
    print('=-='*20)
print("****** Gracias por usar nuestro servicio ******")
