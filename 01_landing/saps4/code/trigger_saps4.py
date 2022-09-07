# Databricks notebook source
# MAGIC %run ../../../utils/utils

# COMMAND ----------

# MAGIC %run ../cssssssssssssssssssssssssssssssssssssssssssssssssssssssssss/utils

# COMMAND ----------

import sys
sys.path.append("Worspace/Repos/main/alicorp")
print(sys.path)

# COMMAND ----------

import json

# JSON file
f = open ('config.json', "r")
#Reading from file
data = json.loads(f.read())
# Iterating through the json
# list
for i in data['emp_details']:#
	print(i)
#Closing file
f.close()


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
