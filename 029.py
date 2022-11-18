v = float(input('Qual a velocidade do carro em km/h? '))
if v > 80:
    print('MULTADO! O limite é de 80km/h')
    print(f'Você deve pagar uma multa de R${(v-80)*7}.')
print('Tenha um bom dia! Dirija com segurança.')
