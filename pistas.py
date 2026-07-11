import abc

"""Classe abstrata com método abstrato acelerar, serve como uma base para todas as classes de pistas que existem no projeto.
Contém o método abstrato dificuldade, onde cada pista implementa uma dificuldade diferente que o carro terá que sofrer."""
class Pista(abc.ABC):
    def __init__(self, nome, comprimento):
        self.nome = nome
        self.__comprimento = comprimento

    def get_comprimento(self):
        return self.__comprimento
    
    @abc.abstractmethod
    def dificuldade(self, carro):
        pass

"""Classe da pista interlagos, diminui um pouco do combustível de cada carro, e diminui a distância que os carros andarão a cada volta."""
class Interlagos(Pista):
    def __init__(self):
        super().__init__("Interlagos", 4309)

    def dificuldade(self, carro):
        consumo = carro.get_combustivel() * 0.15
        carro.set_combustivel(carro.get_combustivel() - consumo)

        carro.dificuldade_pista = 0.95

"""Classe da pista Mônaco, diminui a distância que os carros andarão a cada volta e desgasta os pneus."""
class Monaco(Pista):
    def __init__(self):
        super().__init__("Mônaco", 3337)

    def dificuldade(self, carro):
        carro.dificuldade_pista = 0.90

        for pneu in carro.pneus:
            pneu.desgastar(3)

"""Classe da pista Silverstone, diminui um pouco do combustível de cada carro e desgasta os pneus."""
class Silverstone(Pista):
    def __init__(self):
        super().__init__("Silverstone", 5891)

    def dificuldade(self, carro):
        consumo = carro.get_combustivel() * 0.18
        carro.set_combustivel(carro.get_combustivel() - consumo)

        for pneu in carro.pneus:
            pneu.desgastar(6)


