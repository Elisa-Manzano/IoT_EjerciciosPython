#Aplicaciones De IoT
#Balderas Manzano Maria Elisa
#GDS0151, 19 de febrero 2020
#Realizar el desglose del IVA de una cifra dada,
PORCENTAJE_IVA = 16

conteo_productos = 1  # Saber en cuál producto vamos
precio_total = 0

while conteo_productos <= 5:
    mensaje = "Ingresa el precio del producto número {}: ".format(
        conteo_productos)
    precio_como_cadena = input(mensaje)
    # Convertir a flotante
    precio = float(precio_como_cadena)
    # Agregarlo al precio total
    precio_total = precio_total + precio
    # Ya leímos un producto, le sumamos al conteo
    conteo_productos = conteo_productos + 1
# Cuando el ciclo termine calculamos el IVA
aumento = precio_total * (PORCENTAJE_IVA / 100)  # Dividir entre 100 porque es un porcentaje
# Sumar el aumento
precio_con_iva = precio_total + aumento
# Imprimir totales
print("Total: ${}".format(precio_total))
print("IVA: ${}".format(aumento))
print("Total con IVA: ${}".format(precio_con_iva))
