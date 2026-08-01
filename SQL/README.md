# 🗄️ SQL for Data Engineering

> A focused SQL learning journey covering database fundamentals, querying, data manipulation, and advanced SQL concepts required for Data Engineering.

![SQL](https://img.shields.io/badge/SQL-Learning-blue)
![Progress](https://img.shields.io/badge/Progress-Day%204%20of%205-success)

---

## 🎯 Objective

Build a strong SQL foundation for Data Engineering through conceptual understanding, hands-on queries, and real-world implementation.

---

## 📚 Topics Covered

### Day 1 — SQL Fundamentals ✅

- Introduction to SQL
- Database Fundamentals
- DBMS & RDBMS
- SQL vs NoSQL
- SQL Architecture
- SQL in Data Engineering

---

### Day 2 — Database Keys ✅

- Primary Key
- Foreign Key
- Candidate Key
- Alternate Key
- Composite Key
- Super Key
- Unique Key

📄 Practice: `database_keys.sql`

---

### Day 3 — Constraints & Data Types ✅

**Constraints**
- NOT NULL
- UNIQUE
- PRIMARY KEY
- FOREIGN KEY
- CHECK
- DEFAULT

**Data Types**
- INT, BIGINT
- DECIMAL, FLOAT
- CHAR, VARCHAR
- BOOLEAN
- DATE, TIME, TIMESTAMP

📄 Practice: `constraints.sql`

---

### Day 4 — SQL Commands, CRUD & Querying ✅

**DDL**
- CREATE
- ALTER
- DROP
- TRUNCATE

**DML & CRUD**
- INSERT
- SELECT
- UPDATE
- DELETE

**Querying & Filtering**
- SELECT
- WHERE
- DISTINCT
- ORDER BY
- LIKE
- IN
- BETWEEN

**Aggregate Functions**
- COUNT()
- SUM()
- AVG()
- MIN()
- MAX()
- GROUP BY
- HAVING

📄 Practice:
- `sql_commands.sql`
- `queries.sql`

---

## 💻 SQL Files

```text
SQL/
│
├── README.md
├── database_keys.sql
├── constraints.sql
├── sql_commands.sql
└── queries.sql
```

Each SQL file contains hands-on implementations of the concepts documented in this README.

---

## 🔄 SQL in Data Engineering

SQL is commonly used by Data Engineers for:

- Data Extraction
- Data Cleaning
- Data Transformation
- Data Validation
- ETL / ELT Pipelines
- Data Quality Checks
- Data Aggregation
- Data Warehousing
- Analytical Queries

Typical workflow:

```text
Raw Data
   ↓
SQL Queries
   ↓
Filtering & Cleaning
   ↓
Transformation
   ↓
Aggregation
   ↓
Processed Data
```

---

## 🏥 Applied to MedIntel

SQL concepts learned during this module are applied to the **MedIntel Healthcare Data Engineering project**.

Examples include:

- Designing `Patients` and `VitalSigns` tables
- Primary and Foreign Key relationships
- Data validation using constraints
- Retrieving patient records
- Filtering vital-sign data
- Aggregating healthcare data
- Generating dashboard-ready queries

Example relationship:

```text
Patients
   │
   │ patient_id (PK)
   ▼
VitalSigns
   └── patient_id (FK)
```

After completing the SQL module, the learned concepts will be implemented together in the MedIntel data pipeline.

---

## 💼 Key Interview Concepts

**Primary Key vs Foreign Key**  
A Primary Key uniquely identifies a record, while a Foreign Key establishes a relationship with another table.

**WHERE vs HAVING**  
`WHERE` filters rows before aggregation, while `HAVING` filters groups after `GROUP BY`.

**DELETE vs TRUNCATE vs DROP**
- `DELETE` removes selected rows.
- `TRUNCATE` removes all rows while keeping the table structure.
- `DROP` removes the table itself.

**GROUP BY**  
Groups rows with common values so aggregate functions can be applied to each group.

---

## 🗓️ 5-Day SQL Roadmap

| Day | Topic | Status |
|-----|-------|--------|
| Day 1 | SQL Fundamentals | ✅ |
| Day 2 | Database Keys | ✅ |
| Day 3 | Constraints & Data Types | ✅ |
| Day 4 | SQL Commands, CRUD, Queries & Aggregations | ✅ |
| Day 5 | Joins, Subqueries, CTEs & Window Functions | ⏳ |

---

## ⏭️ Day 5 — Advanced SQL

The final SQL learning day will cover:

- INNER JOIN
- LEFT JOIN
- RIGHT JOIN
- FULL OUTER JOIN
- Self Join
- Subqueries
- Common Table Expressions (CTEs)
- Window Functions
- ROW_NUMBER()
- RANK()
- DENSE_RANK()
- PARTITION BY

A final `advanced_sql.sql` file will contain the practical implementation.

---

## 🎯 Expected Outcome

After completing this SQL module, I will be able to use SQL for:

**Data Retrieval → Filtering → Transformation → Aggregation → Joining → Analytical Processing**

These skills provide the SQL foundation required for building Data Engineering pipelines.