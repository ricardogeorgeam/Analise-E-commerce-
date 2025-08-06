Análise de Vendas E-commerce: Implementação de Arquitetura Medalhão
📌 Sobre o Projeto
Este projeto visa realizar uma análise aprofundada dos dados de vendas de um e-commerce, utilizando uma arquitetura de dados robusta e moderna, a Arquitetura Medalhão (Bronze, Prata, Ouro). O objetivo é garantir a qualidade e a organização dos dados em cada etapa do processo ETL (Extract, Transform, Load), culminando na criação de um painel analítico interativo no Power BI para fornecer insights acionáveis para o negócio.

🎯 Objetivo da Análise
O objetivo principal deste projeto é criar um painel analítico no Power BI conectando à camada Ouro da arquitetura Medalhão com dados de vendas. Para isso, a análise busca responder a nove dúvidas de negócio cruciais:

Performance de Vendas no Tempo: Como as vendas se comportam ao longo do tempo (diário, semanal, mensal, anual)? Há sazonalidade, tendências de crescimento ou queda?

Principais Produtos e Categorias Vendidas: Quais produtos e categorias geram a maior parte da receita? Quais são os "carros-chefe"?

Ticket Médio dos Pedidos: Qual o valor médio gasto por pedido? Há espaço para aumentar o ticket médio?

Métodos de Pagamento Preferidos: Quais são os métodos de pagamento mais utilizados pelos clientes? Há algum que cause mais problemas (rejeições)?

Vendas por Vendedor/Geografia: Quais vendedores estão performando melhor? Há concentração de vendas em certas regiões ou estados?

Análise da Base de Clientes: Quantos clientes temos? Quantos são recorrentes? Qual o perfil dos nossos clientes (cidade/estado)?

Impacto do Valor do Frete nas Vendas: O frete está sendo um fator decisivo na conclusão da compra? Clientes pagam mais por frete rápido?

Status dos Pedidos e Pontos de Falha: Quais os status mais comuns dos pedidos (entregues, cancelados, em processamento)? Onde estão os gargalos no processo?

Tempo Médio de Processamento/Entrega de Pedidos: Quanto tempo leva para um pedido ser processado e entregue? Há oportunidades para otimizar a logística?

📊 Metodologia Utilizada
O projeto segue uma metodologia estruturada em etapas, com foco na implementação da Arquitetura Medalhão para o processo ETL:

ETL com Python e Pandas: Utilização de scripts Python e da biblioteca Pandas para extração, transformação e carga dos dados.

Camadas de Dados (Bronze → Prata → Ouro): Organização dos dados em diferentes níveis de refinamento.

Modelagem de Dados: Criação de um modelo de dados otimizado para análise no Power BI.

Visualização no Power BI: Desenvolvimento de um painel interativo para apresentar os insights.

📁 Estrutura da Arquitetura Medalhão

Camada

Descrição

Exemplo

Bronze

Dados brutos, extraídos diretamente da fonte, sem qualquer transformação.

Arquivos .csv originais: avaliacoes, categorias, clientes, localizacao, pagamentos, pedidos, pedidos_itens, produtos, vendedores.

Prata

Dados limpos e transformados, prontos para análises mais detalhadas.

Remoção de nulos, tratamento de tipos de dados, remoção de duplicatas, normalização de colunas.

Ouro

Dados analíticos agregados e modelados, otimizados para consumo por ferramentas de BI.

Tabelas de Fato e Dimensão, agregações por período, KPIs calculados.

🔧 Tecnologias Utilizadas
Python: Linguagem principal para o processo ETL.

Pandas: Biblioteca Python para manipulação e análise de dados.

SQLAlchemy (Opcional): Para interagir com bancos de dados.

Power BI Desktop: Ferramenta para visualização e criação do painel analítico.

(Opcional) SQLite/PostgreSQL: Para armazenar a camada Ouro.

(Opcional) Google Drive ou Azure: Para armazenamento em nuvem.

🫧 Limpeza e Manipulação dos Dados Realizada
A etapa de limpeza de dados foi crucial para garantir a qualidade e a confiabilidade das informações. Os principais passos incluíram:

Inspeção Inicial: Tradução da base de dados (originalmente em inglês) para o português e consulta ao codebook para compreensão das colunas.

Identificação de Problemas: Detecção de valores ausentes (nulos), registros duplicados e inconsistências de formatação.

Correção de Erros: Conversão de tipos de dados e padronização de valores para garantir a consistência.

Tratamento de Outliers: Investigação de outliers utilizando boxplot e IQR. Os outliers foram mantidos quando justificáveis pelo contexto de negócio (e.g., variações salariais em diferentes cargos).

Validação: Verificações pós-limpeza para confirmar a integridade dos dados.

🔍 Principais Descobertas e Insights (Baseado nos Dashboards Iniciais)
Com base nos dashboards de e-commerce analisados, destacam-se os seguintes insights:

Alto Volume de Entregas: 92 mil pedidos entregues de um total de 94 mil, indicando alta taxa de sucesso.

Baixa Eficiência na Entrega no Prazo: Apenas 30,87% dos pedidos são entregues no prazo, um ponto crítico que exige otimização logística.

Crescimento Robusto: Faturamento de R$ 15,79 milhões com um aumento de R$ 8,6 milhões.

Ticket Médio Consistente: O ticket médio se mantém em torno de R$ 140, com flutuações.

Categorias de Destaque: "Cama, mesa e banho" (29,44%), "Beleza", "Esportes" e "Decoração" são as categorias mais vendidas.

Sazonalidade de Vendas: Pico significativo de volume de vendas no final de 2017 e início de 2018.

Prevalência do Cartão de Crédito: Principal método de pagamento utilizado.

Oportunidades de Melhoria: Necessidade de investigar as causas dos 625 pedidos cancelados e 527 pedidos "Indisponíveis".

📝 Próximos Passos
Finalizar a Camada Ouro: Concluir a modelagem de dados e as agregações para o consumo no Power BI.

Desenvolvimento do Painel no Power BI: Construir o painel analítico interativo.

Análise Aprofundada dos Gargalos: Investigar as causas da baixa taxa de entrega no prazo e dos cancelamentos.

Otimização do Ticket Médio: Explorar estratégias de cross-selling e up-selling.

Monitoramento Contínuo: Implementar um processo de monitoramento dos dados e do painel.

Autor: Ricardo Albuquerque
