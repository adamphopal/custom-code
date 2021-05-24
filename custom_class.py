class Person(object):
    def __init__(self, name):
        self.name = name

    def reveal_username(self):
        print("My name is {}".format(self.name))



class InstaUser(Person):
    def __init__(self, name, insta_name):
        super(InstaUser, self).__init__(name)
        self.insta_name = insta_name

    def reveal_username(self):
        super(InstaUser, self).reveal_username()
        print(".....And my Instagram username is {}".format(self.insta_name))


#hamim = Person('Hamim')
#hamim.reveal_username()

hams = InstaUser('Hamim Phopal', 'hamimphopal')

hams.reveal_username()

drizzy = InstaUser('Drake', 'champagnepapi')

drizzy.reveal_username()
