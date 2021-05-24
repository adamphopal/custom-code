#5. create a simple class wit the name "human",
#which would give out the name and age of the person
#example: i am hamim and my age is 25

#2 varialbes, and 4 methods


class human:
    name = None
    age = None
    def get_name(self):
        print("Enter your name")
        self.name=input()
    def get_age(self):
        print("Enter your age")
        self.age=input()
    def put_name(self):
        print("Your name is",self.name)
    def put_age(self):
        print("Your age is",self.age)


person1 = human()
person1.get_name()
person1.get_age()

person1.put_age(), person1.put_name()
        
