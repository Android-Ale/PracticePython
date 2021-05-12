nome = input('Qual é seu nome ?')
print('Prazer em lhe conhecer, {}.'.format(nome))
nome = input ('Qual o seu nome ?')
print('Prazer em conhecer, {:>20}.'.format(nome))
#usando o {} d´para colocar número e simbolos dentro para modificar a posição da variável.
nome = input ('Qual o seu nome ?')
print('Prazer em conhecer, {:<20}.'.format(nome))
nome = input ('Qual o seu nome ?')
print('Prazer em conhecer, {:^20}.'.format(nome))
#outro exemplo:
nome = input ('Qual o seu nome ?')
print('Prazer em conhecer, {:=^20}.'.format(nome))