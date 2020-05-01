class User():
    def __init__(self, first_name, last_name, age, phone_no):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone_no = phone_no
        self.login_attempts = 0

    def describe_user(self):
        print("My name is " + self.first_name + " " + self.last_name)
        print("I am "+str(self.age) + " years old")
        print("My phone no is " + str(self.phone_no))

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def read_login_attempts(self):
        print('Login attempts='+str(self.login_attempts))


my_user = User('Monica', 'Maibram', 30, 9738417758)
my_user.describe_user()
my_user.increment_login_attempts()
my_user.read_login_attempts()
my_user.increment_login_attempts()
my_user.read_login_attempts()
my_user.reset_login_attempts()
my_user.read_login_attempts()
