def aumentar(p, n, form=False):
    aumentado = (p/100)*(100+n)
    if form:
        return moeda(aumentado)
    else:
        return aumentado


def diminuir(p, n, form=False):
    diminuido = (p/100)*(100-n)
    if form:
        return moeda(diminuido)
    else:
        return diminuido


def dobro(n, form=False):
    if form:
        return moeda(n*2)
    else:
        return n*2


def metade(n, form=False):
    if form:
        return moeda(n/2)
    else:
        return n/2


def moeda(n, form=False):
    g = f'{n:.2f}'
    return f"R${str(g).replace('.', ',')}"


def resumo(p, a, d):
    from moeda import dobro, metade, aumentar, diminuir
    import dado
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'{"Preço analisado:":<5}', f'{moeda(p):>10}')
    print(f'{"Dobro do preço:":<5}', f'{dobro(p, True):>10}')
    print(f'{"Metade do preço:":<5}', f'{metade(p, True):>10}')
    print(f'{"80% de aumento:":<5}', f'{aumentar(p, a, True):>10}')
    print(f'{"35% de redução:":<5}', f'{diminuir(p, d, True):>10}')
    print('-'*30)
