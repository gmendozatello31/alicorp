# Databricks notebook source
# MAGIC %sql
# MAGIC drop table if exists bronze.zsd_a639 ;
# MAGIC create table bronze.zsd_a639
# MAGIC (
# MAGIC MANDT STRING,
# MAGIC ZSD_CAPLIC STRING,
# MAGIC ZSD_CCLCON STRING,
# MAGIC ZSD_CSOCIE STRING,
# MAGIC ZSD_CSEDE STRING,
# MAGIC ZSD_CMATER STRING,
# MAGIC ZSD_KFRST STRING,
# MAGIC ZSD_FFINVA STRING,
# MAGIC ZSD_FINIVA STRING,
# MAGIC ZSD_KBSTAT STRING,
# MAGIC ZSD_CRECON STRING,
# MAGIC 
# MAGIC CREATE_AT timestamp,
# MAGIC YEAR_MONTH_DAY string,
# MAGIC ORIGIN_FILE string
# MAGIC )
# MAGIC using delta
# MAGIC partitioned by (YEAR_MONTH_DAY)
# MAGIC LOCATION '/mnt/data_sx/bronze/zsd_a639'
# MAGIC     