#integrantes: Laylla Melissa do Nascimento Fontes, Otávio Fernandes Barros, Maysa Ruth Silva Maraço, Francisco Marcio Queiroz Duarte
import abc
import random
import csv
import os
import time

"""Cria uma barra de progresso que representa visualmente o progresso de cada carro, com distancia
percorrida e combustível restante no carro."""
def barra(valor, total, tamanho=20):
    porcentagem = valor / total
    if porcentagem > 1:
        porcentagem = 1
    preenchido = int(tamanho * porcentagem)
    return "█" * preenchido + "░" * (tamanho - preenchido)

"""Limpa o terminal, utilizado para limpar o terminal a cada nova volta percorrida. Facilitando a visualização
a cda nova volta."""
def limpar_tela():
    os.system("cls")

"""Exibe o cabeçalho do simulador de corrida"""
def cabecalho():
    print("=" * 45)
    print("SIMULADOR DE CORRIDA")
    print("=" * 45)

"""Responsável por exibir mensagens no terminal."""
class LogMixin:
    def imprimir(self, msg):
        print(msg)

"""Representa a interface de um box, cria contrato para que as classes que herdem dele tenham o método realizar()"""
class Box(abc.ABC):
    @abc.abstractmethod
    def realizar(self, carro):
        pass

"""Classe abstrata com método abstrato acelerar, serve como base para os veículos que 
quiserem participar da corrida, de modo que todos tenham que ter o método de acelerar()."""
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

"""Define um piloto participante da corrida, informando o nome e a quantidade de vitórias que ele possui."""
class Piloto:
    def __init__(self, nome):
        self.nome = nome
        self.__vitorias = 0
    
    def get_vitorias(self):
        return self.__vitorias
    
    def set_vitorias(self):
        self.__vitorias += 1

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

"""É utilizada pelo pitstop para abastecer os veículos, todo o combustível adicionado
nos carros é tirado do objeto bomba que está associado ao pitstop."""
class Bomba_Combustivel(LogMixin):
    def __init__(self, combustivel_atual):
        self.combustivel_atual = combustivel_atual

    def abastecer(self, quantidade, carro):
        if quantidade > self.combustivel_atual:
            self.imprimir("A bomba não possui combustível suficiente!")
            return
        
        carro.set_combustivel(carro.get_combustivel() + quantidade)
        self.combustivel_atual -= quantidade
    

"""Define tudo que um pitstop deve ter, realizando a troca de pneus e o abastecimento do carro, e utilizando o método da interface Box."""
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


"""Representa um carro que participará da corrida, usando os atributos base da classe Veiculo e 
implementando o método acelerar()."""
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
    
    def desgaste_medio(self):
        total = 0
        for pneu in self.pneus:
            total += pneu.desgaste
        return total / 4

"""Representa uma equipe formada pelos participantes da corrida."""
class Equipe(LogMixin):
    def __init__(self, nome):
        self.nome = nome
        self.__participantes = []

    def listar_participantes(self):
        for p in self.__participantes:
            self.imprimir(f"Carro: {p.modelo} | Piloto: {p.piloto.nome}")

    def adicionar_participantes(self, participante):
        self.__participantes.append(participante)
        participante.equipe = self.nome

"""Representa a pista, os objetos dessa classe que definem quanto os carros vão ter que andar
até chegarem ao final da corrida, o comprimento da pista que define a chegada dos veículos."""
class Pista:
    def __init__(self, nome, comprimento):
        self.nome = nome
        self.__comprimento = comprimento

    def get_comprimento(self):
        return self.__comprimento

"""Controla toda a simulação de corrida, ela que cria e salva as classificações de cada participante a cada corrida e que
faz com que mostre o progresso de cada veículo a cada volta da corrida."""
class Corrida(LogMixin):
    def __init__(self, participantes, pista, pitstop):
        self.participantes = participantes
        self.distancia_total = pista.get_comprimento()
        self.pitstop = pitstop
        self.volta = 0
    
    def salvar_classificacao(self):
        self.imprimir("Salvando classificação...")
        with open("classificacao.csv", "w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(["Posição", "Piloto", "Equipe"])
            for posicao, carro in enumerate(self.resultado, start=1):
                escritor.writerow([
                posicao,
                carro.piloto.nome,
                carro.equipe ])
        self.imprimir("Arquivo criado com sucesso!")

    def iniciar(self):
        self.resultado = []
        self.volta=0
        time.sleep(1)
        for c in self.participantes:
            c.distancia = 0
            c.set_combustivel(c.get_combustivel_max())
            c.tempo_box = 0
            for pneu in c.pneus:
                pneu.trocar()

        self.imprimir("Corrida iniciada!!\n")
        while len(self.resultado) < len(self.participantes):
            limpar_tela()
            cabecalho()
            self.volta += 1
            self.imprimir(f"\n Volta: {self.volta}\n")

            random.shuffle(self.participantes)
            for carro in self.participantes:
                if carro not in self.resultado:
                    self.imprimir(carro.acelerar())

                    if carro.precisa_pitstop():
                        self.pitstop.realizar(carro)

                    if carro.distancia >= self.distancia_total:
                        self.imprimir(f"{carro.modelo} chegou!")
                        self.resultado.append(carro)

            self.mostrar_classificacao()
            time.sleep(6)

        self.resultado[0].piloto.set_vitorias()
        self.imprimir("\nCorrida finalizada!")
        self.imprimir("\n VENCEDOR")
        self.imprimir(f"{self.resultado[0].modelo} venceu com {self.resultado[0].piloto.nome}")
        self.imprimir("---Classificação---")
        lugar_podio = 1
        for c in self.resultado:
            self.imprimir(f"{lugar_podio}° - {c.modelo} | Piloto: {c.piloto.nome}")
            lugar_podio += 1
        self.salvar_classificacao()

    def mostrar_classificacao(self):
        ordem = sorted(
                self.participantes,key=lambda carro: carro.distancia,reverse=True)
        self.imprimir("\n--- CLASSIFICAÇÃO ---")
        for posicao, carro in enumerate(ordem, start=1):
            self.imprimir(f"""{posicao}º {carro.modelo}
Progresso:
{barra(carro.distancia,self.distancia_total)}
Combustível:
{barra(carro.get_combustivel(), carro.get_combustivel_max())} Pneus: {carro.desgaste_medio():.0f}%""")
