class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = ''
        self.login_attemps = 0

    def discribe_user(self):
        if self.middle_name:
            full_name = self.first_name + ' ' + self.middle_name
            full_name += ' ' + self.last_name
        else:
            full_name = self.first_name + ' ' +  self.last_name

        print(full_name)

    def greet_user(self):
        print('HELLO! ' + self.first_name.title())

    def increment_login_attemps(self):
        self.login_attemps += 1

    def reset_login_attemps(self):
        self.login_attemps = 0

    def read_login_attemps(self):
        print(self.login_attemps)

the_one = User('wang','wei')
#调用多次
the_one.increment_login_attemps()
the_one.read_login_attemps()
the_one.increment_login_attemps()
the_one.read_login_attemps()
the_one.increment_login_attemps()
the_one.read_login_attemps()
the_one.increment_login_attemps()
the_one.read_login_attemps()
print('')
#重置
the_one.reset_login_attemps()
the_one.read_login_attemps()






