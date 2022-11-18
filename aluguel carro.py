d = float(input('Quantos dias o carro ficou com você? '))
km = float(input('Quantos km você rodou? '))
print(
    f'Considerando que o aluguel custa R$ 60/dia e R$0,15 por km rodado, o preço a pagar é R${(d*60+km*0.65):.2f}.')
