-- Databricks notebook source
-- MAGIC %sql
-- MAGIC drop table if exists bronze.csks ;
-- MAGIC create table bronze.csks
-- MAGIC (
-- MAGIC mandt string,
-- MAGIC kokrs string,
-- MAGIC kostl string,
-- MAGIC datbi string,
-- MAGIC datab string,
-- MAGIC bkzkp string,
-- MAGIC pkzkp string,
-- MAGIC bukrs string,
-- MAGIC gsber string,
-- MAGIC kosar string,
-- MAGIC verak string,
-- MAGIC verak_user string,
-- MAGIC waers string,
-- MAGIC kalsm string,
-- MAGIC txjcd string,
-- MAGIC prctr string,
-- MAGIC werks string,
-- MAGIC logsystem string,
-- MAGIC ersda string,
-- MAGIC usnam string,
-- MAGIC bkzks string,
-- MAGIC bkzer string,
-- MAGIC bkzob string,
-- MAGIC pkzks string,
-- MAGIC pkzer string,
-- MAGIC vmeth string,
-- MAGIC mgefl string,
-- MAGIC abtei string,
-- MAGIC nkost string,
-- MAGIC kvewe string,
-- MAGIC kappl string,
-- MAGIC koszschl string,
-- MAGIC land1 string,
-- MAGIC anred string,
-- MAGIC name1 string,
-- MAGIC name2 string,
-- MAGIC name3 string,
-- MAGIC name4 string,
-- MAGIC ort01 string,
-- MAGIC ort02 string,
-- MAGIC stras string,
-- MAGIC pfach string,
-- MAGIC pstlz string,
-- MAGIC pstl2 string,
-- MAGIC regio string,
-- MAGIC spras string,
-- MAGIC telbx string,
-- MAGIC telf1 string,
-- MAGIC telf2 string,
-- MAGIC telfx string,
-- MAGIC teltx string,
-- MAGIC telx1 string,
-- MAGIC datlt string,
-- MAGIC drnam string,
-- MAGIC khinr string,
-- MAGIC cckey string,
-- MAGIC kompl string,
-- MAGIC stakz string,
-- MAGIC objnr string,
-- MAGIC funkt string,
-- MAGIC afunk string,
-- MAGIC cpi_templ string,
-- MAGIC cpd_templ string,
-- MAGIC func_area string,
-- MAGIC sci_templ string,
-- MAGIC scd_templ string,
-- MAGIC ski_templ string,
-- MAGIC skd_templ string,
-- MAGIC eew_csks_ps_dummy string,
-- MAGIC vname string,
-- MAGIC recid string,
-- MAGIC etype string,
-- MAGIC jv_otype string,
-- MAGIC jv_jibcl string,
-- MAGIC jv_jibsa string,
-- MAGIC ferc_ind string,
-- MAGIC create_at timestamp ,
-- MAGIC origin_file string ,
-- MAGIC year_month_day string 
-- MAGIC )
-- MAGIC using delta
-- MAGIC partitioned by (year_month_day)
-- MAGIC LOCATION '/mnt/data_s4/bronze/csks'
