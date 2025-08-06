# Análise de Vendas E-commerce: Implementação de Arquitetura Medalhão

## 📌 Sobre o Projeto
Este projeto realiza uma análise aprofundada dos dados de vendas de um e-commerce, utilizando a **Arquitetura Medalhão (Bronze, Prata, Ouro)**.  
O objetivo é garantir a **qualidade e organização dos dados** em cada etapa do processo ETL (Extract, Transform, Load), culminando na criação de um **painel analítico interativo no Power BI** para fornecer insights acionáveis para o negócio.

---

## 🎯 Objetivo da Análise
Criar um **painel analítico no Power BI** conectado à **camada Ouro** da Arquitetura Medalhão com dados de vendas.  
A análise responde a nove questões de negócio essenciais:

1. **Performance de Vendas no Tempo:** Como as vendas se comportam ao longo do tempo? Há sazonalidade?
2. **Principais Produtos e Categorias:** Quais itens geram a maior parte da receita?
3. **Ticket Médio:** Qual o valor médio gasto por pedido?
4. **Métodos de Pagamento:** Quais são os mais utilizados? Há problemas de rejeição?
5. **Vendas por Vendedor/Geografia:** Há concentração em certas regiões?
6. **Análise de Clientes:** Quantos clientes são recorrentes? Qual seu perfil?
7. **Impacto do Frete:** O frete influencia na decisão de compra?
8. **Status de Pedidos:** Quais os gargalos do processo?
9. **Tempo de Processamento e Entrega:** Há oportunidades de otimização logística?

---

## 📊 Metodologia Utilizada

1. **ETL com Python e Pandas:** Extração, transformação e carga dos dados.
2. **Camadas Bronze → Prata → Ouro:** Dados organizados em níveis de refinamento.
3. **Modelagem de Dados:** Criação de tabelas de fato e dimensão.
4. **Visualização:** Desenvolvimento de painel interativo no Power BI.

---

## 📁 Estrutura da Arquitetura Medalhão

| Camada | Descrição | Exemplo |
|--------|-----------|---------|
| **Bronze** | Dados brutos extraídos diretamente da fonte. | Arquivos `.csv` originais: avaliações, categorias, clientes, localização, pagamentos, pedidos, pedidos_itens, produtos, vendedores. |
| **Prata** | Dados limpos e transformados, prontos para análise. | Remoção de nulos, normalização de colunas, tratamento de duplicatas. |
| **Ouro** | Dados analíticos agregados e modelados. | Tabelas de Fato e Dimensão, KPIs calculados, agregações por período. |

---

## 🔧 Tecnologias Utilizadas

- **Python**: Linguagem principal para ETL.  
- **Pandas**: Manipulação e análise de dados.  
- **SQLAlchemy (Opcional)**: Conexão com bancos de dados.  
- **Power BI Desktop**: Visualização e dashboards.  
- **SQLite/PostgreSQL (Opcional)**: Armazenamento da camada Ouro.  
- **Google Drive ou Azure (Opcional)**: Armazenamento em nuvem.  

---

## 🫧 Limpeza e Manipulação dos Dados

- **Inspeção inicial:** Tradução da base (originalmente em inglês) e análise de colunas.  
- **Identificação de problemas:** Valores nulos, duplicatas, inconsistências de formatação.  
- **Correção de erros:** Conversão de tipos de dados, padronização de valores.  
- **Tratamento de outliers:** Utilização de Boxplot e IQR.  
- **Validação:** Verificação pós-limpeza para integridade dos dados.  

---

## 🔍 Principais Descobertas e Insights

- **92 mil pedidos entregues** de um total de 94 mil (alta taxa de sucesso).  
- **Somente 30,87% das entregas ocorreram no prazo** → gargalo logístico.  
- **Faturamento de R$ 15,79 milhões**, com crescimento de R$ 8,6 milhões.  
- **Ticket médio em torno de R$ 140**.  
- **Categorias mais vendidas:** "Cama, mesa e banho" (29,44%), "Beleza", "Esportes" e "Decoração".  
- **Pico de vendas** no final de 2017 e início de 2018.  
- **Cartão de crédito** como método de pagamento mais utilizado.  
- **625 pedidos cancelados** e **527 pedidos indisponíveis** → oportunidade de análise de causa.  

---

## 📝 Próximos Passos

- Finalizar a modelagem de dados da **Camada Ouro**.  
- Construir o **painel analítico interativo no Power BI**.  
- Investigar causas de baixa taxa de entrega no prazo e dos cancelamentos.  
- Desenvolver estratégias para **otimização do ticket médio** (cross-selling e up-selling).  
- Implementar **monitoramento contínuo de dados e dashboards**.  

---

## Autor
**Ricardo Albuquerque**  
