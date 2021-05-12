frase = str(input('Digite uma frase:')).strip().upper()
palavra = frase.split()
junta = ''.join(palavra)
inverso = ''
print('Frase é : {}'.format(junta))
for letra in range(len(junta) -1, -1, -1):
    inverso += junta[letra]
print(inverso)
if inverso == junta:
    print('Essa frase: ({}) é um palindromo.'.format(frase))
    print('Pois de trás para frente fica {}.'.format(inverso))
else:
    print('Essa frase ({}) não é um palindromo.'.format(frase))
    print('Pois de trás para frente fica {}.'.format(inverso))
print(palavra)
print(frase)
print(junta)
print(inverso)

print(type([]))
print(type({}))
print(type(()))
