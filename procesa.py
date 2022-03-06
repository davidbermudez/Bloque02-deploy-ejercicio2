"""Módulo procesa para ejercicio de clase."""


def procesa(operacion, operando1, operando2=1):
    if operacion == "s":
        res = suma(operando1, operando2)
    elif operacion == "r":
        res = resta(operando1, operando2)
    elif operacion == "d":
        res = divide(operando1, operando2)
    elif operacion == "c":
        res = cuenta_vocales(operando1, operando2)
    else:
        res = None
        print("operación no permitida")

    return res


def suma(a, b):
    x = "noseusa"  # comentar / descomentar para pruebas
    return a + b


def resta(a, b):
    return a - -b  # error para pruebas


def divide(a, b):
    if b == 0:
        return None
    else:
        return a / b


def cuenta_vocales(a, b):
    cadena = str(a) + str(b)
    contador = 0
    for letra in cadena:
        if letra.lower() in "aeiou":
            contador += 1
    return contador
