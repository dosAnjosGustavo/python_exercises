print('Vamos analisar se sua frase é um palíndromo.')
'''f = (input('Digite uma frase: ')).strip().upper()
p = f.split()
j = ''.join(p)
i = ''
for p in range(len(f)-1, -1, -1):
    i += j[p]
print(f'O inverso de {j} é {i}.')
if i == j:
    print('Sua frase é um palíndromo.')
else:
    print('Sua frase não é um palíndromo.')'''

frase = input('Qual a frase? ').upper().replace(' ', '')
if frase == frase[::-1]:
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo.')
