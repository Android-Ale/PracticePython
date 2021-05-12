print('=-'*3+'DEZ TERMOS DE UMA PA'+'-='*3)
pa = int(input('Primeiro Termo:'))
razão = int(input('Razão:'))
contador = 9
print(pa, end=' ')
adicionador = 0
while contador != 0:
    print('->', end=' ')
    pa += razão
    print(pa, end=' ')
    contador -= 1
    adicionador += 1
    if contador == 0:
        conta = int(input('Quantos termos você quer mostrar mais ?'))
        contador = conta
print('A progreção finaliza em {} termos mostrados.'.format(adicionador + 1))
print('ACABOU.')