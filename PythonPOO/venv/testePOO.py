class carro:
    def __init__(self, nome, placa, modelo, fabrica, ano, tamanho):
        self.nome = nome
        self.placa = placa
        self.modelo = modelo
        self.fabrica = fabrica
        self.ano = ano
        self.tamanho = tamanho

    def inf(self):
        print('Nome: ' + str(self.nome))
        print('placa: ' + (self.placa))
        print('Modelo: ' + str(self.modelo))
        print('Fabrica: ' + str(self.fabrica))
        print('Ano: ' + str(self.ano) )
        print('Tamanho' + str(self.tamanho))
        print('-----------------------------------------')

class Palho(carro):
    def __init__(self, nome, placa):
        self.modelo = "palho"
        self.ano = 2009
        self.fabrica = "volkswaguer"
        self.tamanho = "6 x 9"
        super.__init__(nome, placa, self.modelo, self.ano, self.fabrica,self.tamanho)
        super().info()

class Viena(carro):
    def __init__(self, nome, placa):
        self.modelo = 'tesla'
        self.ano = 2015
        self.fabrica = 'fiena'
        self.tamanho = '5 x 8'
        super.__init__(nome, placa, self.modelo, self.ano, self.fabrica, self.tamanho)
        super().info()

c1 = Palho('Palho', '225A')
c2 = Viena('Viena','356B')
c1.info
c2.info
    