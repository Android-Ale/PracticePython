print('LER NÚMEROS INTEIROS E PARES')
n = int(input('Digite um número: '))
if n != 0:
    if n % 2 == 0:
        print('Os números paras inteiros do inicia até {} é:'.format(n))
        for c in range(0, n + 1, 2):
            print(c, end=' ')
    else:
        print('Os números impares inteiros do inicia até {} é:'.format(n))
        for d in range(1, n + 2, 2):
            print(d, end=' ')
else:
    print('Esse número {} é neutro.'.format(n))

