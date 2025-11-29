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


#key:value. Access by using key as index
studentDict = {}  #Student ID: [name, DoB]
courses = {}    #courseID: course name
courseMarks = {}    #courseID:{studentID: grade}
classStudentNumber = 0

def leapYearCheck(year):
    if year % 4 == 0 and year % 100 == 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False



def studentInput():
    global studentDict
    DOB = "dd/mm/yy"
    studentName = str(input("Let's input student's name: "))
    studentID = str(input("Now let's input his/her ID: "))
    print("Now, we input DOB")          
    DOBDate = int(input("First, the date: "))
    DOBMonth = int(input("Second, the month: "))
    DOBYear = int(input("Last, the year: "))
    if DOBYear > 2025:
        print("Year problem: Time travel is real!")
    elif DOBMonth < 1 or DOBMonth > 12:
        print("Month problem: What world does that student come from?")
    elif ((DOBMonth in [4,6,9,11]) and DOBDate > 30) or DOBDate < 1:
        print("Date problem: There is a poem about how many days in a month. Make sure to check that out") 
    elif (DOBMonth not in [4,6,9,11] and DOBDate > 31) or DOBDate < 1:
        print("Date problem: There is a poem about how many days in a month. Make sure to check that out")
    elif ((DOBMonth == 2 and leapYearCheck(DOBYear) == False) and DOBDate > 28) or DOBDate < 1:
        print("Date problem: Do you know there is a leap year rule?")
    elif ((DOBMonth == 2 and leapYearCheck(DOBYear) == True) and DOBDate > 29) or DOBDate < 1:
        print("Date problem: Do you know there is a leap year rule?")
    else:
        DOB = str(DOBDate) + "/" + str(DOBMonth) + "/" + str(DOBYear)
        studentDict[studentID] = [studentName, DOB]

def courseInput():
    global courses
    courseName = str(input("Now let's input the name of the course: "))
    courseID = str(input("Now let's input the ID of the course: "))
    courses[courseID] = courseName

def classInput():
    global classStudentNumber
    classStudentNumber = int(input("How about inputting the number of student in the class?: "))
    if classStudentNumber < 0:
        print("Negative? You must be joking")
    else:
        for i in range(0, classStudentNumber):
            studentInput()

def markInput():
    global courseMarks
    studentsMark = {}
    mark = -1
    print("Here is a list of available courses. Pick one please")
    print(courses)
    courseSelect = str(input("Please input the course you want based on the key: "))
    if courseSelect not in courses.keys():
        print("course input problem: Did you make that key up?")
        return None
    print("Here's the student list. So that you can pick the ID to input after")
    print(studentDict)
    for i in range(0, classStudentNumber):
        studentID = str(input("Please input student's ID: "))
        if studentID not in studentDict.keys():
            print("student ID input problem: Did you make that ID up?")
            return None
        mark = int(input("Input grade: ")) 
        if mark < 0 or mark > 20:
            print("Grade input problem: How did you get that grade?")
            print("Anyway, it seems you have to do this from the start again")
            return None
        studentsMark[studentID] = mark
    courseMarks[courseSelect] = studentsMark

def listCourse():
    print(courses.values())

def listStudent():
    print(studentDict.values())

def showMark():
    studentIDList = list(studentDict.keys())
    print("Here is the course list for you to check")
    print(courses)
    courseID = str(input("Please input courseID (which is one of the keys): "))
    if courseID not in courses.keys():
        print("Yeah, no, this thing is not in the course list")
        return None
    tempList = list(studentDict.values())
    for i in range(0, len(tempList)):
        print(str(tempList[i]) + ": " + str(courseMarks[courseID][studentIDList[i]]))



# --- Testing lines (AI generated) ---

# Manually add some students
studentDict["S01"] = ["Alice", "15/5/2000"]
studentDict["S02"] = ["Bob", "20/7/2001"]
classStudentNumber = 2

# Manually add some courses
courses["C01"] = "Math"
courses["C02"] = "Physics"

# Manually add marks
courseMarks["C01"] = {"S01": 18, "S02": 15}
courseMarks["C02"] = {"S01": 17, "S02": 16}

print("\n--- List of courses ---")
listCourse()

print("\n--- List of students ---")
listStudent()

print("\n--- Show marks for Math ---")
print(courseMarks["C01"])   # quick direct check
