n = int(input('Digite um valor (999 para parar): '))
soma = n
cont = 1
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Foram digitados {cont} números e a soma entre eles é {soma}.')
