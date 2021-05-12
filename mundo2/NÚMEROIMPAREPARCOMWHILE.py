c = 's'
par = impar = 0
while c == 's':
    n = (int(input('Digite um número:')))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
    c = input('Deseja continuar ?').lower()
if par > 1:
    print('Existem {} números pares.'.format(par))
elif par <= 1:
    print('Existe {} número par.'.format(par))
if impar > 1:
    print('Existem {} números impares.'.format(impar))
elif impar <= 1:
    print('Existe {} número impar.'.format(impar))

print('Fim')
