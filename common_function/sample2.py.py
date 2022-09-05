# Databricks notebook source
def cube_root(n):
    print("The cube root of", n, "is", n**(1.0/3))

# COMMAND ----------

print("\n".join(sys.path))

# COMMAND ----------

import sys
import os
sys.path.append(os.path.abspath('/Workspace/Repos/gmendozatello@gmail.com/alicorp/'))
 
from common.sample2 import cube_root
cube_root(8)
