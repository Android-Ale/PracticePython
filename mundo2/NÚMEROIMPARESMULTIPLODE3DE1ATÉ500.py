#print('NÚMERO IMPARES, MULTIPLO DE 3 DE 1 ATÉ 500')
#for c in range(3,500,6):
#    print(c)
print('NÚMERO IMPARES, MULTIPLO DE 3 DE 1 ATÉ 500')
acumulando = 0
contador = 0
for c in range(1,501,2):
    if c % 3 == 0:
        acumulando = acumulando + c
        contador = contador + 1
print('A soma de {} valores solicitado é {}.'.format(contador, acumulando))
