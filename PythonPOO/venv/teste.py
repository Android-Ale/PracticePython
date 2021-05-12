class Computador:
    def __init__(self,marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram= memoria_ram
        self.placa_de_video = placa_de_video

    def ligar(self):
        print('estou ligado')

    def Desligar(self):
        print('Estou desligando')

    def Exibir_informações_desse_computador(self):
        print(self.marca, self.memoria_ram, self.placa_de_video)
computador1 = Computador('Azus', '8gb', 'Nvideo')
computador1.ligar()
computador1.Desligar()
computador1.Exibir_informações_desse_computador()
