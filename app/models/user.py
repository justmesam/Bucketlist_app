""" the user module """
import uuid
from werkzeug.security import check_password_hash
from app.models.data import Data
from app.models.bucketlist import Bucketlist

class User(object):
    """main user class"""

    def __init__(self, username, email, password, _id=None):
        self.username = username
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    @staticmethod
    def user_exists(email):
        """method checks if the user already exist"""
        data = [i['email'] for i in Data.users if email == i['email']]
        return "".join(data) == email

    @staticmethod
    def user_login_verify(email, password):
        """ methods verifys user password and email"""
        user_exist = User.user_exists(email)
        if user_exist is True:
            emails_password = "".join([i['password']\
             for i in Data.users if email == i['email']])
            return check_password_hash(emails_password, password)
        return False

    @staticmethod
    def get_username(email):
        """Gets users username for use in session at login"""
        username = [i['username'] for i in Data.users if email == i['email']]
        return "".join(username)

    @classmethod
    def register(cls, username, email, password):
        """method registers a user to the app"""
        user = cls.user_exists(email)
        if user is False:
            new_user = cls(username, email, password)
            new_user.save_to_users()
            return True
        else:
            return False

    def user_data(self):
        """ The method returns user data to be saved"""
        return {
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
    def create_item(_id, item_name, description):
        """method used to create bucketlist items"""
        data_ = Data.get_the_data(_id, Data.bucketlists)
        for data in data_:
            bucketlist = Bucketlist(data['title'],
                                    data['owner'],
                                    data['intro'],
                                    data['owner_id'],
                                    data['_id'])
            bucketlist.new_item(item_name=item_name,
                                description=description)

    def save_to_users(self):
        """this method saves the user to users"""
        Data.add_data(self.user_data())

    @staticmethod
    def current_user(email):
        """
        method gets user details using the session username to create the instance
         of the user logged so as to create a bucketlist"""
        for user in Data.users:
            if email == user['email']:
                return user
