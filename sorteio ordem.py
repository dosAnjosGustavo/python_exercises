import random
a = input('Digite um nome: ')
b = input('Digite um nome: ')
c = input('Digite um nome: ')
d = input('Digite um nome: ')
deck = [a, b, c, d]
random.shuffle(deck)
print(f'A ordem de apresentação será {deck}.')
