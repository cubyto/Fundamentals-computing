# %%
print("PROBLEMA 1")


def signo(num):
    if num == 0:
        return 0
    if num > 0:
        return 1
    else:
        return -1


userNum1 = int(input("Ingrese un numero ya sea positivo o negativo> "))

checkNum = signo(userNum1)
print(f"Su numero es {checkNum}")

# %%
print("PROBLEMA 2")


def absolute(num):
    if num > 0:
        return num
    else:
        return num * -1


userNum2 = int(input("Ingrese un numero ya sea positivo o negativo> "))

checkNum = signo(userNum1)
print(f"Su numero es {checkNum}")

# %%
print("PROBLEMA 3")
from math import pow
from re import escape


def cuadrado(num):
    return pow(num, 2)


userNum3 = int(input("Ingrese un numero ya sea positivo o negativo> "))

powNum = cuadrado(userNum3)
print(f"El cuadrado del numero {userNum3} es {powNum}")

# %%
print("PROBLEMA 4")


def maximo(a, b, c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    if a > b and c > b:
        return c


numbers4 = input("Ingrese 3 numeros separados por un espacio> ")
num1_4, num2_4, num3_4 = map(int, numbers4.split())
numMax = maximo(num1_4, num2_4, num3_4)
print(f"Entre los numeros {numbers4.replace(' ', ', ')} el maximo es {numMax}")

# %%
print("PROBLEMA 5")


def dividesto(a, b):
    if a / b:
        return True
    return False


numbers5 = input("Ingrese 3 numeros separados por un espacio> ")
num1_5, num2_5 = map(int, numbers4.split())
checkDiv = dividesto(num1_5, num2_5)
print(checkDiv)


# %%
print("PROBLEMA 6")


def isCommonDivsor(a, b, c):
    if b / a and c / a:
        return f"{b} y {c}"
    elif b / a:
        return f"{b}"
    else:
        return f"{c}"


numbers6 = input("Ingrese 3 numeros separados por un espacio> ")
num1_6, num2_6, num3_6 = map(int, numbers6.split())
checkDiv6 = isCommonDivsor(num1_6, num2_6, num3_6)
print(f"{num1_6} es divisor de {checkDiv6}")

# %%
print("PROBLEMA 7")


def isCommonMultiple(a, b, c):
    if a / b or a / c:
        return True
    return False


numbers7 = input("Ingrese 3 numeros separados por un espacio> ")
num1_7, num2_7, num3_7 = map(int, numbers7.split())
checkMul7 = isCommonDivsor(num1_7, num2_7, num3_7)
print(checkMul7)

# %%
print("PROBLEMA 8")


def swap(a, b):
    a, b = b, a
    return [a, b]


numbers8 = input("Ingrese 3 numeros separados por un espacio> ")
num1_8, num2_8 = map(int, numbers8.split())
print(f"Tu 1er numro es {num1_8} y el 2do es {num2_8}")
checkMul8 = swap(num1_8, num2_8)
print(f"Ahora tu 1er numro es {num1_8} y el 2do es {num2_8}")

# %%

print("PROBLEMA 9")


def contarPos(lista):
    posNeg = {"positivos": 0, "negativos": 0}
    for num in lista:
        if num > 0:
            posNeg["positivos"] += 1
        else:
            posNeg["negativos"] += 1
    return posNeg


numbers8 = input("Ingrese 3 numeros separados por un espacio> ")
num1_8, num2_8 = map(int, numbers8.split())
print(f"Tu 1er numro es {num1_8} y el 2do es {num2_8}")
checkMul8 = swap(num1_8, num2_8)
print(f"Ahora tu 1er numro es {num1_8} y el 2do es {num2_8}")

# %%
print("PROBLEMA Adicional")


def check_num(listaAdi):

    cantidad2 = {}
    for num in listaAdi:
        if num in cantidad2:
            cantidad2[num] += 1
        else:
            cantidad2[num] = 1

    countFilter = {k: v for k, v in cantidad2.items() if v == 1}
    return countFilter


lista1 = [1, 3, 1, 3, 6, 4, 5, 6, 6, 6, 8, 9]
isInLista = check_num(lista1)
for k, v in isInLista.items():
    print(f"El numero {k} se repite {v} veces")

# %%
print("PROBLEMA 2")


def sumaD(limit):
    suma = 0
    num = ""
    for i in range(1, limit):
        num += str(i)
        suma += int(num)
    return suma


res = sumaD(4)
print(res)


# %%
print("PROBLEMA 3")


def get_num():
    while True:
        try:
            num = int(input("Ingresar el numero a calcular> "))
            if num < 0:
                print("Ingresa un numero positivo")
            else:
                return num
        except:
            print("Ingresa un numero por favor")


def fact_N(n):
    if n == 0:
        return 1
    else:
        return n * fact_N(n - 1)


num = get_num()

fact = fact_N(num)
print(fact)

n = get_num()
try:
    for i in range(2, n + 1, 2):
        res = fact_N(i)
        print(f"El factorial de {i} es {res}")
except ValueError:
    print("El factorial pedido es muy grande")

# %%
print("PROBLEMA 4")
num_n = int(input("Ingrese el numero de elementos que tiene su grupo> "))
num_k = int(input("Ingrese el numero de elementos que quiere tomar> "))
fact_k = fact_N(num_k)
fact_n = fact_N(num_n)
fact_difNK = fact_N(num_n - num_k)

comb = fact_n / fact_k * fact_difNK
print(comb)

# %%
print("PROBLEMA 5")


def get_num():
    while True:
        try:
            num = int(input("Ingresar el numero a calcular> "))
            if num < 0:
                print("Ingresa un numero positivo")
            else:
                return num
        except:
            print("Ingresa un numero por favor")


def es_primo(n, divisor=2):
    if n <= 1:
        return False
    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False
    return es_primo(n, divisor + 1)


numero = get_num()
res = es_primo(numero)
print(res)

# %%
print("PROBLEMA 6")


# Ejemplo de uso
def get_range():
    while True:
        try:
            cadena = input(
                "En que rango desea saber los numeros primos, separados por un espacio y en orden creciente"
            )
            init, limit = map(int, cadena.split())
            if not init > limit:
                print(f"{init} no puede ser mayor que {limit}")
            else:
                return [init, limit]
        except ValueError:
            print(ValueError)
            print("Ingrese numeros por favor")


initNum, limitNum = get_range()

for i in range(numero):
    if es_primo(i):
        print(f"{i} es un número primo.")
    else:
        print(f"{i} no es un número primo.")
# %%
print("PROBLEMA 8")


def only_letters(string):
    status = False
    for char in string:
        if "A" < char.upper() < "Z":
            status = True
    return status


def count_vocal(string):
    listVocal = ["a", "e", "i", "o", "u"]
    vocales = sum(1 for char2 in string if char2 in listVocal)
    return vocales


def count_consonant(string):
    listVocal = ["a", "e", "i", "o", "u"]
    consonat = sum(1 for char2 in string if not char2 in listVocal)
    return consonat


cadena = input("Ingrese una cadena de texto> ")
num_vocales = 0
num_consonant = 0
if only_letters(cadena):
    num_vocales = count_vocal(cadena)
    num_consonant = count_consonant(cadena)
print(f"En la cadena {cadena}")
print(f"Hay {num_vocales} vocales")
print(f"Hay {num_consonant} consonantes")

# %%
print("PROBLEMA 9")
from random import randint


def move(lista):
    element1 = lista[0]
    element2 = lista[1]
    for i in range(2, len(lista)):
        if i + 2 == len(lista):
            lista.append(element1)
            lista.append(element2)
            lista[-1], lista[-2] = lista[-3], lista[-4]
        if i % 2 == 0:
            element1, lista[i] = lista[i], element1
            element2, lista[i + 1] = lista[i + 1], element2
    lista[0], lista[1] = 0, 0
    return lista


listaToMove = [randint(1, 100) for i in range(10)]
print(listaToMove)
res = move(listaToMove)
print(res)

# %%
print("PROBLEMA 10")
from random import randint


def move(lista):
    for i in range(len(lista)):
        if i % 2 == 0 or i == 0:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
    return lista


listaToMove = [randint(1, 100) for i in range(10)]
print(listaToMove)
res = move(listaToMove)
print(res)

# %%
print("PROBLEMA 10")


def check(lista):
    status = True
    for i in range(int(len(lista) / 2) + 1):
        if not lista[i] == lista[-(i + 1)]:
            status = False
    return status


cadena = input(
    "Ingrese una lista de numeros, separada por espacios, nosotros veremos si es igual leida del reves"
)
listaToCheck = map(int, cadena.split())
print(listaToCheck)
res = check(listaToCheck)
print(res)

# %%
print("PROBLEMA 10")


def delete(lista):
    for i in range(len(lista)):
        for j in range(i):
            if lista[i] == lista[j]:
                lista[i] = None
                break
    resToSend = [num for num in lista if num is not None]
    return resToSend


listaToDelete = [1, 3, 1, 3, 6, 4, 5, 6, 6, 6, 8, 9]
res = delete(listaToDelete)
print(listaToDelete)
print(res)
