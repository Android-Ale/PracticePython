n = 1
adição = cont = 0
while True:
    print('-' * 20)
    n = int(input('Quer ver a tabuada de qual valor:'))
    print('-' * 20)
    if n < 0:
        break
    cont = adição = 0
    while cont != 10:
        adição += 1
        cont += 1
        print(f'{n} x {adição} = {n * adição}')
print('Fim.')