"""
Data Pipelines with Pandas: DataFrame Creation, Filtering, and CSV Export
"""
import pandas as pd
import numpy as np

# Create a sample dataset
print("1. Creating DataFrame from scratch...")
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'age': [25, 30, 35, 28, 32],
    'salary': [50000, 60000, 75000, 55000, 80000],
    'department': ['Sales', 'IT', 'Finance', 'Sales', 'IT']
}
df = pd.DataFrame(data)
print(df)
print()

# Filter operations
print("2. Filtering: employees with age > 28...")
filtered_age = df[df['age'] > 28]
print(filtered_age)
print()

print("3. Filtering: IT department...")
filtered_dept = df[df['department'] == 'IT']
print(filtered_dept)
print()

# Complex filtering
print("4. Complex filter: IT dept AND salary > 60000...")
filtered_complex = df[(df['department'] == 'IT') & (df['salary'] > 60000)]
print(filtered_complex)
print()

# Data manipulation
print("5. Adding a new column (bonus = 10% of salary)...")
df['bonus'] = df['salary'] * 0.1
print(df)
print()

# Save to CSV
print("6. Saving filtered data to CSV...")
filtered_age.to_csv('employees_over_28.csv', index=False)
print("   Saved: employees_over_28.csv")
print()

# Read from CSV
print("7. Reading CSV back...")
df_loaded = pd.read_csv('employees_over_28.csv')
print(df_loaded)
print()

# Basic statistics
print("8. Summary statistics:")
print(df[['age', 'salary']].describe())
