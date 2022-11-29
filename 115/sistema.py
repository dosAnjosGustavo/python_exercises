from lib.interface import *
from lib.interface.arquivo import *
from time import sleep

arq = 'pessoas.txt'

if arqExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado.')

while True:
    resposta = menu(
        ['Ver pessoa cadastrada', 'Cadastrar nova pessoa', 'Sair do sistema'])
    sleep(0.3)
    if resposta == 1:
        cabeçalho('Opção 1')
    elif resposta == 2:
        cabeçalho('Opção 2')
    elif resposta == 3:
        cabeçalho('Você saiu do sistema.')
        break
    else:
        print('\033[31mDigite uma opção válida!\033[m')
    sleep(0.3)
