lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[1:])
print(lanche[:2])
print(lanche[-2])
print(lanche[1:3])

for cont in lanche:
    print(f'Eu vou comer {cont}.')
print('')
# =
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}.')
print('')
# --
for cont in range(0, len(lanche)):
    print(f'{cont}º, vou comer {lanche[cont]}.')
print('')
# =
for pos, comida in enumerate(lanche):
    print(f'{pos}º, vou comer {comida}.')
# --
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b  # != b + a
print(sorted(c))  # len(c), c.count(5), c.index(8)
# --
# del (tupla)  # = apagar uma tupla; não é possível apagar itens dentro da tupla, somente a tupla inteira.
