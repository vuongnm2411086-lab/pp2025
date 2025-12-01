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
    

class course:
    def __init__(self):
        self.__courseID = None
        self.__courseName = None
        self.__studentMarks = {}
    def __getCourseName__(self):
        return self.__courseName
    def __setCourseName__(self, name):
        self.__courseName = name
    def __getCourseID__(self):
        return self.__courseID
    def __setCourseID__(self, id):
        self.__courseID = id
    def __getStudentMarks__(self):
        return self.__studentMarks
    
    def inputMark(self, studentList):
        if type(studentList) != list:
            print("It should be a list")
        else:
            for i in studentList:
                if type(i) != object:
                    print("The list should be filled with objects only. Please don't add stuffs to it")
                    break
                else:
                    mark = -1
                    while mark < 0:
                        print("Invalid. Try again")
                        int(input(f"Please input mark for the {studentList[0].__getName__()}"))
                    self.__studentMarks[studentList[0].__getID__()] = mark


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

def inputCourse(name, id):
    if courseListLength <= len(courseList):
        print("Capacity over")
        return None
    else:
        newCourse = course()
        newCourse.__setCourseName__(name)
        newCourse.__setCourseID__(id)
        courseList.append(newCourse)

def listStudent():
    for i in studentList:
        print(i.__getName__())

def listCourse():
    for i in courseList:
        print(i.__getCourseName__())


