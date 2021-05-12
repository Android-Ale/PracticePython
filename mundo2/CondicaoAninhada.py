nome = (str(input('Qual seu nome ?')))
if nome == 'Arthur':
    print('tenha um bom dia, {}.'.format(nome))
elif nome == 'pedro' or nome == 'maria' or nome == 'joão' or nome == 'josé' or nome == 'paulo':
    print('Nome bem comum, {}.'.format(nome))
elif nome in 'Ana cláudia' or 'vitória' or 'natalia':
    print('belo nome feminino, {}.'.format(nome))
else:
    print('Nome bem normal, {}.'.format(nome))
