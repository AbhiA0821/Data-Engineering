-- Day 4: SQL Querying & Aggregations

-- SELECT
SELECT * FROM Employees;

-- Select specific columns
SELECT name, salary
FROM Employees;

-- WHERE
SELECT *
FROM Employees
WHERE salary > 50000;

-- DISTINCT
SELECT DISTINCT department
FROM Employees;

-- ORDER BY
SELECT *
FROM Employees
ORDER BY salary DESC;

-- LIKE
SELECT *
FROM Employees
WHERE name LIKE 'R%';

-- IN
SELECT *
FROM Employees
WHERE department IN ('Engineering', 'Analytics');

-- BETWEEN
SELECT *
FROM Employees
WHERE salary BETWEEN 40000 AND 60000;

-- COUNT
SELECT COUNT(*) AS total_employees
FROM Employees;

-- AVG
SELECT AVG(salary) AS average_salary
FROM Employees;

-- MIN and MAX
SELECT
    MIN(salary) AS minimum_salary,
    MAX(salary) AS maximum_salary
FROM Employees;

-- SUM
SELECT SUM(salary) AS total_salary
FROM Employees;

-- GROUP BY
SELECT
    department,
    COUNT(*) AS employee_count
FROM Employees
GROUP BY department;

-- HAVING
SELECT
    department,
    AVG(salary) AS average_salary
FROM Employees
GROUP BY department
HAVING AVG(salary) > 50000;