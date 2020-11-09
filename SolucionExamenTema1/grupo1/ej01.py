# Ejercicio 1

def peque(num):
    cadena_numero = str(num)
    pequenio = ''.join(sorted(cadena_numero))
    return int(pequenio)

def grande(num):
    peque_cadena = str(peque(num))
    grande_cadena = peque_cadena[::-1]
    return int(grande_cadena)

def dif(num):
    return grande(num)-peque(num)


def grandes(*args):
    result = []
    for n in args:
        result.append(grande(n))
    return result

def peques(*args):
    result = []
    for n in args:
        result.append(peques(n))
    return result


print(peque(1984))
print(grande(1984))
print(dif(1984))
print(grandes(1983, 1347, 8789))
