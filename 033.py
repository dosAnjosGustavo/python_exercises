print('Vamos descobrir qual número é o maior e qual é o menor dentre três números.')
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o último número: '))
me = a
if b < a and b < c:
    me = b
if c < a and c < b:
    me = c
ma = a
if b > a and b > c:
    ma = b
if c > a and c > b:
    ma = c
print(f'O menor número é {me}, é o maior é {ma}.')
