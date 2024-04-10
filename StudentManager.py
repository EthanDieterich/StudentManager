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
    def __init__ (self, name):
        self.name = name
        self.students = []
        
    def add_Student(self, student):
        self.students.append(student)
        
    def lastName_Sort(self):
        self.students.sort(key = Student.get_lastName)
        print("Roster sorted by last name")
        
    def studentID_Sort(self):
        self.students.sort(key = Student.get_studentID)
        print("sort by student ID")

    def GPA_Sort(self):
        self.students.sort(key = Student.get_gpa)
        print("sort by GPA")
    
    def creditHours_Sort(self):
        self.students.sort(key = Student.get_creditHours)
        print("sort by credit hours")
    
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
        print("---------------")
        print("Name:", self.first_name, self.last_name)
        print("Credits:", self.credit_hours)
        print("Grade Level:", self.year)
        print("GPA(Out of 4.0):", self.gpa)
        
    def get_lastName(self):
        return self.last_name
    
    def get_studentID(self):
        return self.student_id
    
    def get_gpa(self):
        return self.gpa
    
    def get_creditHours(self):
        return self.credit_hours
        
def xml_File_Reader(file_path, roster):
    #Check correct file type
    if not file_path.endswith(".xml"):
        print("Invalid File Type")
        return

    print("Loading:",file_path)
    #Open xml File
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
        
        #make student object and add student to roster
        student = Student(student_id, first_name, last_name, credit_hours,year, gpa)
        roster.add_Student(student)
    return 
      
def json_File_Reader(file_path, roster):
    #Check correct file type
    if not file_path.endswith(".json"):
        print("Invalid File Type")
        return

    print("Loading:",file_path)
    #Open json File
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
        
        #make student object and add student to roster
        student = Student(student_id, first_name, last_name, credit_hours,year, gpa)
        roster.add_Student(student)
    return     
    
def csv_File_Reader(file_path, roster):
    #Check correct file type
    if not file_path.endswith(".csv"):
        print("Invalid File Type")
        return

    print("Loading:",file_path)
    #Open csv File
    with open(file_path,'r') as file:
        csv_reader = csv.reader(file)
        #skip header row
        next(csv_reader)

    # Iterate through each row in the CSV
        for student_data in csv_reader:
            student_id = student_data[0]
            first_name = student_data[1]
            last_name = student_data[2]
            credit_hours = student_data[3]
            year = student_data[4]
            gpa = student_data[5] 
            
        #make student object and add student to roster
            student = Student(student_id, first_name, last_name, credit_hours,year, gpa)
            roster.add_Student(student)
    return 

def any_File_Reader(file_path, roster):
    fileType = file_path[-3:] 
    if fileType == "xml":
        xml_File_Reader(file_path, roster)
    elif fileType == "son":
        json_File_Reader(file_path, roster)
    elif fileType == "csv":
        csv_File_Reader(file_path, roster)
    else:
        print("Invalid File Type")
    return 
    
def folder_Open(file_type, roster):
    file_readers = {
    'xml' : xml_File_Reader,
    'json' : json_File_Reader,
    'csv' : csv_File_Reader,
    'any' : any_File_Reader
    }
    folder_path = os.path.join(os.getcwd(), file_type+"StudentFiles" )
    files = os.listdir(folder_path)
  
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        file_readers[file_type](file_path, roster)
    return
    
def read_Files_Menu(roster):
    file_types = {
        '1' : "xml",
        '2' : "json",
        '3' : "csv",
        '4' : "any"
        }
    print("---------------")
    print("Load Data Menu:")
    print("1. Open .xml type files (xmlStudentFiles)")
    print("2. Open .json type files (jsonStudentFiles)")
    print("3. Open .csv type files (csvStudentFiles)")
    print("4. Open any type files (anyStudentFiles)")
    print("---------------")
    choice = input("Enter Your Choice: ")
    if choice in file_types:
        folder_Open(file_types[choice], roster)
    else: 
        print("Invalid Choice")
    return
        
def sort_Students_Menu(roster):
    print("---------------")
    print("Sort Students Menu:")
    print("1. Sort by last name")
    print("2. Sort by Student ID")
    print("3. Sort by GPA")
    print("4. Sort by Credit Hours")
    print("---------------")
    choice = input("Enter Your Choice: ")
    print()
    match choice:
        case "1":
            roster.lastName_Sort()
        case "2":
            roster.studentID_Sort()
        case "3":
            roster.GPA_Sort()
        case "4":
            roster.creditHours_Sort()
        case _:
            print("Invalid Choice")   
    
def select_Roster_Menu(roster_options):
    while True:
        #Menu Options
        print("---------------")
        print("Roster Selection Menu: ")
        print("0. Create new roster")
        if len(roster_options) == 0:
            print("No existing rosters to select from.")
        else: 
            for key, value in roster_options.items():
                print(str(key)+".", value.name)
        print("---------------")
        choice = input("Enter Your Choice: ")
        
        #User Selection
        if choice in roster_options.keys():
            return roster_options[choice]
        elif choice == "0":
            index = str(len(roster_options)+1)
            roster_name = input("Enter New Roster Name: ")
            roster_options[index] = roster_name
            roster_options[index] = Student_Roster(roster_name)
            return roster_options[index]
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
            case "1":
                read_Files_Menu(roster)
            case "2":
                roster.print_Student_Roster()
            case "3":
                sort_Students_Menu(roster)
            case "4":
                roster = select_Roster_Menu(roster_options)
            case "5":
                print("placeholder")
            case "6":
                print("placeholder")
            case "7":
                print('Goodbye')
                break
            case _:
                print("Invalid Choice")
            
    
    

