def voto(n):
    from datetime import date
    anoatual = date.today().year
    i = anoatual - n
    print(f'Com {i} anos: ', end='')
    if i < 16:
        print('NÃO VOTA.')
    elif 16 <= i < 18 or i > 70:
        print('VOTO OPCIONAL.')
    else:
        print('VOTO OBRIGATÓRIO.')


while True:
    voto(int(input('Em que ano você nasceu? ')))
    cont = ' '
    while cont not in 'SN':
        cont = input('Quer continuar? [S/N] ').upper()[0]
    if cont == 'N':
        print('FIM.')
        break
