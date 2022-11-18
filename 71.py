print('='*30)
print('BANCO CEV')
print('='*30)
total = int(input('Que valor você quer sacar? R$'))
ced = 50
c50 = c20 = c10 = c1 = 0
while True:
    while total >= 50:
        total -= 50
        c50 += 1
        if total < 50:
            break
    while total >= 20:
        total -= 20
        c20 += 1
        if total < 20:
            break
    while total >= 10:
        total -= 10
        c10 += 1
        if total < 20:
            break
    while total >= 1:
        total -= 1
        c1 += 1
        if total < 1:
            break
    break
print(f'''Total de {c50} cédulas de R$50
Total de {c20} cédulas de R$20
Total de {c10} cédulas de R$10
Total de {c1} cédulas de R$1''')
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
