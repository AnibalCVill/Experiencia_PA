from random import randint

def adivinar_numero():
    num=randint(1,10)

    print("Ingrese su numero")
    numero_ingresar = input()
    if numero_ingresar == num:
        print("Felicidades, adivinaste el numero")
    else:
        print("Mal, era el", num)
