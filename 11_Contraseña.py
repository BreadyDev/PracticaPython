def passw(contraseña:str):
    may, minu, num = False, False, False
    
    for letra in contraseña:
        if letra.isupper():
            may = True
        
        if letra.islower():
            minu = True
        
        if letra.isdigit():
            num = True
        
    if len(contraseña) >= 8 and may and minu and num:
        return True
    else:
        return False
        
pruebas = ["Abcdefgh1", "Abcd1", "12345678"] 

for prueba in pruebas:
    
    print("La contraseña: " + prueba + " es:") 
    if passw(prueba):
        print("Valida")
    else:
        print("Invalida")   