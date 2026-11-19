
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


BASE_DIR = Path(__file__).resolve().parent


df = pd.read_csv("Test1/Week1_Assessment/employees2.csv")
print("Original Employee Data:")
print(df)

print("\nMissing values:")
print(df.isnull().sum())

df = df.drop_duplicates()

# Correct data types
df["id"] = pd.to_numeric(df["id"], errors="coerce")
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")

# Fill missing salaries with median salary
median_salary = df["salary"].median()
df["salary"] = df["salary"].fillna(median_salary)

# Convert columns to integer types
df["id"] = df["id"].astype(int)
df["age"] = df["age"].astype(int)
df["salary"] = df["salary"].astype(int)

print("\nCleaned Employee Data:")
print(df)

print("\nData types:")
print(df.dtypes)


summary = df.groupby("department").agg(
    headcount=("id", "count"),
    average_salary=("salary", "mean"),
    maximum_salary=("salary", "max")
).reset_index()

print("\nDepartment Summary:")
print(summary)

departments = pd.read_csv("Test1/Week1_Assessment/department.csv")

print("\nDepartment Data:")
print(departments)

inner_merge = pd.merge(
    departments, summary,
    on="department",
    how="inner"
)

print("\nINNER JOIN:")
print(inner_merge)

left_merge = pd.merge(
    departments, summary,
    on="department",
    how="left"
)

print("\nLEFT JOIN:")
print(left_merge)

# OUTER JOIN
outer_merge = pd.merge(
    departments, summary,
    on="department",
    how="outer"
)

print("\nOUTER JOIN:")
print(outer_merge)

# Find departments with no employees
no_employees = outer_merge.loc[
    outer_merge["headcount"].isna(), "department"
].tolist()

print("\nDepartments with no employees:")
print(no_employees)
plt.figure(figsize=(8, 5))
plt.bar(
    summary["department"],
    summary["average_salary"],
    label="Average Salary"
)
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.legend()
plt.tight_layout()
plt.savefig(BASE_DIR / "bar_chart.png")
plt.close()

# HISTOGRAM: Salary distribution
plt.figure(figsize=(8, 5))
plt.hist(
    df["salary"],
    bins=5,
    label="Employee Salaries"
)
plt.title("Employee Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.legend()
plt.tight_layout()
plt.savefig(BASE_DIR / "histogram.png")
plt.close()

# SCATTER PLOT: Age vs Salary
plt.figure(figsize=(8, 5))
plt.scatter(
    df["age"],
    df["salary"],
    label="Employees"
)
plt.title("Employee Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.legend()
plt.tight_layout()
plt.savefig(BASE_DIR / "scatter_chart.png")
plt.close()

# LINE CHART: Average salary by department
plt.figure(figsize=(8, 5))
plt.plot(
    summary["department"],
    summary["average_salary"],
    marker="o",
    label="Average Salary"
)
plt.title("Department-wise Average Salary")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.legend()
plt.tight_layout()
plt.savefig(BASE_DIR / "line_chart.png")
plt.close()

print("\nAll four charts saved successfully!")
