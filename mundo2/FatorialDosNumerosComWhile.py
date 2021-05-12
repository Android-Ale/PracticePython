print('=-'*3+'Fatorial'+'-='*3)
n = int(input('Digite o número:'))
fatorial = n
n += 1
print('Calculando {}!'.format(fatorial), end=' ')
while n != 1:
    if n == 0:
        n = 1
        print(n - 1)
    f = (n - 1)
    print(f, end=' x ')

    fatorial *= f
    n = f
print('0 =', fatorial)


