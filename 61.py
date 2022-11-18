print('Vamos verificar os 10 primeiros termos de uma progressão aritmética.')
pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
print('Os 10 primeiros termos são:')
termo = pt
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += r
    cont += 1
print('Fim.')
