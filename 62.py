from time import sleep
print('Vamos verificar os 10 primeiros termos de uma progressão aritmética.')
pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
print('Os 10 primeiros termos são: ', end='')
termo = pt
cont = 1
quantidade = 0
adicional = 10
while adicional != 0:
    quantidade = quantidade + adicional
    while cont <= quantidade:
        print(f'{termo} -> ', end='')
        termo += r
        cont += 1
    print('PAUSA.')
    print('Quer visualizar mais termos?')
    adicional = int(
        input('Se sim, digite a quantidade a mais. Caso não queira, digite 0: '))
print('FIM')
