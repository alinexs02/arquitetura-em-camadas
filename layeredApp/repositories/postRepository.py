from repositories.mysql import *
from domain.post import Post

class PostRepository:
    
    def add(self, post: Post):
        executeCommand(f"INSERT INTO Post (message, user_id) VALUES ('{post.message}', {post.user_id})")
    
    def getAll(self) -> list[Post]:
        result = executeQuery(f"SELECT * FROM Post")
        data = []
        for item in result:
            post = Post(item[0], item[1], item[2])
            data.append(post)
        return data