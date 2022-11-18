print('Vamos calcular sua média de duas notas.')
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1+n2)/2
if m < 5:
    print(f'Média {m:.2f}: REPROVADO.')
elif m >= 7:
    print(f'Média {m:.2f}: APROVADO.')
else:
    print(f'Média {m:.2f}: RECUPERAÇÃO.')
