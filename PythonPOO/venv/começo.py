print('conversor do tempo')
print('-'*30)

r = 'yap'

while r == 'yap':

    print(f'escolha:')
    print(f'converter horas para minutos ou segundos, digite 1')
    print(f'converter minutos para horas ou seguntos, digite 2')
    print(f'converter segundos para minutos ou horas, digite 3')

    ex = float(input('Digite uma das três opções:...'))
    if ex == 2:
        print(f'Deseja converter para horas ou segundo ?'
              f' Digite 1 para horas ou 2 para segundo.')
        ex1 = float(input('Escolha uma das duas opções:..'))
        if ex1 == 1:
            print('conversor para segundos')
            print('--------------------------')
            n = float(input('Digite a quantidade em minutos:...'))

            convs = n * 60

            print(f'Quantidade em segundos são: {convs}')

        else:
            if ex1 == 2:
                print('conversor para segundos')
                print('--------------------------')
                n = float(input('Digite a quantidade em minutos:...'))

                convs = n * 60

                print(f'Quantidade em segundos são: {convs}')

    if ex == 1:
        print(f'Deseja converter para minutos ou segundo ?'
              f' Digite 1 para minutos ou 2 para segundo.')
        ex1 = float(input('Escolha uma das duas opções:..'))
        if ex1 == 1:
            print('conversor para minutos')
            print('--------------------------')
            n = float(input('Digite a quantidade em minutos:...'))

            convs = n * 60

            print(f'Quantidade em segundos são: {convs}')

        else:
            if ex1 == 2:
                print('conversor para segundos')
                print('--------------------------')
                n = float(input('Digite a quantidade em minutos:...'))

                convs = n * 60

                print(f'Quantidade em segundos são: {convs}')

    if ex == 3:
        print(f'Deseja converter para horas ou minutos ?'
              f' Digite 1 para horas ou 2 para minutos.')
        ex1 = float(input('Escolha uma das duas opções:..'))
        if ex1 == 1:
            print('conversor para horas')
            print('--------------------------')
            n = float(input('Digite a quantidade em minutos:...'))

            convs = n * 60

            print(f'Quantidade em segundos são: {convs}')

        else:
            if ex1 == 2:
                print('conversor para minutos')
                print('--------------------------')
                n = float(input('Digite a quantidade em minutos:...'))

                convs = n * 60

                print(f'Quantidade em segundos são: {convs}')
    print('yap para continuar ou no para finalizar:')
    r = str(input('Deseja continuar... ?').lower())
    if r == 'no':
        print('Fim...')
        ex1 -= ex1
    else:
        ex1 -= ex1
        while r != 'no':
            print(r)
            print('Não entendi, tente novamente:')
            print('yap para continuar ou no para finalizar:')
            r = str(input('Deseja continuar... ?').lower())
            if r in 'no':
                print('Fim...')
                ex1 -= ex1
                r == 'yap'
            while r != 'yap':
                 print(r)
                 print('Não entendi, tente novamente:')
                 print('yap para continuar ou no para finalizar:')
                 r = str(input('Deseja continuar... ?').lower())

