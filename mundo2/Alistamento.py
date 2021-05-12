n = int((input('Digite o ano do seu nascimento: ')))
m = 2019 - n
print(m)
if m < 18:
    print('Você ainda irá se alistar no serviço militar.')
    print('Falta {} para você alistar-se.'.format(18 - m))
elif m == 18:
    print('Você está na hora de alistar-se no serviço militar.')
else:
    print('Você passou do tempo de alistar-se no serviço militar.')
    print('já passou {} do seu alistamento.'.format(m - 18))
