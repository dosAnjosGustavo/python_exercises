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


def leiaReal(msg):
    n = 0
    while True:
        try:
            n = float(input(msg))
        except ValueError:
            print('ERRO! Digite um número real válido.')
        except KeyboardInterrupt:
            print('Usuário preferiu não digitar esse número.')
            return n
        else:
            return n  # return funciona como se fosse um break


inteiro = leiaInt('Digite um número inteiro: ')
real = leiaReal('Digite um número real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}.')
