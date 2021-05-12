c = 0
v = 0
while c != 5:
    n1 = float(input('Digite o número:'))
    n2 = float(input(('Digite outro número:')))
    print('''
    [1] somar
    [2] multiplicação
    [3] maior
    [4] novos números
    [5] finalizar.''')
    v = int(input('Escolha os números:'))
    if v == 5:
        c = v
        print('Fim.')
    if v == 1:
        print('A soma de {} e {} é : {}'.format(int(n1), int(n2), n1 + n2))
    if v == 2:
        m = n1*n2
        print('A multiplicação de ambos os números são: {}.'.format(m))
    if v == 3:
        if n1 > n2:
            m = n1
            print('O maior número é {}, e o menor é {}.'.format(m, n2))
        else:
            m = n2
            print('O maior número é {}, e menor número é {}.'.format(m, n1))
    if v == 4:
        print('Digite outros valores.')

