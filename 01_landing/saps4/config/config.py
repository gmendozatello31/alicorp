# Databricks notebook source
json_file = '''
    [
        { "table": {
                    "name": "KNA1",
                    "partition_field": "D"
                   },
          "reprocess": {
                     "active":"N",
                     "days":"0"
                     },
         "schedule": {
                     "format":"daily",
                     "day":[]
                    }
         },
         { "table": {
                    "name": "TVFKT",
                    "partition_field": "M"
                   },
          "reprocess": {
                     "active":"S",
                     "days":"10"
                     },
         "schedule": {
                     "format":"month",
                     "day":["04","15","30","13"]
                    }
         },
         { "table": {
                    "name": "KNVV",
                    "partition_field": "M"
                   },
          "reprocess": {
                     "active":"S",
                     "days":"5"
                     },
         "schedule": {
                     "format":"month",
                     "day":["04","15","30","13"]
                    }
         }
    ]
    '''

def conf_json_order ():
    list_table = json.loads(json_file)
    return list_table

