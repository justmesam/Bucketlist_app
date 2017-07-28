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
        return self.app.post('/login/',
                             data=dict(email=email,
                                       password=password),
                             follow_redirects=True)
    def register(self, username, email, password, confirm):
        """register helper """
        return self.app.post('/register/',
                             data=dict(username=username,
                                       email=email,
                                       password=password,
                                       confirm=confirm),
                             follow_redirects=True)
    def logout(self):
        """logout helper   """
        return self.app.get('/logout/',
                            follow_redirects=True)

    def test_register(self):
        result = self.register('johny', 'johndoe@gmail.com', '54321', '54321')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'You have been registered!  johny ', result.data)

    def test_an_existing_user(self):
        result = self.register('jane', 'janedoe@gmail.com', '54321', '54321')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'You have been registered!  jane ', result.data)
        result0 = self.register('jane', 'janedoe@gmail.com', '54321', '54321')
        self.assertEqual(result0.status_code, 200)
        self.assertIn(b'Email exists!!! You can login instead!', result0.data)

    def test_login_success(self):
        result = self.register('sam','sam@email.com', '12345','12345')
        self.assertIn(b'You have been registered!  sam ', result.data)
        result0 = self.logout()
        self.assertTrue(b'You have successfully logged out' in result0.data)
        result1 = self.login('sam@email.com', '12345')
        self.assertEqual(result1.status_code, 200)
        self.assertIn(b'You have successfully logged in!!', result1.data)


    def test_login_invalid(self):
         result = self.login('sam@email.com', '12345')
         self.assertEqual(result.status_code, 200)
         self.assertIn(b"Email do not exist!!  first register", result.data)

    def test_logout(self):
        result0 = self.register('sam', 'sam@gmail.com', '54321', '54321')
        self.assertEqual(result0.status_code, 200)
        self.assertIn(b'You have been registered!  sam ', result0.data)
        result = self.logout()
        self.assertTrue(b'You have successfully logged out' in result.data)

    def test_user_access_and_authentication(self):
        with self.app:
            result = self.app.post('/create_bucketlist/',
                                   data=dict(title='going to ibiza',
                                             body='attending MCR concert'),
                                   follow_redirects=True)

            self.assertIn(b'No Access, Please login first', result.data)

    def test_create_bucketlist(self):
        result0 = self.register('rock', 'rock@gmail.com', '54321', '54321')
        self.assertEqual(result0.status_code, 200)
        self.assertIn(b'You have been registered!  rock ', result0.data)
        with self.app:
            result = self.app.post('/create_bucketlist/',
                                   data=dict(title='going to ibiza',
                                             body='attending MCR concert'),
                                   follow_redirects=True)
            self.assertIn(b' You have created a bucketlist', result.data)

if __name__ == '__main__':
    unittest.main()
