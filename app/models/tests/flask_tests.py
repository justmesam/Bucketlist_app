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
        self.assertEqual(result.status_code, 200)

if __name__ == '__main__':
    unittest.main()
