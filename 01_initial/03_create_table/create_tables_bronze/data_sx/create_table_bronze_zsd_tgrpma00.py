# Databricks notebook source
# MAGIC %sql
# MAGIC drop table if exists bronze.zsd_tgrpma00 ;
# MAGIC create table bronze.zsd_tgrpma00
# MAGIC (
# MAGIC MANDT STRING,
# MAGIC ZSD_CENTOR STRING,
# MAGIC ZSD_CGRPMA STRING,
# MAGIC ZSD_NCORRE STRING,
# MAGIC ZSD_TIPPRO STRING,
# MAGIC ZSD_CCATEG STRING,
# MAGIC ZSD_CMARCA STRING,
# MAGIC ZSD_CFAMMT STRING,
# MAGIC ZSD_CVARIE STRING,
# MAGIC ZSD_CLINEA STRING,
# MAGIC ZSD_CSGMAT STRING,
# MAGIC ZSD_CJERAR STRING,
# MAGIC ZSD_CMATER STRING,
# MAGIC ZSD_QCONGR STRING,
# MAGIC ZSD_CUNMED STRING,
# MAGIC ZSD_TIPOUM STRING,
# MAGIC ZSD_LINCLU STRING,
# MAGIC ZSD_DUSCRE STRING,
# MAGIC ZSD_FCREAC STRING,
# MAGIC ZSD_DUSMOD STRING,
# MAGIC ZSD_FMODIF STRING,
# MAGIC ZSD_LACUM STRING,
# MAGIC ZSD_PACUM STRING,
# MAGIC ZSD_UNACUM STRING,
# MAGIC ZSD_DFRASE STRING,
# MAGIC ZSD_DLETRA STRING,
# MAGIC ZSD_BUKRS STRING,
# MAGIC ZSD_ZFLAGM STRING,
# MAGIC ZSD_FCLAIN STRING,
# MAGIC ZSD_FFORCL STRING,
# MAGIC ZSD_MINXCO STRING,
# MAGIC ZSD_QXMATE STRING,
# MAGIC ZSD_MINCOB STRING,
# MAGIC ZSD_UNICOB STRING,
# MAGIC ZSD_CGRMAT STRING,
# MAGIC ZSD_CLINS4 STRING,
# MAGIC ZCPLATS4 STRING,
# MAGIC ZCSPLATS4 STRING,
# MAGIC ZSD_CPACK STRING,
# MAGIC ZSD_LATRM STRING,
# MAGIC 
# MAGIC 
# MAGIC CREATE_AT timestamp,
# MAGIC YEAR_MONTH_DAY string,
# MAGIC ORIGIN_FILE string
# MAGIC )
# MAGIC using delta
# MAGIC partitioned by (YEAR_MONTH_DAY)
# MAGIC LOCATION '/mnt/data_sx/bronze/zsd_tgrpma00'
# MAGIC     