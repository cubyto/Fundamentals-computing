# %%
print("PROBLEMA 1")
listaVocal = ["a", "e", "i", "o", "u"]
string = ", ".join(listaVocal)
print(f"Las coales son {string}")
# %%
print("PROBLEMA 5")


def get_list(centinela):
    lista = []
    num = int(input("Ingrese un numero> "))
    if num == -1:
        return lista

    while num != centinela:
        try:
            num = int(input("Ingrese un numero> "))
            if num <= 0:
                print("Ingresar un numero positivo")
            else:
                lista.append(num)
        except ValueError:
            print("Ingresar un numero porfavor")
    return lista


def es_primo(n, divisor=2):
    if n <= 1:
        return False
    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False
    else:
        return es_primo(n, divisor + 1)


listaNum = get_list(-1)
stringList = ", ".join(str(num) for num in listaNum)
countPrimos = sum(1 for num in listaNum if es_primo(num))
print(
    f"La cantidad de numeros primos ingresados en la lista {countPrimos} y la lista es {stringList}"
)
# %%
print("PROBLEMA 6")
from random import *

listaRandom = [randint(-100, 100) for i in range(10)]
minZero = sum(1 for num in listaRandom if num < 0)
maxZero = sum(1 for num in listaRandom if num > 0)
strMinZero = ", ".join(str(num) for num in listaRandom if num < 0)
strMaxZero = ", ".join(str(num) for num in listaRandom if num > 0)
print(
    f"En la lista {listaRandom}, los numeros positivos son {strMaxZero} y su cantidad es {maxZero}, los negativos son {strMinZero} y su cantidad es {minZero}"
)
# %%
print("PROBLEMA 7")
from random import *

listaNotas = [randint(1, 20) for i in range(10)]
max = 0
min = 20
for num in listaNotas:
    if num > max:
        max = num
    elif num < min:
        min = num
print(f"En {listaNotas} el maximo es {max} y el minimo es {min}")
# %%
print("PROBLEMA 8")


def get_list1(centinela):
    lista = []
    num = int(input("Ingrese un numero> "))
    if num == -1:
        return lista

    while num != centinela:
        try:
            num = int(input("Ingrese un numero> "))
            if num <= 0:
                lista.append(num)
            else:
                lista.append(num)
        except ValueError:
            print("Ingresar un numero porfavor")
    return lista


listaUser = get_list1(0)
numMax = max(listaUser)
numMin = min(listaUser)
print(f"En la lista {listaUser} el maximo es {numMax} y el minimo es {numMin}")

# %%

print("PROBLEMA 9")
lista = [1, 3, 1, 3, 6, 4, 5, 6, 6, 6, 8, 9]
sum = 0
for i in range(1, len(lista) + 1, 2):
    sum += lista[i]
string = ", ".join(str(lista[i]) for i in range(1, len(lista) + 1, 2))

print(
    f"En la lista {lista} los numeros en posicion par son {string} y su suma es {sum}"
)

# %%

print("PROBLEMA 10")
from math import pow, sqrt


def get_list_num(limit):
    lista = []
    num = int(input("Ingrese un numero> "))
    count = 0
    while count != limit:
        try:
            num = int(input("Ingrese un numero> "))
            if num <= 0:
                print("Ingresar un numero positivo")
            else:
                lista.append(num)
        except ValueError:
            print("Ingresar un numero porfavor")
        count += 1
    return lista


def make_str(lista):
    return ", ".join(str(num) for num in lista)


listaNum = get_list_num(10)
avg = sum(listaNum) / len(listaNum)
var = sum(pow((num - avg), 2) for num in listaNum)
desEst = sqrt(var)

string = make_str(listaNum)

print(f"Para la lista de numeros {string}")
print(f"La media aritmetica es {avg}")
print(f"La varianza es {var}")
print(f"La desviacion estandar es {desEst}")


# %%

print("PROBLEMA 11")
from random import randint


def is_my_num(lista):
    print("Usted solo tiene 5 intentos")
    count = 0
    while count != 6:
        try:
            num = int(input("Ingresa un numero> "))
            if not num in lista:
                print(f"{num} no esta en la lista")
            else:
                return print(f"El numero {num} si esta en la lista")
        except ValueError:
            print("Ingresar un numero porfavor")
        count += 1
    return print("Se le acabaron los intentos")


lista19 = [randint(1, 100) for i in range(1, 100)]
res = is_my_num(lista19)

# %%

print("PROBLEMA 12")
lista = [1, 3, 1, 3, 6, 4, 5, 6, 6, 6, 8, 9]
cantidad2 = {}
for num in lista:
    if num in cantidad2:
        cantidad2[num] += 1
    else:
        cantidad2[num] = 1
print(lista)
print(cantidad2)

countFilter = {k: v for k, v in cantidad2.items() if v > 1}
string = ", ".join(f"el {k} se repite {v} veces" for k, v in cantidad2.items() if v > 1)
print("-------------")
print(string)

for k, v in countFilter.items():
    print(f"El numero {k} se repite {v} veces")

# %%

print("PROBLEMA 14")
lista14_1 = [1, 3, 4, 5, 45, 6, 7, 8, 90, 8]
lista14_2 = [3, 5, 4, 5, 3, 6, 87, 7, 90, 8]

list_sum = {}
list_prod = {}
for i in range(len(lista14_1)):
    num1 = lista14_1[i]
    num2 = lista14_2[i]
    suma = num1 + num2
    prod = num1 * num2
    list_sum[f"{num1} y {num2}"] = suma
    list_prod[f"{num1} y {num2}"] = prod

print(lista14_1)
print(lista14_2)

print("SUMA")
for k, v in list_sum.items():
    print(f"La suma de {k} es {v}")

print("PRODUCTO")
for k, v in list_prod.items():
    print(f"La suma de {k} es {v}")

print("PROBLEMA 15")
from random import randint

lista15 = [randint(1, 20) for i in range(10)]

for i in range(1, len(lista15) + 1):
    lista15[i - 1] = lista15[-i]
print(lista15)

# %%

print("PROBLEMA 16")
lista16 = [randint(1, 20) for i in range(10)]
listaInvert = []

for i in range(1, len(lista16) + 1):
    listaInvert.append(lista16[-i])
print(lista16)
print(listaInvert)

# %%

print("PROBLEMA 19")
from random import randint


def get_data(lista):
    while True:
        try:
            cadena = input(
                "Ingresa la pocicion a partir de la que se insertara y desplazara, tmbn el numero ambos separados por un espacio> "
            )
            pos, num = map(int, cadena.split())
            print(cadena, cadena.split())
            if not -1 < pos < len(lista):
                print(f"{pos} no esta en el rango de la longitud de la cadena mostrada")
            else:
                return [pos, num]
        except ValueError:
            print(ValueError)
            print("Ingrese numeros por favor")


lista = [randint(0, 100) for i in range(10)]
print(lista)
print(f"La lista tiene una longitud de {len(lista)}")

indexNum, changeValue = get_data(lista)

for i in range(len(lista) + 1):
    if indexNum == len(lista):
        lista.append(changeValue)
    if i == indexNum:
        changeValue, lista[i] = lista[i], changeValue
        indexNum = i + 1
print(lista, len(lista))
