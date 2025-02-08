Projeto: DetectorDeFraudesFinanceiras

Descrição:
Este projeto simula um sistema de detecção de fraudes financeiras, demonstrando a aplicação de dois padrões de projeto:
1. Factory
2. Strategy

Estrutura do Projeto:
- main.py: Arquivo principal que integra o fluxo de pré-processamento, treinamento e predição.
- modelo_factory.py: Implementação do padrão Factory para criação de modelos de predição (classificador e regressor).
- pre_processamento.py: Implementação do padrão Strategy para o pré-processamento dos dados (normalização e padronização).
- README.txt: Este arquivo explicativo.

Padrões de Projeto Aplicados:

1. Factory
   - Objetivo: Centralizar a criação de instâncias de modelos, facilitando a adição de novos tipos de modelos sem a necessidade de alterar o código cliente.
   - Implementação: Classe ModeloFactory (arquivo modelo_factory.py), que cria instâncias de ModeloClassificador ou ModeloRegressor com base em um parâmetro.
   - Vantagens: Reduz acoplamento e torna o código mais modular e extensível.

2. Strategy
   - Objetivo: Permitir a intercambialidade de algoritmos de pré-processamento, possibilitando alterar o método de processamento dos dados em tempo de execução.
   - Implementação: 
       - Interfaces e classes de estratégias (NormalizacaoStrategy e PadronizacaoStrategy) no arquivo pre_processamento.py.
       - Classe PreProcessador que utiliza a estratégia definida para processar os dados.
   - Vantagens: Facilita a manutenção e a extensão, permitindo a aplicação de diferentes técnicas de pré-processamento conforme necessário.

Como Executar o Projeto:
1. Certifique-se de ter o Python instalado.
2. Navegue até a pasta "DetectorDeFraudesFinanceiras".
3. Execute o comando: python main.py

Conclusão:
A aplicação dos padrões Factory e Strategy neste projeto demonstra como estruturar um sistema de detecção de fraudes de forma modular e flexível, facilitando futuras manutenções e a inclusão de novas funcionalidades.
