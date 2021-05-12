acum =0
núm = int(input('Digite um número:'))
for c in range(1, núm + 1):
    if núm % c == 0:
        print('\033[0;31m', end='')
        acum += 1
    else:
        print('\033[32m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} é divisível {} vezes.'.format(núm, acum))
if acum == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
