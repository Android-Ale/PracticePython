import random
import time
contador = n = 0
print('-'*25)
nome = 'MEGA'
print(f'^@{nome:^20}@^')
print('-'*25)
aposta = []
aposta1 = int(input('Quantos jogos você quer que eu sorteie ?'))
print('=-='*3, f'{aposta1} JOGOS ESTÃO SENDO SORTEADOS', '=-='*3)
while contador != aposta1:
    while n != 6:
        número = random.randint(1, 60)
        if número not in aposta:
            aposta.append(número)
            n += 1
    contador += 1
    aposta.sort()
    time.sleep(1)
    print(f'jogo {contador}: {aposta}')
    n = 0
    aposta.clear()