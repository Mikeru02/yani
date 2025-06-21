# Open function file

import json

def open_file(file):
  data = {}
  with open(file, "r") as data_file:
    data = json.load(data_file)

  return data

