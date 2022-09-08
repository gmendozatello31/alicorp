# Databricks notebook source
import json 

json_file = '''
    [
        { "name": "KNA1","partition_field": "d"},
        { "name": "KNVH","partition_field": "d"},
        { "name": "KNVV","partition_field": "d"},
        { "name": "KNB1","partition_field": "d"},
        { "name": "LIPS","partition_field": "d"},
        { "name": "LIKP","partition_field": "d"},
        { "name": "VBAP","partition_field": "d"},
        { "name": "VBAK","partition_field": "d"}
    ]
    '''

def conf_json ():
    list_table = json.loads(json_file)
    return list_table


print("****** conf_json  *********")
