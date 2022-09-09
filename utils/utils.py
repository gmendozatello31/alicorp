# Databricks notebook source
# Databricks notebook source
from datetime import datetime,timedelta
from delta.tables import *
from pyspark.sql import DataFrame
from typing import List
from google.cloud import secretmanager
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from google.cloud import storage
from pyspark.sql.types import  *
import os,requests,json,base64,time,smtplib
import pyspark.sql.functions as f 
import yaml as yml
import logging
from pyspark.sql import SQLContext

sqlContext = SQLContext(spark.sparkContext)

def create_table (save_path:str,table_name:str):
    """ 
    definicion :  
        Creacion de tabla de forma automatica
    Parameters:
        save_path (str): ruta de la tabla en storage
        table_name (str): nombre de la tabla 
    Returns:
        
    """
    
    spark.sql(f" drop table if exists {table_name}")
    # spark.sql("CREATE TABLE " + table_name + " USING DELTA LOCATION '" + save_path + "'")
    spark.sql(f" CREATE TABLE {table_name}  USING DELTA LOCATION '{save_path}'" )

######## funcion max_file_storage
def existe_table (dataBase:str,table:str)-> bool:
    """ 
    definicion :  
        Validamos si existe tabla
    Parameters:
        dataBase (str): base datos
        table_name (str): tabla  
    Returns:
        bool : True si existe / False no existe
    """
    table_names_in_db = sqlContext.tableNames(dataBase)
    table_exists = table in table_names_in_db
    return table_exists
    
    
######## funcion max_file_storage
def max_file_storage (path_storage:str)-> dict:
    """ 
    definicion :  
        Metodo que retonar el maximo valor del archivo que se encuentra en el storage
    Parameters:
        str1 (str): ruta donde buscara la maxima fecha
    Returns:
        dict : diccionario con nombre,fecha en date y string
    """
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
def init_logging(name):
    """ 
    definicion : 
        Init logging settings
    Parameters:
                name (str): Logger name
    Returns: 
                logger: logger instance
    """
    MSG_FORMAT = "%(asctime)s %(levelname)s %(name)s: %(message)s"
    DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

    logging.basicConfig(format=MSG_FORMAT, datefmt=DATETIME_FORMAT)
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    return logger

######## funcion setup_logging
def date_process(var:str)->str:
    """ 
    definicion :  
        Metodo para guardar e imprimir los logs 
    Parameters:
        cadena de busqueda para la fecha 
    Returns:
        dict : diccionario con nombre,fecha en date y string
    """
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


######## transfor_basic
def transfor_basic (df:DataFrame,typeTrans:str,listVal:List)->DataFrame:
    """
    definicion :  
        transformacion basica para df
    Parameters:
       df : Dataframe de la capa bronce a silver 
    Returns:
        df : Dataframe con las transformaciones Basicas 
    """
    # transformation lower title
    if typeTrans == 'basic':
        for x in df.schema.names:
            df=df.withColumnRenamed(x,x.lower())
        for x in df.schema.names:
            df=df.withColumn(x,f.upper(f.trim(f.col(x))))
        
        
    if typeTrans == 'integer':
        for x in listVal:
            #print(x)
            df = df.withColumn(x.lower(),f.col(x).cast("integer"))
    
    if typeTrans == 'timestamp':
        for x in listVal:
            df = df.withColumn(x.lower(),f.to_date(f.unix_timestamp(f.col(x), "yyyymmdd").cast("timestamp")))
    
    if typeTrans == 'decimal':
        for x in listVal:
            df = df.withColumn(x.lower(),f.regexp_replace(latets_bronze[x],' ','').cast('decimal(22,3)'))
            
    if typeTrans == 'double':
        for x in listVal:
            df = df.withColumn(x.lower(),f.regexp_replace(latets_bronze[x],' ','').cast('double'))

    return df

  
    
def getColumnsToSelect(sourceTable:str)->List:
    """
    definicion :  
        Devuelve los select necesarios en cada capa para la tranformacion
    Parameters:
       nombre de la tabla  
    Returns:
        Lista de campos
    """
    listCols = ''
    listColsDelta = spark.sql("select * from " + sourceTable + " limit 1").schema.names
    columnsToSelect = ','.join(listColsDelta)
    
    return columnsToSelect.lower()

def getDate()->datetime:
    """ 
    definicion :  
        Devuelve fecha en formato date
    Parameters:
       sin parametros
    Returns:
        fecha
    """
    
    now = datetime.now()
    stringDate = now.strftime("%d-%m-%Y")
    date = datetime.strptime(stringDate, '%d-%m-%Y').date()
    return date
  

