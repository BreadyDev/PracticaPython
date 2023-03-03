def sumas_en_array(lista:list):
    res = []
    for x in range(len(lista[0])):
        for i in range(len(lista[0])):
            if (lista[0][x] + lista[0][i]) == lista[1] and x != i:
                res.append([lista[0][x], lista[0][i]])
    return res

def suma_en_array(lista:list):
    
    for x in range(len(lista[0])):
        for i in range(len(lista[0])):
            if (lista[0][x] + lista[0][i]) == lista[1] and x != i:
                return [lista[0][x], lista[0][i]]

elementos = [[1,2,3,4,5,6], 7]

print(suma_en_array(elementos))
print(sumas_en_array(elementos))