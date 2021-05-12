n1 = float(input('Digite a nota do aluno: '))
n2 = float(input('Digite outra nota do aluno: '))
media = (n1 + n2) / 2
print('Média: {}.'.format(media))
if media >= 7.0:
    print('Aluno aprovado.')
elif media < 5.0:
    print('Aluno reprovado.')
elif media <= 6.9:
    print('Aluno em recuperação.')
