def system(manual):
    return help(manual)


while True:
    print('~'*30)
    print('SISTEMA DE AJUDA PyHELP'.center(30))
    print('~'*30)
    x = input('Função ou Biblioteca > ')
    if x == 'FIM':
        print('~'*20)
        print('ATÉ LOGO!'.center(20))
        print('~'*20)
        break
    print('~'*50)
    print(f"Acessando o manual do comando '{x}'".center(50))
    print('~'*50)
    system(x)
