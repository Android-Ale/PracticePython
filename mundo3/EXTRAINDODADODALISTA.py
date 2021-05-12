número = []
contador = cinco = 0
while True:
    número.append(int(input('Digitw o número: ')))
    if número.count(5) >= 1:
        print('eu vi')
        cinco = 5
    contador += 1
    while True:
        resposta = str(input('Deseja continhuar ? [N/S]:')).lower().strip()
        if resposta in 'sn':
            break
    if resposta == 'n':
        break
print('=-='*20)
if contador == 1:
    print(f'Você digitou {contador} elemento')
    print(f'O valor é {número}')
if contador > 1:
    print(f'Você digitou {contador} elementos')
    número.sort(reverse=True)
    print(f'Os valores em ordem crescente são {número}')
if cinco == 5:
    print('O valor cinco faz parte da lista !')
else:
    print('O valor cinco não faz parte da lista !')

#PODERIA SER DESSA FORMA TB, POIS O COMANDO in TAMBÉM FAZ BUSCAS
#NOS LAÇOS, TUPLAS, LISTAS ENTRE OUTROS
if 5 in número:
    print('O valor cinco faz parte da lista !')
else:
    print('O valor cinco não faz parte da lista !')
