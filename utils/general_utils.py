# Databricks notebook source
######## import
from datetime import datetime,timedelta
from pyspark.sql import SparkSession
from delta.tables import *
from pyspark.sql.types import *
from pyspark.dbutils import DBUtils
import time

spark = SparkSession.builder.getOrCreate()
dbutils = DBUtils(spark)
######## funcion max_file_storage
def max_file_storage (path_storage:str)-> dict:
    #definicion :
    #    Metodo que retonar el maximo valor del archivo que se encuentra en el storage
    #Parameters:
    #    str1 (str): ruta donde buscara la maxima fecha
    #Returns:
    #    dict : diccionario con nombre,fecha en date y string

    # valor inicial de busqueda
    val= datetime(1999,1,1,0,0,0)
    list=[]
    list = dbutils.fs.ls(path_storage)
    for list_process_csv in range(len(list)):
        name=list[list_process_csv][1]
        # day = f'{name[0:4]}-{name[4:6]}-{name[6:8]} {name[9:11]}:{name[11:13]}:{name[13:15]}'
        # date = datetime.strptime(day, '%Y-%m-%d %H:%M:%S')
        day = f'{name[0:8]}'
        date = datetime.strptime(day, '%Y%m%d')
        filter = f'{name[0:15]}'
        if date >= val:
            val=date
            dict_file = {'name': name,'day': day,'date':date,'filter':filter}
    return dict_file

######## funcion setup_logging
def date_process(var:str)->str:
     #definicion :
    #    Metodo para guardar e imprimir los logs
    #Parameters:
    #
    #Returns:
    #    dict : diccionario con nombre,fecha en date y string

    now = datetime.now()
    date_now=now-timedelta(hours=5)

    year = '{:02d}'.format(date_now.year)
    month = '{:02d}'.format(date_now.month)
    day = '{:02d}'.format(date_now.day)

    if var == 'yyyymm':
        current = '{}{}'.format(year,month)
    elif var == 'yyyy' :
        current = '{}'.format(year)
    elif var=='yyyymmdd':
        current = '{}{}{}'.format(year,month,day)
    elif var=='yyyymmddhhmmss':
        current = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

    #current='20211019'
    return current
