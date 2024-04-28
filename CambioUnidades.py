from tkinter import *
from tkinter import ttk
#Se van a convertir algunas unidades como Volumen, Temperatura, Velocidades, Areas, Peso y Longitudes
def conversion(seleccion, unidad, cambio, valor):
    conversiones = {
        'Longitudes': {
            'Kilometros': {
                'Millas': 0.621371,
                'Pies': 3280.84,
                'Pulgadas': 39370.08
            },
            'Millas': {
                'Kilometros': 1.60934,
                'Pies': 5280,
                'Pulgadas': 63360
            },
            'Pies': {
                'Kilometros': 0.0003048,
                'Millas': 0.000189393939,
                'Pulgadas': 12
            },
            'Pulgadas': {
                'Kilometros': 0.0000254,
                'Millas': 0.0000157828283,
                'Pies': 1/12
            }
        },
        'Pesos': {
            'Kilogramos': {
                'Libras': 2.20462,
                'Onzas': 35.274
            },
            'Libras': {
                'Kilogramos': 0.453592,
                'Onzas': 16
            },
            'Onzas': {
                'Kilogramos': 0.0283495,
                'Libras': 0.0625
            }
        },
        'Volumenes': {
            'Litros': {
                'Galones': 0.264172,
                'Onzas liquidas': 33.814
            },
            'Galones': {
                'Litros': 3.78541,
                'Onzas liquidas': 128
            },
            'Onzas liquidas': {
                'Litros': 0.0295735,
                'Galones': 0.0078125
            }
        },
        'Temperaturas': {
            'Kelvin': {
                'Celcius': lambda x: round(x - 273.15),
                'Fahrenheit': lambda x: round(x * 9/5 - 459.67)
            },
            'Celcius': {
                'Kelvin': lambda x: round(x + 273.15),
                'Fahrenheit': lambda x: round(x * 9/5 + 32)
            },
            'Fahrenheit': {
                'Kelvin': lambda x: round((x + 459.67) * 5/9),
                'Celcius': lambda x: round((x - 32) * 5/9)
            }
        },
        'Areas': {
            'Metros cuadrados': {
                'Pies cuadrados': 10.7639,
                'Acres': 0.000247105
            },
            'Pies cuadrados': {
                'Metros cuadrados': 0.092903,
                'Acres': 0.0000229568
            },
            'Acres': {
                'Metros cuadrados': 4046.86,
                'Pies cuadrados': 43560
            }
        },
        'Velocidades': {
            'Kilometro hora': {
                'Pies hora': 3280.84,
                'Millas hora': 0.621371
            },
            'Pies hora': {
                'Kilometro hora': 0.0003048,
                'Millas hora': 0.000189393939
            },
            'Millas hora': {
                'Kilometro hora': 1.60934,
                'Pies hora': 5280
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

def on_select(event):
    # Esta función se ejecutará cuando el usuario seleccione una opción
    seleccion = BDesplegable.get()
    print("El usuario seleccionó:", seleccion)
    if seleccion in unidad:
        opciones = Label(frame, text=f"\n".join(unidad[seleccion]), bg= 'silver', pady=10)
        opciones.grid(row=2, column=0, sticky='we')
    else:
        print('WTF')

lista = ['Longitudes','Pesos','Volumenes','Temperaturas','Areas','Velocidades']

unidad = {'Longitudes': ['Millas','Pies', 'Kilometros', 'Pulgadas'],
              'Pesos': ['Kilogramos', 'Libras', 'Onzas'],
              'Volumenes': ['Litros', 'Galones', 'Onzas Liquidas'],
              'Temperaturas': ['Kelvin', 'Celcius', 'Fahrenheit'],
              'Areas': ['Metros cuadrados', 'Pies cuadrados','Acres'],
              'Velocidades': ['Kilometro hora', 'Pies hora', 'Millas hora']}
"""
while True:
    print('CONVERTIDOR DE UNIDADES'.center(31,'-'))

    

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
"""

ventana = Tk()
ventana.title("CONVERSION DE UNIDADES")

ancho = 550
alto = 450

ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

x = (ancho_pantalla // 2) - (ancho // 2)
y = (alto_pantalla // 2) - (alto // 2)

ventana.geometry(f'{ancho}x{alto}+{x}+{y}')

ventana.resizable(0, 0)

ventana.config(background='silver')

frame = Frame(ventana)
frame.pack()
descripcion = Label(frame, text='En este programa podras elegir entre varios tipos de unidades para ver que conversiones tienes disponibles para realizar.', background='silver', wraplength=550)
descripcion.grid(row=0, column=0)

BDesplegable = ttk.Combobox(frame, text="Unidades a elegir", values=lista, font= ('Arial', 20), background='silver')
# Vincula el evento '<<ComboboxSelected>>' a la función on_select
BDesplegable.bind("<<ComboboxSelected>>", on_select)
BDesplegable.grid(row=1, column= 0)


ventana.mainloop()