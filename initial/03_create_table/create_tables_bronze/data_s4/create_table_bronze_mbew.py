# Databricks notebook source
# MAGIC %sql
# MAGIC drop table if exists bronze.mbew ;
# MAGIC create table bronze.mbew
# MAGIC (
# MAGIC mandt string ,
# MAGIC matnr string ,
# MAGIC bwkey string ,
# MAGIC bwtar string ,
# MAGIC lvorm string ,
# MAGIC lbkum string ,
# MAGIC salk3 string ,
# MAGIC vprsv string ,
# MAGIC verpr string ,
# MAGIC stprs string ,
# MAGIC peinh string ,
# MAGIC bklas string ,
# MAGIC salkv string ,
# MAGIC vmkum string ,
# MAGIC vmsal string ,
# MAGIC vmvpr string ,
# MAGIC vmver string ,
# MAGIC vmstp string ,
# MAGIC vmpei string ,
# MAGIC vmbkl string ,
# MAGIC vmsav string ,
# MAGIC vjkum string ,
# MAGIC vjsal string ,
# MAGIC vjvpr string ,
# MAGIC vjver string ,
# MAGIC vjstp string ,
# MAGIC vjpei string ,
# MAGIC vjbkl string ,
# MAGIC vjsav string ,
# MAGIC lfgja string ,
# MAGIC lfmon string ,
# MAGIC bwtty string ,
# MAGIC stprv string ,
# MAGIC laepr string ,
# MAGIC zkprs string ,
# MAGIC zkdat string ,
# MAGIC timestamp string ,
# MAGIC bwprs string ,
# MAGIC bwprh string ,
# MAGIC vjbws string ,
# MAGIC vjbwh string ,
# MAGIC vvjsl string ,
# MAGIC vvjlb string ,
# MAGIC vvmlb string ,
# MAGIC vvsal string ,
# MAGIC zplpr string ,
# MAGIC zplp1 string ,
# MAGIC zplp2 string ,
# MAGIC zplp3 string ,
# MAGIC zpld1 string ,
# MAGIC zpld2 string ,
# MAGIC zpld3 string ,
# MAGIC pperz string ,
# MAGIC pperl string ,
# MAGIC pperv string ,
# MAGIC kalkz string ,
# MAGIC kalkl string ,
# MAGIC kalkv string ,
# MAGIC kalsc string ,
# MAGIC xlifo string ,
# MAGIC mypol string ,
# MAGIC bwph1 string ,
# MAGIC bwps1 string ,
# MAGIC abwkz string ,
# MAGIC pstat string ,
# MAGIC kaln1 string ,
# MAGIC kalnr string ,
# MAGIC bwva1 string ,
# MAGIC bwva2 string ,
# MAGIC bwva3 string ,
# MAGIC vers1 string ,
# MAGIC vers2 string ,
# MAGIC vers3 string ,
# MAGIC hrkft string ,
# MAGIC kosgr string ,
# MAGIC pprdz string ,
# MAGIC pprdl string ,
# MAGIC pprdv string ,
# MAGIC pdatz string ,
# MAGIC pdatl string ,
# MAGIC pdatv string ,
# MAGIC ekalr string ,
# MAGIC vplpr string ,
# MAGIC mlmaa string ,
# MAGIC mlast string ,
# MAGIC lplpr string ,
# MAGIC vksal string ,
# MAGIC hkmat string ,
# MAGIC sperw string ,
# MAGIC kziwl string ,
# MAGIC wlinl string ,
# MAGIC abciw string ,
# MAGIC bwspa string ,
# MAGIC lplpx string ,
# MAGIC vplpx string ,
# MAGIC fplpx string ,
# MAGIC lbwst string ,
# MAGIC vbwst string ,
# MAGIC fbwst string ,
# MAGIC eklas string ,
# MAGIC qklas string ,
# MAGIC mtuse string ,
# MAGIC mtorg string ,
# MAGIC ownpr string ,
# MAGIC xbewm string ,
# MAGIC bwpei string ,
# MAGIC mbrue string ,
# MAGIC oklas string ,
# MAGIC dummy_val_incl_eew_ps string ,
# MAGIC oippinv string ,
# MAGIC create_at timestamp ,
# MAGIC origin_file string ,
# MAGIC year_month_day string 
# MAGIC )
# MAGIC using delta
# MAGIC partitioned by (year_month_day)
# MAGIC LOCATION '/mnt/data_s4/bronze/mbew'
# MAGIC     