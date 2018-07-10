from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test','Test Author')

        self.assertEqual('Test',b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([],b.posts)

    def test_repr_no_posts(self):
        b = Blog('Test Title', 'Test Author')
        #expected = 'Title: Test Title, Author: Test Author, Posts: []'
        expected = 'Title: Test Title by Author: Test Author (0 posts)'

        self.assertEqual(b.__repr__(),expected)

    def test_repr_one_post(self):
        b = Blog('Test Title', 'Test Author')
        b.posts = ['Test Post']
        expected = 'Title: Test Title by Author: Test Author (1 post)'

        self.assertEqual(b.__repr__(), expected)

    def test_repr_multi_posts(self):
        b = Blog('Test Title', 'Test Author')
        b.posts = ['Test Post 1', 'Test Post 2']
        #expected = 'Title: Test Title, Author: Test Author, Posts: [\'Test Post\']'
        expected = 'Title: Test Title by Author: Test Author (2 posts)'

        self.assertEqual(b.__repr__(), expected)

    def test_json(self):
        b = Blog('Test Title','Test Author')
        expected = {'title':'Test Title','author':'Test Author', 'posts':[]}

        self.assertDictEqual(b.json(),expected)


