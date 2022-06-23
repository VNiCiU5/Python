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



