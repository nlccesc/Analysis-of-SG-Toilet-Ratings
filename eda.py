import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

file_path = r"file path of your excel/csv file"
cleaned_data = pd.read_excel(file_path)
cleaned_data['TotalScore'] = pd.to_numeric(cleaned_data['TotalScore'], errors='coerce')

# Distribution of total scores
plt.figure(figsize=(10, 6))
sns.histplot(cleaned_data['TotalScore'], kde=True)
plt.title('Distribution of Total Scores')
plt.xlabel('Total Score')
plt.ylabel('Frequency')
plt.show()

# Box plot for cleanliness scores by score of scent
plt.figure(figsize=(12, 8))
sns.boxplot(x='ScentScore', y='TotalScore', data=cleaned_data)
plt.title('Cleanliness Scores by Scent Score')
plt.xlabel('Scent Score')
plt.ylabel('Cleanliness Score')
plt.xticks(rotation=45)
plt.show()
