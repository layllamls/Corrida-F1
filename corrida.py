#integrantes: Laylla Melissa do Nascimento Fontes, Otávio Fernandes Barros, Maysa Ruth Silva Maraço, Francisco Marcio Queiroz Duarte
import abc
import random
import csv
import time
import interface as i

"""Responsável por exibir mensagens no terminal."""
class LogMixin:
    def imprimir(self, msg):
        print(msg)

"""Representa a interface de um box, cria contrato para que as classes que herdem dele tenham o método realizar()"""
class Box(abc.ABC):
    @abc.abstractmethod
    def realizar(self, carro):
        pass

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


"""Representa uma equipe formada pelos carros participantes da corrida."""
class Equipe(LogMixin):
    def __init__(self, nome):
        self.nome = nome
        self.__participantes = []

    def listar_participantes(self):
        for p in self.__participantes:
            self.imprimir(f"Carro: {p.modelo}")

    def adicionar_participantes(self, participante):
        self.__participantes.append(participante)
        participante.equipe = self.nome

"""Controla toda a simulação de corrida, essa classe que cria e salva as classificações de cada participante a cada corrida e que
faz com que mostre o progresso de cada veículo a cada volta da corrida."""
class Corrida(LogMixin):
    def __init__(self, participantes, pista, pitstop):
        self.participantes = participantes
        self.pista = pista
        self.distancia_total = pista.get_comprimento()
        self.pitstop = pitstop
        self.volta = 0
        self.interface = i.Interface()
    
    def salvar_classificacao(self):
        self.imprimir("Salvando classificação...")
        with open("classificacao.csv", "w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(["Posição", "Carro", "Equipe"])
            for posicao, carro in enumerate(self.resultado, start=1):
                escritor.writerow([
                posicao,
                carro.modelo,
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
            self.interface.limpar_tela()
            self.interface.cabecalho()
            self.volta += 1
            self.imprimir(f"\n Volta: {self.volta}\n")

            random.shuffle(self.participantes)
            for carro in self.participantes:
                if carro not in self.resultado:
                    self.pista.dificuldade(carro)
                    self.imprimir(carro.acelerar())

                    if carro.precisa_pitstop():
                        self.pitstop.realizar(carro)

                    if carro.distancia >= self.distancia_total:
                        self.imprimir(f"{carro.modelo} chegou!")
                        self.resultado.append(carro)

            self.mostrar_classificacao()
            time.sleep(6)

        self.imprimir("\nCorrida finalizada!")
        self.imprimir("\n VENCEDOR")
        self.imprimir(f"{self.resultado[0].modelo} venceu a corrida!!")
        self.imprimir("---Classificação---")
        lugar_podio = 1
        for c in self.resultado:
            self.imprimir(f"{lugar_podio}° - {c.modelo} | Equipe: {c.equipe}")
            lugar_podio += 1
        self.salvar_classificacao()

    def mostrar_classificacao(self):
        ordem = sorted(
                self.participantes,key=lambda carro: carro.distancia,reverse=True)
        self.imprimir("\n--- CLASSIFICAÇÃO ---")
        for posicao, carro in enumerate(ordem, start=1):
            self.imprimir(f"""{posicao}º {carro.modelo}
Progresso:
{self.interface.barra(carro.distancia,self.distancia_total)}
Combustível:
{self.interface.barra(carro.get_combustivel(), carro.get_combustivel_max())} Pneus: {carro.desgaste_medio():.0f}%""")
