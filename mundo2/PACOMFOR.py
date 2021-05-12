#print('='*20)
#print('DEZ TERMOS DE UMA PA')
#print('='*20)
#pt = int(input('Primeri Termo:'))
#raz = int(input('Razão:'))
#for c in range(pt, 11):
#    print(pt+ raz + c)
print('='*20)
print('DEZ TERMOS DE UMA PA')
print('='*20)
pt = int(input('Primeri Termo:'))
raz = int(input('Razão:'))
pa = pt + (11 - 1) * raz
for c in range(pt, pa, raz):
    print('{}'.format(c), end=' -> ')
print('ACABOU')
