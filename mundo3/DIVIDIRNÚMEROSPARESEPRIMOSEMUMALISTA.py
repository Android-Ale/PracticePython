número = []
pares = []
ímpares = []
for c in range(0, 7):
    número.append(int(input('Digite o valor: ')))
for n in número:
    if n % 2 == 0:
        pares.append(n)
    else:
        ímpares.append(n)
pares.sort()
ímpares.sort()
print('=-='*10)
print(f'números pares : {pares}')
print(f'números ímpares: {ímpares}')