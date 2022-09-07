# Databricks notebook source
# MAGIC %sql
# MAGIC drop table if exists silver.iview ; 
# MAGIC create table silver.iview
# MAGIC (
# MAGIC FECHAS STRING,
# MAGIC CANAL STRING,
# MAGIC CADENA STRING,
# MAGIC SUB_CADENA STRING,
# MAGIC DEPARTAMENTO STRING,
# MAGIC DISTRITO STRING,
# MAGIC LOCAL STRING,
# MAGIC CLUSTER STRING,
# MAGIC CODIGO_LOCAL_ALICORP STRING,
# MAGIC LOCAL_ALICORP STRING,
# MAGIC CATEGORIA STRING,
# MAGIC FAMILIA STRING,
# MAGIC MARCA STRING,
# MAGIC VARIEDAD STRING,
# MAGIC FORMATO STRING,
# MAGIC CODIGO_DE_PRODUCTO DOUBLE,
# MAGIC MATERIAL STRING,
# MAGIC SUBNEGOCIO STRING,
# MAGIC DUENO_MARCA STRING,
# MAGIC EAN13 DOUBLE,
# MAGIC COD_CADENA STRING,
# MAGIC UNIDADES_B2B DECIMAL(22,3),
# MAGIC VALORES_COSTO_B2B DECIMAL(22,3),
# MAGIC PESO_EN_TONELADAS DECIMAL(22,3),
# MAGIC VALORES_VENTA_B2B DECIMAL(22,3),
# MAGIC VENTAS_SIN_IGV DECIMAL(22,3),
# MAGIC FACTOR_DE_CONVERSION DECIMAL(22,3),
# MAGIC PRECIOS_B2B DECIMAL(22,3),
# MAGIC CODIGO_SAP_LOCAL STRING,
# MAGIC CREATE_AT timestamp,
# MAGIC YEAR_MONTH_DAY string,
# MAGIC ORIGIN_FILE string
# MAGIC )
# MAGIC using delta
# MAGIC partitioned by (YEAR_MONTH_DAY)
# MAGIC location '/mnt/data_iview/silver/iview';