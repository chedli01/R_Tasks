import pandas as pd

# Load the Excel file
df = pd.read_excel("Exemple2Reference_SReg_PW2.xlsx")
import statsmodels.api as sm

X_with_const = sm.add_constant(df['x'])
regression = sm.OLS(df['y'], X_with_const).fit()
anova_table = sm.stats.anova_lm(regression, typ=2)

print(anova_table)
