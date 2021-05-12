print('['*5+'Calculo IMC'+']'*5)
p = float(input('Digite o seu peso: '))
a = float(input('Digite sua altura: '))
imc = p / (a*a)
print('Seu IMC é de {:.2f}.'.format(imc))
if imc < 18.5:
     print('Magreza.')
elif imc >= 18.5:
    print('Peso Ideal.')
elif imc > 24.69:
     print('Acima do peso.')
elif imc > 30:
     print('Obesidade.')
elif imc > 39.9:
    print('Obesidade grave.')
