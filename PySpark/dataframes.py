from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType
)

spark = (
    SparkSession.builder
    .appName("PySparkDataFrames")
    .master("local[*]")
    .getOrCreate()
)

data = [
    (101, "Rahul", 35),
    (102, "Priya", 28),
    (103, "Amit", 42)
]

schema = StructType([
    StructField("patient_id", IntegerType(), False),
    StructField("name", StringType(), False),
    StructField("age", IntegerType(), True)
])

df = spark.createDataFrame(data, schema)

print("Patient Data:")
df.show()

print("Schema:")
df.printSchema()

print("Selected Columns:")
df.select("patient_id", "name").show()

spark.stop()