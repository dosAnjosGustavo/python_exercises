print('Digite dois valores para compararmos qual é maior.')
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
if n1 > n2:
    print(f'O primeiro valor é maior.')
elif n1 < n2:
    print(f'O segundo valor é maior.')
else:
    print(f'Os dois valores são iguais.')
