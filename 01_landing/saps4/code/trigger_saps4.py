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
    logger.info(f'Procesando tabla: {t_table} - partición : {t_partition}')
    
    
    try:
        max_file=max_file_storage(t_location)
        name_file = max_file.get("name")
        file_location_csv= f'{t_location}{name_file}'
        logger.info(f'file_location_csv : {file_location_csv} - name_file : {name_file}')
        df = read_df(file_location_csv,name_file,t_partition,t_table,logger)
        
    except Exception as e:
        #Email("la capa Bronze de Customers_Hierarchy", str(e))
        logger.info(f' Error : {t_table}')
        
    
        


# COMMAND ----------

list_columns = df.schema.names

# COMMAND ----------

from pyspark.sql import SQLContext
sqlContext = SQLContext(spark.sparkContext)
table_names_in_db = sqlContext.tableNames('landing')

#for f in table_names_in_db :
#    print(f)
    
table_exists = 'kna12' in table_names_in_db
print(table_exists)

# COMMAND ----------

for f in list_columns :
    print(f)
    

