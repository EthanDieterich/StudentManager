# -*- coding: utf-8 -*-
"""
Student Manager by Ethan Dieterich
This code uses 3 folder in the directory xmlStudentFiles, jsonStudentFiles, and csvStudentFiles
"""
import os
import xml.etree.ElementTree as ET

class Student:
    def __init__ (self, student_id, first_name, last_name, credit_hours,year, gpa):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.credit_hours = credit_hours
        self.year = year
        self.gpa = gpa
        

def xml_Folder_Open():
    folder_path = os.path.join(os.getcwd()+"\\xmlStudentFiles")
    print(folder_path)
    print(os.listdir(folder_path))
    files = os.listdir(folder_path)
    students = []
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        students.extend(xml_File_Reader(file_path))
        
    return students
        
def xml_File_Reader(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    print(tree.getroot())
    students = []
    
    for student_element in root.findall('student'):    
        student_id = student_element.find("student_id").text
        first_name = student_element.find("first_name").text
        last_name = student_element.find("last_name").text
        credit_hours = student_element.find("credit_hours").text
        year = student_element.find("year").text
        gpa = student_element.find("gpa").text
        
        student = Student(student_id, first_name, last_name, credit_hours,year, gpa)
        students.append(student)
    return students

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
        students = menuOptions[choice]()
    else: 
        print("Invalid Choice")
    return students
        
if __name__ == '__main__':
    student_roster = initialMenu()
    
    
    
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

