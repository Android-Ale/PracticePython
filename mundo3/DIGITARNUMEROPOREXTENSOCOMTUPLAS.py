número = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
          'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
          'doze', 'treze', 'quatoze', 'quinze', 'dezesses', 'dezessete',
          'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número entre zero e vinte: '))
    if n < 0 or n > 20:
        while True:
            print('-Digite o número entre zero e vinte !-')
            n = int(input('Digite um número entre zero e vinte: '))
            if n > -1 and n < 21:
                print(f'O número digitado foi: {número[n]}')
                break
    else:
        print(f'O número digitado foi: {número[n]}')
    while True:
        resposta = str(input('Quer continuar ? [S/N] ')).lower().strip()
        if resposta in 'sn':
            break
    if resposta == 'n':
        break
