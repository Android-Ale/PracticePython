print('\033[1;7;35;40m#'*5+'\033[1;7;35;40mConfederaçao Nacional De Nataçao'+'\033[1;7;35;40m#'*5)
a = int(input('Digite o ano do seu nascimento: '))
m = 2019 - a
print(m)
if m <= 9:
    print('O atleta tem {} anos e sua categoria é mirim.'.format(m))
elif m <= 14:
    print('O atleta tem {} anos e sua categoria é infantil.'.format(m))
elif m <= 19:
    print('O atleta tem {} anos e sua categoria é junior.'.format(m))
elif m <=20:
    print('O atleta tem {} anos e sua categoria é sênior.'.format(m))
else:
    print('O atleta tem {} anos e sua categoria é mestre.'.format(m))