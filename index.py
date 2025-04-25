import pandas as pd

# Load the Excel file
df = pd.read_excel("Exemple2Reference_SReg_PW2.xlsx")

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Assuming df is already loaded with data
X = df['x'].values.reshape(-1, 1)
y = df['y'].values

model = LinearRegression()
model.fit(X, y)

# Plot the data and regression line
plt.scatter(df['x'], df['y'], color='blue', label='Data')
plt.plot(df['x'], model.predict(X), color='red', label='Regression line')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Regression Line')
plt.legend()
plt.show()
