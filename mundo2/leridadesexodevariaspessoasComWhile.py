contador = 0
contador1 = 0
contador2 = 0
f = 'a'
while True:
    print('-' * 20)
    print('CADASTRAR UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    while True:
        sexo = str(input('Sexo: [M/F]')).lower()
        if sexo in 'FfMm':
            break
    if idade > 18:
        contador += 1
    if sexo == 'm':
        contador1 += 1
    if sexo == 'f' and idade < 20:
        contador2 += 1
    print('-'*20)
    while True:
        r = str(input('Quer continuar ? [S/N]')).lower()
        if r == 'n':
            f = r
        if r in 'sn':
            break
    if f == 'n':
        break
print('='*20)
print('FIM DO PROGRAMA')
print('='*20)
print(f'Total de pessoas com mais de 18 anos: {contador}')
print(f'Ao todo temos {contador1} homens cadastrados.')
print(f'E temos {contador2} mulher com menos de 20 anos.')
