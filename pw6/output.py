from domains import student as s
from domains import course as c
import input


def listCourse():
    
    if len(input.courseList) <= 0:
        print("Warning 96: No courses")
    else:
        for index in range(len(input.courseList)):
            print(f"{index}. {input.courseList[index].__str__()}")

def listCourseAlt():
    
    tempList = []
    if len(input.courseList) <= 0:
        return tempList
    else:
        for index in range(len(input.courseList)):
            tempList.append(f"{index}. {input.courseList[index].__str__()}")
        return tempList

def listStudent():
    
    if len(input.studentList) <= 0:
        print("Warning 114: No students")
    else:
        for index in range(len(input.studentList)):
            print(f"{index}. {input.studentList[index].__str__()}")

def listStudentAlt():
    
    tempList = []
    if len(input.studentList) <= 0:
        return tempList
    else:
        for index in range(len(input.studentList)):
            tempList.append(f"{index}. {input.studentList[index].__str__()}")
        return tempList

def showStudentMarks(theCourse):
    
    if isinstance(theCourse, c.course) == False:
        print("Error 132: Invalid function argument")
    elif theCourse not in input.courseList:
        print("Error 134: Invalid course")
    elif len(input.studentList) <= 0:
        print("Warning 136: No students")
    else:
        tempDict = {}
        key = None
        value = None
        for student in input.studentList:
            key = f"{student.getName()} ({student.getID()})"
            try: value = student.getMarks()[theCourse.getCourseName()]
            except KeyError: value = None
            tempDict[key] = value
        return tempDict
    
def showStudentMarksAlt(theCourse):
    
    text = "text"
    if isinstance(theCourse, c.course) == False:
        text = "Error 152: Invalid argument"
        return text
    elif theCourse not in input.courseList:
        text = "Error 155: Object not exist in list"
        return text
    elif len(input.studentList) <= 0:
        text = "Warning 158: No objects"
        return text
    else:
        tempDict = {}
        key = None
        value = None
        for student in input.studentList:
            key = f"{student.getName()} ({student.getID()})"
            try: value = student.getMarks()[theCourse.getCourseName()]
            except KeyError: value = None
            tempDict[key] = value
        return tempDict
    
def calcGPA(theStudent):
    import numpy
    import math
    
    if isinstance(theStudent, s.student) == False:
        print("Error 175: Argument is a not a student")
        return None
    else:
        creditList = []
        marks = numpy.array(list(theStudent.getMarks().values()))
        keyList = list(theStudent.getMarks().keys())
        for key in keyList:
            for theCourse in input.courseList:
                if key == theCourse.getCourseName():
                    creditList.append(theCourse.getCourseCredit())
        creditList = numpy.array(creditList)
        try: gpa = math.floor(float(numpy.average(a=marks, weights=creditList))*100)/100
        except ZeroDivisionError: 
            #print("Error 188: Divided by zero due to empty course list")
            gpa = None
        return gpa

def sortByGPA():
    
    tempDict = {}
    sortedstudentList = []
    try: sortedstudentList = sorted(input.studentList, key=lambda theStudent: calcGPA(theStudent), reverse= True)
    except TypeError: print("Error 197: Unable to sort due to invalid argument(s) for sorted()")
    for theStudent in sortedstudentList:
        tempDict[f"{theStudent.getName()} ({theStudent.getID()})"] = float(calcGPA(theStudent))
    return tempDict

def sortByGPAAlt():
    
    text = "text"
    tempDict = {}
    sortedstudentList = []
    try: sortedstudentList = sorted(input.studentList, key=lambda theStudent: calcGPA(theStudent), reverse= True)
    except TypeError: 
        text = "Error 209: Unable to sort due to invalid argument(s)"
        return text
    for theStudent in sortedstudentList:
        try: tempDict[f"{theStudent.getName()} ({theStudent.getID()})"] = float(calcGPA(theStudent))
        except TypeError: tempDict[f"{theStudent.getName()} ({theStudent.getID()})"] = calcGPA(theStudent)
    return tempDict



