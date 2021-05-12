aluno = []
turma = []
contador = 0
while True:
    aluno.append(str(input('Nome:')))
    aluno.append((input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    while True:
        resposta = str(input('Quer continuar ? [N/S]: ')).lower().strip()
        if resposta in 'ns':
            break
    turma.append(aluno[:])
    aluno.clear()
    if resposta == 'n':
        break
print('=-='*20)
print('No     NOME           MÉDIA')
print('-'*20)
for dado in turma:
    m = (dado[1] + dado[2]) / 2
    contador += 1
    print(f'{contador} {dado}   {m:2}')
print('-'*20)