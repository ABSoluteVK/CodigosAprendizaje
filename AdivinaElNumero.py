from random import randint

def Juego(intentos, rango_min, rango_max):
    numeroSecreto = randint(rango_min, rango_max)
    for intento in range(1, intentos + 1):
        print(f'Intento número {intento}'.center(40, '-'))
        while True:
            try:
                acierto = int(input('Dame tu número: '))
                break
            except ValueError:
                print("Por favor, introduce un número válido.")
        if numeroSecreto == acierto:
            print(f'¡Felicidades! Has ganado en {intento} intentos.')
            return
        elif acierto > numeroSecreto:
            print('El número que buscas es más pequeño.')
        else:
            print('El número que buscas es más grande.')
    print(f'El número correcto era {numeroSecreto}. ¡Has perdido, suerte la próxima vez!')

modos = ['fácil', 'medio', 'difícil', 'imposible']
reglas = {
    'fácil': 'Tendrás que adivinar un número entre el 1 y el 100 en tan solo 10 intentos.',
    'medio': 'Tendrás que adivinar un número entre el 1 y el 1000 en tan solo 10 intentos.',
    'difícil': 'Tendrás que adivinar un número entre el 1 y el 10000 en tan solo 10 intentos.',
    'imposible': 'Tendrás que adivinar un número entre el 1 y el 100 en tan solo 3 intentos.'
}

print('Selecciona el modo de juego'.center(51, '-'))
for posicion, modo in enumerate(modos, start=1):
    print(f'{posicion}) {modo.capitalize()}')
print('')
while True:
    try:
        Dificultad = int(input('Selecciona el modo de juego (1-4): '))
        if 1 <= Dificultad <= len(modos):
            print(' ')
            print('Las reglas del modo de juego son las siguientes'.center(51, '-'))
            print(reglas[modos[Dificultad - 1]])
            print('')
            ContinuarJuego = int(input('Confirmar juego Sí(1)/No(2): '))
            print('')
            if ContinuarJuego == 1:
                break
            elif ContinuarJuego == 2:
                continue
            else:
                print('Error!')
        else:
            print('¡Tienes que elegir una dificultad válida! (Un número que corresponda a una dificultad)')
    except ValueError:
        print("Por favor, introduce un número válido.")

if Dificultad == 1:
    Juego(10, 1, 100)
elif Dificultad == 2:
    Juego(10, 1, 1000)
elif Dificultad == 3:
    Juego(10, 1, 10000)
elif Dificultad == 4:
    Juego(3, 1, 100)
