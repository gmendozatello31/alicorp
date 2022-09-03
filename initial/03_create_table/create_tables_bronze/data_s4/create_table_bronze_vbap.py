# Databricks notebook source
# MAGIC %sql
# MAGIC drop table if exists bronze.vbap ;
# MAGIC create table bronze.vbap
# MAGIC (
# MAGIC mandt string,
# MAGIC vbeln string,
# MAGIC posnr string,
# MAGIC matnr string,
# MAGIC matwa string,
# MAGIC pmatn string,
# MAGIC charg string,
# MAGIC matkl string,
# MAGIC arktx string,
# MAGIC pstyv string,
# MAGIC posar string,
# MAGIC lfrel string,
# MAGIC fkrel string,
# MAGIC uepos string,
# MAGIC grpos string,
# MAGIC abgru string,
# MAGIC prodh string,
# MAGIC zwert string,
# MAGIC zmeng string,
# MAGIC zieme string,
# MAGIC umziz string,
# MAGIC umzin string,
# MAGIC meins string,
# MAGIC smeng string,
# MAGIC ablfz string,
# MAGIC abdat string,
# MAGIC absfz string,
# MAGIC posex string,
# MAGIC kdmat string,
# MAGIC kbver string,
# MAGIC kever string,
# MAGIC vkgru string,
# MAGIC vkaus string,
# MAGIC grkor string,
# MAGIC fmeng string,
# MAGIC uebtk string,
# MAGIC uebto string,
# MAGIC untto string,
# MAGIC faksp string,
# MAGIC atpkz string,
# MAGIC rkfkf string,
# MAGIC spart string,
# MAGIC gsber string,
# MAGIC netwr string,
# MAGIC waerk string,
# MAGIC antlf string,
# MAGIC kztlf string,
# MAGIC chspl string,
# MAGIC kwmeng string,
# MAGIC lsmeng string,
# MAGIC kbmeng string,
# MAGIC klmeng string,
# MAGIC vrkme string,
# MAGIC umvkz string,
# MAGIC umvkn string,
# MAGIC brgew string,
# MAGIC ntgew string,
# MAGIC gewei string,
# MAGIC volum string,
# MAGIC voleh string,
# MAGIC vbelv string,
# MAGIC posnv string,
# MAGIC vgbel string,
# MAGIC vgpos string,
# MAGIC voref string,
# MAGIC upflu string,
# MAGIC erlre string,
# MAGIC lprio string,
# MAGIC werks string,
# MAGIC lgort string,
# MAGIC vstel string,
# MAGIC route string,
# MAGIC stkey string,
# MAGIC stdat string,
# MAGIC stlnr string,
# MAGIC stpos string,
# MAGIC awahr string,
# MAGIC erdat string,
# MAGIC ernam string,
# MAGIC erzet string,
# MAGIC taxm1 string,
# MAGIC taxm2 string,
# MAGIC taxm3 string,
# MAGIC taxm4 string,
# MAGIC taxm5 string,
# MAGIC taxm6 string,
# MAGIC taxm7 string,
# MAGIC taxm8 string,
# MAGIC taxm9 string,
# MAGIC vbeaf string,
# MAGIC vbeav string,
# MAGIC vgref string,
# MAGIC netpr string,
# MAGIC kpein string,
# MAGIC kmein string,
# MAGIC shkzg string,
# MAGIC sktof string,
# MAGIC mtvfp string,
# MAGIC sumbd string,
# MAGIC kondm string,
# MAGIC ktgrm string,
# MAGIC bonus string,
# MAGIC provg string,
# MAGIC eannr string,
# MAGIC prsok string,
# MAGIC bwtar string,
# MAGIC bwtex string,
# MAGIC xchpf string,
# MAGIC xchar string,
# MAGIC lfmng string,
# MAGIC stafo string,
# MAGIC wavwr string,
# MAGIC kzwi1 string,
# MAGIC kzwi2 string,
# MAGIC kzwi3 string,
# MAGIC kzwi4 string,
# MAGIC kzwi5 string,
# MAGIC kzwi6 string,
# MAGIC stcur string,
# MAGIC aedat string,
# MAGIC ean11 string,
# MAGIC fixmg string,
# MAGIC prctr string,
# MAGIC mvgr1 string,
# MAGIC mvgr2 string,
# MAGIC mvgr3 string,
# MAGIC mvgr4 string,
# MAGIC mvgr5 string,
# MAGIC kmpmg string,
# MAGIC sugrd string,
# MAGIC sobkz string,
# MAGIC vpzuo string,
# MAGIC paobjnr string,
# MAGIC ps_psp_pnr string,
# MAGIC aufnr string,
# MAGIC vpmat string,
# MAGIC vpwrk string,
# MAGIC prbme string,
# MAGIC umref string,
# MAGIC knttp string,
# MAGIC kzvbr string,
# MAGIC sernr string,
# MAGIC objnr string,
# MAGIC abgrs string,
# MAGIC bedae string,
# MAGIC cmpre string,
# MAGIC cmtfg string,
# MAGIC cmpnt string,
# MAGIC cmkua string,
# MAGIC cuobj string,
# MAGIC cuobj_ch string,
# MAGIC cepok string,
# MAGIC koupd string,
# MAGIC serail string,
# MAGIC anzsn string,
# MAGIC nachl string,
# MAGIC magrv string,
# MAGIC mprok string,
# MAGIC vgtyp string,
# MAGIC prosa string,
# MAGIC uepvw string,
# MAGIC kalnr string,
# MAGIC klvar string,
# MAGIC sposn string,
# MAGIC kowrr string,
# MAGIC stadat string,
# MAGIC exart string,
# MAGIC prefe string,
# MAGIC knumh string,
# MAGIC clint string,
# MAGIC chmvs string,
# MAGIC stlty string,
# MAGIC stlkn string,
# MAGIC stpoz string,
# MAGIC stman string,
# MAGIC zschl_k string,
# MAGIC kalsm_k string,
# MAGIC kalvar string,
# MAGIC kosch string,
# MAGIC upmat string,
# MAGIC ukonm string,
# MAGIC mfrgr string,
# MAGIC plavo string,
# MAGIC kannr string,
# MAGIC cmpre_flt string,
# MAGIC abfor string,
# MAGIC abges string,
# MAGIC j_1bcfop string,
# MAGIC j_1btaxlw1 string,
# MAGIC j_1btaxlw2 string,
# MAGIC j_1btxsdc string,
# MAGIC wktnr string,
# MAGIC wktps string,
# MAGIC skopf string,
# MAGIC kzbws string,
# MAGIC wgru1 string,
# MAGIC wgru2 string,
# MAGIC knuma_pi string,
# MAGIC knuma_ag string,
# MAGIC kzfme string,
# MAGIC lstanr string,
# MAGIC techs string,
# MAGIC mwsbp string,
# MAGIC berid string,
# MAGIC pctrf string,
# MAGIC logsys_ext string,
# MAGIC j_1btaxlw3 string,
# MAGIC j_1btaxlw4 string,
# MAGIC j_1btaxlw5 string,
# MAGIC stockloc string,
# MAGIC sloctype string,
# MAGIC msr_ret_reason string,
# MAGIC msr_refund_code string,
# MAGIC msr_approv_block string,
# MAGIC nrab_knumh string,
# MAGIC trmrisk_relevant string,
# MAGIC sgt_rcat string,
# MAGIC vbkd_posnr string,
# MAGIC veda_posnr string,
# MAGIC handoverloc string,
# MAGIC ext_ref_item_id string,
# MAGIC handoverdate string,
# MAGIC handovertime string,
# MAGIC tc_aut_det string,
# MAGIC manual_tc_reason string,
# MAGIC fiscal_incentive string,
# MAGIC tax_subject_st string,
# MAGIC fiscal_incentive_id string,
# MAGIC spcsto string,
# MAGIC revacc_refid string,
# MAGIC revacc_reftype string,
# MAGIC dataaging string,
# MAGIC absta string,
# MAGIC besta string,
# MAGIC cmppi string,
# MAGIC cmppj string,
# MAGIC costa string,
# MAGIC dcsta string,
# MAGIC fksaa string,
# MAGIC fssta string,
# MAGIC gbsta string,
# MAGIC lfgsa string,
# MAGIC lfsta string,
# MAGIC lssta string,
# MAGIC manek string,
# MAGIC rfgsa string,
# MAGIC rfsta string,
# MAGIC uvall string,
# MAGIC uvfak string,
# MAGIC uvprs string,
# MAGIC uvvlk string,
# MAGIC uvp01 string,
# MAGIC uvp02 string,
# MAGIC uvp03 string,
# MAGIC uvp04 string,
# MAGIC uvp05 string,
# MAGIC wbsta string,
# MAGIC emcst string,
# MAGIC slcst string,
# MAGIC total_lccst string,
# MAGIC pcsta string,
# MAGIC reqqty_bu string,
# MAGIC handle string,
# MAGIC pbs_state string,
# MAGIC ifrs15_relevance string,
# MAGIC ifrs15_total_ssp string,
# MAGIC revfp string,
# MAGIC capped_net_amount string,
# MAGIC capped_net_amount_alert_thld string,
# MAGIC session_creation_date string,
# MAGIC session_creation_time string,
# MAGIC original_plant string,
# MAGIC atp_abc_substitution_status string,
# MAGIC dummy_slsdocitem_incl_eew_ps string,
# MAGIC po_quan string,
# MAGIC po_unit string,
# MAGIC mill_se_gposn string,
# MAGIC mill_batch_sel_f string,
# MAGIC cpd_updat string,
# MAGIC zapcgki string,
# MAGIC apcgk_extendi string,
# MAGIC zabdati string,
# MAGIC aufpl_olc string,
# MAGIC aplzl_olc string,
# MAGIC ad01profnr string,
# MAGIC admoi string,
# MAGIC adicc string,
# MAGIC adpri string,
# MAGIC addns string,
# MAGIC adacn string,
# MAGIC labsg string,
# MAGIC fabsg string,
# MAGIC pr_l_l string,
# MAGIC pr_f_f string,
# MAGIC pr_f_l string,
# MAGIC ferc_ind string,
# MAGIC fsh_season_year string,
# MAGIC fsh_season string,
# MAGIC fsh_collection string,
# MAGIC fsh_theme string,
# MAGIC fsh_crsd string,
# MAGIC fsh_searef string,
# MAGIC fsh_candate string,
# MAGIC fsh_psm_pfm_split string,
# MAGIC fsh_vas_rel string,
# MAGIC fsh_vas_prnt_id string,
# MAGIC fsh_transaction string,
# MAGIC fsh_item_group string,
# MAGIC fsh_item string,
# MAGIC fsh_vasref string,
# MAGIC fsh_grid_cond_rec string,
# MAGIC fsh_pqr_uepos string,
# MAGIC kostl string,
# MAGIC fonds string,
# MAGIC fistl string,
# MAGIC fkber string,
# MAGIC grant_nbr string,
# MAGIC budget_pd string,
# MAGIC iuid_relevant string,
# MAGIC equnr string,
# MAGIC eqart string,
# MAGIC j_3glvart string,
# MAGIC j_3gdatvo string,
# MAGIC j_3gdatbi string,
# MAGIC j_3gbelnri string,
# MAGIC j_3gposnri string,
# MAGIC prs_objnr string,
# MAGIC prs_sd_spsnr string,
# MAGIC prs_work_period string,
# MAGIC tas string,
# MAGIC betc string,
# MAGIC mod_allow string,
# MAGIC cancel_allow string,
# MAGIC pay_method string,
# MAGIC bpn string,
# MAGIC rep_freq string,
# MAGIC fmfgus_key string,
# MAGIC rfm_psst_rule string,
# MAGIC rfm_psst_group string,
# MAGIC pargb string,
# MAGIC aufpl_oaa string,
# MAGIC aplzl_oaa string,
# MAGIC vlcendcu string,
# MAGIC wrf_charstc1 string,
# MAGIC wrf_charstc2 string,
# MAGIC wrf_charstc3 string,
# MAGIC arsnum string,
# MAGIC arspos string,
# MAGIC wtysc_clmitem string,
# MAGIC zzdce string,
# MAGIC create_at timestamp,
# MAGIC year_month_day string,
# MAGIC origin_file string
# MAGIC )
# MAGIC using delta
# MAGIC partitioned by (year_month_day)
# MAGIC LOCATION '/mnt/data_s4/bronze/vbap'
# MAGIC     