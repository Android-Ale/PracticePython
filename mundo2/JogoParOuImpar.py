print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)
contador = 0
import random
while True:
    número = int(input('Diga o valor:'))
    while True:
        escolha = str(input('Par ou Ímpar ? [P/I]:')).lower()
        if escolha in 'pi':
            break
    lista = [0,1,2,3,4,5,6,7,8,9,10]
    escolha1 = random.choice(lista)
    m = número
    adição = número + escolha1
    if adição % 2 == 0:
        print('-'*20)
        print(f'Você jogou {número} e o computador {escolha1}. Total de {adição} DEU PAR')
        print('-' * 20)
    else:
        print('-' * 20)
        print(f'Você jogou {número} e o computador {escolha1}. Total de {adição} DEU ÍMPAR')
        print('-' * 20)
    if  escolha == 'i' and adição % 2 != 0:
            contador += 1
            print('Você ACERTOU !')
            print('Vamos jogar novamente...')
            print('=-' * 20)
    else:
        if escolha == 'p' and adição % 2 == 0:
            print('Você ACERTOU !')
            print('Vamos jogar novamente...')
            print('=-' * 20)
            contador += 1
        else:
            print('Você PERDEU !')
            break
print('=-'*20)
print(f'GAME OVER ! Você venceu {contador} vezes.')