import random
def cachipun():
    """
    Esta función representa el juego de cachipun.
    Debes pedir al usuario que elija piedra, papel o tijera, y luego comparar su elección con la de la computadora.
    La computadora debe elegir una opción al azar.
    """

    usuario = str(input('Ingrese "PIEDRA", "PAPEL" o "TIJERA"'))
    lista = ['PIEDRA', 'PAPEL', 'TIJERA']
    comp = random.choice(lista)

    if usuario == comp:
        print('Empataste')
    else:
        if usuario == 'PIEDRA' and comp == 'PAPEL':
            print(f'Perdiste, la computadora eligio {comp}')
        elif usuario == 'TIJERA' and comp == 'PIEDRA':
            print(f'Perdiste, la computadora eligio {comp}')
        elif usuario == 'PAPEL' and comp == 'TIJERA':
            print(f'Perdiste, la computadora eligio {comp}')
        else:
            print(f'Ganaste, la computadora eligio {comp}')
    