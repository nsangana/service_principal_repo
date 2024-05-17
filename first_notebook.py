# Databricks notebook source
df = spark.table("nsangana_catalog.hls_patient_readmission.patient_encrypted")

# COMMAND ----------

df.count()

# COMMAND ----------

df.printSchema()

# COMMAND ----------


