palabra = str(input("Ingresa una palabra: ").lower().replace(" ", ""))
i = len(palabra) - 1
arbalap = ""

while  i >= 0:
    arbalap = arbalap + palabra[i]
    i -= 1
    
if palabra == arbalap:
    print("La palabra es palindroma")
else:
    print("La palabra no es palindroma")