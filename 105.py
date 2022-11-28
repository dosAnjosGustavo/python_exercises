def notas(*n, sit=False):
    """Função para analisar notas e situções de vários alunos.
    n: uma ou mais notas dos alunos (aceita várias)
    sit: valor opcional, indicando se deve ou não adicionar a situação
    return: dicionário com várias informações sobre a situação da turma)
    """
    dicio = dict()
    dicio['total'] = (len(n))
    dicio['maior'] = max(n)
    dicio['menor'] = min(n)
    dicio['média'] = sum(n)/len(n)
    if sit:
        if dicio['média'] >= 7:
            dicio['situação'] = 'BOA'
        elif 7 > dicio['média'] > 6:
            dicio['situação'] = 'RAZOÁVEL'
        else:
            dicio['situação'] = 'RUIM'
    return dicio


resp = notas(3.5, 10, 6.5)
print(resp)
help(notas)
