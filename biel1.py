print('Digite números inteiros para somá-los. Se quiser parar, digite 999.')
maior = media = cont = 0
while True:
    try:
        numero = int(input('Digite: '))
        break
    except ValueError:
        print('Digite um número inteiro.')
while numero != 999:
    try:
        cont += 1
        if cont == 1:
            menor = maior = numero
        else:
            if numero < menor:
                menor = numero
            elif numero > maior:
                maior = numero
        media = (maior+menor)/2
        numero = int(input('Digite: '))
    except ValueError:
        print('Digite um número inteiro.')

print(
    f'Dentre os números inseridos, o maior foi {maior} e o menor foi {menor}. A média entre eles é {media}.')
