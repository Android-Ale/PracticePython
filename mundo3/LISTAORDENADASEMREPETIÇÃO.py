'''lista = []
for contador in range(0, 5):
        lista.append(input('Digite o número:'))
        print(contador)
print(lista)
print(f'contador final: {contador}')
for contador, número in enumerate(lista):
    print(f'Na posição {contador}, temos o número {número}')'''
lista = []
for contador in range(0, 5):
    número = int(input('Digite o valor:'))
    if contador == 0 or número > lista[-1]:
        lista.append(número)
    else:
        posição = 0
        while posição < len(lista):
            if número <= lista[posição]:
                lista.insert(posição, número)
                break
            posição += 1
print('=-'*30)
print(f'Os valores digitados em ordem foram {lista}')