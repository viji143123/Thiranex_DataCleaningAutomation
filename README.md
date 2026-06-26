# Data Cleaning & Reporting Automation

## Project Overview

This project automates the process of cleaning raw data and generating reports using Python. It handles common data quality issues such as missing values, duplicate records, and inconsistent data, then creates a cleaned dataset, summary report, and visualization.

## Objective

* Automate data cleaning tasks.
* Handle missing values and duplicate records.
* Generate summary reports automatically.
* Create visual charts for better data analysis.

## Tools & Technologies

* Python
* Pandas
* Matplotlib
* OpenPyXL
* VS Code

## Features

* Load data from a CSV file.
* Fill missing values.
* Remove duplicate records.
* Save cleaned data to an Excel file.
* Generate a summary statistics report.
* Create a bar chart showing employee distribution by department.

## Project Structure

```text
DataCleaningAutomation/
│── employees.csv
│── data_cleaning.py
│── Cleaned_Data.xlsx
│── Summary_Report.xlsx
│── department_chart.png
│── README.md
```

## How to Run the Project

### 1. Clone the Repository

```bash
git clone <repository-link>
```

### 2. Open the Project Folder

```bash
cd DataCleaningAutomation
```

### 3. Install Required Libraries

```bash
pip install pandas matplotlib openpyxl
```

### 4. Run the Project

```bash
python data_cleaning.py
```

## Output

After running the program, the following files will be generated:

* **Cleaned_Data.xlsx** – Cleaned dataset
* **Summary_Report.xlsx** – Statistical summary
* **department_chart.png** – Department-wise employee chart

## Learning Outcomes

* Data preprocessing using Python
* Handling missing and duplicate values
* Automating report generation
* Creating basic data visualizations
* Working with Excel files using Python

## Future Enhancements

* Add interactive Power BI dashboards.
* Support multiple datasets.
* Generate PDF reports automatically.
* Build a graphical user interface (GUI).

## Author

**Vijayalakshmi**
