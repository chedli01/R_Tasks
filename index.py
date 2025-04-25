import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.anova import anova_lm
import scipy.stats as stats

# Load the data
df = pd.read_excel("Exemple2Reference_SReg_PW2.xlsx")

# Task 2: Scatter plot
plt.scatter(df['x'], df['y'], color='blue', label="Data points")
plt.title('Scatter plot of x vs y')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# Task 3: Fit the regression model using sm.OLS
X = df['x']
y = df['y']
X_with_const = sm.add_constant(X)
model = sm.OLS(y, X_with_const)
results = model.fit()
print(results.summary())

# # Task 4: Plot regression line
plt.scatter(df['x'], df['y'], color='blue', label="Data points")
plt.plot(df['x'], results.fittedvalues, color='red', label="Regression Line")
plt.title('Regression Line with Data Points')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# # Task 5: Perform ANOVA
anova_table = anova_lm(results, typ=2)
print(anova_table)

# Task 6: Confirm Gaussian character of residuals
residuals = results.resid
# plt.hist(residuals, bins=15, edgecolor='black', color='lightgray')
# plt.title('Histogram of Residuals')
# plt.xlabel('Residuals')
# plt.ylabel('Frequency')
# plt.show()

# sm.qqplot(residuals, line ='45')
# plt.show()

# shapiro_test = stats.shapiro(residuals)
# print(f"Shapiro-Wilk test p-value: {shapiro_test.pvalue}")
# if shapiro_test.pvalue > 0.05:
#     print("The residuals follow a Gaussian distribution.")
# else:
#     print("The residuals do not follow a Gaussian distribution.")

# # Task 7: Confidence Interval for coefficients
conf_interval = results.conf_int(alpha=0.05)
print(f"Confidence interval for the coefficients:\n{conf_interval}")

# # Task 9: Predict y for x = 500
x_new = pd.DataFrame({'const': [1], 'x': [500]})
y_pred = results.predict(x_new)
print(f"Predicted y for x = 500: {y_pred[0]}")
