#Se van a convertir algunas unidades como Volumen, Temperatura, Velocidades, Areas, Peso y Longitudes
def conversion(seleccion, unidad, cambio, valor):
    conversiones = {
        'longitudes': {
            'kilometros': {
                'millas': 0.621371,
                'pies': 3280.84,
                'pulgadas': 39370.08
            },
            'millas': {
                'kilometros': 1.60934,
                'pies': 5280,
                'pulgadas': 63360
            },
            'pies': {
                'kilometros': 0.0003048,
                'millas': 0.000189393939,
                'pulgadas': 12
            },
            'pulgadas': {
                'kilometros': 0.0000254,
                'millas': 0.0000157828283,
                'pies': 1/12
            }
        },
        'pesos': {
            'kilogramos': {
                'libras': 2.20462,
                'onzas': 35.274
            },
            'libras': {
                'kilogramos': 0.453592,
                'onzas': 16
            },
            'onzas': {
                'kilogramos': 0.0283495,
                'libras': 0.0625
            }
        },
        'volumenes': {
            'litros': {
                'galones': 0.264172,
                'onzas liquidas': 33.814
            },
            'galones': {
                'litros': 3.78541,
                'onzas liquidas': 128
            },
            'onzas liquidas': {
                'litros': 0.0295735,
                'galones': 0.0078125
            }
        },
        'temperaturas': {
            'kelvin': {
                'celcius': lambda x: round(x - 273.15),
                'fahrenheit': lambda x: round(x * 9/5 - 459.67)
            },
            'celcius': {
                'kelvin': lambda x: round(x + 273.15),
                'fahrenheit': lambda x: round(x * 9/5 + 32)
            },
            'fahrenheit': {
                'kelvin': lambda x: round((x + 459.67) * 5/9),
                'celcius': lambda x: round((x - 32) * 5/9)
            }
        },
        'areas': {
            'metros cuadrados': {
                'pies cuadrados': 10.7639,
                'acres': 0.000247105
            },
            'pies cuadrados': {
                'metros cuadrados': 0.092903,
                'acres': 0.0000229568
            },
            'acres': {
                'metros cuadrados': 4046.86,
                'pies cuadrados': 43560
            }
        },
        'velocidades': {
            'kilometro hora': {
                'pies hora': 3280.84,
                'millas hora': 0.621371
            },
            'pies hora': {
                'kilometro hora': 0.0003048,
                'millas hora': 0.000189393939
            },
            'millas hora': {
                'kilometro hora': 1.60934,
                'pies hora': 5280
            }
        }
    }

    if callable(conversiones[seleccion][unidad][cambio]):
        calculo = conversiones[seleccion][unidad][cambio]
        return calculo(valor)
    else:
        calculo = valor * conversiones[seleccion][unidad][cambio]
        calculo = round(calculo, 5)
        return calculo

def unidades(tipounidad):
    # Todas las unidades
    unidad = {'longitudes': ['millas','pies', 'kilometros', 'pulgadas'],
              'pesos': ['kilogramos', 'libras', 'onzas'],
              'volumenes': ['litros', 'galones', 'onzas liquidas'],
              'temperaturas': ['kelvin', 'celcius', 'fahrenheit'],
              'areas': ['metros cuadrados', 'pies cuadrados','acres'],
              'velocidades': ['kilometro hora', 'pies hora', 'millas hora']}
    #Bucle con para guardar todas las unidades en la lista
    lista_unidades = []

    for i in range(len(unidad[tipounidad])):
        lista_unidades.append(unidad[tipounidad][i])

    return lista_unidades

def PedirUnidades(lista):
    #Bucle para comprobar y volver a pedir las unidades
    while True:
        print('\nTus opciones son las siguientes:')
        for i in range(len(lista)):
            print(f'{i+1}) {lista[i].capitalize()}  ')

        unidad = input('\nElige tu unidad: ')
        cambio = input('Elige la unidad a la que quieres convertirla: ')
        if unidad.lower() in lista and cambio.lower() in lista:
            break
        else:
            print('\nTu unidad o el cambio elegido no existe entre las opciones!')
    return unidad, cambio
#Bucle programa principal 

while True:
    print('CONVERTIDOR DE UNIDADES'.center(31,'-'))

    lista = ['longitudes','pesos','volumenes','temperaturas','areas','velocidades','salir']

    for i in range(len(lista)):
        print(f'{i + 1} - {lista[i].capitalize()}')

    seleccion = input('\nElige una opcion: ')

    if seleccion.lower() == lista[-1]:
        break

    elif seleccion.lower() in lista[:-1]:  # Si la selección está en la lista de unidades
        unidades_cambio = unidades(seleccion.lower())  # Obtenemos las unidades de cambio
        unidad, cambio = PedirUnidades(unidades_cambio)  # Pedimos al usuario que elija las unidades
        valor = float(input(f'\nQue valor de {unidad} quieres convertir: '))  # Pedimos al usuario que ingrese el valor a convertir
        solucion = conversion(seleccion, unidad, cambio, valor)  # Realizamos la conversión
        print(f'\nEl nuevo valor de tus unidades es: {solucion}\n')  # Mostramos el resultado

    else:
        print('\nPor favor, introduce una respuesta valida\n')
