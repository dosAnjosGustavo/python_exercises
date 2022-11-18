print(f'''{'-=-'*19
}
Vamos analisar se três números podem formar um triangulo.
{'-=-'*19
}''')
a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
c = float(input('Digite o terceiro número: '))
if a < b+c and b < a+c and c < a+b:
    print(f"Os números informados podem formar um triângulo.")
else:
    print(f"Os números informados não podem formar um triângulo.")
if a == b == c:
    print('Seu triângulo é equilátero.')
if a != b != c:
    print('Seu triângulo é escaleno.')
if a == b or a == c or b == c:
    print('Seu triângulo é isósceles.')
