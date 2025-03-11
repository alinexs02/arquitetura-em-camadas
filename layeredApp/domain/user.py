class User:
    id:int
    login:str
    password:str

    def __init__(self, id = 0, login="",password=""):
        self.id = id
        self.login = login
        self.password = password