import duckdb

# Connect to a persistent DuckDB database
con = duckdb.connect("healthcare.duckdb")

# Create table
con.execute("""
CREATE TABLE IF NOT EXISTS patients (
    patient_id INTEGER,
    name VARCHAR,
    age INTEGER,
    city VARCHAR
)
""")

# Insert sample records
con.execute("""
INSERT INTO patients VALUES
(101, 'Rahul', 35, 'Pune'),
(102, 'Priya', 28, 'Mumbai'),
(103, 'Amit', 42, 'Kolhapur')
""")

# Query data
result = con.execute("""
SELECT *
FROM patients
WHERE age > 30
""").fetchall()

for row in result:
    print(row)

con.close()