import abc
import random

class Veiculo(abc.ABC):
    def __init__(self, marca, modelo, velocidade_max):
        self.__marca = marca
        self.modelo = modelo
        self.__velocidade_max = velocidade_max

    def get_velocidade_max(self):
        return self.__velocidade_max
    
    def set_velocidade_max(self, nova_velocidade):
        self.__velocidade_max = nova_velocidade
        
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
        self.__vitorias = 0
    
    def get_vitorias(self):
        return self.__vitorias
    
    def set_vitorias(self):
        self.__vitorias += 1 

class Carro(Veiculo):
    def __init__(self, marca, modelo, velociade_max, piloto):
        super().__init__(marca, modelo, velociade_max)
        self.piloto = piloto
        self.distancia = 0

    def acelerar(self):
        velocidade = random.randint(self.get_velocidade_max() - 40, self.get_velocidade_max())
        self.distancia += velocidade
        return f"{self.modelo} acelerando a {velocidade} km/h (Distancia: {self.distancia})"
    
class Mcqueen:
    def __init__(self, velocidade_max, piloto):
        self.__velocidade_max = velocidade_max
        self.piloto = piloto
        self.distancia = 0

    def get_velocidade_max(self):
        return self.__velocidade_max
    
    def set_velocidade_max(self, nova_velocidade):
        self.__velocidade_max = nova_velocidade
    
    def acelerar(self):
        velocidade = random.randint(self.get_velocidade_max() - 40, self.get_velocidade_max())
        self.distancia += velocidade
        return f"Mcqueen acelerando a {velocidade} km/h (Distancia: {self.distancia})"
    
class Equipe:
    def __init__(self, nome):
        self.nome = nome
        self.__participantes = []

    def get_participantes(self):
        return self.__participantes
    
    def adicionar_participantes(self, participante):
        self.__participantes.append(participante)

    def listar_participantes(self):
        for participante in self.get_participantes():
            print(f"Carro: {participante.modelo} | Piloto: {participante.piloto.nome}")

class Corrida:
    def __init__(self, participantes, pista):
        self.participantes = participantes
        self.distancia_total = pista.comprimento
        self.resultado = []

    def iniciar(self):
        print("Corrida iniciada!!\n")
        while len(self.resultado) < len(self.participantes):
            for participante in self.participantes:
                if participante not in self.resultado:
                    print(participante.acelerar())
                    if participante.distancia >= self.distancia_total:
                        print(f"{participante.modelo} chegou!")
                        self.resultado.append(participante)

        print("\nCorrida finalizada!")
        

class Pista:
    def __init__(self, nome, comprimento):
        pass