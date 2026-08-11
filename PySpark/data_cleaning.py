from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

spark = (
    SparkSession.builder
    .appName("PySparkDataCleaning")
    .master("local[*]")
    .getOrCreate()
)

data = [
    (101, "Rahul", 35, 82),
    (102, "Priya", None, 95),
    (103, "Amit", 42, None),
    (104, "Sneha", 31, 88)
]

columns = ["patient_id", "name", "age", "heart_rate"]

df = spark.createDataFrame(data, columns)

print("Original Data:")
df.show()

# Handle missing values
df_clean = df.fillna({
    "age": 0,
    "heart_rate": 0
})

# Create a status column
df_clean = df_clean.withColumn(
    "heart_rate_status",
    when(col("heart_rate") > 100, "High")
    .otherwise("Normal")
)

# Rename a column
df_clean = df_clean.withColumnRenamed(
    "heart_rate",
    "heart_rate_bpm"
)

print("Cleaned Data:")
df_clean.show()

# Remove duplicates
df_clean = df_clean.dropDuplicates()

print("Final Data:")
df_clean.show()

spark.stop()