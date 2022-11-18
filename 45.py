from random import choice
print('O computador desafia você a jogar Jokenpô!')
jogador = input('Digite pedra, papel ou tesoura: ')
while 'pedra' not in jogador and 'papel' not in jogador and 'tesoura' not in jogador:
    jogador = input('Opção não listada. Digite pedra, papel ou tesoura: ')
game = ['pedra', 'papel', 'tesoura']
pc = str(choice(game))
if jogador == 'pedra' and pc == 'papel' or jogador == 'papel' and pc == 'tesoura' or jogador == 'tesoura' and pc == 'pedra':
    print(f'O computador jogou {pc}, você perdeu!')
elif jogador == pc:
    print(f'O computador jogou {pc}, deu empate!')
else:
    print(f'Parabéns, você ganhou! O computador jogou {pc}.')
