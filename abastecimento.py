import pandas as pd
import matplotlib.pyplot as plt

# 1. Carregar os dados
df = pd.read_excel("abastecimentos.xlsx", parse_dates=["data"])

# 2. Visualizar primeiras linhas
print("Primeiros registros:")
print(df.head())

# 3. Estatísticas básicas
print("\nResumo estatístico:")
print(df.describe())

# 4. Criar colunas derivadas
df["consumo_km_l"] = df["km"].diff() / df["litros"]  # km rodados entre abastecimentos / litros
df["custo_por_km"] = df["total_pago"] / df["km"].diff()

print("\nCom novas colunas:")
print(df.head())

# 5. Visualizações simples
plt.figure(figsize=(10,5))
plt.plot(df["data"], df["preco_litro"], marker="o")
plt.title("Preço do litro ao longo do tempo")
plt.xlabel("Data")
plt.ylabel("Preço (R$)")
plt.grid(True)
plt.show()

plt.figure(figsize=(10,5))
plt.plot(df["data"], df["consumo_km_l"], marker="o", color="green")
plt.title("Consumo médio (km/l)")
plt.xlabel("Data")
plt.ylabel("Km/l")
plt.grid(True)
plt.show()

# 6. Salvando dataset atualizado
df.to_excel("abastecimentos_processados.xlsx", index=False)
