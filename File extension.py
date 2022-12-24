"""
Created on Sun Dec 25 00:41:53 2022

@author: SANJANA
"""
#Program to get the filename from the user and print the extension of the file
#Let file_name be the variable used to store the filename
#Let file_extension be the variable used to store the split up file name
file_name=input("Enter the filename ")
file_extension=file_name.split(".")
if len(file_extension)>0:
    print("The extension of the file is :",file_extension[-1])
else:
    print("Unknown extension")