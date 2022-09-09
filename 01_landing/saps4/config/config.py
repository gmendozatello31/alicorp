# Databricks notebook source
import json 

json_file = '''
    [
        { "name": "KNA1","partition_field": "D","reproces":"N","days":"0"},
        { "name": "KNVH","partition_field": "D","reproces":"N","days":"0"},
        { "name": "KNVV","partition_field": "D","reproces":"N","days":"0"},
        { "name": "KNB1","partition_field": "D","reproces":"N","days":"0"},
        { "name": "LIPS","partition_field": "D","reproces":"N","days":"0"},
        { "name": "LIKP","partition_field": "D","reproces":"N","days":"0"},
        { "name": "VBAP","partition_field": "D","reproces":"N","days":"20"},
        { "name": "VBAK","partition_field": "D","reproces":"S","days":"0"},
        { "name": "MARA","partition_field": "D","reproces":"N","days":"0"},
        { "name": "MAKT","partition_field": "D","reproces":"N","days":"0"},
        { "name": "TVFKT","partition_field": "M","reproces":"N","days":"0"}
    ]
    '''

def conf_json ():
    list_table = json.loads(json_file)
    return list_table


print("****** conf_json  *********")

# COMMAND ----------

json_file = '''
    [
        { "table": {
                    "name": "KNA1",
                    "partition_field": "D"
                   },
          "reproces": {
                     "active":"N",
                     "days":"0"
                     },
         "schedule": {
                     "format":"daily",
                     "day":["04","15","30","09"]
                    }
         },
         { "table": {
                    "name": "TVFKT",
                    "partition_field": "M"
                   },
          "reproces": {
                     "active":"N",
                     "days":"0"
                     },
         "schedule": {
                     "format":"month",
                     "day":["04","15","30","09"]
                    }
         }
    ]
    '''

def conf_json_order ():
    list_table = json.loads(json_file)
    return list_table

