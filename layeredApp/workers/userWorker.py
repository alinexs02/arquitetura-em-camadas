from domain.user import User
from repositories.userRepository import UserRepository

class UserWorker:
    repository:UserRepository

    def __init__(self):
        self.repository = UserRepository()
    
    def add(self, user:User):
        #escondendo a senha com uma função de hash para melhorar a segurança
        user.password = str(hash(user.password))
        self.repository.add(user)
    
    def getAll(self)->list[User]:
        return self.repository.getAll()