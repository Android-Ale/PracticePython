n = int(input('Digite um número: '))
print('''Tabela de conversão: 
1 - Binário 
2 - Octal 
3 - Hexadecimal''')
b = int(input('Digite o número correspondente a base para a conversão: '))
if b == 1:
    print('{} em Binário é {}'.format(n, bin(n)))
elif b == 2:
    print('{} em Octal é {}'.format(n, oct(n)))
elif b == 3:
    print('{} em Hexadecimal é {}'.format(n, hex(n)))
else:
    print('Digite uma base de conversão válida!')