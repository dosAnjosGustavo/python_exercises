def escreva(msg):
    n = len(msg)
    print('-'*(n+4))
    print(f'{msg}'.center(n+4))
    print('-'*(n+4))


escreva('Olá mundo!')
