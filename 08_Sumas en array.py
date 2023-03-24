# Funcion que recibe un array y un numero objetivo, regresa un arreglo con los dos primero numeros del array que sumen el numero objetivo
from time import time

elementos = [[2,3,4,5,6], 7]

def sumas_en_array(lista:list):
    res = []
    for x in range(len(lista[0])):
        for i in range(len(lista[0])):
            if (lista[0][x] + lista[0][i]) == lista[1] and x != i:
                res.append([x, i])
    return res

def suma_en_array(lista:list):
    res = []
    for x in range(len(lista[0])):
        if (lista[1]-lista[0][x]) in lista[0]:
            #return [x, lista[0].index(lista[1]-lista[0][x])]
            res.append([x, lista[0].index(lista[1]-lista[0][x])])
            
    return res

inicio_1 = time()

print(suma_en_array(elementos))
print(time() - inicio_1)

inicio_2 = time()

print(sumas_en_array(elementos))
print(time() - inicio_2)