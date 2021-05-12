from math import hypot
print('==TRIÂNGULO==')
co = float(input('Digite o número do cateto oposto:'))
ca = float(input('Digite o número do cateto adjacente:'))
#h = co * 2 + ca * 2
#.format(h/2)
print('O comprimento da hipotenusa do triângulo é: {}'.format(hypot(co, ca)))
print('==TRIÂNGULO==')
