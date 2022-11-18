print('Escolha um número para tabuar.')
n = int(input('Digite o número: '))
for c in range(0, 11):
    print(f'{n}x{c}: {n*c}.')
