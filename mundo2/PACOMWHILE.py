print('=-'*3+'DEZ TERMOS DE UMA PA'+'-='*3)
pa = int(input('Primeiro Termo:'))
razão = int(input('Razão:'))
contador = 9
print(pa, end=' ')
while contador != 0:
    print('->',end=' ')
    pa += razão
    print(pa, end=' ')
    contador -= 1
print('ACABOU.')