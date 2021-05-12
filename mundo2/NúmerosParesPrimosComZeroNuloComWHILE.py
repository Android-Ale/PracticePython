n = 1
par = impar = 0
while n != 0:
    n = (int(input('Digite o número')))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
if par > 1:
    print('A quantidade de números pares são {}'.format(par))
if par <= 1:
    print('A quantidade de número par é {}'.format(par))
if impar > 1:
    print('A quantidade de números ímpares são {}'.format(impar))
if impar <= 1:
    print('A quantidade de número ímpar é {}'.format(impar))