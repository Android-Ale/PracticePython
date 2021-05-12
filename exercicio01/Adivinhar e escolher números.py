import random
m = ['0', '1', '2', '3', '4', '5']
n = str(input('Qual numeração você acha ?'))
escolhido = random.choice(m)
if n == escolhido:
    print('Você acertou !')
else:
    print('Você errou !')
print('O número escolhido foi: {}'.format(escolhido))




