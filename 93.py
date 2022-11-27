player = {}
gols = []
player['nome'] = input('Nome do jogador: ')
games = int(input(f'Quantas partidas {player["nome"]} jogou? '))
for v in range(0, games):
    gols.append(int(input(f'Quantos gols na partida {v+1}? ')))
player['gols'] = (gols)[:]
player['total'] = sum(gols)
print('-='*30)
print(player)
print('-='*30)
for k, v in player.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador {player["nome"]} jogou {games} partidas.')
for k, v in enumerate(player['gols']):
    print(f'Na partida {k+1}, fez {v} gols.')
print(f'Foi um total de {player["total"]} gols.')
