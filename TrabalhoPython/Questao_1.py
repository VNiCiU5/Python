import numpy
import numpy as np

def Questao1():

    print("questão 1")


    array = np.empty(4, dtype = int)

    for i in range(4):
        array[i] = input(i)

    print(array)

    max_value = np.max(array)

    print("maior valor: ", max_value)

    min_value = np.min(array)

    print("menor valor: ",min_value)

    soma = 0

    for i in array:
        soma = soma + i

    print("soma de valores: ", soma)

    media = soma / 4
    print("media de valores ", media)



    for i in range(0,len(array)):
        if array[i] % 2 == 0:
            print("numero pares com resto 0:", array[i])

    for i in range(0,len(array)):
        if array[i] % 2 != 0:
            print("numero impares:", array[i])