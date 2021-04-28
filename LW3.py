from math import *
import numpy as np

studentL = {}
def inst(id, name, dob):
    studentL[id] = [name, dob]
def NoS():
    global nos
    nos = int(input("Number of Students: "))
listSt = []
class Student():
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
    
    def print_St(self):
        print("ID student : " + self.id)
        print("Name student : " + self.name)
        print("Dob student : " + self.dob)
    
def CreateList_St():
    for i in range(0,nos):
        listSt.append("s" + str(i))

def In_St():
    print("Enter Student Information: ")
    for i in range(0,nos):
        print("Student " + str(i+1))
        id  = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        DoB = input("Enter Student DoB: ")
        inst(id, name,DoB)
        listSt[i] = Student(id,name,DoB)

def print_St():
    print("All Students: ")
    for i in range(0,nos):
        print("Student " + str(i+1))
        listSt[i].print_St()

 
        
NoS()
CreateList_St()
In_St()
print_St()
class Course:
    def __init__(self, id, name, credit):
        self.c_id = id
        self.c_name = name
        self.credit = credit

    def get_id(self):
        return self.c_id

    def get_name(self):
        return self.c_name

    def get_credit(self):
        return self.credit

    def Course_list(self):
        print("Course's ID: " + self.c_id)
        print("Course's name: " + self.c_name)
        print("Course's credit: " + self.credit)


def CountStudent():
    count = int(input("How many students are there: "))
    return count


def student_detail():
    s_id = input("ID: ")
    s_name = input("Name: ")
    DoB = input("Date of birth: ")
    return s_id, s_name, DoB

def Gpa_sort():
    s_sorted = sorted(students, key=lambda student: student.gpa, reverse=True)
    for student in s_sorted:
        student.Student_list()
        
def CountCourse():
    count = int(input("How many courses are there: "))
    return count


def course_detail():
    c_id = input("ID: ")
    c_name = input("Name: ")
    credit = input("Credit: ")
    return c_id, c_name, credit

def Credit(courses, c_id):
    for course in courses:
        course.get_id() == c_id
        return course.get_credit()

def Add_mark(courses, c_id):
    for course in courses:
        course.get_id() == c_id
        return course.get_name()
#Input Course Info
def setMark():

    global index
    mark = float(input("Mark: "))
    listMark[index] = MarkTable(checkNameStudent, checkNameCourse, floor(mark))
    index += 1

#Print list
def printMarkList():
    print("\n")
    print("----------The Mark List---------- ")
    for i in range(len(listMark)):
        print("---------" + str(i + 1) + "st Record" + "---------")
        listMark[i].getMarkInfo()

#Get Student's Average
def studentAverage():
    nameTemp = input("Student Name you want to get Average: ")
    averageMark(nameTemp)

#Main
index = 0
numberStudent()
createListStudent()
setStudent()
printStudentList()

print("\n")
numberCourse()
createListCourse()
setCourse()
printCourseList()

print("\n")
numberRecord()
for i in range(numberRecord):
    createListMark()
    setMark()
printMarkList()
studentAverage()