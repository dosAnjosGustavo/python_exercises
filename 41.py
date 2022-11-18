from datetime import date
print('A Confederação Nacional de Natação precisa saber qual sua categoria.')
an = int(input('Informe seu ano de nascimento: '))
ab = date.today().year
x = ab - an
if x <= 9:
    print('MIRIM.')
elif x <= 14 and x > 9:
    print('INFANTIL.')
elif x <= 19 and x > 14:
    print('JUNIOR.')
elif x <= 20 and x > 19:
    print('SÊNIOR.')
else:
    print('MASTER.')
