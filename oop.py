#Inheritance - Creating Subclasses
#Inheritance allows us to inherit attributes and methods from a parent class

class Programmer:
    
    language = 'Python'

    def __init__(self, first, last, github, education, website):
        self.first = first
        self.last = last
        self.github = github
        self.education = education
        self.website = website       

    def fullname(self):
        return('My education: {}, My Fullname is {} {}'.format(self.education, self.first, self.last))

    def reveal_github(self):
        return("My github username is {}".format(self.github))

    def open_website(self):
        return("My personal website is {}".format(self.website))


class Book(Programmer):
    def __init__(self, first, last, github, education, website, prog_book, book_link):
        super().__init__(first, last, github, education, website)
        self.prog_book = prog_book
        self.book_link = book_link


    def fullname(self):
        super().fullname()
        return('My education: {}, Programming Books I used: {}, Link to buy it: {}, My Fullname is: {} {}'.format(self.education, self.prog_book, self.book_link, self.first, self.last))

    

b1 = Book('Hamim', 'Phopal', 'hamimphopal50', 'self-taught', 'http://167.71.157.4/', "The Self-Taught Programmer: The Definitive Guide to Programming Professionally", 'https://www.amazon.com/Self-Taught-Programmer-Definitive-Programming-Professionally-ebook/dp/B01M01YDQA')
#p1 = Programmer('Hamim', 'Phopal', 'hamimphopal50', 'self-taught', 'http://167.71.157.4/')

print(b1.fullname())
print(b1.open_website())
print(b1.reveal_github())
#print(b1.book_link)
#print(b1.prog_book)
#print(p1.fullname())
#print(p1.open_website())
#print(p1.reveal_github())
