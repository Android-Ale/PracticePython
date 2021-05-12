'''p = 'a'
s = 'i'
while p != 'N':
    s = str(input('Digite o sexo da pessoa:')).upper()
    if s != 'M':
        if s != 'F':
            print('Valor errado({}), digite F/M: '.format(s.upper()))
    p = str(input(('Deseja continuar ? S/N'))).upper()
    if p != 'N':
        if p != 'S':
            print('Valor errado {}.')
            p = str(input(('Deseja continuar ? S/N'))).upper()'''

sexo = str(input('Informe seu sexo: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Favor informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))
