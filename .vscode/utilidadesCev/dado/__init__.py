def leiaDinheiro(msg):
    while True:
        x = input(msg)
        g = str(x).replace(',', '').replace('.', '').isnumeric()
        if g == True:
            i = str(x).replace(',', '.')
            return float(i)
        else:
            print(f'ERRO: "{x}" é um preço inválido!')
