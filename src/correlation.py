import pandas as pd
from src.config import df_custumers



correlation_matrix = df_custumers[['Charges.Total', 'tenure', 'DailyAccounts', 'Churn']].corr()
print(correlation_matrix)

