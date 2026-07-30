# SQL (Structured Query Language)

> My journey of learning SQL from fundamentals to advanced concepts for Data Engineering, Data Analytics, and real-world applications.

---

# 📖 Table of Contents

- Learning Objectives
- Introduction
- What is SQL?
- Why SQL?
- History of SQL
- Database Fundamentals
- RDBMS
- SQL vs NoSQL
- SQL Architecture
- Database Keys
- SQL in Data Engineering
- SQL in MedIntel
- Progress Tracker
- Next Topics
- References

---

# 🎯 Learning Objectives

- Understand SQL fundamentals.
- Learn relational database concepts.
- Master database design.
- Build a strong foundation for Data Engineering.
- Prepare for SQL interviews.
- Apply SQL concepts in real-world projects.

---

# 📘 Introduction

SQL (Structured Query Language) is the standard language used to communicate with relational databases.

It allows developers and data professionals to create, retrieve, update, delete, and manage structured data efficiently.

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

SQL is used because it enables efficient management of structured data.

Applications include:

- Data Engineering
- Data Analytics
- Business Intelligence
- Machine Learning
- Backend Development
- Reporting
- Dashboard Development

---

# 📜 History of SQL

- Developed by IBM in the early 1970s.
- Originally named **SEQUEL**.
- Later standardized by ANSI and ISO.
- Today it is supported by almost every relational database.

---

# 🗄 Database Fundamentals

A database is an organized collection of related data.

Examples:

- Hospital Database
- Banking Database
- Student Database
- Employee Database
- E-Commerce Database

---

# 🏛 Relational Database Management System (RDBMS)

An RDBMS stores data using tables made up of rows and columns.

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
| Relational | Non-Relational |
| Table-based | Document / Key-Value / Graph |
| Fixed Schema | Flexible Schema |
| Uses SQL | Uses Different Query Languages |
| ACID Support | BASE (depends on DB) |

---

# 🏗 SQL Architecture

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

Database Keys uniquely identify records and establish relationships between tables.

Benefits:

- Maintain Data Integrity
- Prevent Duplicate Data
- Improve Query Performance
- Establish Relationships

---

## Primary Key

A Primary Key uniquely identifies each row.

Properties:

- Cannot be NULL
- Cannot contain duplicate values
- Only one Primary Key per table

Example

| Student_ID | Name |
|------------|------|
|101|Rahul|
|102|Priya|

---

## Foreign Key

A Foreign Key creates relationships between tables.

Students

| Student_ID | Name |
|------------|------|
|101|Rahul|

Marks

| Mark_ID | Student_ID |
|----------|------------|
|1|101|

Student_ID is the Foreign Key.

---

## Candidate Key

A column that can uniquely identify a record.

Multiple Candidate Keys may exist.

One becomes the Primary Key.

---

## Alternate Key

A Candidate Key that is not selected as the Primary Key.

Example:

Primary Key → Employee_ID

Alternate Key → Email

---

## Composite Key

Two or more columns combined to uniquely identify a row.

Example:

(Student_ID, Subject_ID)

---

## Unique Key

Ensures unique values.

Unlike Primary Key:

- Usually allows one NULL (depends on the database)
- Multiple Unique Keys allowed

---

## Super Key

Any combination of columns capable of uniquely identifying a record.

Example:

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

# 📊 SQL in Data Engineering

SQL is one of the core technologies used in Data Engineering.

Typical use cases include:

- Querying large datasets
- ETL pipelines
- Data Cleaning
- Data Validation
- Data Warehousing
- Reporting
- Dashboard Development
- Data Transformation
- Data Analysis

---

# 🏥 SQL in MedIntel

MedIntel is an end-to-end Healthcare Data Engineering project.

SQL is used for:

- Creating database schemas
- Managing patient records
- Managing vital sign records
- Creating Primary & Foreign Key relationships
- Writing analytical queries
- Supporting ETL pipelines
- Dashboard reporting

Example

Patients

```
Patient_ID (Primary Key)
```

VitalSigns

```
Patient_ID (Foreign Key)
```

This relationship connects every patient's vital signs with the patient information.

---

# 📈 Progress Tracker

| Day | Topic | Status |
|------|-------------------------------|--------|
| Day 1 | SQL Fundamentals | ✅ Completed |
| Day 2 | Database Keys | ✅ Completed |
| Day 3 | SQL Constraints | ⏳ Planned |
| Day 4 | Data Types & SQL Commands | ⏳ Planned |
| Day 5 | CRUD Operations & SELECT Queries | ⏳ Planned |
| Day 6 | Functions, GROUP BY, HAVING & Joins | ⏳ Planned |
| Day 7 | Advanced SQL, Mini Project & Interview Questions | ⏳ Planned |

---

# 📅 Next Topics

- SQL Constraints
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

⭐ **Repository Goal**

Build a complete SQL handbook from beginner to advanced level while applying concepts to real-world Data Engineering projects such as **MedIntel**.