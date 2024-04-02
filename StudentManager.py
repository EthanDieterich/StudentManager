# -*- coding: utf-8 -*-
"""
Student Manager by Ethan Dieterich
This code uses 3 folder in the directory xmlStudentFiles, jsonStudentFiles, and csvStudentFiles
"""
import os

def xml_Folder_Open():
    path = os.getcwd()+"\\xmlStudentFiles"
    print(path)
    print(os.listdir(path))
    
def json_Folder_Open():
    print("open json")
    
def csv_Folder_Open():
    print("open csv")

def initialMenu():
    menuOptions = {
        '1' : xml_Folder_Open,
        '2' : json_Folder_Open,
        '3' : csv_Folder_Open
        }
    print("Opening Student File Menu:")
    print("1. Open .xml type files")
    print("2. Open .json type files")
    print("3. Open .csv type files")
    choice = input("Enter Your Choice: ")
    print()
    if choice in menuOptions:
        menuOptions[choice]()
    else: 
        print("Invalid Choice")
        
if __name__ == '__main__':
    initialMenu()
    
    """
    while True:
        print("---------------")
        csv_file.display_data()
        
        print("Menu:")
        print("1. Open Record")
        print("2. Close and Save Record")
        print("3. Add to Record")
        print("4. Delete from Record")
        print("5. Sum Record")
        print("6. Sort Record")
        print("7. Exit")
        print("---------------")
    
        choice = input("Enter Your Choice: ")
        print()
        if choice in menu:
            menu[choice]()
        elif choice == '7':
            print('bye')
            break
        else:
            print("invalid choice")
    """

