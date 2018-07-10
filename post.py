class Post:
    def __init__(self,title,content):
        self.title = title
        self.content = content

    def __repr__(self):
        return 'Title: {self.title}, Content: {self.content}'.format(self=self)

    def json(self):
        return {
            'title': self.title,
            'content': self.content,
        }
