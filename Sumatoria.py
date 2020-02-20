#Aplicaciones De IoT
#Balderas Manzano Maria Elisa
#GDS0151, 19 de febrero 2020
#Función que cree solicite 10 valores de una lista y haga la sumatoria de los mismos
#e imprima.
def sumalista(listaNumeros):
    laSuma = 0
    for i in listaNumeros:
        laSuma = laSuma + i
    return laSuma
#Ingrese Numeros a sumar
print(sumalista([1,1,1,1,1,1,1,1,1,1]))
