
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









