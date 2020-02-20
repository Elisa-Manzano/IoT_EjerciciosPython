#Aplicaciones De IoT
#Balderas Manzano Maria Elisa
#GDS0151, 19 de febrero 2020

#Conversion de grados

fahrenheit = int(input('Ingrese una temperatura en grados Fahrenheit: '))
celsius = (fahrenheit - 32) * 5.0/9.0
# Hacemos uso de la funcion str.format() para darle formato a nuestra respuesta
print('{} grados Fahrenheit son {} grados Celsius '.format(fahrenheit, celsius))
celsius = int(input('Ingrese la temperatura en grados Celsius: '))
fahrenheit = 9.0/5.0 * celsius +32
print('{} grados Celsius son {} grados Fahrenheit'.format(celsius, fahrenheit))
def fahrenheit_celsius():
    '''convierte temperatura en grados fahrenheit a grados celsius'''
    fahrenheit = int(input('Ingrese la temperatura en grados Fahrenheit: '))
    celsius = (fahrenheit -32 ) * 5.0/9.0
    return '{} grados Fahrenheit son {} grados Celsius'.format(fahrenheit, celsius)
def celsius_fahrenheit():
    '''convierte temperatura en grados celsius a fahrenheit'''
    celsius = int(input('Ingrese la temperatura en grados Celsius: '))
    fahrenheit = 9.0/5.0 * celsius +32
    return '{} grados Fahrenheit son {} grados Celsius'.format(fahrenheit, celsius)
while True:
    print('1.- Fahrenheit a Celsius')
    print('2.- Celsius a Fahrenheit')
    try:
        opcion = int(input('Seleccione una opción: '))
        if opcion == 1:
            print(fahrenheit_celsius())
        elif opcion == 2:
            print(celsius_fahrenheit())
        elif opcion == 3:
            print('Hasta luego')
        else:
            raise ValueError
    except ValueError:
        print('Ingrese solo números.(1/2)')
