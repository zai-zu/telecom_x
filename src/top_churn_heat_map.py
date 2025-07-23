from src.config import df_custumers
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Calculate churn rate for each combination of Contract and PaymentMethod
churn_heatmap = (
    df_custumers.groupby(['Contract', 'PaymentMethod'])['Churn']
    .apply(lambda x: (x == 1).mean()*100)
    .unstack()
)

plt.figure(figsize=(10, 7))
sns.set(font_scale=1.05, style="whitegrid")
ax = sns.heatmap(churn_heatmap, annot=True, fmt=".1f", cmap="YlGnBu", linewidths=.6, cbar_kws={'label': 'Churn Rate (%)'})
plt.title("Churn Rate Heatmap by Contract and Payment Method", fontsize=16, weight='bold', pad=18)
plt.xlabel("Payment Method", fontsize=13)
plt.ylabel("Contract Type", fontsize=13)
plt.tight_layout(pad=2)

# Save figure
os.makedirs("reports", exist_ok=True)
plt.savefig("reports/churn_heatmap_contract_paymentmethod.png", bbox_inches='tight', dpi=300)
plt.show()




