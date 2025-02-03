import sched
import time
import logging
import shutil
import os


logging.basicConfig(filename='scheduled.log',level=logging.INFO,format='%(asctime)s %(message)s')

def cleanUpDir(temp_dir):
 #size=os.path.getsize(temp_dir)   
    
    if os.path.exists(temp_dir):
        #logging.info(len(temp_dir))
        #print(os.path.getsize(temp_dir))
        print(os.listdir(temp_dir))
    else:
        print("The directory does not exist")




def checkDuplicateFile(file,temp_dir):
    for files in os.listdir(temp_dir):
        if file == files:
            print(file)
            os.remove(file) 
        #print("These are the files in: \b {}".format(temp_dir))
        #if os.path.isfile(file):
         #   print("{} is a file in a directory!".format(file))
          #  print( os.path.getsize(file))
           # return file
        #else:
         #   print("This file does not exist")


#temp_dir=input("Enter directory you are looking for: ")
#cleanUpDir(temp_dir)        

temp_dir=input("Enter path to directory and file name you are looking for: ")
file=input("Enter file you are looking for: ")
checkDuplicateFile(file,temp_dir)
    


