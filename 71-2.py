print('='*30)
print('BANCO CEV')
print('='*30)
total = int(input('Que valor você quer sacar? R$'))
ced = 50
c50 = c20 = c10 = c1 = 0
while True:
    if total >= ced:
        total -= ced
        c50 += 1
    else:
        if c50 > 0:
            print(f'Total de {c50} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        c50 = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
