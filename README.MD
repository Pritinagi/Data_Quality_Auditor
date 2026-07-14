<div align="center">

# 📊 Data Quality Auditor

### Validate • Detect • Report

A modular Python application that performs automated data quality checks on employee CSV datasets. It detects missing values, invalid records, and duplicate data while generating structured reports and detailed application logs.

</div>

---

# ✨ Features

* 📂 Reads employee data from CSV files
* 🔍 Detects missing values in selected columns
* 📧 Validates email addresses
* 🎂 Validates employee age
* 💰 Validates salary values
* 📅 Validates joining dates
* 🔁 Detects duplicate records across configurable columns
* 📄 Generates a detailed Data Quality Report
* 📝 Maintains application logs using Python Logging
* ⚠️ Handles runtime errors with exception handling
* 🧪 Includes automated testing using Pytest

---

# ⚙️ Quick Start

### Prerequisites

* Python 9.1.1
* Git (optional)

### Clone the Repository

```bash
git clone https://github.com/Pritinagi/Data_Quality_Auditor
cd data-quality-auditor
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Project

```bash
python main.py
```

### Run Tests

```bash
pytest
```

---

# 📂 Project Structure

```text
Data Quality Auditor/
│
├── data/
│
├── logs/
│
├── reports/
│
├── tests/
│   ├── __init__.py
│   └── test_validators.py
│
├── config.py
├── data_loader.py
├── logger_config.py
├── main.py
├── report_generator.py
├── validators.py
├── requirements.txt
└── README.md
```

## Module Overview

| Module                | Responsibility                              |
| --------------------- | ------------------------------------------- |
| `main.py`             | Controls the complete data quality pipeline |
| `data_loader.py`      | Loads employee data from CSV files          |
| `validators.py`       | Performs all validation checks              |
| `report_generator.py` | Generates the final quality report          |
| `logger_config.py`    | Configures application logging              |
| `config.py`           | Stores configurable project settings        |
| `tests/`              | Unit tests for validation functions         |

---

# 🔄 Project Workflow

```text
Employee CSV
      │
      ▼
 Data Loader
      │
      ▼
 Validators
 ├── Missing Values
 ├── Email Validation
 ├── Age Validation
 ├── Salary Validation
 ├── Joining Date Validation
 └── Duplicate Detection
      │
      ▼
 Report Generator
      │
      ├── Data Quality Report
      └── Application Log
```

---

# 📄 Sample Input

```csv
first_name,last_name,email,age,salary,joining_date,department
John,Doe,john@example.com,30,55000,01/10/2023,IT
Jane,,janeexample.com,17,-5000,15/14/2024,HR
```

---

# 📊 Generated Output

The project automatically creates:

### 📄 Data Quality Report

Contains:

* Dataset summary
* Total rows and columns
* Missing value summary
* Invalid email count
* Invalid age count
* Invalid salary count
* Invalid joining date count
* Duplicate values with occurrence counts

### 📝 Application Log

Logs every major step of the pipeline, including:

* CSV loading
* Validation execution
* Report generation
* Warnings
* Errors and exceptions

---

# ⚙️ Configuration

Project settings are managed through `config.py`.

You can configure:

* Input CSV file path
* Report output location
* Log file location
* Age validation limits
* Salary validation limits
* Accepted joining date range
* Date format

---

# 🧪 Testing

The project includes a comprehensive Pytest suite covering scenarios such as:

* Missing values
* Valid and invalid emails
* Age validation
* Salary validation
* Joining date validation
* Duplicate detection
* Edge cases
* Exception handling


Run all tests:

```bash
pytest
```
---


<div align="center">

**Built as a portfolio project to demonstrate Python programming and data quality validation concepts.**

</div>
