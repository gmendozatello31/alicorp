-- Databricks notebook source
-- MAGIC %sql
-- MAGIC drop table if exists datagov.registros_observados_anterior_stg ;
-- MAGIC create table datagov.registros_observados_anterior_stg 
-- MAGIC (
-- MAGIC  frente string,
-- MAGIC  fecha_proceso date,
-- MAGIC  id_control string,
-- MAGIC  dbkey  string
-- MAGIC )
-- MAGIC using delta
-- MAGIC partitioned by (frente)
-- MAGIC 
-- MAGIC LOCATION '/mnt/data_governance/calidad-de-datos/data/registros_observados_anterior_stg'