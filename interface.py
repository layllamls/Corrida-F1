import os
"""Responsável por controlar toda a interface do terminal, exibindo o cabeçalho, a barra de progresso e limpando a tela
durante a execução da corrida."""
class Interface:
    def pista(self, distancia, total, tamanho=60):
        porcentagem = min(distancia/total, 1)
        if porcentagem > 1:
            porcentagem = 1

        posicao = int((tamanho -1) * porcentagem)
        pista = ""
        for i in range(tamanho):
            if i == posicao:
                pista += "🏎"
            elif i == tamanho - 1:
                pista += "░"
            else:
                pista += "_"

        return pista
            
    def barra(self, valor, total, tamanho=20):
        porcentagem = valor / total
        if porcentagem > 1:
            porcentagem = 1
        preenchido = int(tamanho * porcentagem)
        return "█" * preenchido + "░" * (tamanho - preenchido)

    def limpar_tela(self):
        os.system("cls")

    def cabecalho(self):
        print("=" * 45)
        print("SIMULADOR DE CORRIDA")
        print("=" * 45)
