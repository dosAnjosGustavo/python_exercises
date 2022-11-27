estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'A chave {k} tem valor {v}.')
