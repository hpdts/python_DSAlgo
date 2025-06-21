from pyspark.sql import SparkSession
from pyspark.sql.functions import col, concat_ws, avg, round


spark = SparkSession.builder.appName("Employee Department Analysis").getOrCreate()

employees = spark.read.csv("employees.csv", header=True, inferSchema=True)

departments = spark.read.csv("departments.csv", header=True, inferSchema=True)

employees = employees.withColumn("full_name", concat_ws(" ", "first_name", "last_name"))


filtered = employees.filter(col("age") > 30)

avg_salary = filtered.groupBy("dept_id").agg(round(avg("salary"),2).alias("avg_salary"))

result = avg_salary.join(departments, on="dept_id", how="left")

final = result.select("dept_name", "avg_salary")

final.show()

#final.write.mode("overwrite").csv("output/avg_salaries", header=True)

spark.stop()