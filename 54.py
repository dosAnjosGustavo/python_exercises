from datetime import date
print('Informe a data de nascimento de 7 pessoas.')
m = 0
n = 0
for c in range(1, 8):
    ano = int(input(f'Ano de nascimento da {c}ª pessoa: '))
    if (date.today().year) - ano >= 18:
        m += 1
    else:
        n += 1
print(
    f'Ao final de {date.today().year}, {m} pessoas terão maioridade, enquanto {n} ainda serão menores de idade.')
