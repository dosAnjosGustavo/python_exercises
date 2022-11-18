from datetime import date
ano = int(input('Digite o ano de seu nascimento: '))
calc = (date.today().year) - ano
if calc < 18:
    print(
        f'Você ainda vai se alistar ao serviço militar. O prazo do seu alistamento é daqui {18-calc} ano(s).')
elif calc == 18:
    print('Esse é o ano do seu alistamento!')
else:
    print(f'O prazo do seu alistamento foi {calc-18} ano(s) atrás.')
