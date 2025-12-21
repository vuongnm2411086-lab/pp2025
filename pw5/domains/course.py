
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
