print('Vamos descobrir se seu número inteiro é primo.')
m = 0
n = int(input('Digite: '))
for c in range(2, n):
    if n % c == 0:
        print(f'Múltiplo de {c}.')
        m += 1
if m == 0:
    print('É primo.')
else:
    print(f'Tem {m} múltiplos acima de 2 e abaixo de {n}.')
