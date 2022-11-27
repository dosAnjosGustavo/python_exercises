galera = []
dados = []
pesopesado = []
pesoleve = []
nomepesado = []
nomeleve = []
q = 0
while True:
    dados.append(input('Digite o nome: '))
    dados.append(float(input('Digite o peso: ')))
    galera.append(dados[:])
    if q == 0:
        pesopesado.append(dados[1])
        nomepesado.append(dados[0])
        pesoleve.append(dados[1])
        nomeleve.append(dados[0])
    else:
        if dados[1] > pesopesado[0]:
            pesopesado.clear()
            nomepesado.clear()
            pesopesado.append(dados[1])
            nomepesado.append(dados[0])
        elif dados[1] == pesopesado[0]:
            nomepesado.append(dados[0])
        elif dados[1] < pesoleve[0]:
            pesopesado.clear()
            nomepesado.clear()
            pesoleve.append(dados[1])
            nomeleve.append(dados[0])
        elif dados[1] == pesoleve[0]:
            nomeleve.append(dados[0])
    q += 1
    dados.clear()
    c = ' '
    while c not in 'SN':
        c = input('Quer continuar? [S/N] ').upper()[0]
    if c == 'N':
        break
print(f'''a) Foram cadastradas {q} pessoas;
b) O maior peso foi {pesopesado[0]}kg, das pessoas: {nomepesado}; e
c) O menor peso foi {pesoleve[0]}kg, das pessoas: {nomeleve}.''')
