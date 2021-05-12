#O APLICATIVO CADASTRA MORADORES DE RUA EM RECIFE
#DEPOIS DISSO AS PESSOAS QUE DESEJAR AJUDAR PODEM DEPOSITAR UMA QUANTIA
#PARA ALMOÇO, ETC
print('Ajuda Recife')
print('Como você deseja ajudar ?')
print('[1]Alimento (almoço/Janta)')
print('[2]Cesta Basicas')
print('[3]roupas')
print('[4]Dinheiro')
print('[5]Outros')
escolha = int(input('Escolha:'))
if escolha == 1:
    lista = (['1°Feijão', '2°Arroz'])
    escolha2 = int(input(f'Escolha uma das opções: {lista}'))
    if escolha2 == 1:
        print(lista[0])
    if escolha2 == 2:
        print(lista[1])
if escolha == 2:
    print('Qual valor da cesta básica ?')
    lista = (['R$120', 'R$150', 'R$200', 'R$250', 'R$300'])
    escolha2 = int(input(f'Escolha uma das opções: {lista}'))
    if escolha2 == 1:
        print(lista[0])
    if escolha2 == 2:
        print(lista[1])
    if escolha2 == 3:
        print(lista[2])
    if escolha2 == 4:
        print(lista[3])
    if escolha2 == 5:
        print(lista[4])
    if escolha2 == 6:
        print(lista[5])
    print('Pagamento pelo cartão: [1]')
    print('Pagamento pelo page.me: [2]')
    pagamento = int(input('Pagamento:'))
    if pagamento == 1:
        print('Informe o número do cartão:')
    if pagamento == 2:
        print('Link do page.me: XxXxXxX.page.me.com.br')