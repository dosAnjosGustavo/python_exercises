print('Digite valores. Se quiser parar, digite [0].')
maior = menor = soma = 0
cont = 1
n = int(input('Digite um valor: '))
maior = menor = n
continua = ''
while n != 0 and continua in 'Ss':
    soma += n
    cont += 1
    n = int(input('Digite um valor: '))
    if n > maior:
        maior = n
    if n < menor and n != 0:
        menor = n
    print(
        f'A média dos {cont} valores digitados é de {soma/cont}. O maior deles é {maior}, e o menor é {menor}.')
    continua = input('Quer continuar? Digite [S/N]: ')
print('Fim.')
