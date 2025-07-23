from src.config import df_custumers
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Calculate the distribution of churn based on categorical variables
categorical_columns = [
    'gender', 'Contract', 'PaymentMethod', 'SeniorCitizen', 'Partner', 'Dependents', 
    'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 
    'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'PaperlessBilling'
]

# Loop through each categorical column and calculate the churn distribution
for col in categorical_columns:
    print(f"\nChurn distribution based on {col}:")
    
    # Group by the categorical column and calculate the churn distribution
    churn_distribution = df_custumers.groupby(col)['Churn'].value_counts(normalize=True).unstack() * 100
    
    # Display the churn distribution (percentage of customers who stayed and who churned)
    print(churn_distribution)
    
    
    
# Filter the data to include only customers who churned (Churn = 1)
df_churned = df_custumers[df_custumers['Churn'] == 1]

# Collect counts for each category of each variable, and store them in a single DataFrame
category_counts = []
for var in categorical_columns:
    counts = df_churned[var].value_counts().reset_index()
    counts.columns = ['category', 'count']
    counts['feature'] = var
    category_counts.append(counts)

# Combine all counts into one DataFrame
all_counts = pd.concat(category_counts, ignore_index=True)

# Create a combined label for plotting
all_counts['label'] = all_counts['feature'] + ": " + all_counts['category'].astype(str)

# Sort values by count (descending) for better visibility
all_counts = all_counts.sort_values(by='count', ascending=True)

# Set the style for better visualization aesthetics
sns.set(style="whitegrid")
plt.figure(figsize=(12, 22))  # Make the figure much taller

# Generate a color gradient based on the count
norm = plt.Normalize(all_counts['count'].min(), all_counts['count'].max())
colors = plt.cm.YlGnBu(norm(all_counts['count']))

# Create the horizontal barplot with reduced bar height for more spacing
bars = plt.barh(
    all_counts['label'],
    all_counts['count'],
    color=colors,
    edgecolor='black',
    height=0.65  # Reduce bar height for more space between bars
)

# Add count labels to each bar for clarity
for bar in bars:
    width = bar.get_width()
    plt.text(width + max(all_counts['count']) * 0.01, bar.get_y() + bar.get_height()/2,
             f'{int(width)}', va='center', fontsize=10)

# Titles and labels
plt.title("Distribution of Categorical Variables Among Churned Customers", fontsize=17, weight='bold', pad=14)
plt.xlabel("Number of Customers (Churned)", fontsize=13)
plt.ylabel("Category", fontsize=13)
plt.tight_layout(pad=2.5)  # Increase padding for more space

# Ensure the 'reports' folder exists
os.makedirs("reports", exist_ok=True)

# Save the plot as a PNG file in the 'reports' folder
plot_path = os.path.join("reports", "all_categorical_churn_horizontal_spaced.png")
plt.savefig(plot_path, bbox_inches='tight', dpi=300)
plt.show()

print(f"Single horizontal barplot for churned customers saved at: {plot_path}")
