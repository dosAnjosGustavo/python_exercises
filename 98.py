from time import sleep
from copy import deepcopy


def lin():
    print('-='*30)


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    i = deepcopy(inicio)
    f = deepcopy(fim)
    p = deepcopy(passo)
    if p < 0:
        p = -p
    print(
        f'Contagem de {i} até {f} de {p} em {p}')
    if fim < inicio:
        fim -= 1
        if passo > 0:
            passo = -passo
    if fim > inicio:
        fim += 1
        if passo < 0:
            passo = -passo
    for c in range(inicio, fim, passo):
        print(f'{c} -> ', end='')
        sleep(0.3)
    print('Fim.')


lin()
sleep(0.3)
contador(1, 10, 1)
sleep(0.3)
lin()
sleep(0.3)
contador(10, 0, 2)
sleep(0.3)
lin()
sleep(0.3)
print('Agora é a sua vez de personalizar a contagem!')
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
contador(a, b, c)
sleep(0.3)
