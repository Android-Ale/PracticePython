'''cont = 1
while True:
#O WHILE TRUE É UM COMANDO QUE FAZ PARA SEMPRE, O COMANDO QUE PODE PARAR ELE É O BREAK.
    print(cont,'... ',end='')
    cont += 1
print('Acabou')'''
cont = 1
while True:
    n = int(input('Digite um número:'))
    if n == 999:
        break
    cont += 1
#O COMANDO BREAK É O COMANDO QUE INTERROMPE O OUTRO COMANDO,
# ENTÃO ELE NÃO LER O ÚLTIMO NÚMERO (999), POR QUE CAI LOGO NO COMANDO BREAK.
'''print('A quantidade de números digitados foi {}'.format(cont))'''
print(f'A quantidade de números digitados foi {cont}')
#EM BAIXO FOI USADO UMA TÉCNICA DE INTERPOLAÇÃO DE STRINGS, BASTA COLOCAR UM 'F' ANTES DA STRING
#E DEPOIS, NOS COCHETES,COLOCAR A VARIÁVEL DESEJADA.
