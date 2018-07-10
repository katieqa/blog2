from post import Post

class Blog:
    def __init__(self, title, author):
        self.posts = []
        self.title = title
        self.author = author

    def __repr__(self):
    #    return 'Title: {}, Author: {}, Posts: {}'.format(self.title, self.author, self.posts)
        return 'Title: {} by Author: {} ({} post{})'.format(self.title,
                                                            self.author,
                                                            len(self.posts),
                                                            's' if len(self.posts) != 1 else '')
    def create_post(self,title,content):
        p = Post(title,content)
        self.posts.append(p)
        return self.posts

    def json(self):
        return {
            'title': self.title,
            'author': self.author,
            'posts': self.posts,
        }