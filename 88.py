from random import randint
print('-'*30)
print(' '*4, 'JOGA NA MEGA SENA', ' '*3)
print('-'*30)
n = int(input('Sortear quantos jogos? '))
lista = []
dados = []
for c in range(0, n):
    cont = 0
    while cont < 6:
        num = randint(1, 61)
        if num not in dados:
            dados.append(num)
            cont += 1
        dados.sort()
    lista.append(dados[:])
    dados.clear()
print(f'SORTEANDO {n} JOGOS')
for c in range(0, n):
    print(f'Jogo {c+1}: {lista[c]}.')
print('BOA SORTE!')
