print('''Vamos calcular aumento salarial.
Quem ganha até R$ 1.250,00 vai passar a receber aumento de 15%.
Quem ganha mais que isso, receberá aumento de 10%.''')
s = float(input('Digite seu salário: R$'))
if s <= 1250:
    print(f'Seu salário passará a ser {s/100*115}.')
else:
    print(f'Seu salário passará a ser {s/100*110}.')
