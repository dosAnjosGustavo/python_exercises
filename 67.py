print('-'*30)
n = int(input('Quer ver a tabuada de qual valor? '))
print('-'*20)
c = 0
while c <= 10:
    print(f'{n}x{c}={n*c}.')
    c += 1
    if c > 10:
        c = 0
        print('-'*20)
        n = int(input('Quer ver a tabuada de qual valor? '))
        print('-'*20)
    if n < 0:
        break
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
