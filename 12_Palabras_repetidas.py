def contar(frase:list):
    from collections import defaultdict
    cont = defaultdict(int)
    
    for palabra in frase:
        cont[palabra] += 1
           
    return dict(cont)


pruebas = ["Hola Mundo Hola", "Python es un lenguaje de programación y es muy popular", "el sol calienta y el rio corre el rio siempre fluye"] 

for prueba in pruebas:
    print(prueba + "\n" + str(contar(prueba.split(" "))))