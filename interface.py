import os
class Interface:
    """Cria uma barra de progresso que representa visualmente o progresso de cada carro, com distancia
    percorrida e combustível restante no carro."""
    def barra(self, valor, total, tamanho=20):
        porcentagem = valor / total
        if porcentagem > 1:
            porcentagem = 1
        preenchido = int(tamanho * porcentagem)
        return "█" * preenchido + "░" * (tamanho - preenchido)

    """Limpa o terminal, utilizado para limpar o terminal a cada nova volta percorrida. Facilitando a visualização
    a cda nova volta."""
    def limpar_tela(self):
        os.system("cls")

    """Exibe o cabeçalho do simulador de corrida"""
    def cabecalho(self):
        print("=" * 45)
        print("SIMULADOR DE CORRIDA")
        print("=" * 45)
