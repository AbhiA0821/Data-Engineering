# 🗄️ SQL for Data Engineering

> A focused SQL learning module covering database fundamentals, querying, data manipulation, and advanced SQL concepts used in Data Engineering.

![SQL](https://img.shields.io/badge/SQL-Completed-success)
![Focus](https://img.shields.io/badge/Focus-Data%20Engineering-blue)

---

## 🎯 Objective

Build a strong SQL foundation for Data Engineering through conceptual understanding, hands-on querying, and practical implementation.

---

## 📚 Topics Covered

### Day 1 — SQL Fundamentals ✅

- Introduction to SQL
- Database Fundamentals
- DBMS & RDBMS
- SQL vs NoSQL
- SQL Architecture
- SQL in Data Engineering

### Day 2 — Database Keys ✅

- Primary Key
- Foreign Key
- Candidate Key
- Alternate Key
- Composite Key
- Super Key
- Unique Key

📄 `database_keys.sql`

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

📄 `constraints.sql`

### Day 4 — SQL Commands, CRUD & Querying ✅

**Commands & CRUD**
- CREATE, ALTER, DROP, TRUNCATE
- INSERT, SELECT, UPDATE, DELETE

**Querying**
- WHERE
- DISTINCT
- ORDER BY
- LIKE
- IN
- BETWEEN

**Aggregations**
- COUNT()
- SUM()
- AVG()
- MIN()
- MAX()
- GROUP BY
- HAVING

📄 `sql_commands.sql`  
📄 `queries.sql`

### Day 5 — Advanced SQL ✅

**Joins**
- INNER JOIN
- LEFT JOIN
- RIGHT JOIN
- FULL OUTER JOIN
- SELF JOIN

**Advanced Concepts**
- Subqueries
- Common Table Expressions (CTEs)
- Window Functions
- PARTITION BY
- ROW_NUMBER()
- RANK()
- DENSE_RANK()

📄 `advanced_sql.sql`

---

## 💻 Hands-On Files

```text
SQL/
├── README.md
├── database_keys.sql
├── constraints.sql
├── sql_commands.sql
├── queries.sql
└── advanced_sql.sql
```

---

## 🔄 SQL in Data Engineering

SQL is used throughout Data Engineering for:

- Data Extraction
- Data Cleaning
- Data Transformation
- Data Validation
- ETL / ELT
- Data Quality Checks
- Aggregations
- Joining datasets
- Analytical Processing

```text
Raw Data
   ↓
SQL Queries
   ↓
Clean & Transform
   ↓
Join & Aggregate
   ↓
Validated Data
   ↓
Analytics / Data Pipeline
```

---

## 🏥 Applied to MedIntel

The SQL concepts learned in this module are applied to the **MedIntel Healthcare Data Engineering project** for:

- Patient and VitalSigns table design
- Primary & Foreign Key relationships
- Data validation using constraints
- Patient data retrieval
- Vital-sign filtering
- Table joins
- Aggregations
- Analytical queries
- Dashboard data preparation

```text
Patients
   │
   │ patient_id (PK)
   ▼
VitalSigns
   └── patient_id (FK)
```

---

## 💼 Key Interview Concepts

- Primary Key vs Foreign Key
- WHERE vs HAVING
- DELETE vs TRUNCATE vs DROP
- INNER JOIN vs LEFT JOIN
- Subquery vs CTE
- GROUP BY and Aggregate Functions
- ROW_NUMBER vs RANK vs DENSE_RANK
- Window Functions
- SQL execution and database fundamentals

---

## ✅ SQL Module Completed

| Day | Topic | Status |
|-----|-------|--------|
| 1 | SQL Fundamentals | ✅ |
| 2 | Database Keys | ✅ |
| 3 | Constraints & Data Types | ✅ |
| 4 | SQL Commands, CRUD & Aggregations | ✅ |
| 5 | Joins, Subqueries, CTEs & Window Functions | ✅ |

---

## 🎯 Outcome

Completed the SQL foundation required for Data Engineering, covering:

```text
Database Fundamentals
        ↓
Keys & Constraints
        ↓
CRUD & SQL Commands
        ↓
Filtering & Aggregation
        ↓
Joins
        ↓
Subqueries & CTEs
        ↓
Window Functions
        ↓
Data Engineering Applications
```

The next step is applying these SQL concepts to an end-to-end Data Engineering project and continuing with the next technologies in the learning roadmap.