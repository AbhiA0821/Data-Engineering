from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, count, max, min

spark = (
    SparkSession.builder
    .appName("PySparkAggregationsJoins")
    .master("local[*]")
    .getOrCreate()
)

patients = [
    (101, "Rahul"),
    (102, "Priya"),
    (103, "Amit")
]

vitals = [
    (101, 82, 120),
    (101, 88, 125),
    (102, 95, 130),
    (103, 76, 118)
]

patients_df = spark.createDataFrame(
    patients,
    ["patient_id", "name"]
)

vitals_df = spark.createDataFrame(
    vitals,
    ["patient_id", "heart_rate", "systolic_bp"]
)

# Aggregation
summary = vitals_df.groupBy("patient_id").agg(
    avg("heart_rate").alias("avg_heart_rate"),
    max("heart_rate").alias("max_heart_rate"),
    min("heart_rate").alias("min_heart_rate"),
    count("*").alias("reading_count")
)

summary.show()

# Inner Join
result = patients_df.join(
    summary,
    on="patient_id",
    how="inner"
)

result.show()

spark.stop()