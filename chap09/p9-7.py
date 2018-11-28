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
#子类管理员
class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileges = ['can add post','can delete post','can ban user']

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege.upper())

the_one = Admin('zhang','tiaotun')
the_one.privileges.append('can play the game')

the_one.show_privileges()

