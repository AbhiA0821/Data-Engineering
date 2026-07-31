# 🗄️ SQL for Data Engineering

> A focused 5-day journey to strengthen SQL fundamentals, advanced querying, and practical Data Engineering skills.

![SQL](https://img.shields.io/badge/SQL-Learning-blue)
![Progress](https://img.shields.io/badge/Progress-Day%203%20of%205-orange)

---

## 🎯 Objective

Build a strong SQL foundation for Data Engineering through concepts, hands-on queries, and real-world implementation.

---

## 📚 Topics Covered

### Day 1 — SQL Fundamentals ✅

- Introduction to SQL
- DBMS & RDBMS
- SQL vs NoSQL
- SQL Architecture
- Role of SQL in Data Engineering

### Day 2 — Database Keys ✅

- Primary Key
- Foreign Key
- Candidate Key
- Alternate Key
- Composite Key
- Super Key
- Unique Key

### Day 3 — Constraints & Data Types 🟡

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

---

## 💻 Practice

```text
SQL/
├── README.md
└── practice/
    ├── database_keys.sql
    ├── constraints.sql
    └── data_types.sql
```

Hands-on SQL examples are maintained separately inside the `practice` folder.

---

## 🏥 Applied in MedIntel

SQL concepts are applied to the MedIntel Healthcare Data Engineering project for:

- Patient & VitalSigns table design
- Primary and Foreign Key relationships
- Data validation using constraints
- Analytical queries
- Data quality checks

```text
Patients
   │
   │ patient_id (PK)
   ▼
VitalSigns
   └── patient_id (FK)
```

---

## 🗓️ 5-Day SQL Roadmap

| Day | Topic | Status |
|-----|-------|--------|
| 1 | SQL Fundamentals | ✅ |
| 2 | Database Keys | ✅ |
| 3 | Constraints & Data Types | 🟡 |
| 4 | SQL Commands, CRUD & Aggregations | ⏳ |
| 5 | Joins, Subqueries, CTEs & Window Functions | ⏳ |

---

## ⏭️ Next

Complete **SQL Data Types**, followed by:

`DDL → DML → CRUD → SELECT → Filtering → Aggregations`

---

## 🎯 Outcome

By the end of this module, I will be able to write SQL queries for **data extraction, transformation, validation, aggregation, and analytical processing** in Data Engineering pipelines.