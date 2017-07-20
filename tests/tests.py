""" module for unit testing my  classes"""
import unittest
import datetime
from werkzeug.security import generate_password_hash
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

## Data tests ##
    def test_user_initializes_with_0(self):
        initial_list = len(self.data.users)
        self.data.users.append(self.user1)
        list_after_append = len(self.data.users)
        self.assertEqual(list_after_append, initial_list + 1)

    def test_items_initializes_with_0(self):
        initial_list = len(self.data.items)
        self.data.items.append(self.item1)
        list_after_append = len(self.data.items)
        self.assertEqual(list_after_append, initial_list + 1)

    def test_bucketlists_initializes_with_0(self):
        initial_list = len(self.data.bucketlists)
        self.data.bucketlists.append(self.bucketlist1)
        list_after_append = len(self.data.bucketlists)
        self.assertEqual(list_after_append, initial_list + 1)

    def test_add_data(self):
        self.data.add_data(self.user1)
        self.assertEqual(len(self.data.users), 1)
        self.data.add_data(self.bucketlist1)
        self.assertEqual(len(self.data.bucketlists), 1)
        self.data.add_data(self.item1)
        self.assertEqual(len(self.data.items), 1)

    def test_get_the_dictionary(self):
        self.data.add_data(self.user1)
        self.data.add_data(self.bucketlist1)
        self.data.add_data(self.item1)
        result = self.data.get_the_dictionary('528drrdd9540dab149eceedb14', self.data.users)
        self.assertEqual(result, self.user1)
        result1 = self.data.get_the_dictionary('sdf528drr0dab149eceedb14', self.data.bucketlists)
        self.assertEqual(result1, self.bucketlist1)
        result2 = self.data.get_the_dictionary('098un528drr0dab149eceedb14', self.data.items)
        self.assertEqual(result2, self.item1)
        self.data.add_data(self.bucketlist1)
        result3 = self.data.get_the_dictionary('528drrdd9540dab149eceedb14', self.data.bucketlists)
        self.assertEqual(len(result3), 2)
        self.data.add_data(self.item1)
        result4 = self.data.get_the_dictionary('sdf528drr0dab149eceedb14', self.data.items)
        self.assertEqual(len(result4), 2)
        result5 = self.data.get_the_dictionary('12345', self.data.items)
        self.assertEqual(result5, "id don't exist")

    def test_get_index(self):
        bucketlist2 = {'title' : 'bucketlist one',
                       'intro' : ' The first bucketlist',
                       '_id' : '54321',
                       'owner' : 'sammy',
                       'owner_id' : '528drrdd9540dab149eceedb14'}
        self.data.add_data(self.bucketlist1)
        self.data.add_data(bucketlist2)
        index_ = self.data.get_index('54321', self.data.bucketlists)
        self.assertEqual(index_, 1)

    def test_delete_dictionary(self):
        initial = len(self.data.bucketlists)
        self.data.add_data(self.bucketlist1)
        result = len(self.data.bucketlists)
        self.data.delete_dictionary('sdf528drr0dab149eceedb14', self.data.bucketlists)
        result1 = len(self.data.bucketlists)
        self.assertEqual(result1, initial)
        self.assertEqual(result1, result - 1)

## bucketlist test ##
    def test_new_item(self):
        bucket1 = Bucketlist('bucket 1', 'sammy',
                             'test intro', '528drrdd9540dab149eceedb14', _id=None)
        bucket1.new_item('dancing in town', 'the description', date=datetime.datetime.utcnow())
        result = self.data.get_the_dictionary('528drrdd9540dab149eceedb14', self.data.items)
        self.assertIsInstance(result, dict)

## user tests ##
    def test_user_exists(self):
        self.data.add_data(self.user1)
        result = User.user_exists('samysam@email')
        self.assertTrue(result)
        result1 = User.user_exists('johndoe@email')
        self.assertFalse(result1)

    def test_register(self):
        self.data.add_data(self.user1)
        result = User.register('john', 'johndoe', 'johndoe@email', '12345')
        self.assertTrue(result)
        result1 = User.register('samuel', 'sammy', 'samysam@email', '12345')
        self.assertFalse(result1)

    def test_create_bucketlist(self):
        user = User('john', 'johny', 'johnjohny', '54321', _id=None)
        user.create_bucketlist('bucketlist challenge', 'bucketlist creation is fun')
        result = len(self.data.bucketlists)
        self.assertEqual(result, 1)

    def test_create_item(self):
        self.data.add_data(self.bucketlist1)
        user = User('john', 'johny', 'johnjohny', '54321', _id=None)
        user.create_item('sdf528drr0dab149eceedb14', 'another description', 'bungee jumping')
        result = len(self.data.items)
        self.assertEqual(result, 1)

    def test_user_login_verify(self):
        self.data.add_data(self.user1)
        pass1 = generate_password_hash('12345')
        pass2 = generate_password_hash('1234567')
        result = User.user_login_verify('samysam@email', pass1)
        result1 = User.user_login_verify('johndoe@email', pass2)
        self.assertTrue(result)
        self.assertFalse(result1)

    def test_get_username(self):
        User.register('john', 'johny', 'johndoe@email', '54321')
        result = User.get_username('johndoe@email')
        self.assertEqual(result, 'johny')

    def test_current_user(self):
        User.register('john', 'johny', 'johndoe@email', '54321')
        result = User.current_user('johny')
        self.assertIsInstance(result, tuple)
        self.assertEqual(result[0], 'john')

if __name__ == '__main__':
    unittest.main()
