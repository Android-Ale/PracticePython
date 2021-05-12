frase = str(input('Digite uma frase:')).strip().upper()
palavra = frase.split()
junta = ''.join(palavra)
inverso = ''
print('Frase é : {}'.format(junta))
inverso += junta[::-1]  #Marcete de fatiamento do python.
print(inverso)
if inverso == junta:
    print('Essa frase: ({}) é um palindromo.'.format(frase))
    print('Pois de trás para frente fica {}.'.format(inverso))
else:
    print('Essa frase ({}) não é um palindromo.'.format(frase))
    print('Pois de trás para frente fica {}.'.format(inverso))