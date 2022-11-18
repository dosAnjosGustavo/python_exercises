import random
a = input('Digite um nome: ')
b = input('Digite um nome: ')
c = input('Digite um nome: ')
d = input('Digite um nome: ')
deck = [a, b, c, d]
print(f'O sorteado foi: {random.choice(deck)}!')
