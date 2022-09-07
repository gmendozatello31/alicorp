# Databricks notebook source
# MAGIC %sql
# MAGIC drop table if exists bronze.t001w ;
# MAGIC create table bronze.t001w
# MAGIC (
# MAGIC MANDT string,
# MAGIC WERKS string,
# MAGIC NAME1 string,
# MAGIC BWKEY string,
# MAGIC KUNNR string,
# MAGIC LIFNR string,
# MAGIC FABKL string,
# MAGIC NAME2 string,
# MAGIC STRAS string,
# MAGIC PFACH string,
# MAGIC PSTLZ string,
# MAGIC ORT01 string,
# MAGIC EKORG string,
# MAGIC VKORG string,
# MAGIC CHAZV string,
# MAGIC KKOWK string,
# MAGIC KORDB string,
# MAGIC BEDPL string,
# MAGIC LAND1 string,
# MAGIC REGIO string,
# MAGIC COUNC string,
# MAGIC CITYC string,
# MAGIC ADRNR string,
# MAGIC IWERK string,
# MAGIC TXJCD string,
# MAGIC VTWEG string,
# MAGIC SPART string,
# MAGIC SPRAS string,
# MAGIC WKSOP string,
# MAGIC AWSLS string,
# MAGIC CHAZV_OLD string,
# MAGIC VLFKZ string,
# MAGIC BZIRK string,
# MAGIC ZONE1 string,
# MAGIC TAXIW string,
# MAGIC BZQHL string,
# MAGIC LET01 string,
# MAGIC LET02 string,
# MAGIC LET03 string,
# MAGIC TXNAM_MA1 string,
# MAGIC TXNAM_MA2 string,
# MAGIC TXNAM_MA3 string,
# MAGIC BETOL string,
# MAGIC J_1BBRANCH string,
# MAGIC VTBFI string,
# MAGIC FPRFW string,
# MAGIC ACHVM string,
# MAGIC DVSART string,
# MAGIC NODETYPE string,
# MAGIC NSCHEMA string,
# MAGIC PKOSA string,
# MAGIC MISCH string,
# MAGIC MGVUPD string,
# MAGIC VSTEL string,
# MAGIC MGVLAUPD string,
# MAGIC MGVLAREVAL string,
# MAGIC SOURCING string,
# MAGIC NO_DEFAULT_BATCH_MANAGEMENT string,
# MAGIC FSH_MG_ARUN_REQ string,
# MAGIC FSH_SEAIM string,
# MAGIC FSH_BOM_MAINTENANCE string,
# MAGIC FSH_GROUP_PR string,
# MAGIC ARUN_FIX_BATCH string,
# MAGIC OILIVAL string,
# MAGIC OIHVTYPE string,
# MAGIC OIHCREDIPI string,
# MAGIC STORETYPE string,
# MAGIC DEP_STORE string,
# MAGIC CREATE_AT timestamp,
# MAGIC ORIGIN_FILE string,
# MAGIC YEAR_MONTH_DAY string
# MAGIC )
# MAGIC using delta
# MAGIC partitioned by (YEAR_MONTH_DAY)
# MAGIC LOCATION '/mnt/data_s4/bronze/t001w'
# MAGIC     