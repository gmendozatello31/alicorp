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

v_year=date_process('yyyy')

for table_landing in list_table :    
    #columnsToSelect = (table_landing['partition_field'] + "-" + table_landing['name']).lower() 
    t_table= table_landing['name'].lower()
    t_partition = table_landing['partition_field'].lower()
    t_capa ='landing'
    t_location = f'{mount}/{raw}/{t_table}/data/{v_year}/'
    logger.info(f'..procesando tabla: {t_table} - partición : {t_partition}')
    
    
    try:
        max_file=max_file_storage(t_location)
        name_file = max_file.get("name")
        file_location_csv= f'{t_location}{name_file}'
        logger.info(f' file_location_csv : {file_location_csv}')
        # CAPA BRONZE
        #print("email")
        #dbutils.notebook.run("./bronze_saps4", 10000,  {"tables_lst" : list_table})  ## json 
    except Exception as e:
        #Email("la capa Bronze de Customers_Hierarchy", str(e))
        logger.info(f' Error : {t_table}')
        
    
        

