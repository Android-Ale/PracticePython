diagr = []
diagr1 = []
diagr2 = []
diagr3 = []
diagr4 = []
diagr5 = []
diagr6 = []
diagr7 = []
diagr8 = []
diagr9 = []
total = 0
for cont in range(0, 9):
    diagr.append(int(input('DIgite o valor')))
diagr1.append(diagr[0])
diagr2.append(diagr[1])
diagr3.append(diagr[2])
diagr4.append(diagr[3])
diagr5.append(diagr[4])
diagr6.append(diagr[5])
diagr7.append(diagr[6])
diagr8.append(diagr[7])
diagr9.append(diagr[8])
print(diagr1, diagr2, diagr3)
print(diagr4, diagr5, diagr6)
print(diagr7, diagr8, diagr9)
if diagr1[0] % 2 == 0:
    total += diagr1[0]
if diagr2[0] % 2 == 0:
    total += diagr2[0]
if diagr3[0] % 2 == 0:
    total += diagr3[0]
if diagr4[0] % 2 == 0:
    total += diagr4[0]
if diagr5[0] % 2 == 0:
    total += diagr5[0]
if diagr6[0] % 2 == 0:
    total += diagr6[0]
if diagr7[0] % 2 == 0:
    total += diagr7[0]
if diagr8[0] % 2 == 0:
    total += diagr8[0]
if diagr9[0] % 2 == 0:
    total += diagr9[0]
totalc = diagr3[0] + diagr6[0] + diagr9[0]
primeiro = diagr4[0]
segundo = diagr5[0]
terceiro = diagr6[0]
if terceiro > segundo and primeiro:
    print(f'O maior valor da linha do meio é {terceiro}')
elif primeiro > terceiro and segundo:
    print(f'O maior número da linha do meio é {primeiro}')
elif segundo > terceiro and primeiro:
    print(f'O maior número da linha do meio é {segundo}')
print(f'A soma dos valores pares são {total}')
print(f'A soma dos valores da terceira coluna são {totalc}')
'''terceitodiagrama = []
terceitodiagrama.append(diagr3[:])
terceitodiagrama.append(diagr4[:])
terceitodiagrama.append(diagr5[:])
for contador, n in enumerate(terceitodiagrama):
    if contador >= 0:
        maior = menor = n'''