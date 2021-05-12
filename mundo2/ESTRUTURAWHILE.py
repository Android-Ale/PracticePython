'''print('estrutura de repetição controlada:', end=' ')
for c in range(1, 11):
    print(c, end=' ')
print('Fim.')'''

'''c = 1
while c < 11:
    print(c, end=' ')
    c += 1
print('Fim.')'''
# DÁ PARA FAZER COM O WHILE TUDO QUE O FOR FAZ, MAS SÓ QUANDO NÃO SABE O LIMITE SÓ DÁ
#PARA FAZER COM O WHILE.
#EXEMPLO:
'''c = 1
while c != 0:
# O '!=' SIGNIFICA DIFERENÇA.
    c = int(input('Digite um número:'.format(c)))
print('Fim.')'''

c = 'S'
while c == 'S':
    n = int(input('Digite algum valor:'))
    c = str(input('Quer continuar ? S/N:')).upper()
#poderia ser .lower se colocar os dois s lá de cima em menusculos
#assim indentifica os dois (maiusculo e menusculo)
print('Fim.')
