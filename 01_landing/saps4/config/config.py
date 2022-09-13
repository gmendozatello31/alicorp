# Databricks notebook source
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
                     "day":[]
                    }
         },
         { "table": {
                    "name": "TVFKT",
                    "partition_field": "M"
                   },
          "reproces": {
                     "active":"S",
                     "days":"10"
                     },
         "schedule": {
                     "format":"month",
                     "day":["04","15","30","09"]
                    }
         },
         { "table": {
                    "name": "KNVV",
                    "partition_field": "M"
                   },
          "reproces": {
                     "active":"S",
                     "days":"5"
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

