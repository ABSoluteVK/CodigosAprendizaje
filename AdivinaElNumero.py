from random import *
#Funcion para jugar al juego
def Juego(intentos, rango_min, rango_max):
    a = 1
    numeroSecreto = randint(rango_min, rango_max)
    while a < intentos+1:
        print(f'Intento numero {a}'.center(40,'-'))
        acierto = int(input('Dame tu numero: '))
        if numeroSecreto == acierto:
            break
        else:
            if acierto > numeroSecreto:
                print('El numero que buscas es mas pequeño.')
            else:
                print('El numero que buscas es mas grande.')
            a += 1
    
    if a == intentos and numeroSecreto == acierto:
        print("Felecidades has ganado por los pelos!")
    elif a == intentos and numeroSecreto != acierto:
        print(f'El numero corresto era {numeroSecreto}. Has perdido suerte la proxima vez!')
    elif numeroSecreto == acierto and a < intentos:
        print(f'Felicidades has ganado en {a} aciertos!')
    else:
        print("wtf")


#Lista para almacenar los niveles de dificultad
modos = ['facil', 'medio', 'dificil','imposible']
#Almacenamos las reglas en un diccionario
reglas = {
    'facil':'Tendras que adivinar un numero entre el 1 y el 100 en tan solo 10 intentos.',
    'medio':'Tendras que adivinar un numero entre el 1 y el 1000 en tan solo 10 intentos.',
    'dificil':'Tendras que adivinar un numero entre el 1 y el 10000 en tan solo 10 intentos.',
    'imposible':'Tendras que adivinar un numero entre el 1 y el 100 en tan solo 3 intentos.'
    }

print(f'Selecciona el modo de juego'.center(51, '-'))

for posicion in range(len(modos)):
    print(f'{posicion + 1}) {modos[posicion].capitalize()}')

#Creamos un bucle para preguntar que modo de juego quiere jugar
while True:
    Dificultad = int(input('Selecciona el modo de juego (1-4): '))
    #Comprobamos que el modo de juego seleccionado es valido
    if Dificultad > 0 and Dificultad <= len(modos):
        #Mostramos las normas antes de continuar con el juego y le preguntamos si esta seguro que quiere jugar en este modo
        print('Las reglas del modo de juego son las siguientes'.center(51, '-'))
        print(reglas[modos[Dificultad - 1]])
        ContinuarJuego = int(input('Confirmar juego Si(1)/No(2): '))
        if ContinuarJuego == 1:
            break
        elif ContinuarJuego == 2:
            continue
        else:
            print('Error!')
    else:
        print('Tienes que elegir una dificultad valida! (Un numero que corresponda a una dificultad)')
if Dificultad-1 == 0:
    Juego(10,1,100)
elif Dificultad-1 == 1:
    Juego(10,1,1000)
elif Dificultad-1 == 2:
    Juego(10,1,10000)
elif Dificultad-1 == 3:
    Juego(3,1,100)
else:
    print('WTF')