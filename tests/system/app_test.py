from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog


class AppTest(TestCase):

    def test_menu_prompt(self):
        with patch('builtins.input') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_print_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called()

    def test_print_blogs(self):
        b = Blog('Test Blog', 'Test Author')
        app.blogs = {'Test': b}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Title: Test Blog by Author: Test Author (0 posts)')

    def test_ask_create_blogs(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect('Test', 'Test Author') #returns the first attribute the first call, second attribute second time it's called etc
            app.ask_create_blog()
            self.assertIsNotNone(app.blogs.get('Test'))

