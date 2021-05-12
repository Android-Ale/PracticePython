print('-'*20)
print('LOJA BARATÃO')
print('-'*20)
fim = 'a'
totalpreço = contadorpreço = menor = contador = 0
menorproduto = ''
while True:
    produto = str(input('Nome do produto:'))
    preço = float(input('Preço: R$'))
    totalpreço += preço
    contador += 1
    if preço > 1000:
        contadorpreço += 1
    if contador == 1:
        menor = preço
    else:
        if preço < menor:
            menor = preço
            menorproduto = produto
    '''print(totalpreço)'''
    while True:
        escolha = str(input('Quer continuar ? [S/N]')).lower()
        if escolha == 'n':
            fim = escolha
        if escolha in 'sn':
            break
    if fim == 'n':
        break
print('-'*10,'FIM DO PROGRAMA','-'*10)
print(f'O total da compra foi R${totalpreço:.2f}')
print(f'Temos {contadorpreço} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {menorproduto} que custa R${menor:.2f} ')