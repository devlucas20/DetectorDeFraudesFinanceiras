# main.py

from modelo_factory import ModeloFactory
from pre_processamento import NormalizacaoStrategy, PadronizacaoStrategy, PreProcessador

def main():
    # Exemplo de dados brutos de transações financeiras
    dados_brutos = [100, 200, 150, 300, 250, 400]

    print("=== Pré-processamento dos dados ===")
    # Utilizando o padrão Strategy: Normalização
    pre_processador = PreProcessador(NormalizacaoStrategy())
    dados_normalizados = pre_processador.executar(dados_brutos)
    print("Dados normalizados:", dados_normalizados)

    # Alternativamente, pode-se usar a estratégia de padronização:
    pre_processador.set_strategy(PadronizacaoStrategy())
    dados_padronizados = pre_processador.executar(dados_brutos)
    print("Dados padronizados:", dados_padronizados)

    print("\n=== Treinamento do modelo ===")
    # Escolha do tipo de modelo a ser utilizado ("classificador" ou "regressor")
    tipo_modelo = "classificador"  # Alterne para "regressor" conforme necessário
    modelo = ModeloFactory.criar_modelo(tipo_modelo)
    
    # Simula o treinamento do modelo com dados processados
    dados_treinamento = dados_normalizados  # ou dados_padronizados
    modelo.treinar(dados_treinamento)

    print("\n=== Predição ===")
    # Simula uma nova transação (valor pós pré-processamento)
    nova_transacao = 0.7  # valor fictício
    resultado = modelo.predizer(nova_transacao)
    print("Resultado da predição:", resultado)

if __name__ == "__main__":
    main()
