#Se van a convertir algunas unidades como Volumen, Temperatura, Velocidades, Areas, Peso y Longitudes
def longitud(unidad, cambio):
    print('\n Elige la unidad a la que quieres ')

def peso():
    print('peso')

def volumen():
    print('volumen')

def temperatura():
    print('temperatura')

def area():
    print('area')

def velocidad():
    print('velocidad')

def unidades(unidad, conversion, tipounidad):
    unidad = {'longitudes': ['millas','pies', 'kilometros', 'pulgadas'],
              'pesos': ['kilogramos', 'libras', 'onzas'],
              'volumen': ['litos', 'galones', 'onzas liquidas'],
              'temperatura': ['kelvin', 'celcius', 'fahrenheit'],
              'area': ['metros cuadrados', 'pies cuadrados','acres'],
              'velocidad': ['kilometro hora', 'pies hora', 'millas hora']}
    print(f'Elige tus unidades, aqui te dejo todas tus opciones:')
    for i in range(len(unidad[tipounidad])):
        print(f'{unidad[tipounidad][i].capitalize()}', end= ' ')

    unidad = input('\n\nElige el tipo de unidad que quieres convertir: ')

#Bucle programa principal 
while True:
    #imprime las opciones a elegir y pide la seleccion
    print('CONVERTIDOR DE UNIDADES'.center(31,'-'))

    lista = ['longitud','peso','volumen','temperatura','area','velocidad','salir']

    for i in range(len(lista)):
        print(f'{i + 1} - {lista[i].capitalize()}')

    seleccion = input('Elige el tipo de unidades que quieras convertir: ')

    # comprobamos las selecciones y llamamos a la funcion encargada de hacer los calculos depues de elegir las unidades
    if seleccion.lower() == lista[-1]:
        break

    elif seleccion.lower() == lista[0]:
        print('\n Elige las unidades que quieres convertir\n'.upper().center(149, '-'))
        unidad = ''
        cambio = ''
        unidades(unidad, cambio, 'longitudes')
        longitud(unidad, cambio)

    elif seleccion.lower() == lista[1]:
        peso()

    elif seleccion.lower() == lista[2]:
        volumen()

    elif seleccion.lower() == lista[3]:
        temperatura()

    elif seleccion.lower() == lista[4]:
        area()

    elif seleccion.lower() == lista[5]:
        velocidad()

    else:
        print('\nPor favor, introduce una respuesta valida\n')
