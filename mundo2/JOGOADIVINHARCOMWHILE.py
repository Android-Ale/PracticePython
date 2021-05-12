from random import randint
computador = randint(0,10)
print('Sou o seu computador... Acabei de pensar em um número entre 0 e 10:')
print('Você consegui adivinhar ?')
acertar = False
palpite = 0
while not acertar:
    jogador = int(input('Qual o número que eu escolhi:'))
    palpite += 1
    if jogador == computador:
        acertar = True
    else:
        if computador > jogador:
            print('O número é maior, tente mais uma vez')
        elif computador > jogador:
            print('O número é menor tente mais uma vez')
print('Parabéns, você acertou !')
print('Quantidade de palpite, durante o jogo {}.'.format(palpite))
