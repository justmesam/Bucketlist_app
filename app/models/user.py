""" the user module """
import uuid
from app.models.data import Data
from app.models.bucketlist import Bucketlist

class User(object):
    """main user class"""

    def __init__(self, name, username, email, password, _id=None):
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex

    @staticmethod
    def user_exists(email):
        """method checks if the user already exist"""
        data = [i['email'] for i in Data.users if email == i['email']]
        return "".join(data) == email

    @classmethod
    def register(cls, name, username, email, password):
        """method registers a user to the app"""
        user = cls.user_exists(email)
        if user is False:
            new_user = cls(name, username, email, password)
            new_user.save_to_users()
            return True
        else:
            return False

    def user_data(self):
        """ The method returns user data to be saved"""
        return {
            'name': self.name,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            '_id' : self._id
        }

    def create_bucketlist(self, title, intro):
        """method used for creating a bucketlist"""
        bucketlist_ = Bucketlist(owner_id=self._id,
                                 title=title,
                                 intro=intro,
                                 owner=self.username)
        bucketlist_.save_to_bucketlists()

    @staticmethod
    def create_item(bucketlist_id, item_name):
        """method used to create bucketlist items"""
        _id = bucketlist_id
        data = Data.get_the_dictionary(_id, Data.bucketlists)
        bucketlist = Bucketlist(data['title'], data['owner'], data['intro'], data['owner_id'])
        bucketlist.new_item(item_name=item_name)

    def save_to_users(self):
        """this method saves the user to users"""
        Data.add_data(self.user_data())
