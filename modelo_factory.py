from abc import ABC, abstractmethod

# Interface abstrata para os modelos
class Modelo(ABC):
    @abstractmethod
    def treinar(self, dados):
        pass

    @abstractmethod
    def predizer(self, entrada):
        pass

# Implementação de um modelo classificador
class ModeloClassificador(Modelo):
    def treinar(self, dados):
        print("Treinando modelo classificador com os dados:", dados)
        # Lógica de treinamento para o classificador (ex.: algoritmo de detecção de fraude)
        
    def predizer(self, entrada):
        print("Realizando predição com o modelo classificador para a entrada:", entrada)
        # Exemplo simplificado: se a entrada for maior que 0.5, considera fraude.
        return "Fraude" if entrada > 0.5 else "Não Fraude"

# Implementação de um modelo regressor
class ModeloRegressor(Modelo):
    def treinar(self, dados):
        print("Treinando modelo regressor com os dados:", dados)
        # Lógica de treinamento para o regressor
        
    def predizer(self, entrada):
        print("Realizando predição com o modelo regressor para a entrada:", entrada)
        # Exemplo simplificado de predição
        return entrada * 0.8

# Classe Factory para criação dos modelos
class ModeloFactory:
    @staticmethod
    def criar_modelo(tipo):
        if tipo == "classificador":
            return ModeloClassificador()
        elif tipo == "regressor":
            return ModeloRegressor()
        else:
            raise ValueError("Tipo de modelo não suportado: " + tipo)
