#n = int(input('Digit your number: between 2000 and 3200'))
import time
'''for n in range(2000, 2300):
    if n % 7 == 0:
        if n % 5 == 1:
            print(f'The number {n} is divider by 7 but not divider by 5')
    else:
        print(f'The number {n} is not divider by 7')'''
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = []
lista3 = []
for n in lista1:
    if n % 2 == 0:
        lista2.append(n)
    else:
        lista3.append(n)
print(lista2)
print(lista3)