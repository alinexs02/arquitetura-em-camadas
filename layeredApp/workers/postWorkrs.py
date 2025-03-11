from domain.post import Post
from repositories.postRepository import PostRepository

class PostWorker:
    repository: PostRepository

    def init(self):
        self.repository = PostRepository()
    
    def add(self, post: Post):
        self.repository.add(post)
    
    def getAll(self) -> list[Post]:
        return self.repository.getAll()