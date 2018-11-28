class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = ''

    def discribe_user(self):
        if self.middle_name:
            full_name = self.first_name + ' ' + self.middle_name
            full_name += ' ' + self.last_name
        else:
            full_name = self.first_name + ' ' +  self.last_name

        print(full_name)

    def greet_user(self):
        print('HELLO! ' + self.first_name.title())

user1 = User('david','liu')
user1.discribe_user()
user1.greet_user()

user2 = User('marry','zhang')
user2.middle_name = 'june'
#句点表示法
user2.discribe_user()
user2.greet_user()

