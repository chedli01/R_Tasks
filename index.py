import pandas as pd

# Load the Excel file
df = pd.read_excel("Exemple2Reference_SReg_PW2.xlsx")

# View the first few rows
import matplotlib.pyplot as plt

plt.scatter(df['x'], df['y'], color='blue')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot of X vs Y')
plt.grid(True)
plt.show()
