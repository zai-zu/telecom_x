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

# 1) Lollipop plot for feature correlations with churn
corr_with_churn = corr_matrix['Churn_num'].drop('Churn_num').sort_values()
corr_with_churn.index = corr_with_churn.index.map(label_map)

plt.figure(figsize=(8, 4))
sns.set(style="whitegrid", font_scale=1.1)
norm = plt.Normalize(corr_with_churn.min(), corr_with_churn.max())
colors = plt.cm.coolwarm(norm(corr_with_churn.values))

y_pos = range(len(corr_with_churn))
plt.hlines(y=y_pos, xmin=0, xmax=corr_with_churn, color=colors, linewidth=5)
plt.scatter(corr_with_churn, y_pos, color=colors, s=100, zorder=3)

for i, val in enumerate(corr_with_churn):
    plt.text(val + 0.02 * (1 if val>=0 else -1), i, f"{val:.2f}", va='center', fontsize=11, fontweight='bold')

plt.yticks(y_pos, corr_with_churn.index)
plt.xlabel("Correlation with Churn", fontsize=12)
plt.title("Key Feature Correlation with Customer Churn", fontsize=14, fontweight='bold')
plt.xlim(corr_with_churn.min() - 0.1, corr_with_churn.max() + 0.1)
plt.tight_layout()
plt.savefig("reports/churn_feature_correlation_lollipop.png", dpi=300)
plt.show()