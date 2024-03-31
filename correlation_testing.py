import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

file_path = r"C:\Users\haoha\OneDrive\Desktop\personal\Personal Projects\SG Toilet Ratings\Cleaned_SG_Toilet_Ratings.xlsx"
cleaned_data = pd.read_excel(file_path)

# Convert all columns to numeric, skipping non-numeric ones
for column in cleaned_data.columns:
    cleaned_data[column] = pd.to_numeric(cleaned_data[column], errors='coerce')

# Drop columns that are all NaN values
cleaned_data.dropna(axis=1, how='all', inplace=True)

# Compute the correlation matrix for numeric columns only
correlation_matrix = cleaned_data.corr()

# Create a mask for the upper triangle
mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))

# Set up the matplotlib figure
plt.figure(figsize=(12, 10))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(230, 20, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(correlation_matrix, mask=mask, cmap=cmap, vmax=.3, center=0,
            annot=True, fmt='.2f', square=True, linewidths=.5, cbar_kws={"shrink": .5})

plt.title('Correlation Matrix of Toilet Ratings')
plt.show()
