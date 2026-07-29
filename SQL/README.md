# SQL (Structured Query Language)

> My journey of learning SQL from fundamentals to advanced concepts for Data Engineering, Data Analytics, and real-world applications.

---

# 📖 Table of Contents

- Introduction
- Learning Objectives
- What is SQL?
- Why SQL?
- History of SQL
- Database Fundamentals
- RDBMS
- SQL vs NoSQL
- SQL Architecture
- Database Keys
- SQL in MedIntel
- Progress Tracker
- Next Topics
- References

---

# 🎯 Learning Objectives

- Understand SQL fundamentals.
- Learn relational database concepts.
- Build a strong foundation for Data Engineering.
- Prepare for SQL interviews.
- Apply SQL concepts in real-world projects like MedIntel.

---

# 📘 Introduction

SQL (Structured Query Language) is the standard language used to communicate with relational databases.

It allows users to create, retrieve, update, delete, and manage data efficiently.

SQL is one of the most important skills for Data Engineers, Data Analysts, Backend Developers, and Database Administrators.

---

# ❓ What is SQL?

SQL stands for **Structured Query Language**.

It is used to:

- Store data
- Retrieve data
- Update records
- Delete records
- Create databases
- Create tables
- Manage relational databases

---

# 💡 Why SQL?

SQL helps organizations efficiently manage and analyze large volumes of structured data.

It is widely used in:

- Data Engineering
- Data Analytics
- Business Intelligence
- Machine Learning
- Backend Development
- Reporting
- Dashboard Development

---

# 📜 History of SQL

- Developed by IBM during the early 1970s.
- Originally called **SEQUEL**.
- Standardized by ANSI and ISO.
- Today almost every relational database supports SQL.

---

# 🗄 Database Fundamentals

A database is an organized collection of data that can be easily accessed, managed, and updated.

Examples:

- Hospital Database
- Student Database
- Banking Database
- E-Commerce Database
- Employee Database

---

# 🏛 Relational Database Management System (RDBMS)

An RDBMS stores data in tables consisting of rows and columns.

Popular RDBMS:

- MySQL
- PostgreSQL
- Oracle Database
- Microsoft SQL Server
- SQLite
- DuckDB

---

# ⚖ SQL vs NoSQL

| SQL | NoSQL |
|------|--------|
| Relational | Non-relational |
| Table-based | Document / Key-Value / Graph |
| Fixed Schema | Flexible Schema |
| SQL Language | Different Query Languages |
| ACID Support | BASE (varies by database) |

---

# 🏗 SQL Architecture

Basic SQL Workflow

```
User

↓

SQL Query

↓

Database Server

↓

Query Processing

↓

Result Returned
```

---

# 🔑 Database Keys

Database Keys are attributes (columns) used to uniquely identify records and establish relationships between tables.

Keys help maintain:

- Data Integrity
- Data Consistency
- Relationships
- Faster Searching
- No Duplicate Records

---

## 1️⃣ Primary Key

A Primary Key uniquely identifies every row in a table.

### Features

- Cannot be NULL
- Cannot contain duplicate values
- Only one Primary Key per table

Example

| Student_ID | Name |
|------------|------|
|101|Rahul|
|102|Priya|

Student_ID is the Primary Key.

---

## 2️⃣ Foreign Key

A Foreign Key links one table with another.

Example

Students

| Student_ID | Name |
|------------|------|
|101|Rahul|

Marks

| Mark_ID | Student_ID |
|----------|------------|
|1|101|

Student_ID in Marks is the Foreign Key.

---

## 3️⃣ Candidate Key

A Candidate Key is any column that can uniquely identify a record.

A table may have multiple Candidate Keys.

One becomes the Primary Key.

---

## 4️⃣ Alternate Key

Candidate Keys that are not selected as the Primary Key are called Alternate Keys.

Example

Primary Key → Employee_ID

Alternate Key → Email

---

## 5️⃣ Composite Key

A Composite Key is formed using two or more columns together.

Example

(Student_ID, Subject_ID)

---

## 6️⃣ Unique Key

A Unique Key ensures unique values.

Unlike Primary Key:

- Usually allows one NULL value
- Multiple Unique Keys can exist

---

## 7️⃣ Super Key

A Super Key is any combination of columns that uniquely identifies a row.

Example

- Employee_ID
- Employee_ID + Name
- Employee_ID + Department

---

# 🔄 Relationship Between Keys

```
Super Key
│
├── Candidate Key
│      │
│      ├── Primary Key
│      │
│      └── Alternate Key
│
Foreign Key
Composite Key
Unique Key
```

---

# 💻 SQL Example

```sql
CREATE TABLE Students (

Student_ID INT PRIMARY KEY,

Name VARCHAR(50),

Email VARCHAR(100) UNIQUE

);

CREATE TABLE Marks (

Mark_ID INT PRIMARY KEY,

Student_ID INT,

Marks INT,

FOREIGN KEY(Student_ID)
REFERENCES Students(Student_ID)

);
```

---

# 🏥 SQL in MedIntel

In the MedIntel project, SQL is used for:

- Creating database tables
- Designing relational schemas
- Managing patient records
- Managing vital sign records
- Creating Primary and Foreign Key relationships
- Retrieving patient information
- Joining multiple healthcare tables
- Building dashboards
- Generating reports
- Supporting ETL pipelines

Example:

Patients Table

```
Patient_ID (Primary Key)
```

VitalSigns Table

```
Patient_ID (Foreign Key)
```

This relationship connects each patient's vital sign records with the corresponding patient.

---

# 💼 Interview Questions

### Q1. What is a Primary Key?

A Primary Key uniquely identifies every record in a table.

---

### Q2. Can a Primary Key contain NULL values?

No.

---

### Q3. Difference between Primary Key and Unique Key?

Primary Key

- No NULL values
- Only one per table

Unique Key

- Allows one NULL (database dependent)
- Multiple Unique Keys allowed

---

### Q4. What is a Foreign Key?

A Foreign Key creates a relationship between two tables.

---

### Q5. What is a Composite Key?

A Composite Key is made using two or more columns together.

---

# 📈 Progress Tracker

| Day | Topic | Status |
|------|------------------------------|--------|
| Day 1 | SQL Fundamentals | ✅ |
| Day 2 | Database Keys | ✅ |
| Day 3 | Constraints | ⏳ |
| Day 4 | SQL Data Types & SQL Commands | ⏳ |
| Day 5 | CRUD, SELECT & Filtering | ⏳ |
| Day 6 | Functions, GROUP BY & Joins | ⏳ |
| Day 7 | Advanced SQL + Interview + Mini Project | ⏳ |

---

# 📅 Next Topics

- Constraints
- SQL Data Types
- DDL Commands
- DML Commands
- DCL Commands
- TCL Commands

---

# 📚 References

- SQL Documentation
- MySQL Documentation
- PostgreSQL Documentation
- DuckDB Documentation
- Microsoft SQL Server Documentation

---

⭐ **Repository Goal:** Build a complete SQL handbook from beginner to advanced level while applying concepts in the MedIntel Data Engineering project.