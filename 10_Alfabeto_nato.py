def nato(palabra:str):
    len_nato = {"a":"Alpha", "b":"Bravo", "c":"Charlie", "d":"Delta", "e":"Echo", "f":"Foxtrot", "g":"Golf", "h":"Hotel", "i":"India", "j":"Juliett", "k":"Kilo", "l":"Lima", "m":"Mike", "n":"November", "o":"Oscar", "p":"Papa", "q":"Quebec", "r":"Romeo", "s":"Sierra", "t":"Tango", "u":"Uniform", "v":"Victor", "w":"Whiskey", "x":"X-Ray", "y":"Yankee", "z":"Zulu", "0":"Zero", "1":"One", "2":"Two", "3":"Three", "4":"Four", "5":"Five", "6":"Six", "7":"Seven", "8":"Eight", "9":"Nine", ".":"Decimal"}
    cant = {1:"", 2:"Double", 3:"Triple", 4:"Quadruple", 5:"Quintuple"}
    cadena = ""
    last = ""
    i = 1
    cont = 1

    palabra = palabra.lower()
    
    try:
        last = len_nato.get(palabra[0])
    except:
        cadena += ""

    while cont < len(palabra):
        letra = len_nato.get(palabra[cont])
        if last == letra and i < 5:
            i += 1
            
        else:
            try:
                cadena += cant.get(i) + " " + last + " "
            except:
                cadena += ""
            i = 1
        
        last = letra
        cont += 1
    try:
        cadena += cant.get(i) + " " + last + " "
    except:
        cadena += ""

    print(cadena)

pruebas = ["Hello World", "1234.56", "LLPPPIIIILLLLLLAA", "R2-D2", "Carro"] 

for prueba in pruebas:
    print(prueba)
    nato(prueba)