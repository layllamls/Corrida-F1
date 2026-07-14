import abc
import random

"""Define um pneu de um veículo, controlando o desgaste e quando trocá-lo ao decorrer da corrida."""
class Pneu:
    def __init__(self):
        self.desgaste = 0
    
    def desgastar(self, quantidade):
        self.desgaste += quantidade
        if self.desgaste > 100:
            self.desgaste = 100
    
    def trocar(self):
        self.desgaste = 0

"""Classe abstrata que representa um veículo participante da corrida.
Define os atributos e comportamentos comuns a todos os carros, obrigando
as subclasses a implementarem o método acelerar()."""
class Veiculo(abc.ABC):
    def __init__(self, modelo, velocidade_max, combustivel_max, combustivel_atual):
        self.modelo = modelo
        self.__velocidade_max = velocidade_max
        self.__combustivel_max = combustivel_max
        self.__combustivel_atual = combustivel_atual

        self.distancia = 0
        self.pneus = [Pneu() for i in range(4)]
        self.tempo_box = 0
        self.dificuldade_pista = 1
    
    def get_velocidade_max(self):
        return self.__velocidade_max
    
    def get_combustivel(self):
        return self.__combustivel_atual
    
    def set_combustivel(self, valor):
        self.__combustivel_atual = valor
    
    def get_combustivel_max(self):
        return self.__combustivel_max
    
    def precisa_pitstop(self):
        desgaste_pneus = any(pneu.desgaste >= 70 for pneu in self.pneus)
        pouco_combustivel = self.get_combustivel() <= 15
        return desgaste_pneus or pouco_combustivel
    
    def desgaste_medio(self):
        total = 0
        for pneu in self.pneus:
            total += pneu.desgaste
        return total / 4

    @abc.abstractmethod
    def acelerar(self):
        pass

"""Todas as classes que herdam de Veiculo contém suas próprias características particulares, de modo que cada uma se comportará de
uma maneira diferente, mesmo tendo o mesmo método acelerar(). Pois algumas consomem mais combustível, outras desgastam mais os pneus, etc."""
class Ferrari(Veiculo):
    def __init__(self):
        super().__init__("Ferrari", 340, 90, 90)
    
    def acelerar(self):
        if self.get_combustivel() <= 0:
            return f"{self.modelo} ficou sem combustível!"
        
        velocidade = random.randint(self.get_velocidade_max() - 40, self.get_velocidade_max())
        self.distancia += velocidade * self.dificuldade_pista
        consumo = velocidade * 0.05
        novo_combustivel = self.get_combustivel() - consumo
        self.set_combustivel(max(0, novo_combustivel))

        if velocidade >= 250:
            desgaste = 7

        elif velocidade >= 200:
            desgaste = 3.5

        else:
            desgaste = 1

        for pneu in self.pneus:
            pneu.desgastar(desgaste)

        return f"{self.modelo} acelerando a {velocidade} km/h (Distância: {self.distancia:.0f})"
    
class Mercedes(Veiculo):
    def __init__(self):
        super().__init__("Mercedes", 352, 80, 80)
    
    def acelerar(self):
        if self.get_combustivel() <= 0:
            return f"{self.modelo} ficou sem combustível!"
        
        velocidade = random.randint(self.get_velocidade_max() - 50, self.get_velocidade_max())
        self.distancia += velocidade * self.dificuldade_pista
        consumo = velocidade * 0.03
        novo_combustivel = self.get_combustivel() - consumo
        self.set_combustivel(max(0, novo_combustivel))

        if velocidade >= 250:
            desgaste = 4

        elif velocidade >= 200:
            desgaste = 2

        else:
            desgaste = 1

        for pneu in self.pneus:
            pneu.desgastar(desgaste)

        return f"{self.modelo} acelerando a {velocidade} km/h (Distância: {self.distancia:.0f})"
    

class McLaren(Veiculo):
    def __init__(self):
        super().__init__("McLaren", 400, 85, 85)
    
    def acelerar(self):
        if self.get_combustivel() <= 0:
            return f"{self.modelo} ficou sem combustível!"
        
        velocidade = random.randint(self.get_velocidade_max() - 45, self.get_velocidade_max())
        self.distancia += velocidade * self.dificuldade_pista
        consumo = velocidade * 0.04
        novo_combustivel = self.get_combustivel() - consumo
        self.set_combustivel(max(0, novo_combustivel))

        if velocidade >= 250:
            desgaste = 6

        elif velocidade >= 200:
            desgaste = 3

        else:
            desgaste = 1

        for pneu in self.pneus:
            pneu.desgastar(desgaste)

        return f"{self.modelo} acelerando a {velocidade} km/h (Distância: {self.distancia:.0f})"
    
    
class CarrosBots(Veiculo):
    def __init__(self, modelo):
        super().__init__(modelo, 340, 80, 80)
    
    def acelerar(self):
        if self.get_combustivel() <= 0:
            return f"{self.modelo} ficou sem combustível!"
        
        velocidade = random.randint(self.get_velocidade_max() - 40, self.get_velocidade_max())
        self.distancia += velocidade * self.dificuldade_pista
        consumo = velocidade * 0.02
        novo_combustivel = self.get_combustivel() - consumo
        self.set_combustivel(max(0, novo_combustivel))

        if velocidade >= 250:
            desgaste = 5

        elif velocidade >= 200:
            desgaste = 2.5

        else:
            desgaste = 1

        for pneu in self.pneus:
            pneu.desgastar(desgaste)

        return f"{self.modelo} acelerando a {velocidade} km/h (Distância: {self.distancia:.0f})"
