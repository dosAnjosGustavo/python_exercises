tabela = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthias', 'Flamengo', 'Athtletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo',
          'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará-SC', 'Atlético-GO', 'Avaí', 'Juventude')
alfa = sorted(tabela)
posição = tabela.index('Avaí')
print(
    f'a) Os 5 primeiros colocados: {tabela[0]}, {tabela[1]}, {tabela[2]}, {tabela[3]}, {tabela[4]}.')
print(
    f'b) Os últimos 4 colocados: {tabela[-1]}, {tabela[-2]}, {tabela[-3]}, {tabela[-4]}.')
print('c) Os times em ordem alfabética: ', end='')
for times in alfa:
    print(f'{times} -> ', end='')
print('Fim.')
print(f'd) Posição da Chapecoense: {posição}.')
