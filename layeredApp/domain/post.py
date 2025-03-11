class post:
    id: int
    message: str
    user_id: int
    
    def init(self, id=0, message="", user_id=0):
        self.id = id
        self.message = message
        self.user_id = user_id