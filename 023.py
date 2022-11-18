numero = int(input('Informe um número: '))
u = numero//1 % 10
d = numero//10 % 10
c = numero//100 % 10
m = numero//1000 % 10
print(f'Analisando o número {numero}.')
print(f'A unidade é {u}.')
print(f'A dezena é {d}.')
print(f'A centena é {c}.')
print(f'O milhar é {m}.')
