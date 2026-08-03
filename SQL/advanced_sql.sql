-- =========================================
-- Day 5: Advanced SQL
-- Joins, Subqueries, CTEs & Window Functions
-- =========================================

CREATE TABLE Departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100)
);

CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100),
    salary DECIMAL(10,2),
    department_id INT,
    manager_id INT,
    FOREIGN KEY (department_id)
        REFERENCES Departments(department_id)
);

-- Sample Data

INSERT INTO Departments VALUES
(1, 'Engineering'),
(2, 'Analytics'),
(3, 'HR');

INSERT INTO Employees VALUES
(1, 'Rahul', 60000, 1, NULL),
(2, 'Priya', 55000, 2, 1),
(3, 'Amit', 50000, 1, 1),
(4, 'Sneha', 45000, 2, 2);


-- =========================================
-- JOINS
-- =========================================

-- INNER JOIN
SELECT
    e.employee_name,
    d.department_name
FROM Employees e
INNER JOIN Departments d
ON e.department_id = d.department_id;


-- LEFT JOIN
SELECT
    e.employee_name,
    d.department_name
FROM Employees e
LEFT JOIN Departments d
ON e.department_id = d.department_id;


-- RIGHT JOIN
SELECT
    e.employee_name,
    d.department_name
FROM Employees e
RIGHT JOIN Departments d
ON e.department_id = d.department_id;


-- FULL OUTER JOIN
SELECT
    e.employee_name,
    d.department_name
FROM Employees e
FULL OUTER JOIN Departments d
ON e.department_id = d.department_id;


-- SELF JOIN
SELECT
    e.employee_name AS employee,
    m.employee_name AS manager
FROM Employees e
LEFT JOIN Employees m
ON e.manager_id = m.employee_id;


-- =========================================
-- SUBQUERY
-- =========================================

-- Employees earning more than average salary

SELECT employee_name, salary
FROM Employees
WHERE salary > (
    SELECT AVG(salary)
    FROM Employees
);


-- =========================================
-- CTE
-- =========================================

WITH HighSalaryEmployees AS (
    SELECT employee_name, salary
    FROM Employees
    WHERE salary > 50000
)

SELECT *
FROM HighSalaryEmployees;


-- =========================================
-- WINDOW FUNCTIONS
-- =========================================

-- ROW_NUMBER

SELECT
    employee_name,
    department_id,
    salary,

    ROW_NUMBER() OVER (
        PARTITION BY department_id
        ORDER BY salary DESC
    ) AS row_number

FROM Employees;


-- RANK

SELECT
    employee_name,
    salary,

    RANK() OVER (
        ORDER BY salary DESC
    ) AS salary_rank

FROM Employees;


-- DENSE_RANK

SELECT
    employee_name,
    salary,

    DENSE_RANK() OVER (
        ORDER BY salary DESC
    ) AS dense_salary_rank

FROM Employees;