# Databricks notebook source
import sys 

my_working_path ="/Workspace/Repos/main/alicorp"
if my_working_path not in sys.path:
    sys.path.append(my_working_path)

print("\n".join(sys.path))

from common.sample2 import cube_root
cube_root(8)
