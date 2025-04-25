# Install and load the readxl package (if not already installed)
install.packages("readxl")
library(readxl)

# Read the Excel file (adjust the path if it's in another location)
data <- read_excel("Exemple2Reference_SReg_PW2.xlsx")

# View the first few rows to confirm
head(data)


