class NPC: #classe base, pai, superclasse.
    def __init__(self, nome, time, força, munição):
        self.nome = nome
        self.time = time
        self.força = força
        self.munição = munição
        self.Vivo=True
        self.Energia=100
    def info(self):
        print('Nome...:' + str(self.nome))
        print('Time...:' + str(self.time))
        print('Força...:' + str(self.força))
        print('Munição...:' + str(self.munição))
        print('Vivo...:' + 'sim' if str(self.vivo) else 'não')
        print('Energia...:'+ str(self.energia))
        print('---------------------------------------')

class Soldado(NPC):
    def __init__(self, nome, time):
        self.força=200
        self.munição=200
        super().__init__(nome, time,self.força, self.munição) # o metodo super ivoca o metodo ou o parametro da classe py

class Guarda(NPC):
    def __init__(self, nome, time):
        self.força=100
        self.munição=20
        super().__init__(nome, time,self.força, self.munição)

class Elite(NPC):
    def __init__(self, nome, time):
        self.força =400
        self.munição =500
        super().__init__(nome, time, self.força, self.munição)
    def inf(self):
        super().info()

s1=Guarda('Olho vivo',1)
s2=Soldado('Bala na agulha',1)
s3=Elite('Ninja',1)
s4=Guarda('Super atento',2)
s5=Soldado('Tiro certo',2)
s6=Elite('Samúrai',2)

s1.info()
s2.info()
s3.info()
s4.info()
s5.info()
s6.info()