p = float(input('Largura da parede:'))
a = float(input('Altura da parede:'))
a1 = p*a
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m²'.format(p, a, a1))
print('Para pintar essa parede, você precisará de {}l de tinta'.format(a1/2))