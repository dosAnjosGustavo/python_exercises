from random import randint
from time import sleep
c = randint(0, 5)
n = int(input('Já pensei em um número entre 0 e 5! Tente adivinhar: '))
print('Processando...')
sleep(2)
print(f'Parabéns, você venceu!' if n ==
      c else f'Você perdeu! O número era {c}.')
