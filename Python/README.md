# 🐍 Python for Data Engineering

> Learning Python for data processing, file handling, automation, and building Data Engineering pipelines.

![Python](https://img.shields.io/badge/Python-Data%20Engineering-blue)
![Status](https://img.shields.io/badge/Status-In%20Progress-orange)

---

## 🎯 Objective

Learn practical Python concepts required for Data Engineering and apply them to data processing and ETL workflows.

---

## 📚 Topics Covered

### Day 6 — Python for Data Engineering 🟡

- File Handling
- Reading & Writing Files
- CSV Processing
- JSON Processing
- Functions
- Exception Handling
- Introduction to Data Processing

📄 `file_handling.py`

---

## 💻 File Handling

Python can be used to read and write different data formats commonly found in Data Engineering.

### CSV

```python
import csv

with open("patients.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```

### JSON

```python
import json

with open("patient.json", "r") as file:
    data = json.load(file)

print(data)
```

---

## 🔄 Python in Data Engineering

Python is commonly used for:

- Data Ingestion
- File Processing
- Data Cleaning
- Data Transformation
- Data Validation
- Automation
- ETL Pipelines
- Database Integration

Typical workflow:

```text
Data Source
    ↓
Python
    ↓
Read Data
    ↓
Clean / Transform
    ↓
Validate
    ↓
Load Data
```

---

## 🏥 Application in MedIntel

Python is used in the MedIntel project for:

- Generating patient vital-sign data
- Processing healthcare data
- Data validation
- Pipeline logic
- Connecting different Data Engineering components

---

## 📂 Files

```text
Python/
├── README.md
├── file_handling.py
├── main.py
├── pyproject.toml
└── .python-version
```

The project environment is managed using `uv`.

---

## ⏭️ Next

The next implementation will focus on:

- Pandas
- Data Cleaning
- Extract, Transform, Load (ETL)
- Building a basic Python ETL pipeline

📄 Upcoming: `etl_basics.py`

---

## 🎯 Outcome

Use Python to **read, process, validate, transform, and prepare data** for Data Engineering pipelines.