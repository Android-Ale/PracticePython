import random
v = 0
m = 0
tentativa = 1
adivinhar = int(input('Digite um valor:'))
while v != adivinhar:
    n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lista = random.choice(n)
    v = lista
    m += 1
    if m == 1:
        print(v)
    tentativa += 1
    adivinhar = int(input('Valor errado, tente novamente:'.format()))
    print(v)
print('valor correto ! você acertou {}.!'.format(adivinhar))
print(v)
print('Você precisou de {} tentativas para acertar.'.format(tentativa))