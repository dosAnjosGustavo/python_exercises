numeros = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(
    input('Digite um número: ')), int(input('Digite um número: ')))
print(f'a) O número 9 apareceu {numeros.count(9)} vez(es);')
if 3 in numeros:
    print(
        f'b) O número 3 apareceu a primeira vez na{numeros.index(3)+1}ª posição; e',)
else:
    print('b) Número 3 não foi digitado; e')
print('c) Os números pares foram: ', end='')
for c in numeros:
    if c % 2 == 0:
        print(f'{c} -> ', end='')
print('Fim.')
