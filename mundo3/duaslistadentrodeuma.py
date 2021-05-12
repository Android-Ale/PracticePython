valor = list()
impar = list()
par = list()
n = 1
numero = 0
while n < 8:
    valor.append(int(input(f'Digite o {n}° valor ')))
    n += 1
for c in valor:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print(f'Número impar: {impar}')
print(f'Número par{par}')