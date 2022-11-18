frase = str(input('Digite uma frase: ')).lower().strip()
A = frase.count('a')
print(f'A letra A aparece {A} vezes na frase.')
primeiro = frase.find('a')+1
print(f'A primeira letra A apareceu na posição {primeiro}')
último = frase.rfind('a')+1
print(f'A última letra A apareceu na posição {último}')
