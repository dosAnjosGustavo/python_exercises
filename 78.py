maior = menor = 0
valores = []
for c in range(0, 5):
    valores.append(input(f'Digite um número para a posição {c}: '))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print(f'Você digitou {valores}.')
print(f'O maior foi {maior} e o menor foi {menor}.')
print('As posições do maior foram: ', end='')
for p, e in enumerate(valores):
    if e == maior:
        print(f'{p} -> ', end='')
print('Fim.')
print('As posições do maior foram: ', end='')
for p, e in enumerate(valores):
    if e == menor:
        print(f'{p} -> ', end='')
print('Fim.')
