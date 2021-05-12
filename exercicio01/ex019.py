v = float(input('Digite a velocidade do seu carro: '))
if v >80:
    print('Você foi multado.')
else:
    print('Você não foi multado.')
print('A multa cobrada é R$7,00 por cada km acima do limite')
print('Multa ao total: R${}. '.format((7*(v - 80))))
