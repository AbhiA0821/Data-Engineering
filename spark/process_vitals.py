from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, max, min, count

spark = (
    SparkSession.builder
    .appName("MedIntelVitalsProcessing")
    .master("local[*]")
    .getOrCreate()
)

# Example vital-sign data
data = [
    (101, 82, 120, 80),
    (101, 88, 125, 82),
    (102, 95, 130, 85),
    (103, 76, 118, 78),
]

columns = [
    "patient_id",
    "heart_rate",
    "systolic_bp",
    "diastolic_bp"
]

df = spark.createDataFrame(data, columns)

print("Raw Vital Signs:")
df.show()

# Basic validation
clean_df = df.filter(
    (df.heart_rate > 0) &
    (df.systolic_bp > 0) &
    (df.diastolic_bp > 0)
)

# Patient-level aggregation
summary_df = clean_df.groupBy("patient_id").agg(
    avg("heart_rate").alias("avg_heart_rate"),
    max("heart_rate").alias("max_heart_rate"),
    min("heart_rate").alias("min_heart_rate"),
    count("*").alias("reading_count")
)

print("Processed Vital Signs:")
summary_df.show()

spark.stop()