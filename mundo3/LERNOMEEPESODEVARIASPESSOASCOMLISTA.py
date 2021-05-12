dado = []
pessoas = []
conte = total = 0
while True:
    dado.append(str(input('Digite o nome: ')))
    dado.append(int(input('Digite a peso:')))
    pessoas.append(dado[:])
    dado.clear()
    while True:
        resp = str(input('Deseja continuar ? [N/S] ')).strip().lower()
        if resp in 'ns':
            break
    if resp == 'n':
        break
for p in pessoas:
    conte += 1
    total += p[1]
    print(p[0], p[1])
m = total/ conte
print(f'Aqui mostra o total de {conte} pessoas cadastradas.')
print(f'A média do peso {m:.2f}')
print('As pessos mais pesadas:')
for p in pessoas:
    if p[1] > m:
        print(p[0], p[1])
        #pessoasgordas.append(p[0])
        #pessoasgordas.append(p[1])
print('As pessoas mais leves:')
for p in pessoas:
    if p[1] <= m:
        print(p[0],p[1])
        #pessoasmagras.append(p[0])
        #pessoasmagras.append(p[1])
#print('lista das pessoas magras:')
#print(pessoasmagras)
#print('=-='*10)
#print('lista das pessoas gordas')
#print(pessoasgordas)