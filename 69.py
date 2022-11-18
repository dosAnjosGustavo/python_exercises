tot18 = totH = totM20 = 0
while True:
    print('-'*25)
    print('CADASTRE UMA PESSOA')
    print('-'*25)
    while True:
        try:
            idade = int(input(f'Idade: '))
            break
        except ValueError:
            print('Digite um número inteiro.')
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input(f'Sexo: [M/F] ')).strip().upper()[0]
    print('-'*25)
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resp in 'N':
        break
print(f'''Foram cadastradas:
a) {tot18} pessoas com mais de 18 anos;
b) {totH} homens; e
c) {totM20} mulheres com menos de 20 anos.''')
