# Test #2 Program - Donna Bui - 3/4/2023 - Professor Henry Estrada's COMSC 078
# This program is similar to the GeometricObjects assignment. It will create two Person objects and determine the age of each person.
# The program will also create two Student objects that inherit the methods from the Person class and have gender parameters and incrementing student ID numbers.

from datetime import *
import math

class Person(object):
    
    def __init__(self, fName = "", lName = ""):
        self.firstName = fName
        self.lastName = lName
    
    def getFirstName(self):
        return self.firstName
    
    def getLastName(self):
        return self.lastName
    
    def setBirthday(self, date):
        self.birthday = date
    
    def getBirthday(self):
        return self.birthday
    
    def getAge(self):
        daysOld = (date.today() - self.birthday).days
        yearsOld = math.floor(daysOld/365)
        return str(yearsOld)
    
    def __str__(self):
        return (self.firstName + " " + self.lastName + " is " + self.getAge() + " years old")
     

class Student(Person):
    
    idNum = 1
    
    def __init__(self, fName = "", lName = "", gender = "N/A"):
        Person.__init__(self, fName, lName) # Call inherited constructor to set values for firstname and lastname
        
        self.idNumber = Student.idNum 
        Student.idNum += 1
        
        # Default values
        self.gender = gender
        self.pronoun = "their"

        # Set specific values if gender is specified
        if gender == "Female":
            self.pronoun = "her"
        if gender == "Male":
            self.pronoun = "his"

    def getidNumber(self):
        return self.idNumber

    def __str__(self):
        return(Person.__str__(self) + ", and " + self.pronoun + " student ID is " + str(self.idNumber))

def main():
    Person1 = Person("Barack", "Obama") # Approximately 61 years old as of 2023
    Person1.setBirthday(date(1961, 8, 4))
    p1birthday = Person1.getBirthday().strftime("%B %d, %Y") # extra bonus for fun, format the person's birthday to MonthName Day, Year
    print(Person1, "and was born on", p1birthday) 

    Person2 = Person("Madonna") 
    Person2.setBirthday(date(1958, 8, 16)) # Approximately 64 years old as of 2023
    print(Person2)
    
    Student1 = Student("Abel", "Baker", "Male") # 22 years old as of 2023
    Student1.setBirthday(date(2001, 2, 1))
    print(Student1)
    
    Student2 = Student("Claudette", "Davis", "Female")
    Student2.setBirthday(date(2002, 5, 27))
    print(Student2)
    
    Student3 = Student("TestStudent")
    Student3.setBirthday(date(2000, 1, 1))
    print(Student3)
    
    Student3 = Student("TestStudent", "2", "Non-Binary")
    Student3.setBirthday(date(2000, 4, 21)) 
    print(Student3)

main()



