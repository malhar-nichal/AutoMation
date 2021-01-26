#! C:/Python38/python


import shutil

location = ["C:/Users/malha/AppData/Local/Temp","C:/Windows/Temp"]

shutil.rmtree (location[0], ignore_errors = True)
shutil.rmtree (location[1], ignore_errors = True)

print ("Done")
