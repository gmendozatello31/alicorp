# Databricks notebook source
# MAGIC %sql
# MAGIC drop table if exists bronze.dsd_pr_fbam ;
# MAGIC create table bronze.dsd_pr_fbam
# MAGIC (
# MAGIC MANDT STRING,
# MAGIC PRONR STRING,
# MAGIC SEQNR STRING,
# MAGIC VBELN STRING,
# MAGIC POSNR STRING,
# MAGIC DOC_TYPE STRING,
# MAGIC TOUR_ID STRING,
# MAGIC VBELN_INT STRING,
# MAGIC POSNR_INT STRING,
# MAGIC VBELN_REL STRING,
# MAGIC POSNR_REL STRING,
# MAGIC ZWERT STRING,
# MAGIC WAERK STRING,
# MAGIC EMSE_DC_FLAG STRING,
# MAGIC 
# MAGIC CREATE_AT TIMESTAMP,
# MAGIC YEAR_MONTH_DAY STRING,
# MAGIC ORIGIN_FILE STRING
# MAGIC )
# MAGIC using delta
# MAGIC partitioned by (YEAR_MONTH_DAY)
# MAGIC LOCATION '/mnt/data_s4/bronze/dsd_pr_fbam'