lista = []
fim = ''
while True:
    if fim == 'n':
        break
    while True:
        número = (input('Digite o valor: '))
        if número not in lista:
            lista.append(número)
            print('Valor adcionado !')
            break
        else:
            print('O valor já existe, tente outro !')
    while True:
            resposta = str(input('Deseja continuar ? [S/N]')).lower().strip()
            if resposta == 'n':
                fim = 'n'
            if resposta in 'ns':
                break
print(f'Resultados adcionados são: {lista}')
lista.sort()
print(f'Em ordem crescente a lista fica: {lista}')
'''lista.append(int(input('Digite o valor: ')))
    print('Valor adcionado com sucesso')
        for contador, valor in enumerate(lista):
                print(f'O número {lista[contador]} já foi colocado, tente outro')'''
print('Fim do programa')
'''if fim == 'n':
        break
    contador += 1
    lista.append(int(input('Digite o valor: ')))
    if lista[]
    while True:
        resposta = str(input('Deseja continuar ? [S/N]')).lower().strip()
        if resposta == 'n':
            fim = 'n'
        if resposta in 'ns':
            break'''