nome = str(input('Digite seu nome completo: ')).strip()
print(f'Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}.')
print(f'Seu nome em minúsculas é {nome.lower()}.')
espaços = nome.count(' ')
print(f'Seu nome tem {len(nome)-espaços} letras.')
primeiro = nome.find(' ')
separado = nome.split()
print(f'Seu primeiro nome é {separado[0]} e ele tem {primeiro} letras.')
