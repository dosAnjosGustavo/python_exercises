from random import randint
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)
v = 0
cont = 0
while True:
    jogador = int(input('Diga um valor: '))
    pc = randint(0, 10)
    soma = jogador + pc
    conj = ' '
    while conj not in 'PI':
        conj = input('Par ou Ímpar (P/I)? ').strip().upper()[0]
    total = ''
    if (soma) % 2 == 0:
        total = 'PAR'
    else:
        total = 'ÍMPAR'
    ('-'*30)
    print(
        f'Você jogou {jogador} e o computador {pc}. Total de {soma} DEU {total}')
    ('-'*30)
    if total == 'PAR' and conj in 'P':
        cont += 1
        print('VOCÊ VENCEU!')
        print('Vamos jogar novamente...')
        print('=-'*15)
    elif total == 'ÍMPAR' and conj in 'I':
        cont += 1
        print('VOCÊ VENCEU!')
        print('Vamos jogar novamente...')
        print('=-'*15)
    else:
        print('VOCÊ PERDEU!')
        print('=-'*15)
        break
print(f'GAME OVER! Você venceu {cont} vez(es).')
