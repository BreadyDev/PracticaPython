def diagonal_p(matriz:list):
    elementos_p, i = [], 0
    
    for linea in matriz:
        elementos_p.append(linea[i])
        i+= 1
        
    return elementos_p    

pruebas = [[[1,2,3],[4,5,6],[7,8,9]],[[1,2],[3,4]],[[5,6,7],[8,9,10],[11,12,13]]]

for prueba in pruebas:
    print("Prueba: " + str(prueba) + "\nResultado: " + str(diagonal_p(prueba)))