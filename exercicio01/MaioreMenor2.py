n = (int(input('Digite um número:')))
m = (int(input('Digite outro número:')))
v = (int(input('Digite mais outro número:')))
menor = m
if n < m and n < v:
    menor = n
if v < m and v < n:
    menor = v
#verificar meior número.
maior = m
if n > m and n > v:
    maior = n
if v > m and v > n:
    maior = v
print('O número maior é {}.'.format(maior))
print('O número menor é {}.'.format(menor))
