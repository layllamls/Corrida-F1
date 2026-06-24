import abc
import random

class Veiculo(abc.ABC):
    def __init__(self, marca, ano, modelo, velocidade_max):
        self.__marca = marca
        self.__ano = ano
        self.modelo = modelo
        self.__velocidade_max = velocidade_max

    def get_velocidade_max(self):
        return self.__velocidade_max
        
    def acelerar(self):
        pass

"""CLASSES JOGO DE CORRIDA
- Carro
- Piloto
- Equipe
- Pista
- Corrida
"""
class Piloto:
    def __init__(self, nome, habilidade):
        self.nome = nome
        self.__habilidade = habilidade
        self.__vitorias = 0

    def get_habilidade(self):
        return self.__habilidade
    
    def get_vitorias(self):
        return self.__vitorias
    
    def adicionar_bonus(self):
        nova_habilidade = self.get_habilidade() + 5
        self.__habilidade = nova_habilidade
        return f"{self.nome} agora possui habilidade igual a: {nova_habilidade}"

    def adicionar_vitoria(self):
        self.__vitorias += 1 

class Carro(Veiculo):
    def __init__(self, marca, ano, modelo, velociade_max, piloto):
        super().__init__(marca, ano, modelo, velociade_max)
        self.piloto = piloto
        self.distancia = 0

    def acelerar(self):
        velocidade = random.randint(self.get_velocidade_max() - 40, self.get_velocidade_max())
        self.distancia += velocidade
        return f"{self.modelo} acelerando a {velocidade} km/h (Distancia: {self.distancia})"
    

