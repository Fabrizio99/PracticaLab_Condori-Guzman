#AUTOR: De la Cruz Quispe Royer Alvaro

def esPrimo(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True            

def applicacion():
    numero = int(input('escribe un numero: '))
    resultado = esPrimo(numero)

    if resultado is True:
        print('el numero es primo!!')
    else:
        print('el numero no es primo!!')


applicacion()