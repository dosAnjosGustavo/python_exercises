from random import randint
from time import sleep
c = randint(0, 10)
x = 1
n = int(input('Já pensei em um número entre 0 e 10! Tente adivinhar: '))
print('Processando...')
sleep(0.3)
while n != c:
    n = int(input('Errou! Tente novamente: '))
    x += 1
    print('Processando...')
    sleep(0.3)
if x == 1:
    print('Parabéns, você acertou de primeira!')
else:
    print(f'Parabéns! Você venceu, mas precisou utilizar {x} palpites.')
