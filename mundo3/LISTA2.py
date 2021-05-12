#COMO COLOCAR UMA LISTA DENTRO DA OUTRA :
lista = []
lista.append('Arthur')
lista.append(25)
print(lista)  # AQUI A VEMOS QUE A LISTA TÊM DOIS ELEMENTO
outralista = []
outralista.append(lista)  #AQUI COLOCAMOS UMA LISTRA DENTRO DA OUTRA
print(outralista)

maisoutralista = [['Arthur', 25], ['Maria', 19], ['Amanda', 27]]#PODEMOS CRIAR UMA ESTRUTURA DENTRO
print(maisoutralista)                                           # DA OUTRA


print(lista[0][0]) #ESSE COMANDO É PARA PEGAR O ELEMENTO QUE ESTÁ DENTRO DE UMA LISTA QUE ESTA DENTRO
                   #DE OUTRA, NA SINTAXE, FICARIA ASSIM: DENTRO DA LISTA ZERO EU QUERO O INTEM ZERO