import duckdb

con = duckdb.connect("healthcare.duckdb")

# Aggregation
result = con.execute("""
SELECT
    city,
    COUNT(*) AS total_patients,
    AVG(age) AS average_age
FROM patients
GROUP BY city
ORDER BY average_age DESC
""").fetchdf()

print(result)

con.close()