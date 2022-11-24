lista = []
while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1+nota2)/2
    lista.append([nome, [nota1, nota2], media])
    cont = ' '
    while cont not in "SN":
        cont = input('Quer continuar? [S/N] ').upper()[0]
    if cont == 'N':
        break
print('-='*20)
print(f"{'No.':<4}{'NOME':<10}{'MÉDIA':>8}")
print('-'*25)
for p, e in enumerate(lista):
    print(
        f"{p:<4}{e[0]:<10}{e[2]:>8.1f}")
print('-'*25)
while True:
    a = int(input('Mostrar notas de qual aluno? (999 interrompe: '))
    if a == 999:
        break
    print(f' Notas de {lista[a][0]} são {lista[0][1]}.')
print('<'*3, 'VOLTE SEMPRE', '>'*3)
