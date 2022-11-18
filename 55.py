print('Vamos ver quem é o mais gordão KKK baleia !')
ma = 0
me = 0
for c in range(1, 6):
    p = float(input(f'Peso da {c}ª pessoa: '))
    if c == 1:
        ma = p
        me = p
    if p > ma:
        ma = p
    elif p < me:
        me = p
print(f'Dentre os lidos, o maior  foi de {ma}kg e o menor de {me}kg.')
