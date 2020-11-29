def cwd ():
  import os
  path = os.getcwd()
  print(f"current working directory: {path}")
  print ("the directory contains the following")
  for file in os.listdir(path):
    print(file)
  
def run ():
  print ("Processing...")
  cwd()

run()