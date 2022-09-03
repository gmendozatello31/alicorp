# Databricks notebook source
# MAGIC %sql
# MAGIC drop table if exists bronze.vbak ;
# MAGIC create table bronze.vbak
# MAGIC (
# MAGIC MANDT string,
# MAGIC VBELN string,
# MAGIC ERDAT string,
# MAGIC ERZET string,
# MAGIC ERNAM string,
# MAGIC ANGDT string,
# MAGIC BNDDT string,
# MAGIC AUDAT string,
# MAGIC VBTYP string,
# MAGIC TRVOG string,
# MAGIC AUART string,
# MAGIC AUGRU string,
# MAGIC GWLDT string,
# MAGIC SUBMI string,
# MAGIC LIFSK string,
# MAGIC FAKSK string,
# MAGIC NETWR string,
# MAGIC WAERK string,
# MAGIC VKORG string,
# MAGIC VTWEG string,
# MAGIC SPART string,
# MAGIC VKGRP string,
# MAGIC VKBUR string,
# MAGIC GSBER string,
# MAGIC GSKST string,
# MAGIC GUEBG string,
# MAGIC GUEEN string,
# MAGIC KNUMV string,
# MAGIC VDATU string,
# MAGIC VPRGR string,
# MAGIC AUTLF string,
# MAGIC VBKLA string,
# MAGIC VBKLT string,
# MAGIC KALSM string,
# MAGIC VSBED string,
# MAGIC FKARA string,
# MAGIC AWAHR string,
# MAGIC KTEXT string,
# MAGIC BSTNK string,
# MAGIC BSARK string,
# MAGIC BSTDK string,
# MAGIC BSTZD string,
# MAGIC IHREZ string,
# MAGIC BNAME string,
# MAGIC TELF1 string,
# MAGIC MAHZA string,
# MAGIC MAHDT string,
# MAGIC KUNNR string,
# MAGIC KOSTL string,
# MAGIC STAFO string,
# MAGIC STWAE string,
# MAGIC AEDAT string,
# MAGIC KVGR1 string,
# MAGIC KVGR2 string,
# MAGIC KVGR3 string,
# MAGIC KVGR4 string,
# MAGIC KVGR5 string,
# MAGIC KNUMA string,
# MAGIC KOKRS string,
# MAGIC PS_PSP_PNR string,
# MAGIC KURST string,
# MAGIC KKBER string,
# MAGIC KNKLI string,
# MAGIC GRUPP string,
# MAGIC SBGRP string,
# MAGIC CTLPC string,
# MAGIC CMWAE string,
# MAGIC CMFRE string,
# MAGIC CMNUP string,
# MAGIC CMNGV string,
# MAGIC AMTBL string,
# MAGIC HITYP_PR string,
# MAGIC ABRVW string,
# MAGIC ABDIS string,
# MAGIC VGBEL string,
# MAGIC OBJNR string,
# MAGIC BUKRS_VF string,
# MAGIC TAXK1 string,
# MAGIC TAXK2 string,
# MAGIC TAXK3 string,
# MAGIC TAXK4 string,
# MAGIC TAXK5 string,
# MAGIC TAXK6 string,
# MAGIC TAXK7 string,
# MAGIC TAXK8 string,
# MAGIC TAXK9 string,
# MAGIC XBLNR string,
# MAGIC ZUONR string,
# MAGIC VGTYP string,
# MAGIC KALSM_CH string,
# MAGIC AGRZR string,
# MAGIC AUFNR string,
# MAGIC QMNUM string,
# MAGIC VBELN_GRP string,
# MAGIC SCHEME_GRP string,
# MAGIC ABRUF_PART string,
# MAGIC ABHOD string,
# MAGIC ABHOV string,
# MAGIC ABHOB string,
# MAGIC RPLNR string,
# MAGIC VZEIT string,
# MAGIC STCEG_L string,
# MAGIC LANDTX string,
# MAGIC XEGDR string,
# MAGIC ENQUEUE_GRP string,
# MAGIC DAT_FZAU string,
# MAGIC FMBDAT string,
# MAGIC VSNMR_V string,
# MAGIC HANDLE string,
# MAGIC PROLI string,
# MAGIC CONT_DG string,
# MAGIC CRM_GUID string,
# MAGIC UPD_TMSTMP string,
# MAGIC MSR_ID string,
# MAGIC TM_CTRL_KEY string,
# MAGIC OIPBL string,
# MAGIC LAST_CHANGED_BY_USER string,
# MAGIC HANDOVERLOC string,
# MAGIC EXT_REF_DOC_ID string,
# MAGIC EXT_REV_TMSTMP string,
# MAGIC DATAAGING string,
# MAGIC ABSTK string,
# MAGIC BESTK string,
# MAGIC CMPSC string,
# MAGIC CMPSD string,
# MAGIC CMPSI string,
# MAGIC CMPSJ string,
# MAGIC CMPSK string,
# MAGIC CMPS_CM string,
# MAGIC CMPS_TE string,
# MAGIC CMGST string,
# MAGIC COSTA string,
# MAGIC DCSTK string,
# MAGIC FKSAK string,
# MAGIC FMSTK string,
# MAGIC FSSTK string,
# MAGIC GBSTK string,
# MAGIC LFGSK string,
# MAGIC LFSTK string,
# MAGIC LSSTK string,
# MAGIC MANEK string,
# MAGIC RFGSK string,
# MAGIC RFSTK string,
# MAGIC SPSTG string,
# MAGIC TRSTA string,
# MAGIC UVALL string,
# MAGIC UVALS string,
# MAGIC UVFAK string,
# MAGIC UVFAS string,
# MAGIC UVPRS string,
# MAGIC UVVLK string,
# MAGIC UVVLS string,
# MAGIC UVK01 string,
# MAGIC UVK02 string,
# MAGIC UVK03 string,
# MAGIC UVK04 string,
# MAGIC UVK05 string,
# MAGIC UVS01 string,
# MAGIC UVS02 string,
# MAGIC UVS03 string,
# MAGIC UVS04 string,
# MAGIC UVS05 string,
# MAGIC WBSTK string,
# MAGIC TOTAL_EMCST string,
# MAGIC TOTAL_SLCST string,
# MAGIC TOTAL_LCCST string,
# MAGIC TOTAL_PCSTA string,
# MAGIC DUMMY_SALESDOC_INCL_EEW_PS string,
# MAGIC ZAPCGKH string,
# MAGIC APCGK_EXTENDH string,
# MAGIC ZABDATH string,
# MAGIC AD01FAREG string,
# MAGIC AD01BASDOC string,
# MAGIC LASTVCHR string,
# MAGIC PSM_BUDAT string,
# MAGIC FSH_KVGR6 string,
# MAGIC FSH_KVGR7 string,
# MAGIC FSH_KVGR8 string,
# MAGIC FSH_KVGR9 string,
# MAGIC FSH_KVGR10 string,
# MAGIC FSH_REREG string,
# MAGIC FSH_CQ_CHECK string,
# MAGIC FSH_VRSN_STATUS string,
# MAGIC FSH_TRANSACTION string,
# MAGIC FSH_VAS_CG string,
# MAGIC FSH_CANDATE string,
# MAGIC FSH_SS string,
# MAGIC FSH_OS_STG_CHANGE string,
# MAGIC J_3GKBAUL string,
# MAGIC MILL_APPL_ID string,
# MAGIC TAS string,
# MAGIC BETC string,
# MAGIC MOD_ALLOW string,
# MAGIC CANCEL_ALLOW string,
# MAGIC PAY_METHOD string,
# MAGIC BPN string,
# MAGIC REP_FREQ string,
# MAGIC LOGSYSB string,
# MAGIC KALCD string,
# MAGIC MULTI string,
# MAGIC SPPAYM string,
# MAGIC WTYSC_CLM_HDR string,
# MAGIC 
# MAGIC CREATE_AT timestamp,
# MAGIC YEAR_MONTH_DAY string,
# MAGIC ORIGIN_FILE string
# MAGIC )
# MAGIC using delta
# MAGIC partitioned by (YEAR_MONTH_DAY)
# MAGIC LOCATION '/mnt/data_s4/bronze/vbak'
# MAGIC     