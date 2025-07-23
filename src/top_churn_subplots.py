import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
from src.config import df_custumers

# Prepara los datos sólo de los que hicieron churn
df_churned = df_custumers[df_custumers['Churn'] == 1]

# Define las variables más relevantes
top_vars = ['Contract', 'PaymentMethod', 'InternetService']

# Crea el subplot
fig, axes = plt.subplots(1, 3, figsize=(18, 7), sharey=False)
sns.set(style="whitegrid")

for i, var in enumerate(top_vars):
    # Cuenta y ordena de mayor a menor
    order = df_churned[var].value_counts().sort_values(ascending=True).index
    # Color gradual
    norm = plt.Normalize(df_churned[var].value_counts().min(), df_churned[var].value_counts().max())
    colors = plt.cm.YlGnBu(norm(df_churned[var].value_counts().sort_values(ascending=True)))
    # Barras horizontales
    bars = axes[i].barh(order, df_churned[var].value_counts().sort_values(ascending=True), color=colors, edgecolor='black', height=0.6)
    # Etiquetas
    for bar in bars:
        width = bar.get_width()
        axes[i].text(width + max(df_churned[var].value_counts())*0.01, bar.get_y() + bar.get_height()/2,
                     f'{int(width)}', va='center', fontsize=11)
    axes[i].set_title(f'Churned by {var}', fontsize=14, weight='bold')
    axes[i].set_xlabel("Number of Churned Customers")
    axes[i].set_ylabel(var)
    axes[i].grid(axis='x', linestyle='--', alpha=0.6)

fig.suptitle("Main Categorical Features of Churned Customers", fontsize=17, weight='bold', y=1.04)
plt.tight_layout(pad=3)

# Guarda en reports
os.makedirs("reports", exist_ok=True)
plt.savefig('reports/churn_top_categories_subplots.png', bbox_inches='tight', dpi=300)
plt.show()

