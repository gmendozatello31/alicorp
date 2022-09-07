# Databricks notebook source
# MAGIC %run ../../../utils/utils

# COMMAND ----------

# MAGIC %run ../config/config

# COMMAND ----------

list_table=conf_json()

# COMMAND ----------

# Python program to read
# json file
import json
# JSON string
a = '''   { "tables": [ 
                    {"name": "Bob", "languages": "English"} ,
                    {"name": "Bob", "languages": "English"} 
                    ] }
    '''
# deserializes into dict
# and returns dict.
y = json.loads(a)
print("JSON string = ", y)

for i in y['tables']:#
	print(i)
