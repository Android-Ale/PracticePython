print('==Preço da passagem: R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais Acima.==')
d = float(input('        Digite a distância da viagem em km: '))
if d <= 200:
    print('O total a pagar:R${}'.format(d*0.50))
else:
    print('O total a pagar:R${}'.format(d*0.45))
