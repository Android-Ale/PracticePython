print('='*20)
print('BANCO RNA')
print('='*20)
contador1 = contador2 = contador3 = contador4 = dinheiro1 = diferença = 0
dinheiro = int(input('Que valor você quer sacar? R$'))
while dinheiro >= 50:
    dinheiro -= 50
    contador1 += 1
    '''print(dinheiro)'''
if dinheiro >= 20:
    while dinheiro >= 20:
        dinheiro -= 20
        contador2 += 1
if dinheiro >= 10:
    while dinheiro >= 10:
        dinheiro -= 10
        contador3 += 1
if dinheiro >= 1:
    while dinheiro >= 1:
        dinheiro -= 1
        contador4 += 1

        '''print(dinheiro)
        print(f'contador2 {contador2}')'''
if contador1 >= 1:
    print(f'Total de {contador1} cédulas de R$50')
if contador2 >= 1:
    print(f'Total de {contador2} cédulas de R$20')
if contador3 >= 1:
    print(f'Total de {contador3} cédulas de R$10')
if contador4 >= 1:
    print(f'Total de {contador4} cédulas de R$1')
print('Volte sempre ao BANCO RNA ! Tenha um bom dia !')