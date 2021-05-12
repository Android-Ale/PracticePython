print("PADARIA ELIZA MARTINEZ")
print("Digite 'A' para refrigerante")
print("Digite 'B' para salgados")
b = input('O que você deseja ?')
if b == 'A' or b == 'a':
    print('Refrigerantes:')
    print('Guarana Antartica [1]')
    print('Coca Cola [2]')
    print('Fanta [3]')
    print('Dole Guarana [4]')
    print('Pepse [5]')
    print('Digite o número: ')
n = int(input())
if n == 1:
    print('Você quer Guarana Antartica ?')
    print('Digite (s) para sim ou (n) para não.')
    p = str(input()).lower()
    if p == 's':
        print('Ok')
    else:
        if p == 'n':
            print('Escolha outro')
        else:
            print('tente novamente')
if n == 2:
    print('Você quer Coca Cola ?')
    print('Digite (s) para sim ou (n) para não.')
    p = str(input()).lower()
    if p == 's':
        print('Ok')
    else:
        if p == 'n':
            print('Escolha outro')
        else:
            print('tente novamente')
if n == 3:
    print('Você quer Fanta ?')
    print('Digite (s) para sim ou (n) para não.')
    p = str(input()).lower()
    if p == 's':
        print('Ok')
    else:
        if p == 'n':
            print('Escolha outro')
        else:
            print('tente novamente')
if n == 5:
    print('Você quer Pepse ?')
    print('Digite (s) para sim ou (n) para não.')
    p = str(input()).lower()
    if p == 's':
        print('Ok')
    else:
        if p == 'n':
         print('Escolha outro')
        else:
            print('tente novamente')

