print('Digite números inteiros para somá-los. Se quiser parar, digite [999].')
n = 0
g = 0
c = 0
n = int(input('Digite: '))
while n != 999:
    g += n
    c += 1
    n = int(input('Digite: '))
print(f'A soma dos {c} números é {g}.')
