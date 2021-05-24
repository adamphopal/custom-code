#What do you understand by inheritance? give an example of it
#one class inherits the properties from another class

class fruit:    #the super class
    def __init__(self):
        print("Im a fruit")

class citrus(fruit):   #child class, single level inheritnace 
    def __init__(self):
        super().__init__()
        print("Im a citrus")


Lemon = citrus()
        

