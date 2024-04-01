import pandas as pd
from scipy.stats import pearsonr

file_path = r"C:\Users\haoha\OneDrive\Desktop\personal\Personal Projects\SG Toilet Ratings\Cleaned_SG_Toilet_Ratings.xlsx"
cleaned_data = pd.read_excel(file_path)

# Convert all columns to numeric if needed.
for col in cleaned_data.columns:
    cleaned_data[col] = pd.to_numeric(cleaned_data[col], errors='coerce')

# Calculate the correlation coefficient for all combinations of columns
significant_correlations = []
non_significant_correlations = []
for i in range(len(cleaned_data.columns)):
    for j in range(i+1, len(cleaned_data.columns)):
        col1 = cleaned_data.columns[i]
        col2 = cleaned_data.columns[j]
        cleaned_data_temp = cleaned_data[[col1, col2]].dropna()
        if cleaned_data_temp.shape[0] > 0:
            correlation, p_value = pearsonr(cleaned_data_temp[col1], cleaned_data_temp[col2])
            if p_value < 0.05:
                significant_correlations.append((col1, col2, correlation, p_value))
            else:
                non_significant_correlations.append((col1, col2, correlation, p_value))

print("Significant correlations:")
for cols in significant_correlations:
    print(f"The Pearson correlation coefficient between '{cols[0]}' and '{cols[1]}' is: {cols[2]}")
    print(f"The p-value is: {cols[3]}")

print("\nNon-significant correlations:")
for cols in non_significant_correlations:
    print(f"The Pearson correlation coefficient between '{cols[0]}' and '{cols[1]}' is: {cols[2]}")
    print(f"The p-value is: {cols[3]}")
