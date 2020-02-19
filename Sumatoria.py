#Función que cree solicite 10 valores de una lista y haga la sumatoria de los mismos
#e imprima.
def sumalista(listaNumeros):
    laSuma = 0
    for i in listaNumeros:
        laSuma = laSuma + i
    return laSuma

print(sumalista([1,1,1,1,1,1,1,1,1,1]))
