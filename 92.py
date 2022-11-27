from datetime import date
anoatual = date.today().year
ficha = {}
ficha['Nome'] = input('Nome: ')
ficha['Ano de nascimento'] = int(input('Ano de nascimento: '))
ficha['Idade'] = anoatual - ficha['Ano de nascimento']
ficha['CTPS'] = int(input('CTPS (0 não tem): '))
if ficha['CTPS'] != 0:
    ficha['Ano de contratação'] = int(input('Ano de contratação: '))
    ficha['Idade na aposentadoria'] = ficha['Ano de contratação'] - \
        ficha['Ano de nascimento'] + 35
    ficha['Salário'] = float(input('Salário: R$ '))
print('-='*20)
for k, v in ficha.items():
    print(f'- {k} é {v}.')
