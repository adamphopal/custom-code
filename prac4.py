
class student:
    def __init__(self):#constructor we creted with init method
        self.name = input("Enter your name: ")
        self.age = input("Enter your age: ")
        self.major = input("Enter your major: ")

    def print_student(self):    #method
        print("name",self.name)
        print("age", self.age)
        print("major", self.major)


student1 = student()

student1.print_student()
        
