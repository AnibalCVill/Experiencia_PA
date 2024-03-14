from random import randint

def juego_del_dado():
    puntaje_humano=0   
    puntaje_computador=0
    turno=0

    while puntaje_humano <=30 and puntaje_computador<=30:
        if turno%2==0:
            print("Es tu turno, presiona Enter para lanzar el dado")
            var = input()
            dado = randint(1,6)
            puntaje_humano+=dado
            print("Has sumado", dado, "puntos, La puntuacion actual es: Humano", puntaje_humano, "Computador", puntaje_computador)
        else:
            print("Es turno del computador")
            dado = randint(1,6)
            puntaje_computador+=dado
            print("El computador ha sumado", dado, "puntos, La puntuacion actual es: Humano", puntaje_humano, "Computador", puntaje_computador)
        turno+=1
    if puntaje_computador>=30:
        print("Perdiste compadre")
    elif puntaje_humano>=30:
        print("Ganaste, felicidades")

