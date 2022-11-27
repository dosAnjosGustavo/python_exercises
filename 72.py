numeros = ('zero', 'um', 'dois', 'trÊs', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
user = int(input('Digite um número entre 0 e 20: '))
while True:
    if user >= 0 and user <= 20:
        print(f'Você digitou o número {numeros[user]}.')
        break
    else:
        user = int(input('Tente novamente. Digite um número entre 0 e 20: '))
