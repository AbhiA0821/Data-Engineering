
### 2. Create `PySpark/transformations.py`

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit


spark = (
    SparkSession.builder
    .appName("PySparkTransformations")
    .master("local[*]")
    .getOrCreate()
)

data = [
    (101, "Rahul", 35),
    (102, "Priya", 28),
    (103, "Amit", 42),
    (104, "Sneha", 31)
]

columns = ["patient_id", "name", "age"]

df = spark.createDataFrame(data, columns)

print("Original Data:")
df.show()

# SELECT
print("Selected Columns:")
df.select("patient_id", "name").show()

# FILTER
print("Patients above 30:")
df.filter(col("age") > 30).show()

# WITH COLUMN
df_new = df.withColumn("age_plus_10", col("age") + 10)

print("New Column:")
df_new.show()

# DROP
df_dropped = df_new.drop("age_plus_10")

print("After Drop:")
df_dropped.show()

# DISTINCT
print("Distinct Records:")
df.distinct().show()

# ACTIONS
print("Total Records:", df.count())

spark.stop()