n1 = (float(input('Digite um número: ')))
n2 = (float(input('Digite outro número: ')))
if n1 > n2:
    print ('O valor {} é maior que o valor {}.'.format(n1, n2))
elif n2 > n1:
    print ('O valor {} é maior que o valor {}.'.format(n2, n1))
else:
    print('Os valores são iguais, não existem valor maior e menor.')