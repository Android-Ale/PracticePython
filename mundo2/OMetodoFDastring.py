j = 'João'
v = 'Vitória'
idade = 33
i = 'john'
n = 987.3
print(f'{i:^20} ESPAÇO')   #DÁ PARA ALIAR(CENTRALIZAR)
print(f'{i:-^20} ESPAÇO')  #DÁ PARA COMPLEMENTAR
print(f'{i:->20} ESPAÇO')   #DÁ PARA ALIAR À DIREITA
print(f'{i:-<20} ESPAÇO')   #DÁ PARA ALIAR À ESQUERDA
print(f'{i:20} ESPAÇO')   #DÁ PARA MODIFICAR O ESPAÇO
print(f'{i} tem {idade} anos e recebi R${n:.2f} de salário.') #DÁ PARA USAR PONTO FLUTUANTE
print(f'Olá, {j} e {v}')                    # (PYTHON - 3.6+ )
print(f'Ambos, {j} e {v} tem {idade} anos.')

#COM O METODO DE F COM STRING, NÃO PRECISA USAR O FORMAT, DIMINUINDO MAIS AS LINHAS DO ALGARITIMO


print('Ambos, {} e {} tem {} anos'.format(j, v, idade))   #( PYTHON - 3)


'''print('Ola, %s e %d' % (j, v))''' #AQUI É A FORMA MAIS ANTIGA... (PYTHON - 2)