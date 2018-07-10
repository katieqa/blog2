from unittest import TestCase
from post import Post

class PostTest(TestCase):
    def test_create_post(self):
        p = Post('Test','Test Content')

        self.assertEqual('Test', p.title)
        self.assertEqual('Test Content', p.content)

    def test_json(self):
        p = Post('Test','Test Content')
        expected = {'title': 'Test', 'content':'Test Content'}

        self.assertDictEqual(p.json(),expected)

    def test_repr(self):
        p = Post('Test', 'Test Content')
        expected = 'Title: Test, Content: Test Content'

        self.assertEqual(p.__repr__(),expected)