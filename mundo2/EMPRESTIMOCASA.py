casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
ano = int(input('Quanto anos de financiamento ?'))
prestacao = casa / (salario * ano)
minimo = (salario * 30) / 100
print('par pagar uma casa de {:.2f} em {} anos'.format(casa, ano), end='')
print(' a prestação será de R$ {:2f}'.format(prestacao))
if prestacao <= minimo:
    print('emprestimo pode ser concedido.')
else:
    print('emprestimo negado.')
