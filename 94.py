
fichas = []
while True:
    pessoa = {'nome': input('Nome: '), 'Sexo': input(
        'Sexo: [M/F] '), 'Idade': int(input('Idade: '))}
    fichas.append(pessoa)
    cont = ' '
    while cont not in 'SN':
        cont = input('Quer continuar? [S/N] ').upper()[0]
    if cont == 'N':
        break
print('-='*30)
print(fichas)
print(f'O grupo tem {len(fichas)} pessoas.')
cont = 0
som = 0
for k in fichas:
    som += fichas[k]['Idade']
    cont += 1
media = som / cont
print(f'A média de idade é de {media}.')
