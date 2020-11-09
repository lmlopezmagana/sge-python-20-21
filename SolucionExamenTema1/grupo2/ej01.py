# Ejercicio 1
from itertools import permutations


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


def mediano_v1(num):
    promedio = (grande(num) + peque(num)) / 2
    min_diferencia = grande(num) - promedio;
    result = -1
    for n in permutaciones_v1(num):
        mayor = max(promedio, n)
        menor = min(promedio, n)
        diferencia = mayor - menor
        if diferencia < min_diferencia:
            min_diferencia = diferencia
            result = n
    return result


def permutaciones_v1(num):
    permutaciones = get_perms(str(num))
    return map(int, permutaciones);


def get_perms(s, i=0):
       """
       Returns a list of all (len(s) - i)! permutations t of s where t[:i] = s[:i].
       """
       # To avoid memory allocations for intermediate strings, use a list of chars.
       if isinstance(s, str):
           s = list(s)

       # Base Case: 0! = 1! = 1.
       # Store the only permutation as an immutable string, not a mutable list.
       if i >= len(s) - 1:
           return ["".join(s)]

       # Inductive Step: (len(s) - i)! = (len(s) - i) * (len(s) - i - 1)!
       # Swap in each suffix character to be at the beginning of the suffix.
       perms = get_perms(s, i + 1)
       for j in range(i + 1, len(s)):
           s[i], s[j] = s[j], s[i]
           perms.extend(get_perms(s, i + 1))
           s[i], s[j] = s[j], s[i]
       return perms


def mediano_v2(num):
    promedio = (grande(num) + peque(num)) / 2
    min_diferencia = grande(num) - promedio;
    result = -1
    for n in permutaciones_v2(num):
        mayor = max(promedio, n)
        menor = min(promedio, n)
        diferencia = mayor - menor
        if diferencia < min_diferencia:
            min_diferencia = diferencia
            result = n
    return result

def permutaciones_v2(num):
    permutaciones = [''.join(p) for p in permutations(str(num))]
    return map(int, permutaciones)


print(peque(2342))
print(grande(2342))
print(dif(2342))
print(mediano_v1(2342))
print(mediano_v2(2342))
