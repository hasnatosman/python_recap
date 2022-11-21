# class declaring........................................

class User:
    # class properties or attributes are..................
    name = ''
    email = ''
    password = ''
    login = False

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    # login method........................................
    def login(self):
        email = input('Enter an email : ')
        password = input('Input your password : ')

        if email == self.email and password == self.password:
            login = True
            print('Login Successful !')
        else:
            print('Login Failed !')

    def logout(self):
        login = False
        print('Logged Out !')

    def isloggedin(self):
        if self.login:
            return True
        else:
            return False

    def profile(self):
        if self.isloggedin():
            print(self.name, '-', self.email)
        else:
            print('User not logged in !')


user1 = User('Hasnat', 'has@gmail.com', '12345')
user2 = User('Osman', 'os@gmail.com', '6789')

user1.login()
user1.profile()
