from random import randint
jogos1 = {}
for cont in range(1, 5):
    jogada = randint(1, 6)
    jogos1['Jogador ' + str(cont)] = jogada
print('Valores sorteados:')
for k, v in jogos1.items():
    print(f'{k} tirou {v} no dado.')
print('-=' * 13)
print(f'{"= RANKING DOS JOGADORES =":^26}')
jogos2 = dict(sorted(jogos1.items(), key=lambda item: item[1], reverse=True))
c = 1
for k, v in jogos2.items():
    print(f'{c}º lugar: {k} com {v}.')
    c += 1
