# Databricks notebook source
import sys 
my_working_path ="/Workspace/Repos/main/alicorp"
if my_working_path not in sys.path:
    sys.path.append(my_working_path)

print("\n".join(sys.path))




# COMMAND ----------


# Databricks notebook source
from common_function.general_functions import max_file_storage

