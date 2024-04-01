import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from itertools import combinations

# Load the dataset
file_path = r"C:\Users\haoha\OneDrive\Desktop\personal\Personal Projects\SG Toilet Ratings\Cleaned_SG_Toilet_Ratings.xlsx"
data = pd.read_excel(file_path)

# Define the target variable
y = data['TotalScore'].apply(pd.to_numeric, errors='coerce')

# Get all columns except the target variable
all_columns = data.columns.tolist()
all_columns.remove('TotalScore')

# Generate all possible combinations of predictors
for r in range(1, len(all_columns) + 1):
    for subset in combinations(all_columns, r):
        subset = list(subset)
        X = data[subset].apply(pd.to_numeric, errors='coerce')

        # Drop any rows with NaN values in X or y
        X = X.dropna()
        y = y.dropna()

        # Ensure that X and y have the same index after dropping NaNs
        X, y = X.align(y, join='inner', axis=0)

        # Check if X and y are not empty
        if not X.empty and not y.empty:
            # Add a constant to the model for the intercept term in statsmodels
            X = sm.add_constant(X)

            # Split the data into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Fit the statsmodels OLS model
            sm_model = sm.OLS(y_train, X_train).fit()

            # Parsing the summary to create a human-readable summary
            p_values = sm_model.pvalues
            significant_vars = p_values[p_values < 0.05].index.tolist()
            nonsignificant_vars = p_values[p_values >= 0.05].index.tolist()

            # Remove 'const' from the lists if present
            significant_vars = [var for var in significant_vars if var != 'const']
            nonsignificant_vars = [var for var in nonsignificant_vars if var != 'const']

            # summary statements
            summary_statement = ""
            if 'const' in p_values and p_values['const'] < 0.05:
                summary_statement += "The model intercept is statistically significant. "
            else:
                summary_statement += "The model intercept is not statistically significant. "

            if significant_vars:
                summary_statement += f"The variables {', '.join(significant_vars)} have a significant correlation with TotalScore. "
            else:
                summary_statement += "No predictor variables have a significant correlation with TotalScore. "

            print(summary_statement)

            # Load the dataset
            model = LinearRegression()
            model.fit(X_train.drop('const', axis=1), y_train)  # Drop the constant term

            # Predict the 'TotalScore' on the test set
            y_pred = model.predict(X_test.drop('const', axis=1))

            # Evaluate the model performance
            mse = mean_squared_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)

            # Print out the performance metrics
            print(f"\nMean Squared Error (MSE): {mse}")
            print(f"R-squared (R2): {r2}")

            # Plot the actual vs predicted values
            plt.scatter(y_test, y_pred)
            plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=2)
            plt.xlabel('Actual')
            plt.ylabel('Predicted')
            plt.title('Actual vs Predicted Total Scores')
            plt.show()
        else:
            print(f"Skipping combination {subset} due to insufficient data after dropping NaNs.")
