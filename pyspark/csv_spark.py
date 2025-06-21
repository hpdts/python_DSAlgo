from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Basic Example").getOrCreate()

df = spark.read.csv("data.csv", header=True, inferSchema=True)

df.printSchema()

filtered = df.filter(df["age"] > 30)

filtered.show()

print("Count:", filtered.count())

spark.stop()