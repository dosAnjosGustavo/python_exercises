p = float(input('Digite o preço do produto: '))
c = input('''Qual será o método de pagamento?
Digite [1] para à vista em dinheiro/cheque;
[2] para à vista no cartão;
[3] para parcelado em 2x no cartão; ou
[4] para parcelado em 3x ou mais no cartão.
Digite a opção: ''')
while '1' not in c and '2' not in c and '3' not in c and '4' not in c:
    c = input('''Método de pagamento não listado.
    Digite algo entre 1 e 4: ''')
if '1' in c:
    print(
        f'Para pagamento à vista no dinheiro/cheque, o produto tem 20% de desconto, ficando apenas R${(p/100)*80}.')
if '2' in c:
    print(
        f'Para pagamento à vista no cartão, o produto tem 5% de desconto, ficando apenas R${(p/100)*95}.')
if '3' in c:
    print(
        f'Para pagamento em 2x no cartão, o preço do produto segue inalterado: R${p}.')
if '4' in c:
    print(
        f'Para pagamento parcelado em 3x ou mais no cartão, cobramos juros de 20% por conta da maquininha, totalizando R${(p/100)*120}.')
