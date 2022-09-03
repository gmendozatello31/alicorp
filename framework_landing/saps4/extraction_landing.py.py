# Databricks notebook source
# Databricks notebook source
from common_function.general_functions import max_file_storage

# COMMAND ----------

import sys 
my_working_path ="/Workspace/alicorp/common_function"
if my_working_path not in sys.path:
    sys.path.append(my_working_path)

print (sys.path)    


# COMMAND ----------

from common_function import 
