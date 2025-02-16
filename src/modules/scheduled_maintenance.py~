import sched
import time
import logging
import shutil
import os


logging.basicConfig(filename='scheduled.log',level=logging.INFO,format='%(asctime)s %(message)s')


#This is to clean up the contents of the directory 
def cleanUpDir():
    temp_dir=input("Enter path of directory you want cleaned up: ")
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir) #removes directory 
        os.makedirs(temp_dir) #recreates the directory 
    else:
        print("The directory does not exist")



#This shows the contents of the directory you choose 
def showDirectory():
    temp_dir=input("Enter directory you would like to see: ")
    for files in os.listdir(temp_dir):
        print(files)

#This deletes a file from the directory 
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
    choice_entry= input("Menu:\n 1:Show contents of directory\n 2:Delete a file\n 3:Clean up directory \n Enter menu option:")
    match choice_entry:
        case "1": 
           return showDirectory()
        case "2":
            return deleteFile()
        case "3":
            return cleanUpDir()
        case _:
            return "The Program is closing"



#choice = input("Enter your menu option:\n 1- Show contents of directory\n 2- Delete a file" )
menu()
