import corrida as c
import carros as ca
import pistas as p 

"""Cria os bots que se tornarão os adversários do jogador, para que a corrida possa acontecer."""
class Bots:
    def definir_bots(self):
        carro_bot1 = ca.CarrosBots("Audi")
        carro_bot2 = ca.CarrosBots("Red Bull")
        equipe_bot1 = c.Equipe("Audi")
        equipe_bot2 = c.Equipe("Red Bull")
        equipe_bot1.adicionar_participantes(carro_bot1)
        equipe_bot2.adicionar_participantes(carro_bot2)
        return [carro_bot1, carro_bot2]

"""Permite que o usuário escolha o carro, pista e equipe que deseja jogar,
retornando a escolha do jogador e da pista."""
class EscolhaJogador:
    def definir_jogador(self):
        pistas = [p.Interlagos(), p.Monaco(), p.Silverstone()]

        equipes = [c.Equipe("Ferrari"), c.Equipe("Mercedes"), c.Equipe("McLaren")]

        carros = [ca.Ferrari(), ca.Mercedes(), ca.McLaren()]

        print("\nEscolha um carro:\n")
        for g, carro in enumerate(carros, start=1):
            print(f"{g} - {carro.modelo}")
        op1 = int(input("Digite a opção: "))
        carro = carros[op1-1]
        
        print("\nEscolha uma pista:\n")
        for j, pista in enumerate(pistas, start=1):
            print(f"{j} - {pista.nome}")
        op2 = int(input("Digite a opção: "))
        pista = pistas[op2-1]

        print("\nEscolha uma equipe:\n")
        for e, equipe in enumerate(equipes, start=1):
            print(f"{e} - {equipe.nome}")
        op3 = int(input("Digite a opção: "))
        equipe = equipes[op3-1]

        equipe.adicionar_participantes(carro)
        return carro, pista

"""Faz com que tudo funcione, como se fosse um sistema geral, exibe as opções
e chama a função da opção escolhida pelo usuário. Por enquanto, somente a opção 1 teve o desenvolvimento
concluido."""
class Gerenciamento:
    
    def corrida_individual(self):
        print("\nCORRIDA INDIVIDUAL\n")
        escolha_jogador = EscolhaJogador()
        jogador, pista = escolha_jogador.definir_jogador()

        bots = Bots()
        adversarios = bots.definir_bots()

        bomba = c.Bomba_Combustivel(30000)
        pitstop = c.Pitstop(bomba)

        participantes = [jogador] + adversarios
        corrida = c.Corrida(participantes, pista, pitstop)
        corrida.iniciar()
        input("\nPressione ENTER para voltar ao menu...")
        c.limpar_tela()

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