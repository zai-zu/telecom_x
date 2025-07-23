import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
from src.config import df_custumers

# Ensure output folder exists
os.makedirs("reports", exist_ok=True)

# Prepare the data for churned customers only (Churn = 1)
df_churned = df_custumers[df_custumers['Churn'] == 1]

# Define the most relevant categorical variables for churn analysis
categorical_vars = ['Contract', 'PaymentMethod', 'InternetService']

# Create the subplot for displaying the analysis
fig, axes = plt.subplots(1, 3, figsize=(18, 7), sharey=False)
sns.set(style="whitegrid", font_scale=1.1)

# Loop through each variable to create the bar charts
for i, var in enumerate(categorical_vars):
    # Get sorted counts for each category in the variable
    category_order = df_churned[var].value_counts().sort_values(ascending=True).index
    
    # Set color gradient based on the count of each category
    norm = plt.Normalize(df_churned[var].value_counts().min(), df_churned[var].value_counts().max())
    colors = plt.cm.YlGnBu(norm(df_churned[var].value_counts().sort_values(ascending=True)))
    
    # Create horizontal bars for each category
    bars = axes[i].barh(category_order, df_churned[var].value_counts().sort_values(ascending=True), 
                        color=colors, edgecolor='black', height=0.6)
    
    # Add text labels on each bar for the counts
    for bar in bars:
        width = bar.get_width()
        axes[i].text(width + max(df_churned[var].value_counts()) * 0.01, bar.get_y() + bar.get_height() / 2,
                     f'{int(width)}', va='center', fontsize=11)
    
    # Set the title and axis labels
    axes[i].set_title(f"Churned by {var.replace(' ', ' ').title()}", fontsize=14, weight='bold')
    axes[i].set_xlabel("Number of Churned Customers", fontsize=12)
    axes[i].set_ylabel(var.replace(' ', ' ').title(), fontsize=12)
     # Remove the spines (borders) around each subplot
    for spine in axes[i].spines.values():
        spine.set_visible(False)
        
    # Add grid lines for better clarity
    axes[i].grid(axis='x', linestyle='--', alpha=0.6)

# Set the overall title for the figure
fig.suptitle("Main Categorical Features of Churned Customers", fontsize=17, weight='bold', y=1.04)

# Adjust the layout for better spacing between subplots
plt.tight_layout(pad=3)

# Save the figure in the 'reports' folder
plt.savefig('reports/churn_top_categories_subplots.png', bbox_inches='tight', dpi=300)

# Show the plot
plt.show()