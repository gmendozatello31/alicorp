# Databricks notebook source
# MAGIC %run ../../../utils/utils

# COMMAND ----------

# MAGIC %run ../config/config

# COMMAND ----------

# Se obtiene la lista de tablas que se procesaran de raw to landing
list_table=conf_json()

logger = init_logging("Landing")

for table_landing in list_table :    
    columnsToSelect = (table_landing['partition_field'] + "-" + table_landing['name']).lower() 
    logger.info(f'..procesando  Tabla:  {columnsToSelect}')
    try:
        # CAPA BRONZE
        print("email")
        #dbutils.notebook.run("./bronze_saps4", 10000,  {"tables_lst" : list_table})  ## json 
    except Exception as e:
        #Email("la capa Bronze de Customers_Hierarchy", str(e))
        print("Error")
        dbutils.notebook.exit(e)
    
        

