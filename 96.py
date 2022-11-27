def área(L, C):
    a = L * C
    print(f'A área de um terreno {L}m x {C}m é de {a}m².')


print('Controle de Terrenos'.center(30))
print('-'*30)
a = float(input('LARGURA (m): '))
b = float(input('COMPRIMENTO (m): '))
área(a, b)
