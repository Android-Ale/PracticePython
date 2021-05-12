class Carro:
    def __init__(self, marca, tipo, modelo):
        self.marca = marca
        self.tipo = tipo
        self.modelo = modelo

    def Parado(self):
        print('Está parado.')

    def Deslocando(self):
        print('Esta se deslocando.')

    def Informações_do_veiculo(self):
        print(self.marca, self.tipo, self.modelo)

perguntas = ['Qual a marca do carro:', 'Qual o tipo do carro:', 'Qual o modelo do carro:']
for c in perguntas:
    info = input(c)
    marca = info
    tipo = info
    modelo = info
    print(marca, tipo, modelo)
    print(info)
print(marca, tipo, modelo)
print(info)
carro1 = Carro('Volksvaguer'+',', 'Não esportivo e Esportivo'+',', 'Palho' )
carro1.Parado()
carro1.Deslocando()
carro1.Informações_do_veiculo()