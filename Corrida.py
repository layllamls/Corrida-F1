import abc
import random

class LogMixin:
    def imprimir(self, msg):
        print(msg)

class Box(abc.ABC):
    @abc.abstractmethod
    def realizar(self, carro):
        pass

class Veiculo(abc.ABC):
    def __init__(self, modelo,piloto, velocidade_max, combustivel_max, combustivel_atual):
        self.modelo = modelo
        self.piloto = piloto
        self.__velocidade_max = velocidade_max
        self.__combustivel_max = combustivel_max
        self.__combustivel_atual = combustivel_atual
    
    def get_velocidade_max(self):
        return self.__velocidade_max
    
    def get_combustivel(self):
        return self.__combustivel_atual
    
    def set_combustivel(self, valor):
        self.__combustivel_atual = valor
    
    def get_combustivel_max(self):
        return self.__combustivel_max

    @abc.abstractmethod
    def acelerar(self):
        pass

class Piloto:
    def __init__(self, nome):
        self.nome = nome
        self.__vitorias = 0
    
    def get_vitorias(self):
        return self.__vitorias
    
    def set_vitorias(self):
        self.__vitorias += 1

class Pneu:
    def __init__(self):
        self.desgaste = 0
    
    def desgastar(self, quantidade):
        self.desgaste += quantidade
        if self.desgaste > 100:
            self.desgaste = 100
    
    def trocar(self):
        self.desgaste = 0

class Pitstop(LogMixin, Box):
    def __init__(self, bomba):
        self.bomba = bomba
    
    def realizar(self, carro):
        tempo = random.randint(5, 15)
        
        for pneu in carro.pneus:
            pneu.trocar()

        carro.tempo_box += tempo

        combustivel_antes = carro.get_combustivel()
        quantidade = carro.get_combustivel_max() - carro.get_combustivel()
        self.bomba.abastecer(quantidade,carro)
        
        self.imprimir(f"{carro.modelo} entrou no box ({tempo}s) | Combustível: {combustivel_antes}L --> {carro.get_combustivel()}L")

class Carro(Veiculo):
    def __init__(self, modelo, piloto, velocidade_max, combustivel_max, combustivel_atual):
        super().__init__(modelo,piloto, velocidade_max, combustivel_max, combustivel_atual)
        self.distancia = 0
        self.pneus = [Pneu() for i in range(4)]
        self.tempo_box = 0
    
    def acelerar(self):
        if self.get_combustivel() <= 0:
            return f"{self.modelo} ficou sem combustível!"

        velocidade = random.randint(self.get_velocidade_max() - 40, self.get_velocidade_max())
        self.distancia += velocidade
        
        consumo = velocidade * 0.02
        novo_combustivel = self.get_combustivel() - consumo
        self.set_combustivel(max(0, novo_combustivel))
        
        if velocidade >= 250:
            desgaste = 5
        
        elif velocidade >= 200:
            desgaste = 3
        
        else:
            desgaste = 1
        
        for pneu in self.pneus:
            pneu.desgastar(desgaste)

        return f"{self.modelo} acelerando a {velocidade} km/h (Distância: {self.distancia})"
    
    def precisa_pitstop(self):
        desgaste_pneus = any(pneu.desgaste >= 70 for pneu in self.pneus)
        pouco_combustivel = self.get_combustivel() <= 15
        return desgaste_pneus or pouco_combustivel

class Equipe:
    def __init__(self, nome):
        self.nome = nome
        self.__participantes = []
        
    def adicionar_participantes(self, participante):
        self.__participantes.append(participante)

    def listar_participantes(self):
        for p in self.__participantes:
            print(f"Carro: {p.modelo} | Piloto: {p.piloto.nome}")

class Pista:
    def __init__(self, nome, comprimento):
        self.nome = nome
        self.__comprimento = comprimento

    def get_comprimento(self):
        return self.__comprimento

class Corrida(LogMixin):
    def __init__(self, participantes, pista, pitstop):
        self.participantes = participantes
        self.distancia_total = pista.get_comprimento()
        self.pitstop = pitstop

    def iniciar(self):
        self.resultado = []

        for c in self.participantes:
            c.distancia = 0
        self.imprimir("Corrida iniciada!!\n")

        while len(self.resultado) < len(self.participantes):
            for carro in self.participantes:
                if carro not in self.resultado:
                    self.imprimir(carro.acelerar())
                    if carro.precisa_pitstop():
                        self.pitstop.realizar(carro)
                    
                    if carro.distancia >= self.distancia_total:
                        self.imprimir(f"{carro.modelo} chegou!")
                        self.resultado.append(carro)

        self.resultado[0].piloto.set_vitorias()
        self.imprimir("\nCorrida finalizada!")
        self.imprimir("---Classificação---")
        lugar_podio = 1
        for c in self.resultado:
            self.imprimir(f"{lugar_podio}° - {c.modelo} | Piloto: {c.piloto.nome}")
            lugar_podio +=1

class Bomba_Combustivel:
    def __init__(self, combustivel_atual):
        self.combustivel_atual = combustivel_atual

    def abastecer(self, quantidade, carro):
        if quantidade > self.combustivel_atual:
            print("A bomba não possui combustível suficiente!")
            return
        
        carro.set_combustivel(carro.get_combustivel() + quantidade)
        self.combustivel_atual -= quantidade