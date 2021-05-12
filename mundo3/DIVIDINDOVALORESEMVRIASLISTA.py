lista = []
pares = []
impares = []
zero = []
while True:
    lista.append(int(input('Digite o valor: ')))
    while True:
        resposta = str(input('Deseja continuar [N/S]: '))
        if resposta in 'ns':
            break
    if resposta == 'n':
        break
for contador, núm in enumerate(lista):
    if núm == 0:
        zero.append(núm)
    if núm % 2 == 0 and núm != 0:
        pares.append(núm)
    else:
        if núm % 2 == 1 and núm != 0:
            impares.append(núm)
print('=-='*10)
print(f'A lista completa é {lista}')
print(f'A lista de números Pares: {pares}')
print(f'A lista de número Impares: {impares}')
print(f'A lista de números neutros {zero}')