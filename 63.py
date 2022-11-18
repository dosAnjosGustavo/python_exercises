print('Sequência de Fibonacci.')
n = int(input('Digite um número: '))
cont = 1
t1 = 0
t2 = 1
quantidade = n
while cont <= quantidade:
    print(f'{t1} -> ', end='')
    cont += 1
    t1 += t2
    if cont <= quantidade:
        print(f'{t2} -> ', end='')
        cont += 1
        t2 += t1
print('FIM')
