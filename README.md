# Analysis-of-SG-Toilet-Ratings

The following project is more of a spur of the moment idea and I just didn't want the data that was thoroughly gathered to go to waste.

Some main takeaways from this analysis is that you can see for yourself on what impacts have what relation, or no relation to the overall cleanliness score of the toilets in MRT Stations in Singapore. 


clean.py



Selection of Data Source: The 'General Data' tab from the provided Excel file was identified as the primary source of useful information. 

Importing Data with Pandas: The pandas library was used to read the Excel file. The file_path variable was defined to specify the location of the Excel file.

Column Specification: column names were assigned to reflect the dataset's structure and content. Key columns such as 'Type', 'Location', and 'TotalScore' were identified, among others, to form the structure of the analysis framework.

Saving cleaned data: Cleaned data is saved into a new file, 'Cleaned_SG_Toilet_Ratings.xlsx'


eda.py


- Data Conversion with `pd.to_numeric()`: This function is crucial for ensuring the 'TotalScore' column is processed as numeric data. It attempts to convert each value to a number, defaulting to NaN (Not a Number) for any entries that resist conversion.

- Distribution Analysis with `histplot()`: Utilizing the seaborn library, `histplot()` is employed to construct a histogram for the 'TotalScore' column, visualizing the distribution of scores. The inclusion of the `kde=True` parameter overlays a Kernel Density Estimate (KDE) on the histogram, providing a smooth, continuous approximation of the distribution.

- Outlier Detection with `boxplot()`: The seaborn library's `boxplot()` function creates a box plot for the 'TotalScore' column, a graphical tool that reveals the central tendency, dispersion, and outliers within the data.

- Visualization with `plt.show()`: Renders the generated plots, `plt.show()` brings the visual analysis to the forefront, allowing users to interact with and draw conclusions from the presented data.



statistical.testing.py


The aim of the script in this file is to calculate Pearson's correlation coefficient and the p=value for testing non-correlation between a parameter and the total score.

Run the code to view all combinations and their statistical significance.


correlation_testing.py


- Computes the correlation matrix for the numeric columns.

- A mask is created for the upper triangle of the correlation matrix. Due to the symmetric properties of the matrix, the heatmap for the correlation matrix will the same information on both sides of the diagonal.

- Generated a custom diverging color map for the heatmap for coloring of cells in the heatmap.


regression_analysis.py

- Performs linear regression analyis
- After cleaning the data and aligning indices, it adds a constant for the intercept term in the statsmodels OLS model. The data is then split into training and testing sets, and the OLS model is fitted.
- The script prints a summary of the model fit, parses this summary to create a human-readable summary, and identifies statistically significant variables. It then fits a sklearn linear regression model, predicts the target variable on the test set, and evaluates the model performance by calculating the Mean Squared Error (MSE) and R-squared (R2). Finally, it plots the actual vs predicted values to visualize the model's performance.
- Run the code to view all combinations and their statistical significance.





