from pyspark.sql import SparkSession


# Create SparkSession
spark = (
    SparkSession.builder
    .appName("PySparkBasics")
    .master("local[*]")
    .getOrCreate()
)


# Sample data
data = [
    (101, "Rahul", 35),
    (102, "Priya", 28),
    (103, "Amit", 42)
]


# Create DataFrame
columns = ["patient_id", "name", "age"]

df = spark.createDataFrame(data, columns)


# Display DataFrame
print("Patient Data:")
df.show()


# Display schema
print("DataFrame Schema:")
df.printSchema()


# Stop SparkSession
spark.stop()
