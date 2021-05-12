print('PRODUTO (NRA)')
tot = 0
pagamento = 0
while True:
    print('Escolha o que você deseja ?')
    print('='*20)
    print('Refrigerantes [3]')
    print('Alimentos salgados [2]')
    print('Alimentos doces (sorvetes) [1]')
    valor = int(input('Digite o número:'))
    if valor == 1:
        while True:
            print('=' * 8 + 'Doces sorvetes' + '=' * 8)
            print('preço do alimento doce e sorvete:')
            print('[1]sorvete x R$8')
            print('[2]sorvete y R$7')
            print('[3]sorvete z R$6')
            print('[4]sorvete w R$10')
            print('[5]sorvete h R$12')
            resposta1 = int(input('Escolha: '))
            if resposta1 == 1:
                t = 8
                tot += t
                print(tot)
                print('Deseja pagar em cartão ou a dinheiro ?')
                escolha = str(input('Digite C para cartão ou D para dinheiro:')).lower()
                if escolha == 'c':
                    print('Digite o número do cartão:')
                    print(f'Valor [R${tot},00')
                if escolha == 'd':
                    print('Pagamento no caixa')
                    pagamento += tot
                    print(f'valor total a pagar: R${pagamento}')
            if resposta1 == 2:
                t = 7
                tot += t
                print('Deseja pagar em cartão ou a dinheiro ?')
                escolha = str(input('Digite C para cartão ou D para dinheiro:')).lower()
                if escolha == 'c':
                    print('Digite o número do cartão:')
                    print(f'Valor [R${tot}00]')
                if escolha == 'd':
                    print('Pagamento no caixa')
                    pagamento += tot
                    print(f'valor total a pagar: R${pagamento}')
            if resposta1 == 3:
                print('Deseja pagar em cartão ou a dinheiro ?')
                escolha = str(input('Digite C para cartão ou D para dinheiro:')).lower()
                if escolha == 'c':
                    print('Digite o número do cartão:')
                    print(f'Valor [R${tot},00]')
                if escolha == 'd':
                    print('Pagamento no caixa')
                    pagamento += tot
                    print(f'valor total a pagar: R${pagamento}')
            if resposta1 == 4:
                print('Deseja pagar em cartão ou a dinheiro ?')
                escolha = str(input('Digite C para cartão ou D para dinheiro:')).lower()
                if escolha == 'c':
                    print('Digite o número do cartão:')
                    print('Valor [R$10,00]')
                if escolha == 'd':
                    print('Pagamento no caixa')
                    pagamento += tot
                    print(f'valor total a pagar: R${pagamento}')
            if resposta1 == 5:
                print('Deseja pagar em cartão ou a dinheiro ?')
                escolha = str(input('Digite C para cartão ou D para dinheiro:')).lower()
                if escolha == 'c':
                    print('Digite o número do cartão:')
                    print('Valor [R$12,00]')
                if escolha == 'd':
                    print('Pagamento no caixa')
                    pagamento += 12.00
                    print(f'valor total a pagar: R${pagamento}')
            resposta = str(input('Deseja continuar ? N/S')).lower()
            if resposta == 'n':
                break
            print('Escolha qual opção:')
    if valor == 3:
        while True:
            print('=' * 8 + 'Refrigerantes' + '=' * 8)
            print('Preço do Refrigerante:')
            print('[1]Coca Cola R$:8,00')
            print('[2]Guaraná Antartica R$:6,00')
            print('[3]Pepsi R$:7,00')
            escolha1 = int(input('Escolha: '))
            if escolha1 == 1:
                print('Deseja pagar em cartão ou a dinheiro ?')
                escolha = str(input('Digite C para cartão ou D para dinheiro:')).lower()
                if escolha == 'c':
                    print('Digite o número do cartão:')
                    print('Valor [R$8,00')
                if escolha == 'd':
                    print('Pagamento no caixa')
                    pagamento += 8.00
                    print(f'valor total a pagar: R${pagamento}')
            if escolha1 == 2:
                print('Deseja pagar em cartão ou a dinheiro ?')
                escolha = str(input('Digite C para cartão ou D para dinheiro:')).lower()
                if escolha == 'c':
                    print('Digite o número do cartão:')
                    print('Valor [R$6,00')
                if escolha == 'd':
                    print('Pagamento no caixa')
                    pagamento += 6.00
                    print(f'valor total a pagar: R${pagamento}')
            if escolha1 == 3:
                print('Deseja pagar em cartão ou a dinheiro ?')
                escolha = str(input('Digite C para cartão ou D para dinheiro:')).lower()
                if escolha == 'c':
                    print('Digite o número do cartão:')
                    print('Valor [R$7,00')
                if escolha == 'd':
                    print('Pagamento no caixa')
                    pagamento += 7.00
                    print(f'valor total a pagar: R${pagamento}')
            resposta = str(input('Deseja continuar ? N/S')).lower()
            if resposta == 'n':
                break
        print('Escolha qual opção:')
    if valor == 2:
        while True:
            print('=' * 8 + 'Alimentos salgados' + '=' * 8)
            print('Preço do Alimento salgado:')
            print('[1]Coxinha R$:2,00')
            print('[2]Pastel de Frango ou Carne R$:3,00')
            print('[3]Enrroladinho R$:2,00')
            escolha1 = int(input('Escolha: '))
            if escolha1 == 1:
                print('Deseja pagar em cartão ou a dinheiro ?')
                escolha = str(input('Digite C para cartão ou D para dinheiro:')).lower()
                if escolha == 'c':
                    print('Digite o número do cartão:')
                    print('Valor [R$:2,00')
                if escolha == 'd':
                    print('Pagamento no caixa')
                    pagamento += 2.00
                    print(f'valor total a pagar: R${pagamento}')
            if escolha1 == 2:
                print('Deseja pagar em cartão ou a dinheiro ?')
                escolha = str(input('Digite C para cartão ou D para dinheiro:')).lower()
                if escolha == 'c':
                    print('Digite o número do cartão:')
                    print('Valor [R$:3,00')
                if escolha == 'd':
                    print('Pagamento no caixa')
                    pagamento += 3.00
                    print(f'valor total a pagar: R${pagamento}')
            if escolha1 == 3:
                print('Deseja pagar em cartão ou a dinheiro ?')
                escolha = str(input('Digite C para cartão ou D para dinheiro:')).lower()
                if escolha == 'c':
                    print('Digite o número do cartão:')
                    print('Valor [R$:2,00')
                if escolha == 'd':
                    pagamento += 2.00
                    print('Pagamento no caixa')
                    print(f'valor total a pagar: R${pagamento}')
            resposta = str(input('Deseja continuar ? N/S')).lower()
            if resposta == 'n':
                break
        print('Escolha qual opção:')
    print('=' * 20)
    print('Pagamento No Caixa:')
    print(f'Valor Total A Pagar :R$?{pagamento:.2f}')
print('Pagamento No Caixa:')
print(f'Valor Total A Pagar : {pagamento}')
