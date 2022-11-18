s = 0
g = 0
print('''Vamos somar somente os números pares.
Digite seis números inteiros abaixo.''')
for c in range(1, 6+1):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        g += 1
        s += n
print(f'A soma entre os {g} pares é {s}.')
