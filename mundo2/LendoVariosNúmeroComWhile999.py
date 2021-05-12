contador = total = 0
while True:
    n = int(input('Digite o número[999 para parar]:'))
    if n == 999:
        break
    total = total + n
    contador += 1
print(f'A soma dos {contador} número total dá {total}')
#print(f'A quantidade de vezes de números digitados {contador}')