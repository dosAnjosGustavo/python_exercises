soma = maisdemil = menor = cont = 0
print('-'*30)
print('LOJA SUPER BARATÃO')
print('-'*30)
while True:
    produto = input('Nome do produto: ')
    preço = float(input('Preço: R$ '))
    cont += 1
    soma += preço
    if preço >= 1000:
        maisdemil += 1
    if cont == 1:
        menor = preço
    else:
        if preço < menor:
            menor = preço
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar in 'N':
        break
print(f'''a) O total gasto foi R$ {soma:.2f};
b) {maisdemil} custam mais de R$ 1.000,00; e
c) O produto mais barato foi R$ {menor:.2f}.''')
