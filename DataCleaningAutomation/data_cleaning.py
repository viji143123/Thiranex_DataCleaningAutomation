import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("employees.csv")

print("Original Data")
print(df)

# Fill missing values
df["Name"] = df["Name"].fillna("Unknown")
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
df["City"] = df["City"].fillna("Unknown")

# Remove duplicate rows
df = df.drop_duplicates()

print("\nCleaned Data")
print(df)

# Save cleaned data
df.to_excel("Cleaned_Data.xlsx", index=False)

# Create summary report
summary = df.describe()
summary.to_excel("Summary_Report.xlsx")

# Create bar chart
df["Department"].value_counts().plot(kind="bar")
plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.savefig("department_chart.png")
plt.show()

print("\nProject Completed Successfully!")