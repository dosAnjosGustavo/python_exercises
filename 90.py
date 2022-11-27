aluno = {}
aluno['nome'] = input('Nome: ')
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'recuperação'
else:
    aluno['situacao'] = 'reprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