def validateDate(df:DataFrame)->DataFrame:
    """
    definicion :  
        validacion de fecha en caso envie null 
    Parameters:
       df 
    Returns:
        df con validacion de campos
    """
    col_list = df.dtypes

    for x,y in col_list:
        if y == 'date':
            df = df.withColumn(x, 
                f.when(df[x] < '1900-01-01', f.to_date(f.lit(None), "yyyy-MM-dd")).
                otherwise(df[x]))
        if y == 'timestamp':
            df = df.withColumn(x, 
                f.when(df[x] < '1900-01-01', f.to_timestamp(f.lit(None), "yyyy-MM-dd HH:mm:ss.S")).
                otherwise(df[x]))
            
    return df
  
# def getEmailCredentials():
#     dsimCredenciales = eval(dbutils.secrets.getBytes(scope="alicorp_dsim", key="SECRET"))
#     return dsimCredenciales

def getEmailCredentials():
    """"
    definicion :  
        metodo de ayuda para el envio de correo
    """
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{os.environ['SECRET_PROJECT']}/secrets/{os.environ['SECRET_SERVICE']}/versions/{os.environ['SECRET_VERSION']}"
    response = client.access_secret_version(request={'name':name})
    payload = response.payload.data.decode('utf-8')

    env_vars = yml.full_load(stream=payload)
    
    return env_vars
    

class Email:
    #deinition :  
    #    metodo de ayuda para el envio de correo
    
      def __init__(self,filename, error):
        secret = getEmailCredentials()
        self.server = smtplib.SMTP(host='smtp.gmail.com',port='587')
        html = f'''
          <html>
            <body>
              <p>
                Estimados,<br>
                hubo un problema en {filename}, por favor revisar el log.<br><br>
                Detalle: {error}
              </p>
            </body>
          </html>
        '''
        self.html = MIMEText(html,'html')
        self.connect(secret)
        self.send_message(secret)
    
      def connect(self,secret):
        self.server.ehlo()
        self.server.starttls()
        self.server.login(secret['EMAIL_FROM'],secret['EMAIL_PASS'])
    
      def send_message(self,secret):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = secret['EMAIL_SUBJECT'] 
        msg['From'] = secret['EMAIL_FROM'] 
        msg['To'] = secret['EMAIL_TO'] 
        msg.attach(self.html)
        self.server.send_message(msg)

# dbutils.secrets.listScopes()
# dbutils.secrets.list("alicorp_dsim")
# my_secret = dbutils.secrets.getBytes(scope="alicorp_dsim", key="SECRET")
# my_secret.decode("utf-8")

# x = eval(my_secret)
# email_from = x['EMAIL_FROM']
# email_pass = x['EMAIL_PASS']
# print(email_from,email_pass)


def create_notebook(notebook_name, content):
    ctx = json.loads(dbutils.notebook.entry_point.getDbutils().notebook().getContext().toJson())
    host_name = ctx['extraContext']['api_url']
    host_token = ctx['extraContext']['api_token']
    notebook_path = "/".join(ctx['extraContext']['notebook_path'].split("/")[:-1])
    notebook_path = f"{notebook_path}/create_tables/{notebook_name}"
    new_path = os.path.join(os.path.dirname(notebook_path), notebook_name)

    data = {
      "content": base64.b64encode(content.encode("utf-8")).decode('ascii'),
      "path": new_path,
      "language": "PYTHON",
      "overwrite": True,
      "format": "SOURCE"
    }
    response = requests.post(
        f'{host_name}/api/2.0/workspace/import',
        headers={'Authorization': f'Bearer {host_token}'},
        json = data
      ).json()
    return response
  
    
#def validateDate(df:DataFrame)->DataFrame:

def read_yaml(bucket:str,file:str)-> yml:
    """
    definicion :  
        metodo para obtener un archivo yaml o un archivo json 
    Parameters:
       ruta del archivo y el bucket
    Returns:
        archivo que se encuentra en storage 
    """
    bucket_gcp = ''
    
    if(bucket=='data_s4'):
        bucket_gcp=os.environ['BUCKET_DATA_S4']
    elif(bucket=='data_sx'):
        bucket_gcp=os.environ['BUCKET_DATA_SX']
    elif(bucket=='data_bwtpm'):
        bucket_gcp=os.environ['BUCKET_DATA_BWTPM']
    elif(bucket=='data_entities'):
        bucket_gcp=os.environ['BUCKET_DATA_ENTITIES']
    elif(bucket=='data_iview'):
        bucket_gcp=os.environ['BUCKET_DATA_IVIEW']
    else:
        bucket_gcp = ''
    #print("bucket : ", bucket_gcp)
    # bucket_gcp=os.environ['BUCKET_DATA_S4']
    storage_client = storage.Client()
    bucket_name = bucket_gcp  # Do not put 'gs://my_bucket_name'
    bucket = storage_client.get_bucket(bucket_gcp)
    blob = bucket.get_blob(file)
    downloaded_file = blob.download_as_string()
    downloaded_yaml_file = yml.safe_load(blob.download_as_text(encoding="utf-8"))
    return downloaded_yaml_file 
  

