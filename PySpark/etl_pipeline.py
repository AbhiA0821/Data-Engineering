from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg

spark = (
    SparkSession.builder
    .appName("MedIntelETL")
    .master("local[*]")
    .getOrCreate()
)

# Extract
data = [
    (101, "Rahul", 82),
    (101, "Rahul", 88),
    (102, "Priya", 95),
    (103, "Amit", 76),
    (103, "Amit", 84)
]

df = spark.createDataFrame(
    data,
    ["patient_id", "name", "heart_rate"]
)

# Transform
cleaned_df = (
    df.filter(col("heart_rate") > 0)
      .dropDuplicates()
)

summary_df = (
    cleaned_df
    .groupBy("patient_id", "name")
    .agg(
        avg("heart_rate").alias("average_heart_rate")
    )
)

# Cache when the same DataFrame is reused
summary_df.cache()

# Load / output
summary_df.show()

summary_df.write.mode("overwrite").parquet(
    "output/patient_summary"
)

spark.stop()