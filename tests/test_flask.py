""" flask testing module """

from unittest import TestCase
from app import app

class TestClass(TestCase):
    """Main testing class for the flask app"""
    def setUp(self):
        """ method runs before each test"""
        app.config['TESTING'] = True
        self.app = app.test_client()

#### ===>>  HELPER METHODS <=== ####

    def login(self, email, password):
        """ login helper """
        return self.app.post('/login',
                             data=dict(email=email,
                                       password=password),
                             follow_redirects=True)
    def register(self, name, username, email, password):
        """register helper """
        return self.app.post('/register',
                             data=dict(name=name,
                                       email=email,
                                       username=username,
                                       password=password),
                             follow_redirects=True)
    def logout(self):
        """logout helper   """
        return self.app.get('/logout',
                            follow_redirects=True)


    def test_login_success(self):
        result = self.login('admin@admin.local', 'default')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'login', result.data)

    def test_login_invalid(self):
         result = self.login('admin', 'defaultx')
         self.assertEqual(result.status_code, 200)
         self.assertIn(b'login', result.data)

    def test_register(self):
        result = self.register('john', 'johny', 'johndoe@gmail', '54321')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'register', result.data)


    def test_logout(self):
        result = self.logout()
        self.assertTrue(b'login' in result.data)

if __name__ == '__main__':
    unittest.main()
