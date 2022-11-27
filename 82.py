lista = []
listapar = []
listaimpar = []
while True:
    try:
        n = int(input('Digite um número: '))
    except ValueError:
        print('Só funciona com número inteiro.')
    lista.append(n)
    if n % 2 == 0:
        listapar.append(n)
    elif n % 2 != 0:
        listaimpar.append(n)
    c = ' '
    while c not in 'SN':
        c = input('Quer continuar? S/N] ').upper()[0]
    if c == 'N':
        break
print(f'''a) lista inteira: {lista};
b) lista par: {listapar}; e
c) lista ímpar: {listaimpar}.''')
