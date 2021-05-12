n = int(input('digite: '))
print('Digite 1 para converter em binário.')
print('Digite 2 para converter em octal')
print('Digite 3 para converter em hexadécimal')
m = int(input('Digite 1, 2 ou 3: '))
if m == 1:
    print('O número {} em binário é {}.'.format(n, bin(n)))
elif m == 2:
    print('O número {} em octal é {}.'.format(n, oct(n)))
elif m == 3:
    print('O número {} em hexadecimal é {}.'.format(n, hex(n)))
else:
    print('Digite um valor válido.')
#print('número: {}.'.format(oct(n)))