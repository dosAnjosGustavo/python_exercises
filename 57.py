s = input('Digite o sexo de uma pessoa [M/F]: ').strip().upper()[0]
while s not in 'MF':
    s = input('Digite M (masculino) ou F (feminino): ')
if s in 'M':
    s = 'Masculino'
elif s in 'F':
    s = 'Feminino'
print(f'O sexo digitado foi {s}.')
