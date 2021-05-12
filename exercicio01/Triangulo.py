print('Digite uma medida para as retas')
reta1 = float(input('Reta 1:'))
reta2 = float(input('Reta 2:'))
reta3 = float(input('Reta3'))
if (reta1 + reta2) > reta3 and (reta3 + reta2) > reta1 and (reta3 + reta1) > reta2:
    print('Dá para fazer um triangulo.')
else:
    print('Não dá para fazer um triangulo.')