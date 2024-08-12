

import random


def juego_adivinanza():
    #generar un numero del 1 al 100
    numero_secreto = random.randint(1,100)
    intentos = 0
    adivinado = False
    
    print("¡Bienvenido al juego de adivinanza de numero!")
    print("¡Debes adivinar un numero del 1 al 100!")
    print("¡Intenta adivinarlo!")
    
    while not adivinado:
        #solicitar un numero del 1 al 100
        adivinanza = input("Introduzaca un numero del 1 al 100: ")
        if adivinanza.isdigit():
            adivinanza = int(adivinanza) #lo estamos pasando de texto a entero
            intentos += 1
            #verificar que la entrada sea un numero
            if adivinanza < numero_secreto:
                print(f"El numero secreto es mayor a {adivinanza}")
            
            elif adivinanza > numero_secreto:
                print(f"El numero secreto es menor a {adivinanza}")
            else:
                print(f"Felicitaciones has ganado! El numero {adivinanza} es el secreto y lo has logrado en {intentos} intentos.")
        else:
            print("Por favor introduzca un numero valido entre el 1 al 100")
            
juego_adivinanza()