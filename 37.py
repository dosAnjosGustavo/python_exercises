n = int(input('Digite o número inteiro que você deseja converter: '))
b = input('''Agora, digite qual será a base de conversão:
[1] para binário
[2] para octal
[3] para hexadecimal
''')
while '1' not in b and '2' not in b and '3' not in b:
    b = input('''Opção não listada.
Digite algo entre 1 e 3: ''')
if '1' in b:
    print(f'binário de {n} é {bin(n)}.')
if '2' in b:
    print(f'octal de {n} é {oct(n)}.')
if '3' in b:
    print(f'hexadecimal de {n} é {hex(n)}.')
