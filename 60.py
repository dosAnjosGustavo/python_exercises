print('Digite um número inteiro para calcular seu fatorial.')
n = int(input('Digite um número: '))
print(f'Calculando {n}! = ', end='')
c = n
f = 1
'''while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1'''
for g in range(c, 0, -1):
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')
