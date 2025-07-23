from src.config import df_custumers
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns


# Set the style for better visualization aesthetics
sns.set(style="whitegrid")

# Create a count plot for the 'Churn' column to show the proportion of churned vs. retained customers
plt.figure(figsize=(8, 6))  # Set the size of the figure
churn_plot = sns.countplot(data=df_custumers, x='Churn', palette='Set2')

# Set the title and labels for the plot
churn_plot.set_title('Customer Churn Distribution', fontsize=16)
churn_plot.set_xlabel('Churn', fontsize=12)
churn_plot.set_ylabel('Count of Customers', fontsize=12)

# Add the percentages on top of the bars for a clearer understanding
total = len(df_custumers)  # Total number of customers
for p in churn_plot.patches:
    height = p.get_height()
    churn_plot.annotate(f'{height / total * 100:.1f}%', 
                        (p.get_x() + p.get_width() / 2., height), 
                        ha = 'center', va = 'center', 
                        fontsize=12, color='black', 
                        xytext=(0, 5), textcoords='offset points')

# Make the plot more aesthetically pleasing
churn_plot.set_xticklabels(churn_plot.get_xticklabels(), rotation=0, fontsize=12)
churn_plot.set_yticklabels([f'{x:,}' for x in churn_plot.get_yticks()], fontsize=12)

# Ensure that the 'reports' folder exists
os.makedirs("reports", exist_ok=True)

# Save the plot as a PNG file in the 'reports' folder
plot_path = os.path.join("reports", "churn_distribution.png")
plt.savefig(plot_path, bbox_inches='tight')

# Show the plot
plt.show()

# Print the path where the plot is saved
print(f"Churn distribution plot saved at: {plot_path}")

