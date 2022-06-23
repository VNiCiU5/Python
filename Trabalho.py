
"""
QUESTAO 1

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

"""





"""
--------------------------------------------------------------------------------------------------
"""





"""

QUESTAO 2

from numpy import random

x = random.randint(1000)


print("numero aleatorio: ", x)
numeroAleatorio = int(x)
i = 0
acerto = 0
acertoFaltantes = 10
print(numeroAleatorio)

for i in range(10):
    while(acerto == 0):
            acertoFaltantes -= 1
            print("quantidade restante de acertos: ", acertoFaltantes)
            print("dê o seu chute: ")
            numero = input()
            numeroint = int(numero)
            print(numeroint)
            if numeroint == numeroAleatorio:
                print("voce acertou!")
                acerto += 1
            elif numeroint > numeroAleatorio:
                print("voce errou, seu numero é maior")
            elif numeroint < numeroAleatorio:
                print("voce errou, seu numero é menor")
"""





"""
--------------------------------------------------------------------------------------------------
"""




"""

QUESTAO 3

import numpy as np

array = np.empty(20, dtype=int)

for i in range(20):
    array[i] = input(i)

print(array)

for i in range(0,len(array)):
   if array[i] % 2 != 0:
       array[i] = 0
   elif array[i] < 30:
       array[i] = 1
   else:
       array[i] = 2

print(array)

"""





"""
--------------------------------------------------------------------------------------------------
"""




"""

QUESTAO 4


anos = 0
qtdCigarros = 0
qtdAnos = 0

print("quantos anos de vida tem a pessoa? ")
anos = int(input())


print("quantidade de cigarros fumados ao dia?")
qtdCigarros = int(input())


print("quantos anos essa pessoa fuma ? ")
qtdAnos  = float(input())


calculoDiario = (10*qtdCigarros)
print("quantidade de minutos reduzidos ao dia", calculoDiario)



redução_em_minutos = qtdAnos * 365 * qtdCigarros * 10
# Um dia tem 24 x 60 minutos
redução_em_dias = redução_em_minutos / (24 * 60)
print("Redução do tempo de vida %8.2f dias." % redução_em_dias)

"""





