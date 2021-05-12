#modos de cores no python
#CÓDIGO ANSI
#o cóigo ANSI começa com 'contra barra' e depois vem o código que é '033'
#então sempre que vc quiser representr uma cor em python vc começa com '\033[style text backgroud m
#então ficaria assim: \033[0;33;44m
#os códigos do style existem 0, 1 , 4, 7
#0 é o código normal do terminal, o 1 é o código em negrito, o 4 é sublinhado, o 7 é negativo.

#a cor do texto também tem opções de cores que vão do trinta até o trinta e sete
#30 é branco, 31 é vermelho, 32 é verde, 33 é amarelo, 34 é azul escuro, 35 é roxo, 36 é azul claro,
#37 é cinza.

#já o backgroud exitem também as opções das cores de fundo que vão de 40 até 47
#40 é branco, 41 é vermelho, 42 é verde, 43 é amarelo, 44 é azul escuro, 45 é roxo, 46 é azul claro,
#47 é cinza.

#  \033[7;33 Esse código inverte a cor branca do texto para preta, assim o texto fica com a cor preta
#O sete inverte...


#print('\033[0;31;47mArthur')
#print('\033[1;7;30mArthur')
#print('\033[7;33;44mArthur')
#n = 3
#v = 2
#print('\033[1;40mA numeralidade encontra-se em \033[1;31;40m{}\033[1;40m e \033[m\033[1;35;40m{}\033[m'.format(n, v))
#nome = 'Arthur'

#print('Prazer em te conhecer, {}{}!!!'.format('\033[1;31;40m', nome))
#print('Prazer em te conhecer, {}{}{}!!!'.format('\033[1;31;40m', nome, '\033[m'))

nome = 'Arthur'
cores = {'limpa': '\033[m',
         'Azul': '\033[34m,',
         'Amarelo': '\033[33m',
         'pretoebranco': '\033[m0;30'}
print('Prazer em te conhecer, {}{}{}!!!'.format(cores['Amarelo'], nome, cores['limpa']))

