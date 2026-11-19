#!/usr/bin/env python
# coding: utf-8

# # Week 1 Assessment – Employee Data Analysis
# 
# ## 1. Introduction
# 
# This notebook analyses employee data using Python, Pandas, NumPy, and Matplotlib.
# 
# ### Objectives
# - Load and inspect employee data.
# - Clean missing values.
# - Analyse salaries by department.
# - Create visualisations.
# - Measure performance using `%timeit`.

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Libraries imported successfully!")


# In[3]:


# Load employee data
df = pd.read_csv("../data/employees2.csv")

# Display the first five rows
df.head()


# In[4]:


# Check the number of rows and columns
print("Dataset shape:", df.shape)

# Check column names and data types
df.info()

# Generate statistical summary
df.describe()


# In[5]:


# Check missing values
print("Missing values before cleaning:")
print(df.isnull().sum())

# Calculate median salary
median_salary = df["salary"].median()

# Fill missing salaries with median
df["salary"] = df["salary"].fillna(median_salary)

# Check missing values after cleaning
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Display cleaned data
df


# In[6]:


# Calculate department-wise salary statistics
department_analysis = df.groupby("department")["salary"].agg(
    employee_count="count",
    average_salary="mean",
    maximum_salary="max",
    minimum_salary="min"
)

# Display results
print(department_analysis)


# In[7]:


# Calculate average salary by department
avg_salary = df.groupby("department")["salary"].mean()

# Create bar chart
plt.figure(figsize=(8, 5))
avg_salary.plot(kind="bar")

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# In[8]:


# Create salary histogram
plt.figure(figsize=(8, 5))

plt.hist(df["salary"], bins=5, edgecolor="black")

plt.title("Employee Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.show()


# In[9]:


# Create scatter plot
plt.figure(figsize=(8, 5))

plt.scatter(df["age"], df["salary"])

plt.title("Employee Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")

plt.tight_layout()
plt.show()


# In[10]:


# Create line chart
plt.figure(figsize=(8, 5))

plt.plot(df["name"], df["salary"], marker="o")

plt.title("Employee Salary Comparison")
plt.xlabel("Employee Name")
plt.ylabel("Salary")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[ ]:


## 12. Key Findings and Conclusion

1. The dataset contains 8 employees across 4 departments.
2. Two missing salary values were identified and replaced with the median salary of 56,000.
3. The IT department has the highest average salary.
4. The Finance department has the lowest average salary.
5. The charts show salary variation across departments and employees. Age alone does not explain salary differences.

### Conclusion

The employee dataset was successfully loaded, cleaned, analysed, and visualised using Pandas, NumPy, and Matplotlib. The `%timeit` command was used to measure the performance of the department-wise salary calculation.


# In[11]:


get_ipython().run_line_magic('timeit', 'df.groupby("department")["salary"].mean()')


# In[ ]:




