import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
from src.config import df_custumers

# Ensure output folder exists
os.makedirs("reports", exist_ok=True)

# Convert Churn to numeric for correlation (0 = stayed, 1 = churned)
df_custumers['Churn_num'] = df_custumers['Churn'].apply(lambda x: 1 if x in ['Yes', 1] else 0)

# Compute DailyAccounts if missing
if 'DailyAccounts' not in df_custumers:
    df_custumers['DailyAccounts'] = df_custumers['Charges.Monthly'] / 30

# Define numeric features and compute correlation
numeric_cols = ['Charges.Total', 'tenure', 'DailyAccounts', 'Churn_num']
corr_matrix = df_custumers[numeric_cols].corr()

# Map original column names to clear labels
label_map = {
    'Charges.Total': 'Total Charges ($)',
    'tenure': 'Customer Tenure (months)',
    'DailyAccounts': 'Daily Billing ($)',
    'Churn_num': 'Churn (0=Stay,1=Leave)'
}

# Rename for display
corr_display = corr_matrix.rename(index=label_map, columns=label_map)


plt.figure(figsize=(6, 5))
sns.set(style="white")
ax = sns.heatmap(
    corr_display,
    annot=True, fmt=".2f",
    cmap="coolwarm", center=0, square=True,
    cbar_kws={'shrink': .8, 'label': 'Correlation'}
)
plt.title("Correlation Matrix of Key Metrics and Churn", fontsize=14, fontweight='bold', pad=12)
plt.tight_layout()
plt.savefig("reports/churn_correlation_heatmap.png", dpi=300)
plt.show()