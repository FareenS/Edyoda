class Student:
    def __init__(self):
        self.__name = None
        self.__rollNumber = None

    def getName(self):
        return self.__name

    def setName(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            print("Invalid input for name. Name should be a string.")

    def getRollNumber(self):
        return self.__rollNumber

    def setRollNumber(self, rollNumber):
        if isinstance(rollNumber, int) and rollNumber > 0:
            self.__rollNumber = rollNumber
        else:
            print("Invalid input for roll number. Roll number should be a positive integer.")

student = Student()

student.setName("John")
print("Name:", student.getName())

student.setRollNumber(101)
print("Roll Number:", student.getRollNumber())