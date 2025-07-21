from src.config import df_custumers
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns

df_custumers.describe()
print("\nBasic Statistics for Numeric Columns:")
print(df_custumers.describe())

# Additional measures: Median, Standard Deviation, etc.
print("\nAdditional Descriptive Metrics:")
numerical_columns = df_custumers.select_dtypes(include=['float64', 'int64']).columns
for col in numerical_columns:
    print(f"\n{col}:")
    print(f"Mean: {df_custumers[col].mean()}")
    print(f"Median: {df_custumers[col].median()}")
    print(f"Standard Deviation: {df_custumers[col].std()}")
    print(f"Min: {df_custumers[col].min()}")
    print(f"Max: {df_custumers[col].max()}")
    print(f"25th Percentile: {df_custumers[col].quantile(0.25)}")
    print(f"75th Percentile: {df_custumers[col].quantile(0.75)}")

# Descriptive statistics for categorical columns
print("\nDescriptive Statistics for Categorical Columns:")
categorical_columns = df_custumers.select_dtypes(include=['object', 'category']).columns

for col in categorical_columns:
    print(f"\n{col}:")
    print(df_custumers[col].value_counts())
    print(f"Most frequent value: {df_custumers[col].mode()[0]}")
    print(f"Frequency of the most frequent value: {df_custumers[col].value_counts().max()}")