lista = []
pares = []
impares = []
for c in range(0, 7):
    v = int(input(f'Digite o {c+1}º número: '))
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
pares.sort()
impares.sort()
lista.append(pares)
lista.append(impares)
print(f'''Os valores pares digitados foram: {lista[0]}.
Os valores ímpares digitados foram: {lista[1]}.''')
