#t = int(input('Quantos anos tem seu carro? '))
#print('carro novo.' if t <= 3 else 'carro velho.')
# print('--FIM--')
#n = input('Qual seu nome? ')
# if n.lower() == 'gustavo':
#    print('Que nome lindo você tem!')
# else:
#    print('Seu nome é tão normal!')
#print(f'Bom dia, {n}.')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print(f'A sua média foi {m}.')
if m >= 7:
    print('Parabéns, você passou!')
else:
    r = (m+6)/2
    print(
        f'Que pena! Mas não desanime, precisará tirar somente {r} na recuperação.')
