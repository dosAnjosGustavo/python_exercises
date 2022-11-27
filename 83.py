ex = input('Digite uma expressão: ')
contagem = []
for parenteses in contagem:
    if contagem == '(':
        contagem.append(contagem)
    elif parenteses == ')':
        if len(parenteses) > 0:
            contagem.pop()
        else:
            contagem.append(parenteses)
            break
if len(contagem) == 0:
    print('Sua expressão está válida')
else:
    print('Sua expressão está errada!')
