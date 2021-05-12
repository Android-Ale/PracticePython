n = int(input('Digite um número:'))
m = int(input('Digite outro número:'))
v = int(input('Digite mais um número:'))
#verificar menor número.
if n < m and n < v:
    maior = n
if m < n and m < v:
    maior = m
if v < n and v < m:
    maior = v
#verificar maior número:
if n > m and n > v:
    menor = n
if m > n and m > v:
    menor = m
if v > n and v > m:
    menor = v
print('O número maior é {}.'.format(maior))
print('O número menor é {}.'.format(menor))



