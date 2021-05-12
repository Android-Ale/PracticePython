acomulando = adicionado = 0
for c in range(1, 7):
    n = int(input('Digite o número: ').format(c))
    if n % 2 == 0:
        acomulando = acomulando + 1
        adicionado = adicionado + n
if acomulando == 1:
    print('A apenas {} número par que é {}.'.format(acomulando, adicionado))
else:
    print('A soma dos {} números pares são {}.'.format(acomulando, adicionado))