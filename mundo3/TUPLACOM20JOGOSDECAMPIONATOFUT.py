time = ('corinthians', 'palmeiras', 'santos', 'gremio',
        'cruzeiro', 'flamengo', 'vasco', 'chapeconhece',
        'atlético', 'botafogo', 'atletico-PR', 'bahia',
        'são paulo', 'fluminense', 'esporte recife',
        'ec vitória', 'coritiba', 'avaí', 'ponte preta',
        'atletico-GO')
#for lista in time:
#    print('>',lista)
print('=-'*20)
print(f'Listas de times: {time}')
print('=-'*20)
print(f'Os cincos primeiros são {time[0:6]}')
print('=-'*20)
print(f'Os quatros últimos colocados {time[-4:]}')
print('=-'*20)
print(f'Times em ordem Alfabetica: {sorted(time)}')
print('=-'*20)
print('A posição do {} é {}°.'.format(time[7], time.index('chapeconhece')+1))
