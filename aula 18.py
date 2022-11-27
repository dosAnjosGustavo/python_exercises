galera = []
dado = []
for c in range(0, 3):
    dado.append(input('Nome: '))
    dado.append(input('Idade: '))
    galera.append(dado[:])
    dado.clear()
print(galera)
