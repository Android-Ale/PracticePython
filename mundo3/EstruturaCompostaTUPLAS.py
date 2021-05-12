#NO MUNDO I E II TRABALHAMOS COM VARIAVÉL SIMPLES
#NO MUNDO III TRABALHAREMOS COM VARIAVÉIS COMPOSTAS

#O FOR PODE SER UTILIZADO PARA VARIAVEIS COMPOSTAS, POR EXEMPLO:
#DIGAMOS QUE NÚMERO É UMA VARIAVEL COMPOSTA, LOGO A SINTAXE USANDO ELA NO FOR
#SERIA - for c in numero:

#AS DUPLAS SÃO IMUTAVÉIS*****

#NO PYTHON VC PODE COMEÇAR A VARIAVEL COMPOSTA COM PARENTESES COM COCHETES OU COM CHAVE
#EXEMPLO:
# TUPLA        ->      numero = (1,2,3,4)

# DICIONARIO   ->      numero = {1,2,3,4}

# LISTA        ->      numero = [1,2,3,4]


'''lanche = ('pizza', 'hamburgue', 'coxinha', 'suco')
print(lanche)'''

#pode-se escrever a dupla sem parentese, EXEMPLO:

'''lanche = 'pizza', 'hamburgue', 'coxinha', 'suco'
print(lanche)'''
#e ele ler o parentese no final (quando roda o algaritimo mesmo não tendo parentese. pois ele
#indentifica como dupla.

#PARA REFERENCIAR UMA PARTE DA VARIAVEL DEVE-SE COLOCAR OS COCHETES E NÚMERAR A PARTE QUE DESEJA
lanche = 'pizza', 'hamburgue', 'coxinha', 'suco'
'''print(lanche[1])
print(lanche[-1])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:3])
print(lanche[-2:])
print(lanche[:-3])
print(lanche)'''

#USANDO FOR PARA VARIAVEIS COMPOSTAS:

'''for c in lanche:
    print(f'Eu vou comer {lanche}')'''
#1°
for contador in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[contador]}, NA POSIÇÃO: {contador}')
    #ESSE É MOSTRA O MESMO RESULTADO DO 2°
    #O 1° É BOM PARA MOSTRAR A POSIÇÃO POIS O 2° NÃO DA PARA MOSTRAR,
#2°
for comida in lanche:
    print(f'Eu vou comer {comida}!')
print('comi para caramba!')
    #ASSIM COMO ESSE MOSTRA O MESMO RESULTADO DO 1°

#3°
for posição, comida in enumerate(lanche):
    print(f'Eu vou comer {lanche[comida]}, NA POSIÇÃO: {posição}')
print('comi par caramba !')
    #O 3° TAMBÉM PODE VER A POSIÇÃO DAS VARIAVEIS COMPOSTA, COMO O 1°
    #NA 3° NÃO PRECISA UTILIZAR O RANGE



#USANDO O METODO SORTED, PARA ORGNIZAR A VARIAVEL COMPOSTA:
print(sorted(lanche)) #COLOCOU EM ORDEM
print(lanche)


                         #OUTRO EXEMPLO DE DUPLA COM NÚMEROS:

a = (1, 2, 5, 4)
b = (5, 8, 1, 2)
c = a + b         #PODE CRIAR UMA OUTRA VARIAVEL COMPOSTA QUE JUNTA AS OUTRAS VARIAVEIS:
print(sorted(c))  #USANDO O METODO SORTED PARA ORDENAR AMBAS AS VARIAVEIS
print(len(c))     #COMO VIMOS O len CONTA QUANTOS ELEMENTOS TEM NA VARIAVEL, AQUI SÃO 8
print(c.count(1)) #AQUI ELE CONTA QUANTAS VEZES O NÚMERO 1 APARECEU NA VARIAVEL c QUE SÃO 2
print(c.index(8)) #USANDO O .index ELE MOSTRAS A POSIÇÃO DO ELEMENTO DA VARIAVEL QUE ESTA NA 5°
print(c.index(2)) #TENDO MAIS DE 1 ELEMNTO IGUAL ELE PEGA A PRIMEIRA POSIÇÃO DO ELEMENTO ESCOLHIDO
print(c.index(2, 4)) #CASO NÃO QUEIRA PEGAR A PRIMEIRA POSIÇÃO DEVE-SE NUMERAR A POSIÇÃO DO LADO
#ESQUERDO, PARA ESCOLHER QUAL DOS ELEMENTOS SERA ESCOLHIDO. ( CHAMAMOS ISSO DE DESLOCAMENTO ! ).

#AS TUPLAS ACEITAM DADOS DE TIPOS DIFERENTES, COMO NÚMEROS E PALAVRAS, EXEMPLO:
pessoa = ('Arthur', 27, 'M', 70.00)
print(pessoa)
# JÁ SABEMOS QUE AS VARIAVEIS COMPOSTAS SÃO IMUTAVEIS; PORÉM,
# PODEMOS USAR O COMANDO del PARA APAGAR A DUPLA:
del(pessoa)
print(pessoa)  #AI APARECERAR UMA MENSAGEM DIZENDO QUE A VARIAVEL NÃO FOI DEFINIDA, DANDO ERRO.