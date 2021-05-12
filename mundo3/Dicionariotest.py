estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa:'))
    estado['sigla'] = str(input('sigla do estado:'))
    #no caso do discionario existe um metodo interno, chamado copy
    brasil.append(estado.copy())
for e in brasil:
    'print(e)'
    for v in e.values():
        print(v, end=' ')
    print()
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
print(f'Transferencia de dados {c}, retornando dados da federação {v}')
