#6. what do you understand about by __init__() method in python?
#Give an example of it

class student:
    def __init__(self,name,age,major):#constructor we creted with init method
        self.name = name
        self.age = age
        self.major = major

    def print_student(self):    #method
        print("name",self.name)
        print("age", self.age)
        print("major", self.major)


student1 = student("Hamim",25, "computer science")

student1.print_student()
        
    
