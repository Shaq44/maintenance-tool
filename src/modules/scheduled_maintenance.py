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
        print(os.path.getsize(temp_dir))
    else:
        print("The directory does not exist")


temp_dir=input("Enter directory you are looking for: ")
cleanUpDir(temp_dir)        
    


