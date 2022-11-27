lista = list()
for cont in range(0, 5):
    lista.append(int(input('Digite um valor: ')))

'''for posição, elemento in enumerate(lista):
    print(f'Posição: {posição}, elemento: {elemento}.')
print('Fim da lista.')'''

print(enumerate(lista))
