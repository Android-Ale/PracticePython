n = int(input('Digite um número: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Milhar: {}'.format(m))
print('Centena: {}'.format(c))
print('Dezena: {}'.format(d))
print('Unidade: {}'.format(u))
#print('Milhar', n[0])
#rint('Centena:', n[1])
#print('Dezena', n[2])
#print('Unidade', n[3])

