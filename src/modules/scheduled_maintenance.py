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




def showDirectory():
    temp_dir=input("Enter directory you would like to see: ")
    for files in os.listdir(temp_dir):
        print(files)
            
def deleteFile():
    file=input("Enter file you wish to delete: ")
    if os.path.isfile(file):
        os.remove(file)
        print("File was deleted")
    else:
        print("This is not a file")    



#temp_dir=input("Enter directory you are looking for: ")
#cleanUpDir(temp_dir)        
    
#file = input("Enter file you wish delete: ")
#deleteFile(file)

#temp_dir= input("Enter directory you would like to see: ")
#showDirectory(temp_dir)

def menu():
    choice_entry= input("Menu:\n 1:Show contents of directory\n 2:Delete a file \n Enter menu option:")
    match choice_entry:
        case "1": 
           return showDirectory()
        case "2":
            return deleteFile()
        case _:
            return "The Program is closing"



#choice = input("Enter your menu option:\n 1- Show contents of directory\n 2- Delete a file" )
menu()
