from corrida import *

class Bots:
    def definir_bots(self):
        piloto_bot1 = Piloto("Carlos Sainz")
        piloto_bot2 = Piloto("Lance Stroll")
        carro_bot1 = Carro("Audi", piloto_bot1, 320, 100, 100)
        carro_bot2 = Carro("Red Bull", piloto_bot2, 330, 110, 110)
        equipe_bot1 = Equipe("Audi")
        equipe_bot2 = Equipe("Red Bull")
        equipe_bot1.adicionar_participantes(carro_bot1)
        equipe_bot2.adicionar_participantes(carro_bot2)
        return [carro_bot1, carro_bot2]

class EscolhaJogador:
    def definir_corredor(self):
        pilotos = [Piloto("Gabriel Bortoleto"), Piloto("Max Verstappen"), Piloto("Lewis Hamilton")]

        carros = [["Ferrari", 320, 100, 100], ["Mercedes", 330, 120, 120], ["McLaren", 310, 110, 110]]

        pistas = [Pista("Interlagos",3000), Pista("Mônaco",2500), Pista("Silverstone",4500)]

        equipes = [Equipe("Ferrari"), Equipe("Mercedes"), Equipe("McLaren")]

        print("\nEscolha um piloto:\n")
        for i, piloto in enumerate(pilotos, start=1):
            print(f"{i} - {piloto.nome}")

        op1 = int(input("Digite a opção: "))
        piloto = pilotos[op1-1]

        print("\nEscolha um carro:\n")
        for j, carro in enumerate(carros, start=1):
            print(f"{j} - {carro[0]}")
        op2 = int(input("Digite a opção: "))
        modelo, velocidade, combustivel_max, combustivel_atual = carros[op2-1]
        carro = Carro(modelo, piloto, velocidade, combustivel_max, combustivel_atual)

        print("\nEscolha uma pista:\n")
        for p, pista in enumerate(pistas, start=1):
            print(f"{p} - {pista.nome}")
        op3 = int(input("Digite a opção: "))
        pista = pistas[op3-1]

        print("\nEscolha uma equipe:\n")
        for e, equipe in enumerate(equipes, start=1):
            print(f"{e} - {equipe.nome}")
        op4 = int(input("Digite a opção: "))
        equipe = equipes[op4-1]

        equipe.adicionar_participantes(carro)
        return carro, pista

class Gerenciamento:
    
    def corrida_individual(self):
        print("\nCORRIDA INDIVIDUAL\n")
        escolha_jogador = EscolhaJogador()
        jogador, pista = escolha_jogador.definir_corredor()

        bots = Bots()
        adversarios = bots.definir_bots()

        bomba = Bomba_Combustivel(30000)
        pitstop = Pitstop(bomba)

        participantes = [jogador] + adversarios
        corrida = Corrida(participantes, pista, pitstop)
        corrida.iniciar()
        input("\nPressione ENTER para voltar ao menu...")
        limpar_tela()

    def torneio(self):
        print("\nTORNEIO ")
        print("Em desenvolvimento...")

    def criar_participantes(self):
        print("\n CRIAR PARTICIPANTES")
        print("Em desenvolvimento...")


    def listar_participantes(self):
        print("\n LISTAR PARTICIPANTES")
        print("Em desenvolvimento...")


    def ranking(self):
        print("\n RANKING")
        print("Em desenvolvimento...")


    def ranking_apostas(self):
        print("\n RANKING DE APOSTAS")
        print("Em desenvolvimento...")


    def menu(self):
        while True:
            print("SIMULADOR DE CORRIDA")
            print("1 - Corrida Individual")
            print("2 - Torneio")
            print("3 - Criar Participantes")
            print("4 - Listar Participantes")
            print("5 - Ranking")
            print("6 - Ranking de Apostas")
            print("0 - Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.corrida_individual()
            elif opcao == "2":
                self.torneio()
            elif opcao == "3":
                self.criar_participantes()
            elif opcao == "4":
                self.listar_participantes()
            elif opcao == "5":
                self.ranking()
            elif opcao == "6":
                self.ranking_apostas()
            elif opcao == "0":
                print("\nPrograma encerrado.")
                break
            else:
                print("\nOpção inválida, insira novamente!")

if __name__ == "__main__":
    gerenciamento = Gerenciamento()
    gerenciamento.menu()
