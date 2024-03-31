import pandas as pd
from scipy.stats import pearsonr


file_path = r"file path of your excel/csv file"
cleaned_data = pd.read_excel(file_path)
cleaned_data['TotalScore'] = pd.to_numeric(cleaned_data['TotalScore'], errors='coerce')


# Calculate the correlation coefficient between one parameter and 'TotalScore'
# I used scentscore here, but you can change it to something else
# Ensure 'ScentScore' is converted to a numeric type if it isn't already
cleaned_data['ScentScore'] = pd.to_numeric(cleaned_data['ScentScore'], errors='coerce')
correlation, p_value = pearsonr(cleaned_data.dropna()['ScentScore'], cleaned_data.dropna()['TotalScore'])
print(f"The Pearson correlation coefficient between 'ScentScore' and 'TotalScore' is: {correlation}")
print(f"The p-value is: {p_value}")


if p_value < 0.05:
    print("The correlation is statistically significant.")
else:
    print("The correlation is not statistically significant.")
