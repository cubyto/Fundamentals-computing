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


def change(lista):
    for i in range(len(lista)):
        if i % 2 == 0 or i == 0:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
    return lista


listaToChange = [randint(1, 100) for i in range(10)]
print(listaToChange)
res = change(listaToChange)
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
