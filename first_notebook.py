# Databricks notebook source
df = spark.table("nsangana.test.patients")

# COMMAND ----------

df.count()

# COMMAND ----------

df.printSchema()

# COMMAND ----------


