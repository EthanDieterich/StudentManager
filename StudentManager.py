# -*- coding: utf-8 -*-
"""
Student Manager by Ethan Dieterich
This code uses 3 folder in the directory xmlStudentFiles, jsonStudentFiles, and csvStudentFiles
"""
import os
import xml.etree.ElementTree as ET
import json
import csv

class Student:
    def __init__ (self, student_id, first_name, last_name, credit_hours, year, gpa):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.credit_hours = credit_hours
        self.year = year
        self.gpa = gpa
        
    
        
    def display_Student(self):
        print("Name:", self.first_name+",", self.last_name)
        print("Credits:", self.credit_hours)
        print("Grade Level:", self.year)
        print("GPA(Out of 4.0):", self.gpa)
        print("----------------------")
        
    def print_Students(students):
        for student in students:
            Student.display_Student(student) 
   
def xml_File_Reader(file_path, students):
    tree = ET.parse(file_path)
    root = tree.getroot()
    #iterate through each student in xml file
    for student_element in root.findall('student'):    
        student_id = student_element.find("student_id").text
        first_name = student_element.find("first_name").text
        last_name = student_element.find("last_name").text
        credit_hours = student_element.find("credit_hours").text
        year = student_element.find("year").text
        gpa = student_element.find("gpa").text
        
        #make student object and add student to list
        student = Student(student_id, first_name, last_name, credit_hours,year, gpa)
        students.append(student)
    return students
    
    
def json_File_Reader(file_path, students):
    #Open Json File
    with open(file_path, 'r') as file:
        students_data = json.load(file)
    
    student_list = students_data['students']
    #Reads each student dictionary in the list
    for student_data in student_list:
        student_id = student_data['student_id']
        first_name = student_data['first_name']
        last_name = student_data['last_name']
        credit_hours = student_data['credit_hours']
        year = student_data['year']
        gpa = student_data['gpa']
        
        #make student object and add student to list
        student = Student(student_id, first_name, last_name, credit_hours,year, gpa)
        students.append(student)
    return students
        
    
def csv_File_Reader(file_path, students):
    with open(file_path,'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
    # Iterate through each row in the CSV
        for student_data in csv_reader:
            student_id = student_data[0]
            first_name = student_data[1]
            last_name = student_data[2]
            credit_hours = student_data[3]
            year = student_data[4]
            gpa = student_data[5] 
            
        #make student object and add student to list
            student = Student(student_id, first_name, last_name, credit_hours,year, gpa)
            students.append(student)
    return students


    
def folder_Open(file_type):
    file_readers = {
    'xml' : xml_File_Reader,
    'json' : json_File_Reader,
    'csv' : csv_File_Reader
    }
    folder_path = os.path.join(os.getcwd(), file_type+"StudentFiles" )
    #print(folder_path)
    #print(os.listdir(folder_path))
    files = os.listdir(folder_path)
    students = []
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        file_readers[file_type](file_path, students)
        
    return students
    
def read_Files_Menu(students):
    file_types = {
        '1' : "xml",
        '2' : "json",
        '3' : "csv"
        }
    print("Load Data Menu:")
    print("1. Open .xml type files")
    print("2. Open .json type files")
    print("3. Open .csv type files")
    choice = input("Enter Your Choice: ")
    print()
    if choice in file_types:
        students.extend(folder_Open(file_types[choice]))
    else: 
        print("Invalid Choice")
    return students
        
#def read_
    
    
    
if __name__ == '__main__':
    student_roster = []
    menu = {
        '1': read_Files_Menu,
        '2': Student.print_Students,
        #'3': ,
        #'4': ,
        #'5': ,
        #'6': 
        }
    while True:
        print("---------------")
        
        print("Main Menu:")
        print("1. Read Files")
        print("2. Print Student Roster")
        print("3. Sort Student Roster")
        print("4.")
        print("5.")
        print("6. Save Student Roster")
        print("7. Exit")
        print("---------------")
    
        choice = input("Enter Your Choice: ")
        print()
        if choice in menu:
            menu[choice](student_roster)
        elif choice == '7':
            print('bye')
            break
        else:
            print("invalid choice")

    
    
    

