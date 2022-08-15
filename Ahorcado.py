import random

def findChars(palabra,caracter):
    posiciones = []
    for i in range(len(palabra)):
        if palabra[i] == caracter:
            posiciones.append(i)
    return posiciones

palabras = ["perro","gato","mouse","helicoptero","teclado","nube","universo","auriculares","celular","python","javascript"]
palabra_random = random.choice(palabras).upper()
guion = "_" * len(palabra_random)

print("Juego del Ahorcado")
contador = 0 
while contador < 8:
    print(guion+"\nTe quedan "+str(8-contador)+" Vidas")
    ingreso = input("ingrese una letra: ").upper()
    if len(ingreso)>1:
        print('No puede ingresar palabras de más de un caracter')
        continue
    else:
        if 91>ord(ingreso)>64:
            posiciones = findChars(palabra_random,ingreso)
            if len(posiciones) == 0:
                print("Perdiste 1 vida")
                       
            else:
                for i in posiciones:
                    guion = guion[:i] + ingreso + guion[i+1:]  
                if guion == palabra_random:
                    break        
                continue
        else:
            print("Solo puede ingresar letras")
            continue
    contador = contador + 1
if contador < 8:
    print("Ganaste, La palabra correcta es: "+palabra_random)
else:
    print("Perdiste, la palabra correcta era: "+palabra_random)   
