# -*- coding: utf-8 -*-
"""
Student Manager by Ethan Dieterich
This code uses 3 folder in the directory xmlStudentFiles, jsonStudentFiles, and csvStudentFiles
"""
import os
import xml.etree.ElementTree as ET
import json

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
    
def json_File_Reader(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    print(data)
   
def folder_Open(folder_name):
    folder_path = os.path.join(os.getcwd(), folder_name)
    print(folder_path)
    print(os.listdir(folder_path))
    files = os.listdir(folder_path)
    students = []
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        students.extend(xml_File_Reader(file_path))
    return students
    
def csv_Folder_Open():
    print("open csv")

def initialMenu():
    folder_Names = {
        '1' : "xmlStudentFiles",
        '2' : "jsonStudentFiles",
        '3' : "csvStudentFiles"
        }
    print("Opening Student File Menu:")
    print("1. Open .xml type files")
    print("2. Open .json type files")
    print("3. Open .csv type files")
    choice = input("Enter Your Choice: ")
    print()
    if choice in folder_Names:
        students = folder_Open(folder_Names[choice])
    else: 
        print("Invalid Choice")
    return students
        
if __name__ == '__main__':
    student_roster = initialMenu()
    Student.print_Students(student_roster)
    
    

