m = 0
conta = 0
contam = 0
for c in range(1, 8):
    n = int(input('Digite o ano de nascimento da {}° pessoa:'.format(c)))
    m = 2019 - n
    if m >= 21:
        conta += 1
    else:
        contam += 1
print('Existem {} pessoas maior de idade.'.format(conta))
print('E existem {} pessoas menor de idade'.format(contam))