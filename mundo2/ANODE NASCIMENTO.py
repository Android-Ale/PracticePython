print('ANO DE NASCIMENTO')
m = 0
for c in range(1, 8):
    n = int(input('Digite o ano de nascimento da {}° pessoa:'.format(c)))
    m = 2019 - n
    if m < 21:
        print('A {}° pessoa tem menos de 21 anos, então não é adulto.'.format(c))
    else:
        print('A {}° pessoa tem mais de 21 anos, então é adulta.'.format(c))

