print('Vamos verificar os 10 primeiros termos de uma progressão aritmética.')
pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
print('Os 10 primeiros termos são:')
for c in range(0, 10):
    print(pt+(c*r), end='')
