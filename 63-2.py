print('Sequência de Fibonacci')
n = int(input('Digite a quantidade de elementos: '))
t1 = 0
t2 = 1
c = 1
while c <= n:
    print(f'{t1} -> ', end='')
    c += 1
    t1 += t2
    if c <= n:
        print(f'{t2} -> ', end='')
        c += 1
        t2 += t1
print('Fim.')
