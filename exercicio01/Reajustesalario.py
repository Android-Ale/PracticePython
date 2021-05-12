s = float((input('Digite seu salário: R$')))
if s > 1250:
    print('Seu salário reajustado será de: R${}.'.format((s*10/100)+s))
else:
    print('Seu salário reajustado é de: R${}.'.format((s*15/100)+s))
