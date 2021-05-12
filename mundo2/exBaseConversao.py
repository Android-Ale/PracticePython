import numbers
n = int(input('Digite um valor: '))
print('1 para binário.')
print('2 para octal')
print('3 para hexadácimal')
m = int(input('escolha os números 1,2 ou 3: '))
if m == 1:
    print('O valor de {} em Binário é :'.format(n, bin(n)))
elif m == 2:
    print('O número {} em ocatal é: {}.'.format(n, oct(n)))
elif m == 3:
    print('O valor {} em hexadessimal é: {}.'.format(n, hex(n)))
else:
    print('digite uma base de conversão valida')
