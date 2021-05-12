#o metodo estatico de classe também recebi um decorador --> @staticmethod
from random import randint
class Pessoa:
    ano_atual = 2020
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod  #decorador
    def por_ano_nascimento(cls, nome, ano_nascimento):
#cls poderia ser qualquer nome que vc desejaria, mas por conversão colocam como cls.
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @classmethod
    def gera_id(): #pode receber parametros como nome, idade, etc... mas aqui queremos apenas
                   #números aleatorios para a pessoa
        rand = randint(1000, 1999)
        return rand



#p1 = Pessoa.por_ano_nascimento('luiz',1988)
#p1 = Pessoa('luiz',32)
p1 = Pessoa('luiz', 32)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
print(Pessoa.gera_id())
print(rand)
print(p1.gera_id())