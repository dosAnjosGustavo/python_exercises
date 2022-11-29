from lib.interface import *


def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except Exception as erro:
        print(f'Houve um erro na criação do arquivo: {erro.__cause__}')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except Exception as erro:
        print(f'Erro ao ler o arquivo: {erro.__cause__}')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except Exception as erro:
        print(f'Houve um erro na abertura no arquivo: {erro.__cause__}')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except Exception as erro:
            print(
                f'Houve um erro na hora de escrever os dados: {erro.__cause__}')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close