######## funcion save datos delta
def save_df (file_location_csv:str,name_file:str,partition:str,path_delta:str) ->str:
    """ 
    definicion :  
        Metodo que retonar el maximo valor del archivo que se encuentra en el storage
    Parameters:
        str1 (str): ruta donde buscara la maxima fecha
    Returns:
        dict : diccionario con nombre,fecha en date y string
    """
    
    now = datetime.now()
    date_current = now - timedelta(hours=5)
    day = '{:02d}'.format(date_current.day)
    
    # valor inicial de busqueda
    file_type = 'csv'
    infer_schema = 'false'
    first_row_is_header = 'true'
    delimiter = ','
    v_current = date_process('yyyymmddhhmmss')
    
    df = spark.read.format(file_type) \
        .option("inferSchema", infer_schema) \
        .option("multiline", "true") \
        .option("encoding", "utf8") \
        .option("header", first_row_is_header) \
        .option("sep", delimiter) \
        .load(file_location_csv)

    df = df \
        .withColumn('CREATE_AT', f.unix_timestamp(f.lit(v_current), 'yyyy-MM-dd HH:mm:ss').cast("timestamp")) \
        .withColumn('ORIGIN_FILE', f.lit(name_file))
    
    if partition == 'm':
        df = df.withColumn('YEAR_MONTH', f.lit(name_file[0:6]))
    else:
        df = df.withColumn('YEAR_MONTH_DAY', f.lit(name_file[0:8]))
       
    for each in df.columns:
        df = df.withColumnRenamed(each , each.strip())
        
    if ((partition == 'm') and ( day=='01' or day=='15' or day=='28' or day=='09' ) ):
        proceso = 'tabla mensual'
        df.write.mode('append').format('delta').save(path_delta)
    elif ((partition == 'd'))  :
        proceso = 'tabla diaria'
        df.write.mode('append').format('delta').save(path_delta)
    else :
        proceso = 'sin registrar'
  
    return proceso
    
    
######## funcion save datos delta
def save_df_schedule (parameter:json) ->str:
    """ 
    definicion :  
        Metodo que retonar el maximo valor del archivo que se encuentra en el storage
    Parameters:
        str1 (str): ruta donde buscara la maxima fecha
    Returns:
        dict : diccionario con nombre,fecha en date y string
    """
    
    now = datetime.now()
    date_current = now - timedelta(hours=5)
    day = '{:02d}'.format(date_current.day)
    
    # valor inicial de busqueda
    file_type = 'csv'
    infer_schema = 'false'
    first_row_is_header = 'true'
    delimiter = ','
    v_current = date_process('yyyymmddhhmmss')
    
    
    file_location_csv = parameter['file_location_csv']
    
    name_file = parameter['name_file']
    partition = parameter['t_partition']
    path_delta = parameter['t_location_delta']
    t_format = parameter['t_format']
    list_day = parameter['t_day']
                        
    
    df = spark.read.format(file_type) \
        .option("inferSchema", infer_schema) \
        .option("multiline", "true") \
        .option("encoding", "utf8") \
        .option("header", first_row_is_header) \
        .option("sep", delimiter) \
        .load(file_location_csv)

    df = df \
        .withColumn('CREATE_AT', f.unix_timestamp(f.lit(v_current), 'yyyy-MM-dd HH:mm:ss').cast("timestamp")) \
        .withColumn('ORIGIN_FILE', f.lit(name_file))
    
    if partition == 'm':
        df = df.withColumn('YEAR_MONTH', f.lit(name_file[0:6]))
    else:
        df = df.withColumn('YEAR_MONTH_DAY', f.lit(name_file[0:8]))
       
    for each in df.columns:
        df = df.withColumnRenamed(each , each.strip())
        
    if (t_format == 'month' ):
        proceso='tabla mensual sin procesar'
        if day in list_day :
                proceso = 'tabla mensual con fecha de carga'
                #print(t_day)
                df.write.mode('append').format('delta').save(path_delta)
    elif (t_format == 'daily')  :
        proceso = 'tabla diaria'
        df.write.mode('append').format('delta').save(path_delta)
    else :
        proceso = 'sin registrar'
  
    return proceso

def validateColumns(df:DataFrame)->DataFrame:
    dfx = df
    for col_name in df.columns: 
    #print(col_name)
        if "/" not in col_name:
            continue
        else:
            #print(col_name)
            new_col_name = col_name.replace('/', '')
            #print(new_col_name)
            dfx = dfx.withColumn(new_col_name,f.col(col_name))
            dfx = dfx.drop(col_name)
    return dfx
  
def valueRoot(value):
    if  value[-1] == '-':
        valor = 'negativo'
        valor = -1* float(value[:-1])
    else: 
        valor = 'positivo'
        valor = float(value)
    return valor


print("****** Version Git *********")

