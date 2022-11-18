somaidade = 0
maisvelho = ''
maioriade = 0
mulhermenos20 = 0
for g in range(1, 5):
    nome = input(f'Digite o nome da {g}ª pessoa: ')
    idade = int(input(f'Digite a idade: '))
    sexo = input(f'Digite o sexo [M/F]: ')
    while 'Mm' or 'Ff' not in sexo:
        sexo = input(f'Digite o sexo da {g}ª pessoa [M/F]: ')
    somaidade += idade
    if g == 1 and sexo in 'Mm':
        maisvelho = nome
        maioriade = idade
    if idade > maioriade and sexo in 'Mm':
        maioriade = idade
        maisvelho = nome
    if sexo in 'Ff' and idade < 20:
        mulhermenos20 += 1
media = somaidade/4
decimal = int((media*10) % 10)
if decimal != 0:
    print(f'A média de idade do grupo é de {media}.')
else:
    print(f'A média de idade do grupo é de {media:.0f}.')
if maioriade > 0:
    print(f'O homem mais velho é {maisvelho}.')
if mulhermenos20 > 0:
    print(f'Há {mulhermenos20} mulheres com menos de 20 anos.')
