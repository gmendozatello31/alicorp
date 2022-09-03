# Databricks notebook source
# MAGIC %sql
# MAGIC drop table if exists gold.zsd_pdgdcc00 ;
# MAGIC create table gold.zsd_pdgdcc00
# MAGIC (
# MAGIC MANDT STRING
# MAGIC ,ZSD_NDFACT STRING
# MAGIC ,ZSD_NPREIM STRING
# MAGIC ,ZSD_SDFACT STRING
# MAGIC ,ZSD_LLQNEX STRING
# MAGIC ,ZSD_LPEDEX STRING
# MAGIC ,ZSD_CMOTIV STRING
# MAGIC ,ZSD_FEMISI STRING
# MAGIC ,ZSD_FVENCI STRING
# MAGIC ,ZSD_FREPAR STRING
# MAGIC ,ZSD_HREPAR STRING
# MAGIC ,ZSD_FLIQUI STRING
# MAGIC ,ZSD_LIMPRE STRING
# MAGIC ,ZSD_LREQGR STRING
# MAGIC ,ZSD_CREAGR STRING
# MAGIC ,ZSD_LPERCE STRING
# MAGIC ,ZSD_VPERCE STRING
# MAGIC ,ZSD_CTPDOC STRING
# MAGIC ,ZSD_CTERRI STRING
# MAGIC ,ZSD_CTRANS STRING
# MAGIC ,ZSD_CENTRE STRING
# MAGIC ,ZSD_CDCFAS STRING
# MAGIC ,ZSD_CPEDID STRING
# MAGIC ,ZSD_CCLPED STRING
# MAGIC ,ZSD_FPEDID STRING
# MAGIC ,ZSD_CPERSO STRING
# MAGIC ,ZSD_CMOTAN STRING
# MAGIC ,ZSD_CCLIEN STRING
# MAGIC ,ZSD_CINTER STRING
# MAGIC ,ZSD_CPAIS STRING
# MAGIC ,ZSD_CCNPAG STRING
# MAGIC ,ZSD_KNUMV STRING
# MAGIC ,ZSD_PBRUTO DECIMAL(22,3)
# MAGIC ,ZSD_PNETO DECIMAL(22,3)
# MAGIC ,ZSD_CUNMPE STRING
# MAGIC ,ZSD_VOLFAC DECIMAL(22,3)
# MAGIC ,ZSD_CUNMVO STRING
# MAGIC ,ZSD_IBRUTO DECIMAL(22,3)
# MAGIC ,ZSD_IDESCT DECIMAL(22,3)
# MAGIC ,ZSD_IRECAR STRING
# MAGIC ,ZSD_IIMPUE DECIMAL(22,3)
# MAGIC ,ZSD_INETO DECIMAL(22,3)
# MAGIC ,ZSD_INEACT DECIMAL(22,3)
# MAGIC ,ZSD_CMONED STRING
# MAGIC ,ZSD_IBRUML DECIMAL(22,3)
# MAGIC ,ZSD_IDESML DECIMAL(22,3)
# MAGIC ,ZSD_IRECML STRING
# MAGIC ,ZSD_IIMPML DECIMAL(22,3)
# MAGIC ,ZSD_INETML DECIMAL(22,3)
# MAGIC ,ZSD_ITPCAM STRING
# MAGIC ,ZSD_TTAX1 STRING
# MAGIC ,ZSD_VTAX1 STRING
# MAGIC ,ZSD_TTAX2 STRING
# MAGIC ,ZSD_VTAX2 DECIMAL(22,3)
# MAGIC ,ZSD_TTAX3 STRING
# MAGIC ,ZSD_VTAX3 STRING
# MAGIC ,ZSD_TTAX4 STRING
# MAGIC ,ZSD_VTAX4 STRING
# MAGIC ,ZSD_TTAX5 STRING
# MAGIC ,ZSD_VTAX5 STRING
# MAGIC ,ZSD_TTAX6 STRING
# MAGIC ,ZSD_VTAX6 STRING
# MAGIC ,ZSD_TTAX7 STRING
# MAGIC ,ZSD_VTAX7 STRING
# MAGIC ,ZSD_TTAX8 STRING
# MAGIC ,ZSD_VTAX8 STRING
# MAGIC ,ZSD_TTAX9 STRING
# MAGIC ,ZSD_VTAX9 STRING
# MAGIC ,ZSD_INAFEC DECIMAL(22,3)
# MAGIC ,ZSD_CMONLO STRING
# MAGIC ,ZSD_CSOCIE STRING
# MAGIC ,ZSD_CSEDE STRING
# MAGIC ,ZSD_CCENTR STRING
# MAGIC ,ZSD_CPUEXP STRING
# MAGIC ,ZSD_COFVTA STRING
# MAGIC ,ZSD_CREGCL STRING
# MAGIC ,ZSD_CREGIM STRING
# MAGIC ,ZSD_CGRPCA STRING
# MAGIC ,ZSD_CCONEX STRING
# MAGIC ,ZSD_LAPLNV STRING
# MAGIC ,ZSD_LDEVME STRING
# MAGIC ,ZSD_FINICI STRING
# MAGIC ,ZSD_FFIN STRING
# MAGIC ,ZSD_DUSCRE STRING
# MAGIC ,ZSD_FCREAC STRING
# MAGIC ,ZSD_DUSMOD STRING
# MAGIC ,ZSD_FMODIF STRING
# MAGIC ,ZSD_LTRGRA STRING
# MAGIC ,ZSD_CNEGOC STRING
# MAGIC ,ZSD_CVETE STRING
# MAGIC ,ZSD_CPEVE STRING
# MAGIC ,ZSD_LVETE STRING
# MAGIC ,ZSD_LSDIST STRING
# MAGIC ,ZSD_CPEDFN STRING
# MAGIC ,ZSD_CSAP STRING
# MAGIC ,ZSD_CORVTA STRING
# MAGIC ,ZSD_CCADIS STRING
# MAGIC ,ZSD_CSECTO STRING
# MAGIC ,ZSD_CTPFZV STRING
# MAGIC ,ZSD_LRUTA STRING
# MAGIC ,ZSD_IDESPD STRING
# MAGIC ,ZSD_GIRO STRING
# MAGIC ,ZSD_TIPUBI STRING
# MAGIC ,ZSD_LPEDAV STRING
# MAGIC ,ZSD_CTIPVT STRING
# MAGIC ,ZSD_FLAGDET STRING
# MAGIC ,ZSD_RECOVE STRING
# MAGIC ,ZSD_SDPPL STRING
# MAGIC ,ZSD_SDSNT STRING
# MAGIC ,ZSD_CHASH STRING
# MAGIC ,ZSD_FCREH STRING
# MAGIC ,ZSD_HCREH STRING
# MAGIC ,ZSD_FTRANS STRING
# MAGIC ,ZSD_CDCFRE STRING
# MAGIC ,ZSD_LENVRG STRING
# MAGIC ,ZSD_FACMARG DECIMAL(22,3)
# MAGIC ,ZSD_IMARGEN DECIMAL(22,3)
# MAGIC ,ZSD_DEPOALIC DECIMAL(22,3)
# MAGIC 
# MAGIC ,CREATE_AT timestamp
# MAGIC ,YEAR_MONTH_DAY string
# MAGIC ,ORIGIN_FILE string
# MAGIC )
# MAGIC using delta
# MAGIC partitioned by (YEAR_MONTH_DAY)
# MAGIC LOCATION '/mnt/data_sx/gold/zsd_pdgdcc00'
# MAGIC     