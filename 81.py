lista = []
cont = 0
consta5 = ''
while True:
    try:
        n = int(input('Digite um número: '))
        lista.append(n)
        cont += 1
        c = ' '
        while c not in 'SN':
            c = input('Você quer continuar: [S/N] ').upper()[0]
        if c == 'N':
            break
    except ValueError:
        print('Digite um número inteiro.')
lista.sort(reverse=True)
if lista.count(5) != 0:
    consta5 = ''
else:
    consta5 = 'não '
print('='*30)
print(f'''Vamos aos resultados...
a)Foram digitados {cont} números;
b) A ordem decrescente dos números é: {lista}; e
c) O valor 5 {consta5}está na lista.''')
print('='*30)
