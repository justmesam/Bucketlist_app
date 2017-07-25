""" main module for the bucketlist """
import uuid
import datetime
from app.models.data import Data
from app.models.item import Item

class Bucketlist(object):
    """main class of the bucketlist"""

    def __init__(self, title, owner, intro, owner_id, _id=None):
        self.title = title
        self.intro = intro
        self.owner = owner
        self.owner_id = owner_id
        self._id = uuid.uuid4().hex if _id is None else _id


    def new_item(self, item_name, description, date=datetime.datetime.utcnow()):
        """method used for creating a  bucket list"""
        item = Item(item_name=item_name,
                    description=description,
                    owner_id=self._id,
                    date=date)
        item.save_to_items()

    def bucketlist_data(self):
        """this method returns bucketlist data to be saved"""
        return {
            'title' : self.title,
            'intro': self.intro,
            '_id' : self._id,
            'owner' : self.owner,
            'owner_id' : self.owner_id
        }

    def save_to_bucketlists(self):
        """this methods saves data to the bucketlists list"""
        Data.add_data(self.bucketlist_data())
