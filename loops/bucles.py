# %%

def divisores1(n):
  lista = list(i for i in range(1, n-1) if n%i==0)
  return lista
data = input('Ingrese el rango a evaluar separando por espacios> ')
num1_str, num2_str = data.split()
divPerfect = []
for i in range(int(num1_str), int(num2_str)):
  listaDiv = divisores1(i)
  if sum(listaDiv) == i:
    print(listaDiv, i)
    divPerfect.append(i)
countNumPerfect = sum(1 for i in divPerfect)
stringNum = ', '.join(str(num) for num in divPerfect)
print(f'La cantidad de numeros perfectos son {countNumPerfect} y son {stringNum}')
# %%

import math

def divisores(n):
    # Usar un conjunto para evitar duplicados
    divisors = {1}
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return divisors

data = input('Ingrese el rango a evaluar separando por espacios> ')

try:
    num1, num2 = map(int, data.split())
    if num1 >= num2:
        print("El primer número debe ser menor que el segundo.")
    else:
        divPerfect = []
        for i in range(num1, num2):
            if i > 1:  # Los números perfectos son mayores que 1
                listaDiv = divisores(i)
                if sum(listaDiv) == i:
                    print(listaDiv, i)
                    divPerfect.append(i)
        
        countNumPerfect = len(divPerfect)
        stringNum = ', '.join(str(num) for num in divPerfect)
        print(f'La cantidad de números perfectos son {countNumPerfect} y son {stringNum}')
except ValueError:
    print("Entrada inválida. Asegúrese de ingresar dos números enteros separados por un espacio.")


lista = [1, 34, 4, 5, 6]
