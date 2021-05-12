print('=-'*5+'PRODUTOS'+'-='*5)
print('''Escolha as opções de pagamento
em baixo:
* À vista (DINHEIRO/CHEQUE : 10% DESCONTO   -  DIGITE '1'

* À vista no CARTÃO : 5% DESCONTO       -      DIGITE '2'

* Em até duas vezes no CARTÃO : PREÇO NORMAL - DIGITE '3'

* 3 VEZES OU MAIS NO CARTÃO : 20% DE Juros  -  DIGITE '4'
''')
v = int(input('Digite a opção que você deseja, mencionada em cima:'))
p = float(input('Preço do produto R$: '))
if v == 1:
    print('O valor total a pagar é de R${}.'.format(p - (p*10/100)))
elif v == 2:
    print('O valor total a pagar é de R${}.'.format(p - (p*5/100)))
elif v == 3:
    print('O valor total a pagar é de R${}.'.format(p))
elif v == 4:
    print('O valor total a pagar é de R${}.'.format(p + (p * 20/100)))
