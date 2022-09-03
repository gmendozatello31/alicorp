# Databricks notebook source
# MAGIC %sql
# MAGIC drop table if exists silver.zsd_pdtmal00 ;
# MAGIC create table silver.zsd_pdtmal00
# MAGIC (
# MAGIC MANDT STRING,
# MAGIC ZSD_NINTPA STRING,
# MAGIC ZSD_NPOSIC STRING,
# MAGIC ZSD_QMATER STRING,
# MAGIC ZSD_CMATER STRING,
# MAGIC ZSD_CUNMED STRING,
# MAGIC ZSD_ITOTML DECIMAL(22,3),
# MAGIC ZSD_ITOTAL DECIMAL(22,3),
# MAGIC ZSD_CMONLO STRING,
# MAGIC ZSD_CMONED STRING,
# MAGIC ZSD_NDCREF STRING,
# MAGIC ZSD_QMATTG STRING,
# MAGIC ZSD_ITOTTG STRING,
# MAGIC ZSD_ICOTOG STRING,
# MAGIC 
# MAGIC CREATE_AT timestamp,
# MAGIC YEAR_MONTH_DAY string,
# MAGIC ORIGIN_FILE string
# MAGIC )
# MAGIC using delta
# MAGIC partitioned by (YEAR_MONTH_DAY)
# MAGIC LOCATION '/mnt/data_sx/silver/zsd_pdtmal00'
# MAGIC     