'''contador = máximo = n = 0
while n != 999:
    n = int(input('Digite um número:'))
    print('Digite 999, para encerrar:')
    contador += 1
    máximo += n
print('O número de vezes de números digitados : {}'.format(contador - 1))
print('om exceção do 999.')
print('As somas dos números clolacados, com excessão do 999 é {}'.format(máximo - 999))'''


contador = máximo = n = 0
n = int(input('Digite um número:'))
while n != 999:
    print('Digite 999, para encerrar:')
    contador += 1
    máximo += n
    n = int(input('Digite um número:'))
#colocando aqui a última vez não irá ser contada
print('A quantidade de números digitados : {}'.format(contador))
#sem precisar de colocar -1
print('Com exceção do 999.')
print('As somas dos números colacados, com excessão do 999 é {}'.format(máximo))
#sem precisar de colocar -999