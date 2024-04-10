# -*- coding: utf-8 -*-
"""
Student Manager by Ethan Dieterich
This code uses 4 folder in the directory anyStudentFiles, xmlStudentFiles, jsonStudentFiles, and csvStudentFiles
"""
import os
import xml.etree.ElementTree as ET
import json
import csv

class Student_Roster:
    def __init__ (self):
        self.students = []
        
    def add_Student(self, student):
        self.students.append(student)
        
    def lastName_sort(self):
        print("sort by last name")
        
    def studentID_sort(self):
        print("sort by student ID")
        
    
    def print_Student_Roster(self):
        for student in self.students:
            Student.display_Student(student) 


class Student:
    def __init__ (self, student_id, first_name, last_name, credit_hours, year, gpa):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.credit_hours = credit_hours
        self.year = year
        self.gpa = gpa
        
    def display_Student(self):
        print("Name:", self.first_name, self.last_name)
        print("Credits:", self.credit_hours)
        print("Grade Level:", self.year)
        print("GPA(Out of 4.0):", self.gpa)
        print("----------------------")
        
def xml_File_Reader(file_path, students):
    print("Loading:",file_path)
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
    print("Loading:",file_path)
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
    print("Loading:",file_path)
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

def any_File_Reader(file_path, students):
    fileType = file_path[-3:] 
    if fileType == "xml":
        xml_File_Reader(file_path, students)
    elif fileType == "son":
        json_File_Reader(file_path, students)
    elif fileType == "csv":
        csv_File_Reader(file_path, students)
    else:
        print("Invalid File Type")
    return students
    
def folder_Open(file_type):
    file_readers = {
    'xml' : xml_File_Reader,
    'json' : json_File_Reader,
    'csv' : csv_File_Reader,
    'any' : any_File_Reader
    }
    folder_path = os.path.join(os.getcwd(), file_type+"StudentFiles" )
    
    files = os.listdir(folder_path)
    
    for file_name in files:
        if file_type[-3:] != file_name[-3] and file_type != "any" :
            print("Invalid File Type")
            continue
        elif 
        file_path = os.path.join(folder_path, file_name)
        file_readers[file_type](file_path, students)
        
    return students
    
def read_Files_Menu(students):
    file_types = {
        '1' : "xml",
        '2' : "json",
        '3' : "csv",
        '4' : "any"
        }
    print("Load Data Menu:")
    print("1. Open .xml type files (xmlStudentFiles)")
    print("2. Open .json type files (jsonStudentFiles)")
    print("3. Open .csv type files (csvStudentFiles)")
    print("4. Open any type files (anyStudentFiles")
    choice = input("Enter Your Choice: ")
    print()
    if choice in file_types:
        students.extend(folder_Open(file_types[choice]))
    else: 
        print("Invalid Choice")
    return students
        
def sort_Students_Menu(roster):
    print("Sort Students Menu:")
    print("1. Sort by last name")
    print("2. Sort by Student ID")
    print("3. Sort by GPA")
    print("4. Sort by Credit Hours")
    choice = input("Enter Your Choice: ")
    print()
    match choice:
        case 1:
            roster.lastName_Sort()
        case 2:
            roster.studentID_Sort()
        case 3:
            roster.GPA_Sort()
        case 4:
            roster.creditHours_Sort()
        case _:
            print("Invalid Choice")
    
    
def select_Roster_Menu(roster_options):
    while True:
        #Menu Options
        print("Student Roster Selection Menu: ")
        print("0. Create new roster")
        if len(roster_options) == 0:
            print("No existing rosters to select from.")
        else: 
            for key, value in roster_options.items():
                print(str(key)+".", value)
        choice = input("Enter Your Choice: ")
        
        #User Selection
        if choice in roster_options:
            return roster_options[choice]
        elif choice == "0":
            index = len(roster_options)+1
            roster_name = input("Enter New Roster Name: ")
            roster_options[index] = roster_name
            roster_options[index] = Student_Roster()
        else:
            print("Invalid Choice")
            
    
if __name__ == '__main__':
    roster_options = {}
    roster = select_Roster_Menu(roster_options)
    
    while True:
        print("---------------")
        print("Main Menu:")
        print("1. Read Files")
        print("2. Print Student Roster")
        print("3. Sort Student Roster")
        print("4. Select/Create Student Roster")
        print("5.")
        print("6. Save Student Roster")
        print("7. Exit")
        print("---------------")    
        choice = input("Enter Your Choice: ")
        
        match choice:
            case 1:
                read_Files_Menu(selected_Roster)
            case 2:
                roster.print_Student_Roster()
            case 3:
                sort_Students_Menu(roster)
            case 4:
                roster = select_Roster_Menu(roster_options)
            case 5:
                print("placeholder")
            case 6:
                print("placeholder")
            case 7:
                print('Goodbye')
                break
            case _:
                print("Invalid Choice")
            
    
    

