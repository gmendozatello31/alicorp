# Databricks notebook source
# MAGIC %sql
# MAGIC drop table if exists bronze.t052u ;
# MAGIC create table bronze.t052u
# MAGIC (
# MAGIC MANDT string,
# MAGIC SPRAS string,
# MAGIC ZTERM string,
# MAGIC ZTAGG string,
# MAGIC TEXT1 string,
# MAGIC 
# MAGIC CREATE_AT timestamp,
# MAGIC YEAR_MONTH string,
# MAGIC ORIGIN_FILE string
# MAGIC )
# MAGIC using delta
# MAGIC partitioned by (YEAR_MONTH)
# MAGIC LOCATION '/mnt/data_s4/bronze/t052u'
# MAGIC     