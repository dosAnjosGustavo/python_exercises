dados = []
galera = []
maior = menor = 0
while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    if len(galera) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    galera.append(dados[:])
    dados.clear()
    stop = ' '
    while stop not in 'SN':
        stop = (input('Quer continuar? [S/N] ')).upper()[0]
    if stop == 'N':
        break
print(f'a) Foram cadastradas {len(galera)} pessoas;')
print(f'b) O maior peso foi {maior}kg, das pessoas: ', end='')
for p in galera:
    if p[1] == maior:
        print(f'{p[0]} -> ', end='')
print('Fim.')
print(f'\nc) O menor peso foi {menor}kg, das pessoas: ', end='')
for p in galera:
    if p[1] == menor:
        print(f'{p[0]} -> ', end='')
print('Fim.')
