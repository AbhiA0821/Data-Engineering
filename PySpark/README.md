<<<<<<< HEAD
# ⚡ PySpark for Data Engineering

> Learning Apache Spark with PySpark for distributed data processing, transformation, and building scalable Data Engineering pipelines.

![PySpark](https://img.shields.io/badge/PySpark-Learning-orange)
![Focus](https://img.shields.io/badge/Focus-Data%20Engineering-blue)

---

## 🎯 Objective

Learn PySpark for processing large-scale datasets and building scalable ETL pipelines.

---

## 📚 Day 1 — PySpark Fundamentals

### Apache Spark

Apache Spark is a distributed data processing framework designed to process large datasets efficiently across multiple machines.

### PySpark

PySpark is the Python API for Apache Spark. It allows Data Engineers to use Spark with Python.

---

## 🏗️ Spark Architecture

Important components:

- Driver Program
- SparkSession
- Cluster Manager
- Executors
- Tasks

Basic architecture:

```text
Application
     ↓
Driver Program
     ↓
Cluster Manager
     ↓
Executors
 ┌────┼────┐
 ↓    ↓    ↓
Task Task Task
```

The **Driver** coordinates the application, while **Executors** perform data-processing tasks.

---

## 🔥 Why PySpark for Data Engineering?

PySpark is useful for:

- Large-scale data processing
- ETL pipelines
- Data cleaning
- Data transformation
- Distributed processing
- Batch processing
- Spark SQL
- Processing CSV, JSON and Parquet data

---

## 🔄 Basic PySpark Workflow

```text
Data Source
    ↓
SparkSession
    ↓
DataFrame
    ↓
Transformations
    ↓
Actions
    ↓
Processed Data
```

---

## 💻 Topics Covered

- Introduction to Apache Spark
- Introduction to PySpark
- Distributed Computing
- Spark Architecture
- Driver & Executors
- SparkSession
- Introduction to DataFrames

---

## 🏥 Application in MedIntel

PySpark will be used in MedIntel as the main data-processing layer for:

- Processing patient vital-sign data
- Data cleaning
- Data transformation
- Data validation
- Large-scale batch processing
- Preparing processed data for analytical storage

Conceptually:

```text
Raw Vital Signs
      ↓
    PySpark
      ↓
Clean & Transform
      ↓
Validate Data
      ↓
Processed Data
      ↓
DuckDB / Analytics
```

---

## 🗓️ PySpark Learning Plan

| Day | Topic |
|-----|-------|
| 1 | Spark Fundamentals & Architecture |
| 2 | SparkSession, DataFrames & Schemas |
| 3 | Transformations & Actions |
| 4 | Data Cleaning & Column Operations |
| 5 | Aggregations & Joins |
| 6 | Spark SQL, Window Functions & Partitioning |
| 7 | Optimization & ETL Pipeline |

---

## ⏭️ Next

**Day 2 — SparkSession, DataFrames & Schemas**

---

## 🎯 Outcome

Understand how Apache Spark performs distributed data processing and how PySpark is used in modern Data Engineering pipelines.
=======
## 📚 Day 2 — DataFrames & Schemas

Today I learned how PySpark represents structured data using DataFrames and schemas.

### Topics Covered

- SparkSession
- DataFrames
- Creating DataFrames
- DataFrame columns
- Schema
- Data Types
- `show()`
- `printSchema()`
- `select()`

### DataFrame Workflow

```text
Raw Data
   ↓
SparkSession
   ↓
DataFrame
   ↓
Schema
   ↓
Select / Inspect Data



## ⏭️ Next

**Day 3 — PySpark Transformations & Actions**

- `select()`
- `filter()`
- `withColumn()`
- `drop()`
- `distinct()`
- Transformations vs Actions
- Lazy Evaluation



## 📚 Day 3 — Transformations & Actions

Today I learned how PySpark processes data using transformations and actions.

### Topics Covered

- Transformations
- Actions
- Lazy Evaluation
- `select()`
- `filter()`
- `withColumn()`
- `drop()`
- `distinct()`
- `show()`
- `count()`
- `collect()`

### Transformations

Transformations create a new DataFrame from an existing DataFrame.

Examples:

```python
df.select("name", "age")

df.filter(df.age > 30)

df.withColumn("age_plus_10", df.age + 10)

df.drop("age")


## 📚 Day 4 — Data Cleaning & Column Operations

### Topics Covered

- Handling NULL values
- `dropna()`
- `fillna()`
- `withColumn()`
- `withColumnRenamed()`
- `when()`
- `otherwise()`
- `col()`
- Removing duplicates
- Data validation

### Data Cleaning Workflow

```text
Raw Data
   ↓
Check Missing Values
   ↓
Handle NULLs
   ↓
Transform Columns
   ↓
Validate Data
   ↓
Remove Duplicates
   ↓
Clean Data

## 📚 Day 5 — Aggregations & Joins

### Topics Covered

- `groupBy()`
- `count()`
- `sum()`
- `avg()`
- `min()`
- `max()`
- Inner Join
- Left Join
- Right Join
- Outer Join

### Aggregation Workflow

```text
DataFrame
   ↓
groupBy()
   ↓
Aggregate Functions
   ↓
Summary Data


## 📚 Day 6 — Spark SQL, Window Functions & Partitioning

### Topics Covered

- Spark SQL
- Temporary Views
- SQL Queries on DataFrames
- Window Functions
- `ROW_NUMBER()`
- `RANK()`
- `DENSE_RANK()`
- `partitionBy()`
- `orderBy()`

### Spark SQL

DataFrames can be registered as temporary SQL views and queried using SQL.

```text
DataFrame
    ↓
Temporary View
    ↓
Spark SQL
    ↓
Result




## 📚 Day 7 — Optimization & ETL Pipeline

### Topics Covered

- Spark Optimization Basics
- `cache()`
- `persist()`
- Repartitioning
- Coalescing
- ETL Pipeline Structure
- Reading Data
- Transforming Data
- Writing Processed Data

### ETL Workflow

```text
Extract
   ↓
Transform
   ↓
Validate
   ↓
Aggregate
   ↓
Load