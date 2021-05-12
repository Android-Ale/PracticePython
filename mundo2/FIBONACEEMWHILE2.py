print('=-'*2+'FIBONACII'+'-='*2)
n = int(input('Digite quantos termos você quer:'))
f = 0
f = 1
t1 = 0
t2 = 1
print('{},{}'.format(t1, t2), end=',')
contador = 3
while contador <= n:
    t3 = t1 + t2
    contador += 1
    print('{}'.format(t3), end=',')
    t1 = t2
    t2 = t3
print(', FIM.')