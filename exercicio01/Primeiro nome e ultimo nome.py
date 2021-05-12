n = str(input('Digite seu nome completo: ')).strip()
print('muito prazer em te conhecer !')
d = n.split()
print('Seu primeiro nome é {}.'.format(d[0]))
print('Seu sobre nome é {}.'.format(d[1]))
print('Seu último nome é {}.'.format(d[len(d)-1]))
#pode ser colocado apenas '.format(d-1). O len, aqui irá contar a lista toda, de 0
# até o fim da lista, o menos um (-1) é subitração da listar por 1 então
# uma lista com 4 itens  colocando -1 iria mostrar o (3) terceiro item que é o ultimo
# A função len() conta o tamanho a string ou o tamanho da lista, é o caso desse exercício,
# portanto a função len() retorna um valor inteiro, que corresponde ao tamanho total. Sabemos
# que nas listas as variáveis ficam guardadas nos índices.
# Ex: lista = ['Maria', 'Aparecida', 'da', 'Silva']
# lista[0] = 'Maria'
# lista[1] = 'Aparecida'
# lista[2] = 'da'
# lista[3] = 'Silva'
# len(lista) = 4
# O primeiro elemento da lista é lista[0] = 'Maria'
# O último elemento da lista é lista[len(lista) - 1] , traduzindo esse linha:
# O último elemento da lista é lista[4-1], logo:
# lista[3] = 'Silva'
#Fica mais prático utilizar um índice negativo, mas o professor, por motivo
# didático, preferiu utilizar a função len().
