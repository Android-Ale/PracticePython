maior = 0
menor = 0
adiçãoidade = 0
maioridadehomem = 0
mulher20 = 0
for pessoa in range(1, 5):
    print('-----{}°Pessoa-----'.format(pessoa))
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo[M/F]:')).strip()
    adiçãoidade += idade
    if pessoa == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and  idade < 20:
        mulher20 += 1
mediaidade = adiçãoidade / 4
print('O nome do homem mais velho é {} e a idade de {} anos.'.format(nomemaisvelho, maioridadehomem))
print('A média de idade do grupo é {} anos.'.format(mediaidade))
print('Existem {} mulheres menos de 20 anos.'.format(mulher20))