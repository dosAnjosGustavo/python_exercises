pessoa = {}
coletivo = []
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ')
    while True:
        pessoa['sexo'] = input(
            'Sexo: [M/F] ').upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    coletivo.append(pessoa.copy())
    cont = ' '
    while cont not in 'SN':
        cont = input('Quer continuar? [S/N] ').upper()[0]
    if cont == 'N':
        break
media = soma/len(coletivo)
print('-='*30)
print(coletivo)
print(f'- {len(coletivo)} pessoas cadastradas.')
print(f'- A média de idade é de {media:.2f}.')
mulheres = []
velhos = []
for k in coletivo:
    if k['sexo'] == 'F':
        mulheres.append(k['nome'])
    if k['idade'] > media:
        velhos.append(k)
print(f'- Mulheres cadastradas foram: ', end='')
for v in mulheres:
    print(f'{v} -> ', end='')
print('Fim')
print('- Lista das pessoas que estão acima da média: ')
for k in velhos:
    print(f'nome = {k["nome"]}; sexo = {k["sexo"]}; idade = {k["idade"]};')
