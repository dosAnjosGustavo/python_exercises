def maior(*n):
    print('-='*30)
    print('Analisando os valores passados...')
    for c in n:
        print(c, end=' ')
    print(f'Foram informados {len(n)} valores ao todo.')
    cont = 0
    maior = 0
    for c in n:
        if cont == 0:
            maior = c
        else:
            if c > maior:
                maior = c
        cont += 1
    print(f'O maior valor informado foi {maior}.')


maior(4, 5, 8, 9, 50, 30, 81, 26)
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
