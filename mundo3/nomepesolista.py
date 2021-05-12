pessoas = list()
grupo = list()
tot = maior = menor = 0
nome = nome1 = b = ''
while True:
    if b == 'n':
        break
    pessoas.append(str(input('Digite seu nome:')))
    pessoas.append(int(input('Digite sua seu peso:')))
    grupo.append(pessoas[:])
    pessoas.clear()
    tot =+ 1
    while True:
        r = str(input('Deseja continuar ?')).lower().strip()
        if r == 'n':
            b = 'n'
        if r in 'ns':
            break

for p in grupo:
    if p[1] >= maior:
        maior = p[1]
        nome1 = p[0]
    else:
        menor = p[1]
        nome = p[0]
print(f'Maior peso {maior}kg de {nome1}')
print(f'menor peso {menor}kg de {nome}')
