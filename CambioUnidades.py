#Se van a convertir algunas unidades como Volumen, Temperatura, Velocidades, Areas, Peso y Longitudes
def longitud(a):

    unidad, cambio = PedirUnidades(a)

    if unidad == 'kilometros' and cambio == 'millas':
        valor = float(input('\nQue valor de Km quieres convertir: '))
        calculo = valor*0.621371

    elif unidad == 'kilometros' and cambio == 'pies':
        valor = float(input('\nQue valor de Km quieres convertir: '))
        calculo = valor*3280.84

    elif unidad == 'kilometros' and cambio == 'pulgadas':
        valor = float(input('\nQue valor de Km quieres convertir: '))
        calculo = valor*39370.08

    elif unidad == 'millas' and cambio == 'kilometros':
        valor = float(input('\nQue valor de millas quieres convertir: '))
        calculo = valor*1.60934

    elif unidad == 'millas' and cambio == 'pies':
        valor = float(input('\nQue valor de millas quieres convertir: '))
        calculo = valor*5280

    elif unidad == 'millas' and cambio == 'pulgadas':
        valor = float(input('\nQue valor de millas quieres convertir: '))
        calculo = valor*63360

    elif unidad == 'pies' and cambio == 'kilometros':
        valor = float(input('\nQue valor de pies quieres convertir: '))
        calculo = valor*0.0003048

    elif unidad == 'pies' and cambio == 'millas':
        valor = float(input('\nQue valor de pies quieres convertir: '))
        calculo = valor*0.000189393939

    elif unidad == 'pies' and cambio == 'pulgadas':
        valor = float(input('\nQue valor de pies quieres convertir: '))
        calculo = valor*12

    elif unidad == 'pulgadas' and cambio == 'pulgadas':
        valor = float(input('\nQue valor de pulgadas quieres convertir: '))
        calculo = valor*0.0000254

    elif unidad == 'pulgadas' and cambio == 'pulgadas':
        valor = float(input('\nQue valor de pulgadas quieres convertir: '))
        calculo = valor*0.0000157828283

    elif unidad == 'pulgadas' and cambio == 'pulgadas':
        valor = float(input('\nQue valor de pulgadas quieres convertir: '))
        calculo = valor/12

    return round(calculo, 5)

def peso(a):
    unidad, cambio = PedirUnidades(a)

def volumen(a):
    unidad, cambio = PedirUnidades(a)

def temperatura(a):
    unidad, cambio = PedirUnidades(a)

def area(a):
    unidad, cambio = PedirUnidades(a)

def velocidad(a):
    unidad, cambio = PedirUnidades(a)

def unidades(tipounidad):
    # Todas las unidades
    unidad = {'longitudes': ['millas','pies', 'kilometros', 'pulgadas'],
              'pesos': ['kilogramos', 'libras', 'onzas'],
              'volumen': ['litos', 'galones', 'onzas liquidas'],
              'temperatura': ['kelvin', 'celcius', 'fahrenheit'],
              'area': ['metros cuadrados', 'pies cuadrados','acres'],
              'velocidad': ['kilometro hora', 'pies hora', 'millas hora']}
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
    #imprime las opciones a elegir y pide la seleccion
    print('CONVERTIDOR DE UNIDADES'.center(31,'-'))

    lista = ['longitud','peso','volumen','temperatura','area','velocidad','salir']

    for i in range(len(lista)):
        print(f'{i + 1} - {lista[i].capitalize()}')

    seleccion = input('\nElige una opcion: ')

    # comprobamos las selecciones y llamamos a la funcion encargada de hacer los calculos depues de elegir las unidades
    if seleccion.lower() == lista[-1]:
        break

    elif seleccion.lower() == lista[0]:
        unidades_cambio = unidades('longitudes')
        solucion = longitud(unidades_cambio)
        print(f'\nEl nuevo valor de tus unidades es: {solucion}\n')

    elif seleccion.lower() == lista[1]:
        unidades_cambio = unidades('pesos')
        peso(unidades_cambio)

    elif seleccion.lower() == lista[2]:
        unidades_cambio = unidades('volumenes')
        volumen(unidades_cambio)

    elif seleccion.lower() == lista[3]:
        unidades_cambio = unidades('temperaturas')
        temperatura(unidades_cambio)

    elif seleccion.lower() == lista[4]:
        unidades_cambio = unidades('areas')
        area(unidades_cambio)

    elif seleccion.lower() == lista[5]:
        unidades_cambio = unidades('velocidades')
        velocidad(unidades_cambio)

    else:
        print('\nPor favor, introduce una respuesta valida\n')
