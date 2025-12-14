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



class student:
    def __init__(self):
        self.__studentID = None
        self.__studentName = None
        self.__dob = None
        self.__marks = {}
    def setID(self, id):
        self.__studentID = id
    def getID(self):
        return self.__studentID
    def getName(self):
        return self.__studentName
    def setName(self, name):
        self.__studentName = name
    def getDOB(self):
        return self.__dob
    def setDOB(self, dob):
        self.__dob = dob
    def setMarks(self, key, value):
        self.__marks[key] = value
    def getMarks(self):
        return self.__marks
    def __str__(self):
        return f"{self.__studentName}: {self.__studentID}"

class course:
    def __init__(self):
        self.__courseID = None
        self.__courseName = None
    def getCourseName(self):
        return self.__courseName
    def setCourseName(self, name):
        self.__courseName = name
    def getCourseID(self):
        return self.__courseID
    def setCourseID(self, id):
        self.__courseID = id
    def __str__(self):
        return f"{self.__courseName}: {self.__courseID}"



studentList = []
courseList = []



def inputStudent(name, id, dob):
    global studentList
    theStudent = student()
    theStudent.setName(name)
    theStudent.setID(id)
    theStudent.setDOB(dob)
    studentList.append(theStudent)

def inputCourse(name, id):
    global courseList
    theCourse = course()
    theCourse.setCourseName(name)
    theCourse.setCourseID(id)
    courseList.append(theCourse)

def inputMark(theCourse, theStudent, mark):
    if isinstance(theCourse, course) == False or isinstance(theStudent, student) == False:
        print("Error 82: Invalid arguments")
    elif len(courseList) <= 0 or len(studentList) <=0:
        print("Error 84: Insufficient list resources")
    elif theCourse not in courseList or theStudent not in studentList:
        print("Error 86: Course or Student does not exist")
    else:
        theStudent.setMarks(theCourse.getCourseName(), mark)

def listCourse():
    global courseList
    if len(courseList) <= 0:
        print("Warning 92: No courses")
    else:
        for index in range(len(courseList)):
            print(f"{index}. {courseList[index].__str__()}")

def listStudent():
    global studentList
    if len(studentList) <= 0:
        print("Warning 100: No students")
    else:
        for index in range(len(studentList)):
            print(f"{index}. {studentList[index].__str__()}")

def showStudentMarks(theCourse):
    global studentList
    if isinstance(theCourse, course) == False:
        print("Error 109: Invalid argument")
    elif theCourse not in courseList:
        print("Error 111: Object not exist in list")
    elif len(studentList) <= 0:
        print("Warning 111: No objects")
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

def controller():
    import datetime
    import time
    option = 1e-10
    while option != 0:
        print("Choose:")
        print("     1.Input student")
        print("     2.Input course")
        print("     3.Input mark")
        print("     4.List students")
        print("     5.List courses")
        print("     6.Show students' marks for a course")
        print("     0. Exit")
        try:
            option = int(input("You choose?> "))
        except ValueError:
            print("Error 140: Invalid input")
            print()
            time.sleep(1)
            continue
        if option not in range(0,7):
            print("Error 145: Invalid option. Try again")
            print()
            time.sleep(1)
            continue
        else:
            if option == 1:
                print()
                name = input("Enter the student's name> ")
                id = input("Enter the student's ID> ")
                check = False
                while check == False:
                    try:
                        predob = input("Enter the student's DOB (DD/MM/YYYY)> ")
                        middob = datetime.datetime.strptime(predob, "%d/%m/%Y")
                        check = True
                    except ValueError:
                        print("Error 161: Invalid format")
                        continue
                dob = middob.strftime("%d/%m/%Y")
                inputStudent(name, id, dob)
            elif option == 2:
                print()
                name = input("Input course's name> ")
                id = input("Input course's ID> ")
                inputCourse(name, id)
            elif option == 3:
                global studentList
                global courseList
                print()
                choice = -1
                choice2 = -1
                mark = None
                print("Select course: ")
                listCourse()
                try:
                    choice = int(input("You choose?> "))
                except ValueError: 
                    print("Error 179: Invalid input")
                    option = 3
                    print()
                    time.sleep(1)
                    continue
                if choice not in range(len(courseList)):
                    print("Error 188: Option not exist. Try again")
                    option = 3
                    print()
                    time.sleep(1)
                    continue
                print("Select student: ")
                listStudent()
                try: 
                    choice2 = int(input("You choose?> "))
                except ValueError: 
                    print("Error 198: Invalid input")
                    option = 3
                    print()
                    time.sleep(1)
                    continue
                if choice2 not in range(len(studentList)):
                    print("Error 204: Option not exist. Try again")
                    option = 3
                    print()
                    time.sleep(1)
                    continue
                try:
                    mark = int(input("Input mark for the selected student> "))
                except ValueError:
                    print("Error 212: Invalid input")
                    continue
                inputMark(courseList[choice], studentList[choice2], mark)
            elif option == 4:
                print()
                listStudent()
                time.sleep(3)
            elif option == 5:
                print()
                listCourse()
                time.sleep(3)
            elif option == 6:
                print()
                choice = -1
                print("Select course: ")
                listCourse()
                try: choice = int(input("You choose?> "))
                except ValueError: 
                    print("Error 230: Invalid input")
                    option = 6
                    print()
                    time.sleep(1)
                    continue
                if choice not in range(len(courseList)):
                    print("Error 236: Course not exist. Try again")
                    option = 3
                    print()
                    time.sleep(1)
                    continue
                print(showStudentMarks(courseList[choice]))
            elif option == 0:
                option = 0
                pass
            else:
                print("How did you get here? Go back!")
                continue
            time.sleep(0.5)


controller()

