-- Day 4: SQL Commands & CRUD Operations

-- CREATE
CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(50),
    salary DECIMAL(10,2)
);

-- INSERT (Create)
INSERT INTO Employees
VALUES (1, 'Rahul', 'Engineering', 50000);

INSERT INTO Employees
VALUES (2, 'Priya', 'Analytics', 55000);

INSERT INTO Employees
VALUES (3, 'Amit', 'Engineering', 60000);

-- SELECT (Read)
SELECT * FROM Employees;

-- UPDATE
UPDATE Employees
SET salary = 58000
WHERE employee_id = 2;

-- DELETE
DELETE FROM Employees
WHERE employee_id = 3;

-- ALTER
ALTER TABLE Employees
ADD email VARCHAR(100);

-- TRUNCATE
-- TRUNCATE TABLE Employees;

-- DROP
-- DROP TABLE Employees;