diagr = []
total = 0
maior = []
for cont in range(0, 9):
    n = int(input('Digite o número: '))
    if n % 2 == 0:
        total += n
    diagr.append(n)
d1 = []
d1. append(diagr[0])
d2 = []
d2.append(diagr[1])
d3 = []
d3.append(diagr[2])
d4 = []
d4.append(diagr[3])
d5 = []
d5.append(diagr[4])
d6 = []
d6.append(diagr[5])
d7 = []
d7.append(diagr[6])
d8 = []
d8.append(diagr[7])
d9 = []
d9.append(diagr[8])
print(d1, d2, d3)
print(d4, d5, d6)
print(d7, d8, d9)
maior = d4[0], d5[0], d6[0]
print(f'O maior número do meio é {max(maior)}')
print(f'O adição dos números pares são {total}')
ad = d3[0] + d6[0] + d9[0]
print((f'A adiçõ dos números da terceira coluna são {ad}'))