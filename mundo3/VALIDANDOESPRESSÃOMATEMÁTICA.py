expr = (str(input('Digite a expressão: ')))
lista = []
for símbolo in expr:
    if símbolo == '(':            #SE 'O CARACTERES' É IGUAL A '('
        lista.append('(')             #LISTA RECEBE '(' O CARACTÉRES
    elif símbolo == ')':
        if len(lista) > 0:         #SE NÃO... SE O CARACTÉRES FOR MAIOR A ')'
            lista.pop()               #LISTA APAGA O ÚLTIMO CARACTÉRES
        else:                   #SE NÃO...
            lista.append(')')      #LISTA ADICIONA O CARACTERE ')'
            break                 #FINALIZAR...
if len(lista) == 0:                        #CASO LISTA FOR IGUAL A ZERO...
    print('Sua expreção está valendo.')
else:                                      #DO CONTRARIO...
    print('Sua expreção está errada.')