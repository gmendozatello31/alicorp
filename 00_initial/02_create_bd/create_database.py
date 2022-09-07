# Databricks notebook source
# MAGIC  %sql
# MAGIC DROP DATABASE IF EXISTS bronze CASCADE;
# MAGIC create database bronze;
# MAGIC 
# MAGIC DROP DATABASE IF EXISTS silver CASCADE;
# MAGIC create database silver;
# MAGIC 
# MAGIC DROP DATABASE IF EXISTS gold CASCADE;
# MAGIC create database gold;
# MAGIC 
# MAGIC DROP DATABASE IF EXISTS dev CASCADE;
# MAGIC create database dev;
# MAGIC 
# MAGIC DROP DATABASE IF EXISTS uf CASCADE;
# MAGIC create database uf;

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP DATABASE IF EXISTS datagov CASCADE;
# MAGIC create database datagov;

# COMMAND ----------


