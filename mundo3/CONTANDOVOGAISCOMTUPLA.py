print('=-'*5+'Vogais'+'-='*5)
contador = 0
tupla = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso',
         'grátis', 'Estudar', 'Praticar', 'Trabalhar', 'Mercado',
         'Programador', 'Futuro')
for palavra in tupla:
    print(f'\nNa palavra ({palavra}) temos:', end=' ')
    for letra in palavra:
        if letra.upper() in 'AÁÃÉÊÍÓÕÔÚEIOU':
            print(f'{letra}',end=',')