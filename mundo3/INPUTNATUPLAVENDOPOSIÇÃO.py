a = (int(input('Digite um número: ')),
     int(input('Digite outro número:')),
     int(input('DIgite mais um número: ')),
     int(input('Digite o último número: ')))
print(f'Você digitou os valores {a}')
print(f'O valor 9 apareceu {a.count(9)} vezes.')
if 3 in a:
    print(f'O valor 3 aparece na posição {a.index(3)+1}°')
else:
    print('O valor 3 não foi digitado.')
print('Os valores pares digitados foram  ', end='')
for número in a:
    if número % 2 == 0:
        print(número, end=',')