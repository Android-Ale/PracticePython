c = 's'
contador = adição = máximo = mínino = 0
while c in 'Ss':
    n = int(input('Digite o número:'))
    contador += 1
    adição += n
    if contador == 1:
        mínino = máximo = n
    else:
        if n > máximo:
            máximo = n
        if n < mínino:
            mínino = n
    c = str(input('Deseja continuar ? S/N')).lower().strip()[0]
média = adição / contador
print('A média dos números digitados são: {:.2f}'.format(média))
print('O menor número é {} e o maior é {}'.format(mínino, máximo))