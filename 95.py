player = {}
gols = []
players = []
games = None
while True:
    player.clear()
    gols.clear()
    player['nome'] = input('Nome do jogador: ')
    while True:
        try:
            games = int(input(f'Quantas partidas {player["nome"]} jogou? '))
            break
        except ValueError:
            print('Digite um número, ainda que seja zero.')
    for v in range(0, games):
        try:
            gols.append(int(input(f'Quantos gols na partida {v+1}? ')))
        except ValueError:
            print('Digite um número, ainda que seja zero.')
    player['gols'] = (gols)[:]
    player['total'] = sum(gols)
    players.append(player.copy())
    cont = ' '
    while cont not in 'SN':
        cont = input('Quer continuar? [S/N] ').upper()[0]
    if cont == 'N':
        break
print(players)
print('-='*30)
print(f'{"cod":<4}', end='')
for i in player.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(players):
    print(f'{k+1:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    n = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if n == 999:
        break
    if n > len(players):
        print(f'Não existe jogador com código {n}.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {players[n-1]["nome"]}:')
        for i, g in enumerate(players[n-1]['gols']):
            print(f'No jogo {i+1} fez {g} gols.')
