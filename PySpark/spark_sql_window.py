from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number, rank, dense_rank

spark = (
    SparkSession.builder
    .appName("SparkSQLWindow")
    .master("local[*]")
    .getOrCreate()
)

data = [
    (101, "Rahul", "Cardiology", 82),
    (102, "Priya", "Neurology", 95),
    (103, "Amit", "Cardiology", 88),
    (104, "Sneha", "Neurology", 90)
]

df = spark.createDataFrame(
    data,
    ["patient_id", "name", "department", "heart_rate"]
)

# Spark SQL
df.createOrReplaceTempView("patients")

result = spark.sql("""
    SELECT *
    FROM patients
    WHERE heart_rate > 85
""")

result.show()

# Window function
window_spec = (
    Window
    .partitionBy("department")
    .orderBy("heart_rate")
)

ranked_df = df.withColumn(
    "row_number",
    row_number().over(window_spec)
)

ranked_df = ranked_df.withColumn(
    "rank",
    rank().over(window_spec)
)

ranked_df = ranked_df.withColumn(
    "dense_rank",
    dense_rank().over(window_spec)
)

ranked_df.show()

spark.stop()