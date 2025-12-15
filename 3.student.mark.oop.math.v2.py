"""Practical work 3: some maths and decorations
• Copy your practical work 2 to 3.student.mark.oop.math.py
• Use math module to round-down student scores to 1-digit
decimal upon input, floor()
• Use numpy module and its array to
• Add function to calculate average GPA for a given student
• Weighted sum of credits and marks
• Sort student list by GPA descending
• Decorate your UI with curses module
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
        self.__credit = None
    def getCourseName(self):
        return self.__courseName
    def setCourseName(self, name):
        self.__courseName = name
    def getCourseID(self):
        return self.__courseID
    def setCourseID(self, id):
        self.__courseID = id
    def setCourseCredit(self, credit):
        self.__credit = credit
    def getCourseCredit(self):
        return self.__credit
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

def inputCourse(name, id, credit):
    global courseList
    theCourse = course()
    theCourse.setCourseName(name)
    theCourse.setCourseID(id)
    theCourse.setCourseCredit(credit)
    courseList.append(theCourse)

def inputMark(theCourse, theStudent, mark):
    import math
    if isinstance(theCourse, course) == False or isinstance(theStudent, student) == False:
        print("Error 85: Invalid arguments")
    elif len(courseList) <= 0 or len(studentList) <=0:
        print("Error 87: Insufficient list resources")
    elif theCourse not in courseList or theStudent not in studentList:
        print("Error 89: Course or Student does not exist")
    else:
        theStudent.setMarks(theCourse.getCourseName(), math.floor(mark*10)/10)

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
    if isinstance(theCourse, course) == False:
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
    if isinstance(theCourse, course) == False:
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
    if isinstance(theStudent, student) == False:
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
            print("Error 188: Divided by zero due to empty course list")
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
        tempDict[f"{theStudent.getName()} ({theStudent.getID()})"] = float(calcGPA(theStudent))
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
        print("     7.Calculate GPA of a student")
        print("     8.Sort the student list by GPA in descending order")
        print("     0.Exit")
        try:
            option = int(input("You choose?> "))
        except ValueError:
            print("Error 233: Invalid input")
            print()
            time.sleep(1)
            continue
        if option not in range(0,9):
            print("Error 238: Invalid option. Try again")
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
                        print("Error 254: Invalid format")
                        continue
                dob = middob.strftime("%d/%m/%Y")
                inputStudent(name, id, dob)
            elif option == 2:
                print()
                name = input("Input course's name> ")
                id = input("Input course's ID> ")
                try: credit = int(input("Input course's credit> "))
                except ValueError: 
                    print("Error 264: Invalid input")
                    option = 2
                    continue
                inputCourse(name, id, credit)
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
                    print("Error 280: Invalid input")
                    option = 3
                    print()
                    time.sleep(1)
                    continue
                if choice not in range(len(courseList)):
                    print("Error 286: Option not exist. Try again")
                    option = 3
                    print()
                    time.sleep(1)
                    continue
                print("Select student: ")
                listStudent()
                try: 
                    choice2 = int(input("You choose?> "))
                except ValueError: 
                    print("Error 296: Invalid input")
                    option = 3
                    print()
                    time.sleep(1)
                    continue
                if choice2 not in range(len(studentList)):
                    print("Error 302: Option not exist. Try again")
                    option = 3
                    print()
                    time.sleep(1)
                    continue
                try:
                    mark = int(input("Input mark for the selected student> "))
                except ValueError:
                    print("Error 310: Invalid input")
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
                    print("Error 328: Invalid input")
                    option = 6
                    print()
                    time.sleep(1)
                    continue
                if choice not in range(len(courseList)):
                    print("Error 334: Course not exist. Try again")
                    option = 3
                    print()
                    time.sleep(1)
                    continue
                print(showStudentMarks(courseList[choice]))
            elif option == 7:
                choice = -1
                print()
                print("Select student: ")
                listStudent()
                try: 
                    choice = int(input("You choose?> "))
                except ValueError: 
                    print("Error 348: Invalid input")
                    option = 7
                    print()
                    time.sleep(1)
                    continue
                if choice not in range(len(studentList)):
                    print("Error 354: Option not exist. Try again")
                    option = 7
                    print()
                    time.sleep(1)
                    continue
                print(f"GPA (All unassigned grade = 0) = {calcGPA(studentList[choice])}")
                time.sleep(3)
            elif option == 8:
                print()
                print(sortByGPA())
                time.sleep(3)
            elif option == 0:
                option = 0
                pass
            else:
                print("How did you get here? Go back!")
                continue
            time.sleep(0.5)

#controller()


import curses
def main(stdscr):
    import time
    import datetime
    option = -1
    curses.curs_set(1)
    curses.echo()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_WHITE)
    stdscr.clear()
    while option != 0:
        stdscr.addstr(0,40,"Welcome to buttered version of the program", curses.color_pair(3))
        stdscr.addstr(1,50, "Let's get started", curses.color_pair(4))
        stdscr.addstr(3,0,"Choose:", curses.color_pair(3))
        stdscr.addstr(4,6,"1.Input student", curses.color_pair(1))
        stdscr.addstr(5,6,"2.Input course", curses.color_pair(1))
        stdscr.addstr(6,6,"3.Input mark", curses.color_pair(1))
        stdscr.addstr(7,6,"4.List students", curses.color_pair(1))
        stdscr.addstr(8,6,"5.List courses", curses.color_pair(1))
        stdscr.addstr(9,6,"6.Show students' marks for a course", curses.color_pair(1))
        stdscr.addstr(10,6,"7.Calculate GPA of a student", curses.color_pair(1))
        stdscr.addstr(11,6,"8.Sort the student list by GPA in descending order", curses.color_pair(1))
        stdscr.addstr(12,6,"0.Exit",curses.color_pair(1))

        stdscr.refresh()

        while option not in range(9):
            stdscr.addstr(14,0,"You choose?> ", curses.color_pair(5))
            stdscr.refresh()
            window = curses.newwin(1,50, 14, 13)
            option = window.getstr(0,0,3)
            option = option.decode('utf-8')
            try: option = int(option)
            except ValueError: 
                window = curses.newwin(1, 50, 15, 0)
                window.addstr(0,0,"Error 415: Invalid option", curses.color_pair(2))
                window.refresh()
                time.sleep(0.5)
                window.clear()
                window.refresh()
                option = -1
                continue
            if option not in range(9):
                window = curses.newwin(1, 50, 15, 0)
                window.addstr(0,0,"Error 424: Invalid option", curses.color_pair(2))
                window.refresh()
                time.sleep(0.5)
                window.clear()
                window.refresh()
                option = -1
                continue
            time.sleep(0.5)


        stdscr.clear()
        stdscr.refresh()
        if option == 1:
            stdscr.addstr(0,0,"Enter the student's name> ", curses.color_pair(5))
            stdscr.refresh()
            name = stdscr.getstr(0,26,50)
            name = name.decode('utf-8')
            stdscr.addstr(1,0,"Enter the student's ID> ", curses.color_pair(5))
            stdscr.refresh()
            id = stdscr.getstr(1,24, 50)
            id = id.decode('utf-8')
            window = curses.newwin(2, 100, 2, 0)
            check = False
            while check == False:
                try:
                    window.addstr(0,0, "Enter the student's DOB (DD/MM/YYYY)> ", curses.color_pair(5))
                    window.refresh()
                    predob = window.getstr(0,38, 16)
                    predob = predob.decode('utf-8')
                    middob = datetime.datetime.strptime(predob, "%d/%m/%Y")
                    check = True
                except ValueError:
                    window.addstr(1,0, "Error 447: Invalid format", curses.color_pair(2))
                    window.refresh()
                    time.sleep(0.5)
                    option = -1
                    window.clear()
                    window.refresh()
                    continue
            dob = middob.strftime("%d/%m/%Y")
            inputStudent(name, id, dob)
            option = -1
            window.clear()
            window.refresh()
            stdscr.clear()
            stdscr.refresh()
        elif option == 2:
            stdscr.addstr(0,0, "Input course's name> ", curses.color_pair(5))
            stdscr.refresh()
            name = stdscr.getstr(0, 21, 50)
            name = name.decode('utf-8')
            stdscr.addstr(1,0, "Input course's ID> ", curses.color_pair(5))
            stdscr.refresh()
            id = stdscr.getstr(1, 19, 50)
            id = id.decode('utf-8')
            try: 
                stdscr.addstr(2, 0, "Input course's credit> ", curses.color_pair(5))
                stdscr.refresh()
                credit = stdscr.getstr(2, 23, 5)
                credit = credit.decode('utf-8')
                credit = int(credit)
            except ValueError:
                stdscr.addstr(3,0,"Error 477: Invalid input", curses.color_pair(2))
                stdscr.refresh()
                option = 2
                stdscr.clear()
                stdscr.refresh()
                option = -1
                continue
            inputCourse(name, id, credit)
            option = -1
            stdscr.clear()
            stdscr.refresh()
        elif option == 3:
            global studentList
            global courseList
            choice = -1
            choice2 = -1
            mark = None
            position = 0
            maxIndex = 0
            stdscr.addstr(position,0,"Select course: ", curses.color_pair(3))
            stdscr.refresh()
            position += 1
            if len(listCourseAlt()) <= 0:
                stdscr.addstr(position, 0, "Warning 500: No courses", curses.color_pair(4))
                stdscr.refresh()
                time.sleep(1)
                position += 1
                option = -1
                stdscr.clear()
                stdscr.refresh()
                continue
            else:
                for index in range(len(listCourseAlt())):
                    stdscr.addstr(position + index, 0, listCourseAlt()[index], curses.color_pair(1))
                    maxIndex += 1
                position += maxIndex
                maxIndex = 0
                stdscr.refresh()
            try:
                stdscr.addstr(position, 0, "You choose?> ", curses.color_pair(5))
                stdscr.refresh()
                choice = stdscr.getstr(position, 13, 5)
                choice = choice.decode('utf-8')
                choice = int(choice)
                position += 1
            except ValueError:
                position += 1
                stdscr.addstr(position, 0, "Error 524: Invalid input", curses.color_pair(2))
                stdscr.refresh()
                position += 1
                option = -1
                time.sleep(1)
                stdscr.clear()
                stdscr.refresh()
                continue
            if choice not in range(len(courseList)):
                stdscr.addstr(position, 0, "Error 533: Option not exist. Try again", curses.color_pair(2))
                stdscr.refresh()
                position += 1
                option = -1
                stdscr.clear()
                stdscr.refresh()
                time.sleep(1)
                continue
            stdscr.addstr(position, 0, "Select student: ", curses.color_pair(3))
            position += 1
            stdscr.refresh()
            if len(listStudentAlt()) <= 0:
                stdscr.addstr(position, 0, "Warning 545: No students", curses.color_pair(4))
                stdscr.refresh()
                time.sleep(1)
                position += 1
                option = -1
                stdscr.clear()
                stdscr.refresh()
                continue
            else:
                for index in range(len(listStudentAlt())):
                    stdscr.addstr(position+index, 0, listStudentAlt()[index], curses.color_pair(1))
                    maxIndex += 1
                position += maxIndex
                maxIndex = 0
                stdscr.refresh()
            try: 
                stdscr.addstr(position, 0, "You choose?> ", curses.color_pair(5))
                stdscr.refresh()
                choice2 = stdscr.getstr(position, 13, 5)
                choice2 = choice2.decode('utf-8')
                choice2 = int(choice2)
                position += 1
            except ValueError:
                position += 1
                stdscr.addstr(position, 0, "Error 569: Invalid input", curses.color_pair(2))
                stdscr.refresh()
                option = -1
                time.sleep(1)
                position += 1
                stdscr.clear()
                stdscr.refresh()
                continue
            if choice2 not in range(len(studentList)):
                stdscr.addstr(position, 0, "Error 578: Option not exist. Try again", curses.color_pair(2))
                stdscr.refresh()
                option = -1
                time.sleep(1)
                position += 1
                stdscr.clear()
                stdscr.refresh()
                continue
            try:
                stdscr.addstr(position, 0, "Input mark for the selected student> ", curses.color_pair(5))
                stdscr.refresh()
                mark = stdscr.getstr(position, 37, 5)
                mark = mark.decode('utf-8')
                mark = int(mark)
                position += 1
            except ValueError:
                position += 1
                stdscr.addstr(position, 0, "Error 595: Invalid input", curses.color_pair(2))
                stdscr.refresh()
                time.sleep(1)
                position += 1
                option = -1
                stdscr.clear()
                stdscr.refresh()
                continue
            inputMark(courseList[choice], studentList[choice2], mark)
            option = -1
            time.sleep(1)
            stdscr.clear()
            stdscr.refresh()
        elif option == 4:
            position = 0
            maxIndex = 0
            if len(listStudentAlt()) <= 0:
                stdscr.addstr(position, 0, "(empty)", curses.color_pair(6))
                stdscr.refresh()
                time.sleep(1)
                position += 1
                option = -1
                stdscr.clear()
                stdscr.refresh()
                continue
            else:
                for index in range(len(listStudentAlt())):
                    stdscr.addstr(position+index, 0, listStudentAlt()[index], curses.color_pair(1))
                    maxIndex += 1
                position += maxIndex
                maxIndex = 0
                stdscr.refresh()
            time.sleep(3)
            option = -1
            stdscr.clear()
            stdscr.refresh()
        elif option == 5:
            position = 0
            maxIndex = 0
            if len(listCourseAlt()) <= 0:
                stdscr.addstr(position, 0, "(empty)", curses.color_pair(6))
                stdscr.refresh()
                time.sleep(1)
                position += 1
                option = -1
                stdscr.clear()
                stdscr.refresh()
                continue
            else:
                for index in range(len(listCourseAlt())):
                    stdscr.addstr(position + index, 0, listCourseAlt()[index], curses.color_pair(1))
                    maxIndex += 1
                position += maxIndex
                maxIndex = 0
                stdscr.refresh()
            time.sleep(3)
            option = -1
            stdscr.clear()
            stdscr.refresh()
        elif option == 6:
            choice = -1
            position = 0
            maxIndex = 0
            stdscr.addstr(0,0,"Select course: ", curses.color_pair(3))
            stdscr.refresh()
            if len(listCourseAlt()) <= 0:
                stdscr.addstr(position, 0, "(empty)", curses.color_pair(6))
                stdscr.refresh()
                time.sleep(1)
                position += 1
                option = -1
                stdscr.clear()
                stdscr.refresh()
                continue
            else:
                for index in range(len(listCourseAlt())):
                    stdscr.addstr(position + index, 0, listCourseAlt()[index], curses.color_pair(1))
                    maxIndex += 1
                position += maxIndex
                maxIndex = 0
                stdscr.refresh()
            try:
                stdscr.addstr(position, 0, "You choose?> ", curses.color_pair(5))
                stdscr.refresh()
                choice = stdscr.getstr(position, 13, 5)
                choice = choice.decode('utf-8')
                choice = int(choice)
                position += 1
            except ValueError: 
                position += 1
                stdscr.addstr(position, 0, "Error 685: Invalid input", curses.color_pair(2))
                stdscr.refresh()
                position += 1
                time.sleep(1)
                option = -1
                stdscr.clear()
                stdscr.refresh()
                continue
            if choice not in range(len(courseList)):
                stdscr.addstr(position, 0, "Error 694: Course not exist. Try again", curses.color_pair(2))
                stdscr.refresh()
                position += 1
                time.sleep(1)
                option = -1
                stdscr.clear()
                stdscr.refresh()
                continue
            stdscr.clear()
            stdscr.refresh()
            maxIndex = 0
            if type(showStudentMarksAlt(courseList[choice])) == str:
                if showStudentMarksAlt(courseList[choice])[0:8] == "Warning ":
                    stdscr.addstr(0,0, showStudentMarksAlt(courseList[choice]), curses.color_pair(4))
                else:
                    stdscr.addstr(0,0, showStudentMarksAlt(courseList[choice]), curses.color_pair(2))
                stdscr.refresh()
                time.sleep(1)
                stdscr.clear()
                stdscr.refresh()
                option = -1
                continue
            else:
                tempList = list(showStudentMarksAlt(courseList[choice]).keys())
                for index in range(len(showStudentMarks(courseList[choice]))):
                    stdscr.addstr(maxIndex + index, 0, f"{tempList[index]}: {showStudentMarks(courseList[choice])[tempList[index]]}", curses.color_pair(1))
                    maxIndex += 1
                maxIndex = 0
                stdscr.refresh()
                time.sleep(3)
                option = -1
                stdscr.clear()
                stdscr.refresh()
        elif option == 7:
            choice = -1
            position = 0
            maxIndex = 0
            stdscr.addstr(0,0,"Select student: ", curses.color_pair(3))
            position += 1
            stdscr.refresh()
            if len(listStudentAlt()) <= 0:
                stdscr.addstr(position, 0, "(empty)", curses.color_pair(6))
                stdscr.refresh()
                time.sleep(1)
                position += 1
                option = -1
                stdscr.clear()
                stdscr.refresh()
                continue
            else:
                for index in range(len(listStudentAlt())):
                    stdscr.addstr(position+index, 0, listStudentAlt()[index], curses.color_pair(1))
                    maxIndex += 1
                position += maxIndex
                maxIndex = 0
                stdscr.refresh()
                try: 
                    stdscr.addstr(position, 0, "You choose?> ", curses.color_pair(5))
                    stdscr.refresh()
                    choice = stdscr.getstr(position, 13, 5)
                    choice = choice.decode('utf-8')
                    choice = int(choice)
                    position += 1
                except ValueError: 
                    position += 1
                    stdscr.addstr(position, 0, "Error 758: Invalid input", curses.color_pair(2))
                    stdscr.refresh()
                    time.sleep(1)
                    option = -1
                    stdscr.clear()
                    stdscr.refresh()
                    continue
                if choice not in range(len(studentList)):
                    stdscr.addstr(position, 0, "Error 766: Option not exist. Try again", curses.color_pair(2))
                    stdscr.refresh()
                    time.sleep(1)
                    option = -1
                    stdscr.clear()
                    stdscr.refresh()
                    continue
                stdscr.addstr(position, 0, f"GPA (All unassigned grade = 0) = {calcGPA(studentList[choice])}", curses.color_pair(1))
                stdscr.refresh()
                time.sleep(3)
                option = -1
                stdscr.clear()
                stdscr.refresh()
        elif option == 8:
            maxIndex = 0
            if type(sortByGPAAlt()) == str:
                stdscr.addstr(0,0, sortByGPAAlt(), curses.color_pair(2))
                stdscr.refresh()
                time.sleep(1)
                stdscr.clear()
                stdscr.refresh()
                option = -1
                continue
            else:
                if len(sortByGPAAlt()) <= 0:
                    stdscr.addstr(0,0, "(Empty)", curses.color_pair(6))
                else:
                    tempList = list(sortByGPAAlt().keys())
                    for index in range(len(sortByGPAAlt())):
                        stdscr.addstr(maxIndex + index, 0, f"{tempList[index]}: {sortByGPAAlt()[tempList[index]]}", curses.color_pair(1))
                        maxIndex += 1
                    maxIndex = 0
                stdscr.refresh()
                time.sleep(3)
                option = -1
                stdscr.clear()
                stdscr.refresh()
        elif option == 0:
            option = 0
            pass
        else:
            stdscr.addstr(0,0,"How did you get here? Go back!", curses.color_pair(3))
            stdscr.refresh()
            time.sleep(0.5)
            continue
    stdscr.refresh()
curses.wrapper(main)

