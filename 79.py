lista = []
while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
    while True:
        try:
            c = input('Quer continuar? [S/N] ').upper()
            if c in 'SN':
                break
        except:
            print('Responda com S ou N.')
    if c == 'N':
        break
lista.sort()
print(f'Você digitou os valores {lista}')
