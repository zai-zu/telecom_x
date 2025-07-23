import pandas as pd
from src.config import df_custumers


# Filter the data for churned (Churn = 1) and non-churned (Churn = 0) customers
df_churned = df_custumers[df_custumers['Churn'] == 1]
df_non_churned = df_custumers[df_custumers['Churn'] == 0]

# Descriptive statistics for 'Charges.Total' and 'tenure' based on churn status
print("\nDescriptive Statistics for 'Charges.Total' and 'tenure' based on Churn Status:")

# For churned customers
print("\nChurned Customers (Churn = 1):")
print(df_churned[['Charges.Total', 'tenure']].describe())

# For non-churned customers
print("\nNon-Churned Customers (Churn = 0):")
print(df_non_churned[['Charges.Total', 'tenure']].describe())

# Compare the mean and median values of 'Charges.Total' and 'tenure' for churned vs non-churned customers
print("\nMean and Median Comparison for 'Charges.Total' and 'tenure':")
mean_churned = df_churned[['Charges.Total', 'tenure']].mean()
median_churned = df_churned[['Charges.Total', 'tenure']].median()
mean_non_churned = df_non_churned[['Charges.Total', 'tenure']].mean()
median_non_churned = df_non_churned[['Charges.Total', 'tenure']].median()

# Display the comparison
print("Mean (Churned):", mean_churned)
print("Median (Churned):", median_churned)
print("Mean (Non-Churned):", mean_non_churned)
print("Median (Non-Churned):", median_non_churned)

# Check if there's a relationship between 'Contract' and 'Churn'
# Group by 'Contract' and calculate churn rates for each contract type
contract_churn_rate = df_custumers.groupby('Contract')['Churn'].value_counts(normalize=True).unstack() * 100

# Display the churn rates by contract type
print("\nChurn Rate by Contract Type:")
print(contract_churn_rate)

# Additional analysis: Check if 'Charges.Total' and 'tenure' are higher for churned or non-churned customers
print("\nComparison of 'Charges.Total' and 'tenure' across contract types:")
contract_summary = df_custumers.groupby('Contract')[['Charges.Total', 'tenure']].describe()

print(contract_summary)