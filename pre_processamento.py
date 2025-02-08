# pre_processamento.py

from abc import ABC, abstractmethod

# Interface para a estratégia de pré-processamento
class PreProcessamentoStrategy(ABC):
    @abstractmethod
    def processar(self, dados):
        pass

# Estratégia concreta: Normalização dos dados
class NormalizacaoStrategy(PreProcessamentoStrategy):
    def processar(self, dados):
        print("Aplicando normalização aos dados:", dados)
        # Exemplo simples: escalonamento para o intervalo [0, 1]
        minimo, maximo = min(dados), max(dados)
        if maximo == minimo:
            return [0 for _ in dados]
        return [(x - minimo) / (maximo - minimo) for x in dados]

# Estratégia concreta: Padronização dos dados
class PadronizacaoStrategy(PreProcessamentoStrategy):
    def processar(self, dados):
        print("Aplicando padronização aos dados:", dados)
        # Calcula média e desvio padrão
        media = sum(dados) / len(dados)
        variancia = sum((x - media) ** 2 for x in dados) / len(dados)
        desvio_padrao = variancia ** 0.5
        if desvio_padrao == 0:
            return [0 for _ in dados]
        return [(x - media) / desvio_padrao for x in dados]

# Classe que utiliza uma estratégia de pré-processamento
class PreProcessador:
    def __init__(self, strategy: PreProcessamentoStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PreProcessamentoStrategy):
        self.strategy = strategy

    def executar(self, dados):
        return self.strategy.processar(dados)
