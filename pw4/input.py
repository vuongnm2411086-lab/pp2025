from domains import student as s
from domains import course as c



studentList = []
courseList = []



def inputStudent(name, id, dob):
    global studentList
    theStudent = s.student()
    theStudent.setName(name)
    theStudent.setID(id)
    theStudent.setDOB(dob)
    studentList.append(theStudent)

def inputCourse(name, id, credit):
    global courseList
    theCourse = c.course()
    theCourse.setCourseName(name)
    theCourse.setCourseID(id)
    theCourse.setCourseCredit(credit)
    courseList.append(theCourse)

def inputMark(theCourse, theStudent, mark):
    import math
    if isinstance(theCourse, c.course) == False or isinstance(theStudent, s.student) == False:
        print("Error 85: Invalid arguments")
    elif len(courseList) <= 0 or len(studentList) <=0:
        print("Error 87: Insufficient list resources")
    elif theCourse not in courseList or theStudent not in studentList:
        print("Error 89: Course or Student does not exist")
    else:
        theStudent.setMarks(theCourse.getCourseName(), math.floor(mark*10)/10)
