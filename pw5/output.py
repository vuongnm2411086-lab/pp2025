from domains import student as s
from domains import course as c
from input import courseList
from input import studentList
import input


def listCourse():
    global courseList
    if len(courseList) <= 0:
        print("Warning 96: No courses")
    else:
        for index in range(len(courseList)):
            print(f"{index}. {courseList[index].__str__()}")

def listCourseAlt():
    global courseList
    tempList = []
    if len(courseList) <= 0:
        return tempList
    else:
        for index in range(len(courseList)):
            tempList.append(f"{index}. {courseList[index].__str__()}")
        return tempList

def listStudent():
    global studentList
    if len(studentList) <= 0:
        print("Warning 114: No students")
    else:
        for index in range(len(studentList)):
            print(f"{index}. {studentList[index].__str__()}")

def listStudentAlt():
    global studentList
    tempList = []
    if len(studentList) <= 0:
        return tempList
    else:
        for index in range(len(studentList)):
            tempList.append(f"{index}. {studentList[index].__str__()}")
        return tempList

def showStudentMarks(theCourse):
    global studentList
    if isinstance(theCourse, c.course) == False:
        print("Error 132: Invalid function argument")
    elif theCourse not in courseList:
        print("Error 134: Invalid course")
    elif len(studentList) <= 0:
        print("Warning 136: No students")
    else:
        tempDict = {}
        key = None
        value = None
        for student in studentList:
            key = f"{student.getName()} ({student.getID()})"
            try: value = student.getMarks()[theCourse.getCourseName()]
            except KeyError: value = None
            tempDict[key] = value
        return tempDict
    
def showStudentMarksAlt(theCourse):
    global studentList
    text = "text"
    if isinstance(theCourse, c.course) == False:
        text = "Error 152: Invalid argument"
        return text
    elif theCourse not in courseList:
        text = "Error 155: Object not exist in list"
        return text
    elif len(studentList) <= 0:
        text = "Warning 158: No objects"
        return text
    else:
        tempDict = {}
        key = None
        value = None
        for student in studentList:
            key = f"{student.getName()} ({student.getID()})"
            try: value = student.getMarks()[theCourse.getCourseName()]
            except KeyError: value = None
            tempDict[key] = value
        return tempDict
    
def calcGPA(theStudent):
    import numpy
    import math
    global courseList
    if isinstance(theStudent, s.student) == False:
        print("Error 175: Argument is a not a student")
        return None
    else:
        creditList = []
        marks = numpy.array(list(theStudent.getMarks().values()))
        keyList = list(theStudent.getMarks().keys())
        for key in keyList:
            for theCourse in courseList:
                if key == theCourse.getCourseName():
                    creditList.append(theCourse.getCourseCredit())
        creditList = numpy.array(creditList)
        try: gpa = math.floor(float(numpy.average(a=marks, weights=creditList))*100)/100
        except ZeroDivisionError: 
            #print("Error 188: Divided by zero due to empty course list")
            gpa = None
        return gpa

def sortByGPA():
    global studentList
    tempDict = {}
    sortedStudentList = []
    try: sortedStudentList = sorted(studentList, key=lambda theStudent: calcGPA(theStudent), reverse= True)
    except TypeError: print("Error 197: Unable to sort due to invalid argument(s) for sorted()")
    for theStudent in sortedStudentList:
        tempDict[f"{theStudent.getName()} ({theStudent.getID()})"] = float(calcGPA(theStudent))
    return tempDict

def sortByGPAAlt():
    global studentList
    text = "text"
    tempDict = {}
    sortedStudentList = []
    try: sortedStudentList = sorted(studentList, key=lambda theStudent: calcGPA(theStudent), reverse= True)
    except TypeError: 
        text = "Error 209: Unable to sort due to invalid argument(s)"
        return text
    for theStudent in sortedStudentList:
        try: tempDict[f"{theStudent.getName()} ({theStudent.getID()})"] = float(calcGPA(theStudent))
        except TypeError: tempDict[f"{theStudent.getName()} ({theStudent.getID()})"] = calcGPA(theStudent)
    return tempDict



