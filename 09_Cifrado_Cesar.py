def cifrado(cad):  
    abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    dic = {valor: clave for clave, valor in dict(enumerate(abc)).items()}
    cif = ""
    
    for letra in cad[0]:
        i = dic.get(letra) + cad[1]
        while i > (len(abc)-1):
            i -= (len(abc))
           
        cif += abc[i]
    print(cif)
        

cad = ["abcdefghijklmnñopqrstuvwxyz", 26]

cifrado(cad)
