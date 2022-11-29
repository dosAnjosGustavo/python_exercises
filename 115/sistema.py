from lib.interface import *
from lib.interface.arquivo import *
from time import sleep

arq = '115\pessoas.txt'

if not arqExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(
        ['Ver pessoa cadastrada', 'Cadastrar nova pessoa', 'Sair do sistema'])
    sleep(0.3)
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Você saiu do sistema.')
        break
    else:
        print('\033[31mDigite uma opção válida!\033[m')
    sleep(0.3)
