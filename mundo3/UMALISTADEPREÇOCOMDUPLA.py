print('-'*40)
nome = 'LISTA DE PREÇO'
print(f'{nome:^40}')
print('-'*40)
tupla = ('lápis', 1.75,
         'caderno',15.90,
         'caneta', 22.30,
         'borracha', 2,
         'compasso',9.90,
         'mochila', 120.32,
         'livro', 34.90)
for posição in range (0,len(tupla)):
    if posição % 2 == 0:
        print(f'{tupla[posição]:.<30}', end='')
    else:
        print((f'R${tupla[posição]:>7.2f}'))