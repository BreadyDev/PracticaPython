def suma_rev(digitos:list):
    suma = []
    sum = 0
    sobra = 0
    dif = 0
    i = 0

    if len(digitos[0]) < len(digitos[1]):
        dif = len(digitos[0]) - len(digitos[1])
        may = 1
    else:
        dif = len(digitos[1]) - len(digitos[0])
        may = 0
        
    for n1, n2 in zip(digitos[0], digitos[1]):
        sum = n1 + n2 + sobra
        if sum >= 10:
            sum -= 10
            sobra = 1
        else:
            sobra = 0
        suma.append(sum)
        
    for i in range(dif, 0):
        sum = digitos[may][i] + sobra
        if sum >= 10:
            sum -= 10
            sobra = 1
        else:
            sobra = 0
        suma.append(sum)
        
    if sobra == 1:
        suma.append(sobra)
        
    return suma

pruebas = [[[1,2,3],[3,2,1]],[[9,9,9],[1,0,0,0]],[[9,9,9],[9,9,9,9]]]
for prueba in pruebas:
    print("Prueba: " + str(prueba) + "\nResultado: " + str(suma_rev(prueba)) + "\n")