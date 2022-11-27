lista = []
for c in range(0, 3):
    n = int(input(f'Digite um valor para [0, {c}]: '))
    lista.append(n)
for d in range(0, 3):
    n = int(input(f'Digite um valor para [1, {d}]: '))
    lista.append(n)
for e in range(0, 3):
    n = int(input(f'Digite um valor para [2, {e}]: '))
    lista.append(n)
soma = 0
for p in lista:
    if p % 2 == 0:
        soma += p
soma3c = lista[2]+lista[5]+lista[8]
maior = lista[3]
if lista[4] > maior:
    maior = lista[4]
if lista[5] > maior:
    maior = lista[5]
print(f'''[ {lista[0]} ] [ {lista[1]} ] [ {lista[2]} ]
[ {lista[3]} ] [ {lista[4]} ] [ {lista[5]} ]
[ {lista[6]} ] [ {lista[7]} ] [ {lista[8]} ]''')
print(f'''A soma dos valores pares é {soma};
A soma dos valores da terceira coluna é {soma3c}; e
O maior valor da segunda linha é {maior}.''')
