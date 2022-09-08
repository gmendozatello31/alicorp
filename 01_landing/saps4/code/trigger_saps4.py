# Databricks notebook source
# MAGIC %run ../../../utils/utils

# COMMAND ----------

# MAGIC %run ../config/config

# COMMAND ----------

# Se obtiene la lista de tablas que se procesaran de raw to landing
list_table=conf_json()
logger = init_logging("Landing")

mount='/mnt/data_s4'
raw='raw'
t_capa ='landing'
v_year=date_process('yyyy')

# recorremos todas las tablas a procesar
for table_landing in list_table :    
    # se obtiene la tabla y particion
    t_table= table_landing['name'].lower()
    t_partition = table_landing['partition_field'].lower()
    
    #se define la ruta de carpeta raw
    t_location = f'{mount}/{raw}/{t_table}/data/{v_year}/'
    
    #se define la ruta de la tabla delta
    t_location_delta = f'{mount}/{t_capa}/{t_table}'
    
    logger.info(f'Procesando tabla: {t_table} - partición : {t_partition}')
    
    
    try:
        #se obtiene maximo archivo a procesar
        max_file=max_file_storage(t_location)
        name_file = max_file.get("name")
        
        #se obtiene el archivo a procesar dentro de raw
        file_location_csv= f'{t_location}{name_file}'
        logger.info(f'file_location_csv : {file_location_csv} - name_file : {name_file}')
        
        #se graba el df en formato delta en el storage
        process = save_df(file_location_csv,name_file,t_partition,t_location_delta)
        logger.info(f'{process}')
        
        #Validamos si existe la tabla creada en databricks
        exis_table = existe_table('landing',t_table)
        
        if exis_table == False :
            create_table(t_location_delta,f'{t_capa}.{t_table}')
            logger.info(f'Creacion de tabla : {t_table}')
        
            
        
    except Exception as e:
        #Email("la capa Bronze de Customers_Hierarchy", str(e))
        logger.info(f'Error : {t_table}')
        
    
        


# COMMAND ----------

process = save_df('/mnt/data_s4/raw/knvv/data/2022/20220831.csv','knvv','d','/mnt/data_s4/landing/knvv')

# COMMAND ----------

# Write the data to its target.
df.write.mode('append').format('delta').save('/mnt/data_s4/landing/knvv')

# COMMAND ----------

save_path = '/mnt/data_s4/landing/knvv'
table_name = 'landing.knvv'
spark.sql(f" drop table if exists {table_name}")
# spark.sql("CREATE TABLE " + table_name + " USING DELTA LOCATION '" + save_path + "'")
spark.sql(f" CREATE TABLE {table_name}  USING DELTA LOCATION '{save_path}'" )

# COMMAND ----------

ambiente='landing'
tabla='knvv'
location = '/mnt/data_s4/landing/knvv'
partitioned ='YEAR_MONTH_DAY'

fields=''

for col in df.dtypes:
    campo = (col[0]+" "+col[1]+",")
    campo = campo.lower()
    fields += campo

fields =  fields[:-1]

query = f"""
drop table if exists {ambiente}.{tabla} ;
create table {ambiente}.{tabla} 
( 
{fields} 
)
using delta
partitioned by ({partitioned})
location '{location}'
"""
print(query)



# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC drop table if exists landing.knvv ;
# MAGIC create table landing.knvv 
# MAGIC ( 
# MAGIC mandt string,kunnr string,bukrs string,pernr string,knb1_eew_cc string,erdat string,ernam string,sperr string,loevm string,zuawa string,busab string,akont string,begru string,knrze string,knrzb string,zamim string,zamiv string,zamir string,zamib string,zamio string,zwels string,xverr string,zahls string,zterm string,wakon string,vzskz string,zindt string,zinrt string,eikto string,zsabe string,kverm string,fdgrv string,vrbkz string,vlibb string,vrszl string,vrspr string,vrsnr string,verdt string,perkz string,xdezv string,xausz string,webtr string,remit string,datlz string,xzver string,togru string,kultg string,hbkid string,xpore string,blnkz string,altkn string,zgrup string,urlid string,mgrup string,lockb string,uzawe string,ekvbd string,sregl string,xedip string,frgrp string,vrsdg string,tlfxs string,intad string,xknzb string,guzte string,gricd string,gridt string,wbrsl string,confs string,updat string,uptim string,nodel string,tlfns string,cession_kz string,avsnd string,ad_hash string,qland string,cvp_xblck_b string,ciiucode string,gmvkzd string,create_at timestamp,origin_file string,year_month_day string 
# MAGIC )
# MAGIC using delta
# MAGIC partitioned by (YEAR_MONTH_DAY)
# MAGIC location '/mnt/data_s4/landing/knvv'
