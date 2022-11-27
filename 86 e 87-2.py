matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
        if c == 2:
            scol += matriz[l][c]
        if l == 1:
            if c == 0 or matriz[l][c] > mai:
                mai = matriz[l][c]
    print()
print(f'''a) A soma dos pares é {spar}.
b) A soma da terceira coluna é {scol}.
c) O maior valor da segunda linha é {mai}.''')
