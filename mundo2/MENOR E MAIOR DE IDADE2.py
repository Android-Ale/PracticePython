from datetime import date
atual = date.today().year
contadormaior = 0
contadormenor = 0
for pessoas in range(1, 8):
    nascimento = int(input('Em que ano a pessoa nasceu ?'))
    idade = atual - nascimento
    if idade >= 21:
        contadormaior += 1
    else:
        contadormenor += 1
if contadormaior > 1:
    print('Existem {} pessoas maiores de idades'.format(contadormaior))
if contadormaior <= 1:
    print('Existe {} pessoa maior de idade'.format(contadormaior))
if contadormenor > 1:
    print('Existem {} pessoas menores de idades'.format(contadormenor))
if contadormenor <= 1:
    print('Existe {} pessoa  menor de idade'.format(contadormenor))



'''m = 0
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
print('E existem {} pessoas menor de idade'.format(contam))'''''