def multy5(x):
    data = x
    if isinstance(data, int):
        return [5 * i for i in range(1, data + 1)]
    if isinstance(data, list):
        sub_lista = []
        for num in data:
            multiploNum = multy5(num)
            sub_lista.append(multiploNum)
        return sub_lista


def apply(func, valor, limite) -> list:
    if limite == 0:
        return [valor]
    final_result = [valor, func(valor), apply(multy5, func(valor), limite - 1)]
    return final_result


resultado = apply(multy5, 2, 4)
print(len(resultado))
for lista in resultado:
    print(lista)
    print("----------------------------------------------------")
