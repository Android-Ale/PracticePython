print('TABUADA COM REPETIÇÃO')
t = int(input('Qual número da tabuada vc quer ver ?:'))
for c in range(0, 11):
    print(t, 'x {:2} = {}'.format(c, c*t))
#O :2 é para almentar o espaço antes da variavel
#podesse colocar se quiser, pois é opcional

