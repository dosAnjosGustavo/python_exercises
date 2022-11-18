s = 0
g = 0
print('Segue abaixo a soma entre todos os números ímpares que são múltiplos de três e que se encontrem entre o intervalo de 1 até 500.')
for c in range(1, 500+1):
    if c % 3 == 0 and c % 2 != 0:
        g += 1  # = g = g + 1
        s += c  # = s = s + c
print(f'A soma dos {g} valores entre eles é: {s}')
