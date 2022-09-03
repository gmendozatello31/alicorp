# Databricks notebook source
# MAGIC %sql
# MAGIC drop table if exists bronze.acdoca ;
# MAGIC create table bronze.acdoca
# MAGIC (
# MAGIC RCLNT string,
# MAGIC RLDNR string,
# MAGIC RBUKRS string,
# MAGIC GJAHR string,
# MAGIC BELNR string,
# MAGIC DOCLN string,
# MAGIC RYEAR string,
# MAGIC DOCNR_LD string,
# MAGIC RRCTY string,
# MAGIC RMVCT string,
# MAGIC VORGN string,
# MAGIC VRGNG string,
# MAGIC BTTYPE string,
# MAGIC AWTYP string,
# MAGIC AWSYS string,
# MAGIC AWORG string,
# MAGIC AWREF string,
# MAGIC AWITEM string,
# MAGIC AWITGRP string,
# MAGIC SUBTA string,
# MAGIC XREVERSING string,
# MAGIC XREVERSED string,
# MAGIC XTRUEREV string,
# MAGIC AWTYP_REV string,
# MAGIC AWORG_REV string,
# MAGIC AWREF_REV string,
# MAGIC SUBTA_REV string,
# MAGIC XSETTLING string,
# MAGIC XSETTLED string,
# MAGIC PREC_AWTYP string,
# MAGIC PREC_AWSYS string,
# MAGIC PREC_AWORG string,
# MAGIC PREC_AWREF string,
# MAGIC PREC_AWITEM string,
# MAGIC PREC_SUBTA string,
# MAGIC PREC_AWMULT string,
# MAGIC XSECONDARY string,
# MAGIC SRC_AWTYP string,
# MAGIC SRC_AWSYS string,
# MAGIC SRC_AWORG string,
# MAGIC SRC_AWREF string,
# MAGIC SRC_AWITEM string,
# MAGIC SRC_AWSUBIT string,
# MAGIC XCOMMITMENT string,
# MAGIC OBS_REASON string,
# MAGIC RTCUR string,
# MAGIC RWCUR string,
# MAGIC RHCUR string,
# MAGIC RKCUR string,
# MAGIC ROCUR string,
# MAGIC RVCUR string,
# MAGIC RBCUR string,
# MAGIC RCCUR string,
# MAGIC RDCUR string,
# MAGIC RECUR string,
# MAGIC RFCUR string,
# MAGIC RGCUR string,
# MAGIC RCO_OCUR string,
# MAGIC RUNIT string,
# MAGIC RVUNIT string,
# MAGIC RRUNIT string,
# MAGIC RIUNIT string,
# MAGIC QUNIT1 string,
# MAGIC QUNIT2 string,
# MAGIC QUNIT3 string,
# MAGIC CO_MEINH string,
# MAGIC RACCT string,
# MAGIC RCNTR string,
# MAGIC PRCTR string,
# MAGIC RFAREA string,
# MAGIC RBUSA string,
# MAGIC KOKRS string,
# MAGIC SEGMENT string,
# MAGIC SCNTR string,
# MAGIC PPRCTR string,
# MAGIC SFAREA string,
# MAGIC SBUSA string,
# MAGIC RASSC string,
# MAGIC PSEGMENT string,
# MAGIC TSL string,
# MAGIC WSL string,
# MAGIC WSL2 string,
# MAGIC WSL3 string,
# MAGIC HSL string,
# MAGIC KSL string,
# MAGIC OSL string,
# MAGIC VSL string,
# MAGIC BSL string,
# MAGIC CSL string,
# MAGIC DSL string,
# MAGIC ESL string,
# MAGIC FSL string,
# MAGIC GSL string,
# MAGIC KFSL string,
# MAGIC KFSL2 string,
# MAGIC KFSL3 string,
# MAGIC PSL string,
# MAGIC PSL2 string,
# MAGIC PSL3 string,
# MAGIC PFSL string,
# MAGIC PFSL2 string,
# MAGIC PFSL3 string,
# MAGIC CO_OSL string,
# MAGIC HSLALT string,
# MAGIC KSLALT string,
# MAGIC OSLALT string,
# MAGIC VSLALT string,
# MAGIC BSLALT string,
# MAGIC CSLALT string,
# MAGIC DSLALT string,
# MAGIC ESLALT string,
# MAGIC FSLALT string,
# MAGIC GSLALT string,
# MAGIC HSLEXT string,
# MAGIC KSLEXT string,
# MAGIC OSLEXT string,
# MAGIC VSLEXT string,
# MAGIC BSLEXT string,
# MAGIC CSLEXT string,
# MAGIC DSLEXT string,
# MAGIC ESLEXT string,
# MAGIC FSLEXT string,
# MAGIC GSLEXT string,
# MAGIC HVKWRT string,
# MAGIC MSL string,
# MAGIC MFSL string,
# MAGIC VMSL string,
# MAGIC VMFSL string,
# MAGIC RMSL string,
# MAGIC QUANT1 string,
# MAGIC QUANT2 string,
# MAGIC QUANT3 string,
# MAGIC CO_MEGBTR string,
# MAGIC CO_MEFBTR string,
# MAGIC HSALK3 string,
# MAGIC KSALK3 string,
# MAGIC OSALK3 string,
# MAGIC VSALK3 string,
# MAGIC HSALKV string,
# MAGIC KSALKV string,
# MAGIC OSALKV string,
# MAGIC VSALKV string,
# MAGIC HPVPRS string,
# MAGIC KPVPRS string,
# MAGIC OPVPRS string,
# MAGIC VPVPRS string,
# MAGIC HSTPRS string,
# MAGIC KSTPRS string,
# MAGIC OSTPRS string,
# MAGIC VSTPRS string,
# MAGIC HVKSAL string,
# MAGIC LBKUM string,
# MAGIC DRCRK string,
# MAGIC POPER string,
# MAGIC PERIV string,
# MAGIC FISCYEARPER string,
# MAGIC BUDAT string,
# MAGIC BLDAT string,
# MAGIC BLART string,
# MAGIC BUZEI string,
# MAGIC ZUONR string,
# MAGIC BSCHL string,
# MAGIC BSTAT string,
# MAGIC LINETYPE string,
# MAGIC KTOSL string,
# MAGIC SLALITTYPE string,
# MAGIC XSPLITMOD string,
# MAGIC USNAM string,
# MAGIC TIMESTAMP string,
# MAGIC EPRCTR string,
# MAGIC RHOART string,
# MAGIC GLACCOUNT_TYPE string,
# MAGIC KTOPL string,
# MAGIC LOKKT string,
# MAGIC KTOP2 string,
# MAGIC REBZG string,
# MAGIC REBZJ string,
# MAGIC REBZZ string,
# MAGIC REBZT string,
# MAGIC RBEST string,
# MAGIC EBELN string,
# MAGIC EBELP string,
# MAGIC ZEKKN string,
# MAGIC SGTXT string,
# MAGIC KDAUF string,
# MAGIC KDPOS string,
# MAGIC MATNR string,
# MAGIC WERKS string,
# MAGIC LIFNR string,
# MAGIC KUNNR string,
# MAGIC FBUDA string,
# MAGIC COCO_NUM string,
# MAGIC KOART string,
# MAGIC UMSKZ string,
# MAGIC MWSKZ string,
# MAGIC HBKID string,
# MAGIC HKTID string,
# MAGIC XOPVW string,
# MAGIC AUGDT string,
# MAGIC AUGBL string,
# MAGIC AUGGJ string,
# MAGIC AFABE string,
# MAGIC ANLN1 string,
# MAGIC ANLN2 string,
# MAGIC BZDAT string,
# MAGIC ANBWA string,
# MAGIC MOVCAT string,
# MAGIC DEPR_PERIOD string,
# MAGIC ANLGR string,
# MAGIC ANLGR2 string,
# MAGIC SETTLEMENT_RULE string,
# MAGIC ANLKL string,
# MAGIC KTOGR string,
# MAGIC PANL1 string,
# MAGIC PANL2 string,
# MAGIC UBZDT_PN string,
# MAGIC XVABG_PN string,
# MAGIC PROZS_PN string,
# MAGIC XMANPROPVAL_PN string,
# MAGIC KALNR string,
# MAGIC VPRSV string,
# MAGIC MLAST string,
# MAGIC KZBWS string,
# MAGIC XOBEW string,
# MAGIC SOBKZ string,
# MAGIC VTSTAMP string,
# MAGIC MAT_KDAUF string,
# MAGIC MAT_KDPOS string,
# MAGIC MAT_PSPNR string,
# MAGIC MAT_PS_POSID string,
# MAGIC MAT_LIFNR string,
# MAGIC BWTAR string,
# MAGIC BWKEY string,
# MAGIC HPEINH string,
# MAGIC KPEINH string,
# MAGIC OPEINH string,
# MAGIC VPEINH string,
# MAGIC MLPTYP string,
# MAGIC MLCATEG string,
# MAGIC QSBVALT string,
# MAGIC QSPROCESS string,
# MAGIC PERART string,
# MAGIC MLPOSNR string,
# MAGIC BUKRS_SENDER string,
# MAGIC RACCT_SENDER string,
# MAGIC ACCAS_SENDER string,
# MAGIC ACCASTY_SENDER string,
# MAGIC OBJNR string,
# MAGIC HRKFT string,
# MAGIC HKGRP string,
# MAGIC PAROB1 string,
# MAGIC PAROBSRC string,
# MAGIC USPOB string,
# MAGIC CO_BELKZ string,
# MAGIC CO_BEKNZ string,
# MAGIC BELTP string,
# MAGIC MUVFLG string,
# MAGIC GKONT string,
# MAGIC GKOAR string,
# MAGIC ERLKZ string,
# MAGIC PERNR string,
# MAGIC PAOBJNR string,
# MAGIC XPAOBJNR_CO_REL string,
# MAGIC SCOPE string,
# MAGIC LOGSYSO string,
# MAGIC PBUKRS string,
# MAGIC PSCOPE string,
# MAGIC LOGSYSP string,
# MAGIC BWSTRAT string,
# MAGIC OBJNR_HK string,
# MAGIC AUFNR_ORG string,
# MAGIC UKOSTL string,
# MAGIC ULSTAR string,
# MAGIC UPRZNR string,
# MAGIC UPRCTR string,
# MAGIC ACCAS string,
# MAGIC ACCASTY string,
# MAGIC LSTAR string,
# MAGIC AUFNR string,
# MAGIC AUTYP string,
# MAGIC PS_PSP_PNR string,
# MAGIC PS_POSID string,
# MAGIC PS_PRJ_PNR string,
# MAGIC PS_PSPID string,
# MAGIC NPLNR string,
# MAGIC NPLNR_VORGN string,
# MAGIC PRZNR string,
# MAGIC KSTRG string,
# MAGIC BEMOT string,
# MAGIC RSRCE string,
# MAGIC QMNUM string,
# MAGIC ERKRS string,
# MAGIC PACCAS string,
# MAGIC PACCASTY string,
# MAGIC PLSTAR string,
# MAGIC PAUFNR string,
# MAGIC PAUTYP string,
# MAGIC PPS_PSP_PNR string,
# MAGIC PPS_POSID string,
# MAGIC PPS_PRJ_PNR string,
# MAGIC PPS_PSPID string,
# MAGIC PKDAUF string,
# MAGIC PKDPOS string,
# MAGIC PPAOBJNR string,
# MAGIC PNPLNR string,
# MAGIC PNPLNR_VORGN string,
# MAGIC PPRZNR string,
# MAGIC PKSTRG string,
# MAGIC CO_ACCASTY_N1 string,
# MAGIC CO_ACCASTY_N2 string,
# MAGIC CO_ACCASTY_N3 string,
# MAGIC CO_ZLENR string,
# MAGIC CO_BELNR string,
# MAGIC CO_BUZEI string,
# MAGIC CO_BUZEI1 string,
# MAGIC CO_BUZEI2 string,
# MAGIC CO_BUZEI5 string,
# MAGIC CO_BUZEI6 string,
# MAGIC CO_BUZEI7 string,
# MAGIC CO_REFBZ string,
# MAGIC CO_REFBZ1 string,
# MAGIC CO_REFBZ2 string,
# MAGIC CO_REFBZ5 string,
# MAGIC CO_REFBZ6 string,
# MAGIC CO_REFBZ7 string,
# MAGIC WORK_ITEM_ID string,
# MAGIC ARBID string,
# MAGIC VORNR string,
# MAGIC AUFPS string,
# MAGIC UVORN string,
# MAGIC EQUNR string,
# MAGIC TPLNR string,
# MAGIC ISTRU string,
# MAGIC ILART string,
# MAGIC PLKNZ string,
# MAGIC ARTPR string,
# MAGIC PRIOK string,
# MAGIC MAUFNR string,
# MAGIC MATKL_MM string,
# MAGIC PLANNED_PARTS_WORK string,
# MAGIC FKART string,
# MAGIC VKORG string,
# MAGIC VTWEG string,
# MAGIC SPART string,
# MAGIC MATNR_COPA string,
# MAGIC MATKL string,
# MAGIC KDGRP string,
# MAGIC LAND1 string,
# MAGIC BRSCH string,
# MAGIC BZIRK string,
# MAGIC KUNRE string,
# MAGIC KUNWE string,
# MAGIC KONZS string,
# MAGIC ACDOC_COPA_EEW_DUMMY_PA string,
# MAGIC VKGRP_PA string,
# MAGIC KMLAND_PA string,
# MAGIC PRODH_PA string,
# MAGIC VKBUR_PA string,
# MAGIC WW009_PA string,
# MAGIC AUART_PA string,
# MAGIC KMORIG_PA string,
# MAGIC KONDA_PA string,
# MAGIC KTGRD_PA string,
# MAGIC MVGR1_PA string,
# MAGIC MVGR2_PA string,
# MAGIC REGIO_PA string,
# MAGIC WW011_PA string,
# MAGIC WW012_PA string,
# MAGIC WW013_PA string,
# MAGIC WW014_PA string,
# MAGIC WW015_PA string,
# MAGIC WW016_PA string,
# MAGIC PAPH1_PA string,
# MAGIC PAPH2_PA string,
# MAGIC PAPH3_PA string,
# MAGIC PAPH4_PA string,
# MAGIC PAPH5_PA string,
# MAGIC PAPH6_PA string,
# MAGIC KDKG1_PA string,
# MAGIC KTOKD_PA string,
# MAGIC MVGR3_PA string,
# MAGIC MVGR4_PA string,
# MAGIC MVGR5_PA string,
# MAGIC PARTNER_PA string,
# MAGIC PLTYP_PA string,
# MAGIC PSTYV_PA string,
# MAGIC VBUND_PA string,
# MAGIC KONDM_PA string,
# MAGIC VRTNR_PA string,
# MAGIC WW017_PA string,
# MAGIC DUMMY_MRKT_SGMNT_EEW_PS string,
# MAGIC RE_BUKRS string,
# MAGIC RE_ACCOUNT string,
# MAGIC FIKRS string,
# MAGIC FISTL string,
# MAGIC MEASURE string,
# MAGIC RFUND string,
# MAGIC RGRANT_NBR string,
# MAGIC RBUDGET_PD string,
# MAGIC SFUND string,
# MAGIC SGRANT_NBR string,
# MAGIC SBUDGET_PD string,
# MAGIC VNAME string,
# MAGIC EGRUP string,
# MAGIC RECID string,
# MAGIC VPTNR string,
# MAGIC BTYPE string,
# MAGIC ETYPE string,
# MAGIC PRODPER string,
# MAGIC BILLM string,
# MAGIC POM string,
# MAGIC CBRUNID string,
# MAGIC JVACTIVITY string,
# MAGIC PVNAME string,
# MAGIC PEGRUP string,
# MAGIC S_RECIND string,
# MAGIC CBRACCT string,
# MAGIC CBOBJNR string,
# MAGIC SWENR string,
# MAGIC SGENR string,
# MAGIC SGRNR string,
# MAGIC SMENR string,
# MAGIC RECNNR string,
# MAGIC SNKSL string,
# MAGIC SEMPSL string,
# MAGIC DABRZ string,
# MAGIC PSWENR string,
# MAGIC PSGENR string,
# MAGIC PSGRNR string,
# MAGIC PSMENR string,
# MAGIC PRECNNR string,
# MAGIC PSNKSL string,
# MAGIC PSEMPSL string,
# MAGIC PDABRZ string,
# MAGIC ACROBJTYPE string,
# MAGIC ACROBJ_ID string,
# MAGIC ACRSOBJ_ID string,
# MAGIC ACRITMTYPE string,
# MAGIC VALOBJTYPE string,
# MAGIC VALOBJ_ID string,
# MAGIC VALSOBJ_ID string,
# MAGIC NETDT string,
# MAGIC RISK_CLASS string,
# MAGIC ACDOC_EEW_DUMMY string,
# MAGIC DUMMY_INCL_EEW_COBL string,
# MAGIC FUP_ACTION string,
# MAGIC MIG_SOURCE string,
# MAGIC MIG_DOCLN string,
# MAGIC DATAAGING string,
# MAGIC 
# MAGIC CREATE_AT timestamp,
# MAGIC YEAR_MONTH_DAY string,
# MAGIC ORIGIN_FILE string
# MAGIC )
# MAGIC using delta
# MAGIC partitioned by (YEAR_MONTH_DAY)
# MAGIC LOCATION '/mnt/data_s4/bronze/acdoca'
# MAGIC     