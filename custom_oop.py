#regular methods, classmethods and staticmethods
#Regular methods automatically take the instance as the first agrument
#Class methods are methods that automatically take the class as the first argument
#Static methods do not take the instance or the class as the first argument.
#They behave just like normal functions, yet they should have some logical connection to our class.

class Programmer:
    
    language = 'Python'

    def __init__(self, first, last, github, education, website):
        self.first = first
        self.last = last
        self.github = github
        self.education = education
        self.website = website       
#regular method taking the instance as the first arguemnt
    def fullname(self):
        return('My education: {}, My Fullname is {} {}'.format(self.education, self.first, self.last))

    def reveal_github(self):
        return("My github username is {}".format(self.github))

    def open_website(self):
        return("My personal website is {}".format(self.website))
#Class methods, we use decorators to alter the funtionality, so you get a class as the first arguemnt
    @classmethod
    def getLanguage(cls):
        return cls.language
#Static methods do not take the instance or the class as the first argument
    @staticmethod
    def info():
        print("This is a Programmer class....using the static method on the info method")



p1 = Programmer('Hamim', 'Phopal', 'hamimphopal50', 'self-taught', 'http://167.71.157.4/')

print(p1.fullname())
print(p1.open_website())
print(p1.reveal_github())
print(Programmer.getLanguage())

Programmer.info()
