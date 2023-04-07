def rev_frase(frase:str):
    frase_sep = frase.split(" ")
    i = -1
    frase_rev = ""
    for palabra in frase_sep:
        frase_rev += frase_sep[i] + " "
        i = i-1
    return frase_rev

pruebas = ["Hola Mundo", "Python es genial", "La lluvia en Sevilla es una maravilla!"]

for prueba in pruebas:
    print("Prueba: " + str(prueba) + "\nResultado: " + str(rev_frase(prueba)) + "\n")