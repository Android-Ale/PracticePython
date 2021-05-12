test = list()
test.append('Arthur')
test.append(25)
galera = list()
#para não ficar os dois como 'filo, 33', deve usar a sintaxe copia [:]
galera.append(test[:])
test[0] = 'Filo'
test[1] = '33'
galera.append(test)
'print(galera)'
#Pode ser feito uma lista pricipal, contendo variais outros listas.
pessoas = [['Arthur', 25],['Aline',30],['natalia',27],['Tifa',22]]
#procurando na lista
'print(pessoas[3][0])'
#voce pode selecionar todas as sublistas com a função for
for p in pessoas:
    'print(p)'
#você pode escolher apenas umas partes de umas sublistas númerando
    'print(p[0])'
#pode interagir
    'print(f{p[0]} tem {p[1]} de idade.)'

#As listas pode adquirir informações com input
aluno = list()
grupo = list()
totaldemenor = totaldemaior = 0
for n in range(0,2):
    aluno.append(str(input('Digite seu nome:')))
    aluno.append(int(input('Digite sua idade:')))
    grupo.append(aluno[:])
    #clear serve para apagar a outra lista que tinha, pois já fizemos a cópia da outra
    aluno.clear()
    #Se quiser mostra só as pessoas com mais de 21 anos:
for p in grupo:
    if p[1] > 21:
        print(f'{p[0]} é maior de idade')
        totaldemaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totaldemenor += 1
print(f'total de maior = {totaldemaior}')
print(f'total de menor = {totaldemenor}')