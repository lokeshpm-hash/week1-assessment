# Week 1 Assessment – Employee Data Analysis

## 1. Project Overview

This project analyses employee data using Python, Pandas, NumPy, and Matplotlib. It includes data cleaning, statistical analysis, and visualisations.

## 2. Project Structure

```text
Week1_Assessment/
├── data/
│   └── employees2.csv
├── notebooks/
│   └── Week1_Employee_Analysis.ipynb
├── reports/
│   ├── bar_chart.png
│   ├── histogram.png
│   ├── line_chart.png
│   └── scatter_chart.png
├── src/
│   ├── Week1_Employee_Analysis.py
│   ├── Task1.py
│   ├── Task2.py
│   ├── Task2-2.py
│   ├── Task3.py
│   └── Task3-2.py
├── .gitignore
├── requirements.txt
└── README.md
```

## 3. Installation and Setup

1. Clone the repository:

```bash
git clone https://github.com/lokeshpm-hash/week1-assessment.git
cd week1-assessment
```

2. Create a virtual environment:

```bash
python -m venv .venv
```

3. Activate the environment on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

## 4. Running the Project

Start Jupyter Notebook:

```bash
jupyter notebook
```

Open `notebooks/Week1_Employee_Analysis.ipynb` and run the cells.

The exported Python script is available at:

```text
src/Week1_Employee_Analysis.py
```

## 5. Key Findings

1. The dataset contains 8 employees across 4 departments.
2. Two missing salary values were replaced with the median salary of 56,000.
3. IT has the highest average salary at approximately 63,666.67.
4. Finance has the lowest average salary at 48,000.
5. Visualisations show salary differences across departments and employees; age alone does not explain salary differences.

## 6. Tools and Libraries

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook
- Git and GitHub

## 7. Performance Measurement

The `%timeit` command was used to measure the execution time of department-wise salary analysis. The observed average was approximately 331 microseconds per loop.

## 8. Repository Information

This project was created as part of the Week 1 Python assessment. The main branch contains the initial project setup, and the feature branch contains the completed analysis.