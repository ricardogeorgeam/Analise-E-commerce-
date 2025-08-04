import numpy as np
import pandas as pd 

base_path = '/Users/ricardo/Documents/Dados/Analise/Analise Ecommerce Medalhao/Analise Vendas/Dados/'
avaliacoes_bronze = pd.read_csv(f'{base_path}avaliacoes.csv')
categorias_bronze = pd.read_csv(f'{base_path}categorias.csv')
clientes_bronze = pd.read_csv(f'{base_path}clientes.csv')
localizacao_bronze = pd.read_csv(f'{base_path}localizacao.csv')
pagamentos_bronze = pd.read_csv(f'{base_path}pagamentos.csv')
pedidos_itens_bronze = pd.read_csv(f'{base_path}pedidos_itens.csv')
pedidos_bronze = pd.read_csv(f'{base_path}pedidos.csv')
produtos_bronze = pd.read_csv(f'{base_path}produtos.csv')
vendedores_bronze = pd.read_csv(f'{base_path}vendedores.csv')

# --- Informações de categorias_bronze ---
print("\n--- Informações de categorias_bronze ---")
print("Primeiras 5 linhas:")
print(categorias_bronze.head())
print("\nInformações gerais:")
categorias_bronze.info() # Não envolva com print()
print("\nEstatísticas descritivas:")
print(categorias_bronze.describe())

# --- Informações de clientes_bronze ---
print("\n--- Informações de clientes_bronze ---")
print("Primeiras 5 linhas:")
print(clientes_bronze.head())
print("\nInformações gerais:")
clientes_bronze.info() # Não envolva com print()
print("\nEstatísticas descritivas:")
print(clientes_bronze.describe())

# --- Informações de localizacao_bronze ---
print("\n--- Informações de localizacao_bronze ---")
print("Primeiras 5 linhas:")
print(localizacao_bronze.head())
print("\nInformações gerais:")
localizacao_bronze.info() # Não envolva com print()
print("\nEstatísticas descritivas:")
print(localizacao_bronze.describe())

# --- Informações de pagamentos_bronze ---
print("\n--- Informações de pagamentos_bronze ---")
print("Primeiras 5 linhas:")
print(pagamentos_bronze.head())
print("\nInformações gerais:")
pagamentos_bronze.info() # Não envolva com print()
print("\nEstatísticas descritivas:")
print(pagamentos_bronze.describe())

# --- Informações de pedidos_bronze ---
print("\n--- Informações de pedidos_bronze ---")
print("Primeiras 5 linhas:")
print(pedidos_bronze.head())
print("\nInformações gerais:")
pedidos_bronze.info() # Não envolva com print()
print("\nEstatísticas descritivas:")
print(pedidos_bronze.describe())

# --- Informações de pedidos_itens_bronze (Você repetiu este no seu código original) ---
# Vou incluir uma vez apenas. Se for intencional ter duas cópias, ajuste.
print("\n--- Informações de pedidos_itens_bronze ---")
print("Primeiras 5 linhas:")
print(pedidos_itens_bronze.head())
print("\nInformações gerais:")
pedidos_itens_bronze.info() # Não envolva com print()
print("\nEstatísticas descritivas:")
print(pedidos_itens_bronze.describe())


# --- Informações de produtos_bronze ---
print("\n--- Informações de produtos_bronze ---")
print("Primeiras 5 linhas:")
print(produtos_bronze.head())
print("\nInformações gerais:")
produtos_bronze.info() # Não envolva com print()
print("\nEstatísticas descritivas:")
print(produtos_bronze.describe())

# --- Informações de vendedores_bronze ---
print("\n--- Informações de vendedores_bronze ---")
print("Primeiras 5 linhas:")
print(vendedores_bronze.head())
print("\nInformações gerais:")
vendedores_bronze.info() # Não envolva com print()
print("\nEstatísticas descritivas:")
print(vendedores_bronze.describe())

print("\n=== Análise Exploratória Inicial Concluída ===")

avaliacoes_prata = avaliacoes_bronze.dropna()
avaliacoes_prata = avaliacoes_bronze.drop_duplicates()

categorias_prata = categorias_bronze.dropna()
categorias_prata = categorias_bronze.drop_duplicates()

clientes_prata = clientes_bronze.dropna()
clientes_prata = clientes_bronze.drop_duplicates()

localizacao_prata = localizacao_bronze.dropna()
localizacao_prata = localizacao_bronze.drop_duplicates()

pagamentos_prata = pagamentos_bronze.dropna()
pagamentos_prata = pagamentos_bronze.drop_duplicates()

pedidos_itens_prata = pedidos_itens_bronze.dropna()
pedidos_itens_prata = pedidos_itens_bronze.drop_duplicates()

pedidos_prata = pedidos_bronze.dropna()
pedidos_prata = pedidos_bronze.drop_duplicates()

produtos_prata = produtos_bronze.dropna()
produtos_prata = produtos_bronze.drop_duplicates()

venderores_prata = vendedores_bronze.dropna()
venderores_prata = vendedores_bronze.drop_duplicates()



