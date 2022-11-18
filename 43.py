print('''Informe seu peso e altura.
Utilize ponto (.) ao invés de vírgula (,) para informar os centímetros e as gramas.''')
p = float(input('Peso (em kg): '))
a = float(input('Altura (em metros): '))
c = p/a**2
if c < 18.5:
    print('Abaixo do peso.')
elif c >= 18.5 and c < 25:
    print('Peso ideal.')
elif c >= 25 and c < 30:
    print('Sobrepeso.')
elif c >= 30 and c < 40:
    print('Obesidade.')
elif c > 40:
    print('Obesidade mórbida.')
