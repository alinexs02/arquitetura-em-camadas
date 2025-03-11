from repositories.mysql import *
from domain.user import User

class UserRepository:
    
    def add(self, user:User):
        executeCommand(f"INSERT INTO Usuario ('login','password') VALUES('{user.login}','{user.password}')")
    
    def getAll(self)->list[User]:
        result = executeQuery(f"SELECT * FROM Usuario")
        data =[]
        for item in result:
            user = User(item[0],item[1],item[2])
            data.append(user)
        return data
