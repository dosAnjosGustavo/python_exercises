def leiaInt(msg):
    n = 0
    while True:
        try:
            n = int(input(msg))
        except ValueError:
            print('ERRO! Digite um número inteiro válido.')
        except KeyboardInterrupt:
            print('Usuário preferiu não digitar esse número.')
            return n
        else:
            return n  # return funciona como se fosse um break


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc
