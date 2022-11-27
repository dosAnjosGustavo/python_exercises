from math import factorial


def fatorial(n, show=False):
    # -> Calcula o Fatorial de um número:
    # :param n: O número a ser calculado.
    # :param show: (opcional) Mostrar ou não a conta.
    # return: O valor do Fatorial de um número n.
    if show == True:
        for c in range(n, 0, -1):
            if c == 1:
                print(f'{c} = ', end='')
            else:
                print(f'{c} x ', end='')
    return print(factorial(n))


while True:
    n = int(input('Digite um número: '))
    calc = ' '
    while calc not in 'SN':
        calc = input('Quer ver o cálculo? [S/N] ').upper()[0]
    if calc == 'S':
        c = True
    else:
        c = False
    fatorial(n, c)
    cont = ' '
    while cont not in 'SN':
        cont = input('Quer continuar? [S/N] ').upper()[0]
    if cont == 'N':
        print('FIM.')
        break
