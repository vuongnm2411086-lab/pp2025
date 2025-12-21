from domains import student as s
from domains import course as c



studentList = []
courseList = []



def inputStudent(name, id, dob, writting: bool):
    global studentList
    theStudent = s.student()
    theStudent.setName(name)
    theStudent.setID(id)
    theStudent.setDOB(dob)
    studentList.append(theStudent)

    if writting == True:
        with open(file="students.txt", mode="a") as file:
            file.write(f"{name}\n{id}\n{dob}\n\n")
        
def inputCourse(name, id, credit, writting: bool):
    global courseList
    theCourse = c.course()
    theCourse.setCourseName(name)
    theCourse.setCourseID(id)
    theCourse.setCourseCredit(credit)
    courseList.append(theCourse)

    if writting == True:
        with open(file="courses.txt", mode="a") as file:
            file.write(f"{name}\n{id}\n{credit}\n\n")

def inputMark(theCourse, theStudent, mark, writting: bool):
    import math
    if isinstance(theCourse, c.course) == False or isinstance(theStudent, s.student) == False:
        print("Error 85: Invalid arguments")
    elif len(courseList) <= 0 or len(studentList) <=0:
        print("Error 87: Insufficient list resources")
    elif theCourse not in courseList or theStudent not in studentList:
        print("Error 89: Course or Student does not exist")
    else:
        theStudent.setMarks(theCourse.getCourseName(), math.floor(mark*10)/10)
    
    if writting == True:
        with open(file="marks.txt", mode="a") as file:
            file.write(f"{theCourse.getCourseName()}\n{theStudent.getID()}\n{mark}\n\n")
        with open(file="marks2.txt", mode="a") as file:
            file.write(f"{theCourse.getCourseName()}\n{theStudent.getName()}\n{mark}\n\n")
        