from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("HelloWorld").getOrCreate()

# Create a simple RDD (Resilient Distributed Dataset) with a list of numbers
data = [1, 2, 3, 4, 5]
rdd = spark.sparkContext.parallelize(data)

# Perform a simple operation: Calculate the sum of the numbers in the RDD
sum_result = rdd.reduce(lambda a, b: a + b)

print(f"Sum of the numbers in the RDD: {sum_result}")

# Stop the SparkSession
spark.stop()