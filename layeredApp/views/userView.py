from domain.user import User
from workers.userWorker import UserWorker

class UserView:
    userWorker : UserWorker
    def __init__(self):
        self.userWorker = UserWorker()

    def createUser(self):
        print("creating user")
        login = input("insert user login: ")
        password = input("insert user password: ")
        repeatPassword = input("repeat the password: ")
        # user = User()
        # user.login = login
        # user.password = password

        if password == repeatPassword:
            user = User(login=login, password=password)
            self.userWorker.add(user)
        else:
            print("Error, passwords didn't match")

    def listUsers(self):
        users = self.userWorker.getAll()
        print("listing Users")
        for user in users:
            # print(f"{user.id} {user.login} {"*"*len(user.password)}")
            print(f"{user.id} {user.login} {user.password}")