d = float(input('Qual o salário do funcionário ? R$'))
print('Um funcionário que ganhava R${}, com 15% de aumento, '
      'passará a receber R${:.2f}.'
      .format(d, d+(d*15/100)))