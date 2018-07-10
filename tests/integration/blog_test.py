from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_create_posts(self):
        b = Blog('Test Title', 'Test Author')
        b.create_post('Test Post Title', 'Test Post Content')
        expected = 'Title: Test Title by Author: Test Author (1 post)'

        self.assertEqual(expected,b.__repr__())
        self.assertEqual(b.posts[0].title, 'Test Post Title')
        self.assertEqual(b.posts[0].content, 'Test Post Content')

    def test_json_no_posts(self):
        b = Blog('Test Title', 'Test Author')
        expected = {
            'title': 'Test Title',
            'author': 'Test Author',
            'posts': []}

        self.assertDictEqual(expected,b.json())

    def test_json(self):
        b = Blog('Test Title', 'Test Author')
        b.create_post('Test Post Title', 'Test Post Content')

        expected = {
                'title': 'Test Title',
                'author': 'Test Author',
                'posts': [{
                    'title': 'Test Post Title',
                    'content': 'Test Post Content'
                }]
        }

        self.assertDictEqual(expected, b.json())


