import sys
import logging

import importlib
from importlib import util
from pathlib import Path 

def load_plug(plug_name):
  path = Path(f"project_bot/plugins/{plug_name}.py")
  print(path)
  name = "project_bot.plugins.{}".format(plug_name)
  spec = importlib.util.spec_from_file_location(name,path) 
  load = importlib.util.module_from_spec(spec) 
  load.logger = logging.getLogger(plug_name) 
  spec.loader.exec_module(load) 
  sys.modules["project_bot.plugins." + plug_name]= load 
  print("INFINITY has Imported " + plug_name)