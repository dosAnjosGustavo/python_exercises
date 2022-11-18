cidade = input('Em que cidade você nasceu? ').strip()
santo = (cidade[:5].upper() == 'SANTO')
print(f'Sua Cidade começa com "Santo"? {santo} ')
