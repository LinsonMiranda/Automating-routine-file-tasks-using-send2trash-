# -*- coding: utf-8 -*-
"""
Spyder Editor

Python program to delete Res files stored after execution of each TC
"""
import os #library to travese through individual files
from send2trash import send2trash #library object - used to send unwanted file to recycle bin
import re #library for regular expression check

filePath = 'D:\Veolia Automation Framework VAL\Scripts'
count_files_deleted = 0

for folderName, subfolders, filenames in os.walk(filePath):

    pattern = "^Res$|Res[\d]+" #Pattern of file name: Res, Res1, Res2,....
    
    #checks if foldername matches with the Res file name pattern
    if re.search(pattern, folderName):
        #If match found,, increments deleted files count and sends folder to recycle bin
        send2trash(folderName)
        count_files_deleted += 1
        print('Folder ' + folderName + ' has been deleted\n\n' )
        
print('Total no of files deleted: ' + str(count_files_deleted))
