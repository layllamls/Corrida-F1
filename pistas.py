import abc

"""Representa a pista, os objetos dessa classe que definem quanto os carros vão ter que andar
até chegarem ao final da corrida, o comprimento da pista que define a chegada dos veículos."""
class Pista(abc.ABC):
    def __init__(self, nome, comprimento):
        self.nome = nome
        self.__comprimento = comprimento

    def get_comprimento(self):
        return self.__comprimento
    
    @abc.abstractmethod
    def dificuldade(self, carro):
        pass

class Interlagos(Pista):
    def __init__(self):
        super().__init__("Interlagos", 4309)

    def dificuldade(self, carro):
        consumo = carro.get_combustivel() * 0.15
        carro.set_combustivel(carro.get_combustivel() - consumo)

        carro.dificuldade_pista = 0.95

class Monaco(Pista):
    def __init__(self):
        super().__init__("Mônaco", 3337)

    def dificuldade(self, carro):
        carro.dificuldade_pista = 0.90

        for pneu in carro.pneus:
            desgaste = pneu.desgaste * 0.19
            pneu.desgastar(desgaste)

class Silverstone(Pista):
    def __init__(self):
        super().__init__("Silverstone", 5891)

    def dificuldade(self, carro):
        consumo = carro.get_combustivel() * 0.18
        carro.set_combustivel(carro.get_combustivel() - consumo)

        for pneu in carro.pneus:
            desgaste = pneu.desgaste * 0.18
            pneu.desgastar(desgaste)


