print('''Vamos analisar a aprovação de seu empréstimo bancário.
Primeiro, informe o valor do imóvel, o salário do comprador e em quantos anos deseja pagar.''')
casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salário do comprador? R$'))
anos = float(input('Em quantos anos pretende pagar? '))
if casa/(anos*12) <= (salario/100)*30:
    print(
        f'''EMPRÉSTIMO PODE SER CONCEDIDO!
        A prestação será de R${casa/(anos*12):.2f} a serem pagas em {anos*12:.0f} parcelas.''')
else:
    print('Infelizmente você não poderá financiar essa casa.')
