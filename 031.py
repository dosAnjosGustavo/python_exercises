d = float(input('Qual a distância da sua viagem em km? '))
if d <= 200:
    p = d*0.50
else:
    p = d*0.45
print(f'Sua viagem vai custar R${p:.2f}.')
