nome = (input('Digite seu nome completo:'))
print(nome)
print(nome.upper())
print(nome.lower())
dividido = nome.split()
print(dividido)
print('Seu primeiro nome tem', len(dividido[0]), 'letras.')
#a =(len(dividido[0]))
#b =(len(dividido[1]))
#c =(len(dividido[2]))
#d =(len(dividido[3]))
#m =a + b + c + d
print('Seu nome completo tem {} letras.'.format(len(nome) - nome.count(' ')))
#print(len(dividido))
#print(len(dividido))
#print(''.join(nome))