# %%
print("PROBLEMA 1")
from math import sqrt


def conteo_div(num):
    listaDiv = []
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            listaDiv.append(i)
            listaDiv.append(num // i)
    return listaDiv


def divMax(obj):
    divMax = []
    numDivMax = 0
    for k, v in obj.items():
        if len(v) > len(divMax):
            numDivMax = k
            divMax = v
    return [numDivMax, divMax]


def main():
    objDiv = {}
    for num in range(1, 101):
        objDiv[num] = conteo_div(num)
    print(objDiv)
    res = divMax(objDiv)
    print(res)


main()

# %%
print("PROBLEMA 2")
from random import randint


def sumad(num):
    lista = map(int, list(str(num)))
    suma = sum(lista)
    return suma


def get_sum_maxima(lista):
    sumDict = {}
    for num in lista:
        sumaNum = sumad(num)
        sumDict[num] = sumaNum
    sumMax = max(v for k, v in sumDict.items())
    resMax = {k: v for k, v in sumDict.items() if v == sumMax}
    return resMax


def main():
    lisNum = [randint(1, 100) for i in range(10)]
    resNum = get_sum_maxima(lisNum)
    print(lisNum)
    print(resNum)


main()
# %%
print("PROBLEMA 3")
