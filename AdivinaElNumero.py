modos = ['facil', 'medio', 'dificil','imposible']
reglas = {
    'facil':'Tendras que adivinar un numero entre el 1 y el 100 en tan solo 10 intentos.',
    'medio':'Tendras que adivinar un numero entre el 1 y el 1000 en tan solo 10 intentos.',
    'dificil':'Tendras que adivinar un numero entre el 1 y el 10000 en tan solo 10 intentos.',
    'imposible':'Tendras que adivinar un numero entre el 1 y el 100 en tan solo 3 intentos.'
    }

print(f'Selecciona el modo de juego'.center(51, '-'))

for posicion in range(len(modos)):
    print(f'{posicion + 1}) {modos[posicion].capitalize()}')

while True:
    Dificultad = int(input('Selecciona el modo de juego (1-4): '))
    if Dificultad > 0 and Dificultad <= len(modos):
        break
    else:
        print('Tienes que elegir una dificultad valida! (Un numero que corresponda a una dificultad)')
print('Las reglas del modo de juego son las siguientes'.center(51, '-'))
print(reglas[modos[Dificultad - 1]])