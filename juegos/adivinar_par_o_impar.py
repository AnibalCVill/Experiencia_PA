import random
def adivinar_par_o_impar(respuesta):
    a=random.randint(0,10)
    respuesta=respuesta.lower()
    if respuesta=="par":
        if a==0 or a==2 or a==4 or a==6 or a==8 or a==10:
            print("Correcto! El numero es:",a)
        else:
            print("Incorrecto :c El numero es:",a)
    if respuesta=="impar":
        if a==0 or a==2 or a==4 or a==6 or a==8 or a==10:
            print("Incorrecto :c El numero es:",a)
        else:
            print("Correcto! El numero es:",a)
respuesta=input("Escoge, par o impar?")
adivinar_par_o_impar(respuesta)