ano = int(input('Digite um ano: '))

print(f'O ano {ano} é bissexto.' if ((ano % 4) == 0 and (ano % 100) != 0 or (ano % 400) == 0)
      else f'O ano {ano} não é bissexto.')
