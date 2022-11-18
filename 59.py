from time import sleep
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite mais um valor: '))
opção = 0
while opção != 5:
    print('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
    ''')
    opção = int(input('DIGITE UMA OPÇÃO: '))
    if opção == 1:
        sleep(0.3)
        print(f'A soma entre {n1} + {n2} é {n1+n2}.')
    elif opção == 2:
        sleep(0.3)
        print(f'O produto entre {n1} x {n2} é {n1*n2}.')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        sleep(0.3)
        print(f'Entre {n1} e {n2}, o maior é {maior}.')
    elif opção == 4:
        sleep(0.3)
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite mais um valor: '))
    elif opção == 5:
        sleep(0.3)
        print('Saindo do programa.')
    else:
        sleep(0.3)
        print('Opção inválida.')
    print('=-='*10)
