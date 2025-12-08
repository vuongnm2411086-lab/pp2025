"""Practical work 1: student mark management
• Functions
• Input functions:
• Input number of students in a class
• Input student information: id, name, DoB
• Input number of courses
• Input course information: id, name
• Select a course, input marks for student in this course

• Listing functions:
• List courses
• List students
• Show student marks for a given course
• Push your work to corresponding forked Github repository"""


import math
import numpy
import curses



studentListLength = int(input("Please input the capacity of the student list (Any negative values will be coverted)> "))
if studentListLength < 0: studentListLength = -1*studentListLength
studentList = []
courseListLength = int(input("Please input the capacity of the course list (Negatives will be converted)> "))
if courseListLength < 0: courseListLength = -1*courseListLength
courseList = []

class student:
    def __init__(self):
        self.__studentID = None
        self.__studentName = None
        self.__dob = None
        self.__GPA = None
    def __setID__(self, id):
        self.__studentID = id
    def __getID__(self):
        return self.__studentID
    def __getName__(self):
        return self.__studentName
    def __setName__(self, name):
        self.__studentName = name
    def __getDOB__(self):
        return self.__dob
    def __setDOB__(self, dob):
        self.__dob = dob
    def __getGPA__(self):
        if self.__GPA == None:
            return -1
        else:
            return self.__GPA
    
    def calcGPA(self):
        studentAllMarks = []
        coursesCredit = []
        for i in courseList:
            studentAllMarks.append(i.__getStudentMarks__()[self.__studentID])
            coursesCredit.append(i.__getCourseCredit__())
        studentAllMarks = numpy.array(studentAllMarks)
        coursesCredit = numpy.array(coursesCredit)
        self.__GPA = numpy.average(studentAllMarks, coursesCredit)
    

class course:
    def __init__(self):
        self.__courseID = None
        self.__courseName = None
        self.__credit = None
        self.__studentMarks = {}
    def __getCourseName__(self):
        return self.__courseName
    def __setCourseName__(self, name):
        self.__courseName = name
    def __getCourseID__(self):
        return self.__courseID
    def __setCourseID__(self, id):
        self.__courseID = id
    def __getCourseCredit__(self):
        return self.__credit
    def __setCourseCredit__(self, credit):
        self.__credit = credit
    def __getStudentMarks__(self):
        return self.__studentMarks
    
    def inputMark(self, studentList):
        if type(studentList) != list:
            print("It should be a list")
        else:
            for i in range(studentList):
                if type(studentList[i]) != object:
                    print("The list should be filled with objects only. Please don't add stuffs to it")
                    break
                else:
                    mark = -1
                    while mark < 0:
                        print("Invalid. Try again")
                        mark = int(input(f"Please input mark for the {studentList[i].__getName__()}"))
                    self.__studentMarks[studentList[i].__getID__()] = math.floor(mark*10)/10


def inputStudent(name, id, dob):
    if studentListLength <= len(studentList):
        print("Capacity over")
        return None
    else:
        newStudent = student()
        newStudent.__setName__(name)
        newStudent.__setID__(id)
        newStudent.__setDOB__(dob)
        studentList.append(newStudent)

def inputCourse(name, id, credit):
    if courseListLength <= len(courseList):
        print("Capacity over")
        return None
    else:
        newCourse = course()
        newCourse.__setCourseName__(name)
        newCourse.__setCourseID__(id)
        newCourse.__setCourseCredit__(credit)
        courseList.append(newCourse)



def listStudent():
    for i in studentList:
        print(i.__getName__())

def listCourse():
    for i in courseList:
        print(i.__getCourseName__())

def sortStudentList():
    sortedStudentList = sorted(studentList, key = lambda student: student.__getGPA__())
    return sortedStudentList
