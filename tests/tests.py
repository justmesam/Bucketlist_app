""" module for unit testing my  classes"""
import unittest
import datetime
from app.models.data import Data
from app.models.user import User
from app.models.bucketlist import Bucketlist
class Testclass(unittest.TestCase):
    """ main test class"""
    def setUp(self):
        self.user1 = {'username': 'sammy',
                      '_id': '528drrdd9540dab149eceedb14',
                      'password': '12345',
                      'name': 'samuel',
                      'email': 'samysam@email'}
        self.bucketlist1 = {'title' : 'bucketlist one',
                            'intro' : ' The first bucketlist',
                            '_id' : 'sdf528drr0dab149eceedb14',
                            'owner' : 'sammy',
                            'owner_id' : '528drrdd9540dab149eceedb14'}
        self.item1 = {'bucketlist_id' : 'sdf528drr0dab149eceedb14',
                      '_id' : '098un528drr0dab149eceedb14',
                      'item_name' : 'dancing in town',
                      'description' : 'its crazy to dance in town ',
                      'owner_id' : '528drrdd9540dab149eceedb14',
                      'date' : '12 - 07 - 2017'}
        self.data = Data
        del self.data.users[:]
        del self.data.items[:]
        del self.data.bucketlists[:]

## bucketlist test ##
    def test_new_item(self):
        bucket1 = Bucketlist('bucket 1', 'sammy',
                             'test intro', '528drrdd9540dab149eceedb14', _id=None)
        bucket1.new_item('dancing in town', 'the description', date=datetime.datetime.utcnow())
        result = self.data.get_the_data('528drrdd9540dab149eceedb14', self.data.items)
        self.assertIsInstance(result, list)

## user tests ##
    def test_user_exists(self):
        self.data.add_data(self.user1)
        result = User.user_exists('samysam@email')
        self.assertTrue(result)
        result1 = User.user_exists('johndoe@email')
        self.assertFalse(result1)

    def test_register(self):
        self.data.add_data(self.user1)
        result = User.register('johndoe', 'johndoe@email', '12345')
        self.assertTrue(result)
        result1 = User.register('sammy', 'samysam@email', '12345')
        self.assertFalse(result1)

    def test_user_login_verify(self):
        result1 = User.user_login_verify('johndoe@email', '1234567')
        self.assertFalse(result1)

    def test_get_username(self):
        User.register('johny', 'johndoe@email', '54321')
        result = User.get_username('johndoe@email')
        self.assertEqual(result, 'johny')

    def test_current_user(self):
        User.register('john', 'johndoe@email', '54321')
        result = User.current_user('johndoe@email')
        self.assertIsInstance(result, dict)
        self.assertEqual(result['username'], 'john')

if __name__ == '__main__':
    unittest.main()
