""" flask testing module """

from unittest import TestCase
from app import app

class TestClass(TestCase):
    """Main testing class for the flask app"""
    def setUp(self):
        """ method runs before each test"""
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_index_page(self):
        result = self.app.get('/', follow_redirects=True)
        result1 = self.app.get('/index', follow_redirects=True)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result1.status_code, 200)


    def test_about_page(self):
        result = self.app.get('/about', follow_redirects=True)
        self.assertEqual(result.status_code, 200)

    def test_FAQ_page(self):
        result = self.app.get('/faqs', follow_redirects=True)
        self.assertEqual(result.status_code, 200)

if __name__ == '__main__':
    unittest.main()
