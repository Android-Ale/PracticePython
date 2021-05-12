pessoas = {'nome': 'Arthur', 'sexo': 'm', 'idade': 26}
print(pessoas)
print(f'O {pessoas["nome"]} tem {pessoas["idade"]}')
print(pessoas.keys())
print(pessoas.items())
print(pessoas.values())
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k in pessoas.items():
    print(k)
for k, v in pessoas.items():
    print(f'{k} = {v}')
'del pessoas["sexo"]'
print(pessoas['sexo'])
pessoas['sexo'] = 'M'
print(pessoas['sexo'])
#Adicionar um elemento:
pessoas['peso'] = 70
for k, v in pessoas.items():
    print(f'{k} = {v}')
