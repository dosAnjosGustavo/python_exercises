lista = []
impar = []
par = []
while True:
    try:
        lista.append(int(input('Digite um número: ')))
    except ValueError:
        print('Digite um número inteiro.')
    cont = ' '
    while cont not in 'SN':
        cont = input('Quer continuar? [S/N] ').upper()[0]
    if cont == 'N':
        break
for c, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'''a) Lista inteira: {lista};
b) pares: {par}; e
c) ímpares: {impar}.''')
