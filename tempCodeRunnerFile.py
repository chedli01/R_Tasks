print(results.summary())

# # # Task 4: Plot regression line
# plt.scatter(df['x'], df['y'], color='blue', label="Data points")
# plt.plot(df['x'], results.fittedvalues, color='red', label="Regression Line")
# plt.title('Regression Line with Data Points')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.show()

# # # Task 5: Perform ANOVA
# anova_table = anova_lm(results, typ=2)
# print(anova_table)