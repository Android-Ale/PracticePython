número = []
#maiorlista = menorlista = []
for contador in range(0, 5):
    número.append(int(input('Digite o valor ')))
    if contador == 0:
        maior = menor = número[contador]
    else:
        if número[contador] > maior:
            maior = número[contador]
        if número[contador] < menor:
            menor = número[contador]
print('=-='*20)
print(f'Você digitou os valores {número}')
print(f'O maior valor é {maior} nas posições', end=' ')
for posição, valor in enumerate(número):
    if valor == maior:
        print(f'{posição + 1}', end=', ')
print()
print(f'O menor valor é {menor} nas posições', end=' ')
for posição, valor in enumerate(número):
    if valor == menor:
        print(f'{posição + 1}', end=', ')
print()
print('=-='*20)


#print(f'O maior número é {max(número)} e sua posição é {número.index(max(número))+1}')
#print(f'O menor número é {min(número)} e sua posição é {número.index(min(número))+1}')