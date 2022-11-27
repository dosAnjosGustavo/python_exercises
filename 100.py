from random import randint


def sorteio(lista):
    print('Sorteando 5 valores da lista: ', end='')
    lista = [randint(1, 10), randint(1, 10), randint(
        1, 10), randint(1, 10), randint(1, 10)]
    for c in lista:
        print(f'{c} ', end='', flush=True)
    print('PRONTO!')


def somaPar(lista):
    pares = 0
    for c in lista:
        if c % 2 == 0:
            pares += c
    print(f'Somando os valores pares de {números}, temos {pares}.')


números = []
sorteio(números)
somaPar(números)
