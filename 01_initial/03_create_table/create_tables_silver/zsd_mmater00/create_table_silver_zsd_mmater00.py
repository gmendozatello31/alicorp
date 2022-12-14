# Databricks notebook source
# MAGIC %sql
# MAGIC drop table if exists silver.zsd_mmater00 ;
# MAGIC create table silver.zsd_mmater00
# MAGIC (
# MAGIC MANDT STRING,
# MAGIC ZSD_CMATER STRING,
# MAGIC ZSD_SMATER STRING,
# MAGIC ZSD_DCORTA STRING,
# MAGIC ZSD_DLARGA STRING,
# MAGIC ZSD_PNETO DECIMAL(22,3),
# MAGIC ZSD_PBRUTO DECIMAL(22,3),
# MAGIC ZSD_CUNMPE STRING,
# MAGIC ZSD_VMATER DECIMAL(22,3),
# MAGIC ZSD_CUNMVO STRING,
# MAGIC ZSD_NFUVTA STRING,
# MAGIC ZSD_LPERCE STRING,
# MAGIC ZSD_CUNMBA STRING,
# MAGIC ZSD_CUNMVT STRING,
# MAGIC ZSD_CEANMB DECIMAL(22,3),
# MAGIC ZSD_CEANMV DECIMAL(22,3),
# MAGIC ZSD_CTPMAT STRING,
# MAGIC ZSD_CJERAR STRING,
# MAGIC ZSD_CGRMAT STRING,
# MAGIC ZSD_CFAMMT STRING,
# MAGIC ZSD_CMARCA STRING,
# MAGIC ZSD_CCATEG STRING,
# MAGIC ZSD_CMRZTE STRING,
# MAGIC ZSD_CMRZDO STRING,
# MAGIC ZSD_CREGIM STRING,
# MAGIC ZSD_CSGMAT STRING,
# MAGIC ZSD_QMINVT STRING,
# MAGIC ZSD_QMINEN STRING,
# MAGIC ZSD_CVARIE STRING,
# MAGIC ZSD_CLINEA STRING,
# MAGIC ZSD_LSERDI STRING,
# MAGIC ZSD_LCOMBV STRING,
# MAGIC ZSD_CCNALM STRING,
# MAGIC ZSD_LSERIA STRING,
# MAGIC ZSD_DUSCRE STRING,
# MAGIC ZSD_FCREAC STRING,
# MAGIC ZSD_DUSMOD STRING,
# MAGIC ZSD_FMODIF STRING,
# MAGIC ZSD_LMODIF STRING,
# MAGIC ZSD_CMUNDO STRING,
# MAGIC ZSD_CGRART STRING,
# MAGIC ZSD_CUNSPSC STRING,
# MAGIC ZSD_CJERS4 STRING,
# MAGIC ZSD_CFAMS4 STRING,
# MAGIC ZSD_CMARS4 STRING,
# MAGIC ZSD_CCATS4 STRING,
# MAGIC ZSD_CVARS4 STRING,
# MAGIC ZSD_CLINS4 STRING,
# MAGIC ZSD_CGRMAS4 STRING,
# MAGIC ZSD_CUNMBAS4 STRING,
# MAGIC ZSD_CUNMVTS4 STRING,
# MAGIC ZSD_CPLATS4 STRING,
# MAGIC ZSD_CSPLATS4 STRING,
# MAGIC 
# MAGIC 
# MAGIC CREATE_AT timestamp,
# MAGIC YEAR_MONTH_DAY string,
# MAGIC ORIGIN_FILE string
# MAGIC )
# MAGIC using delta
# MAGIC partitioned by (YEAR_MONTH_DAY)
# MAGIC LOCATION '/mnt/data_sx/silver/zsd_mmater00'
# MAGIC     
