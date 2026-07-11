import os
"""Responsável por controlar toda a interface do terminal, exibindo o cabeçalho, a barra de progresso e limpando a tela
durante a execução da corrida."""
class Interface:
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
