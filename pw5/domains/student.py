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