import random
def memoria():
    """
    Esta función representa el juego de memoria.
    Debes generar una secuencia de números al azar y mostrarla al usuario.
    Luego, debes pedir al usuario que repita la secuencia.
    Se debe mostrar un mensaje si el usuario acierta o no.
    """
    sec = ''
    
    for i in range(0,5):
        num = str(random.randint(0,9))
        sec += num
    usuario = str(input(f'repita la siguiente secuencia: {sec}'))
    if usuario == sec:
        print('acertaste!')
    else:
        print('no acertaste!')