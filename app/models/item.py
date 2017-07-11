""" The bucketlist item module"""
import uuid
from app.models.data import Data

class Item(object):
    """ Main item class"""
    def __init__(self, bucketlist_id, item_name, owner, owner_id, date, _id=None):
        self.bucketlist_id = bucketlist_id
        self.item_name = item_name
        self.owner = owner
        self.owner_id = owner_id
        self.date = date
        self._id = uuid.uuid4().hex


    def item_data(self):
        """returns the data to be saved to items list"""
        return {
            'bucketlist_id' : self.bucketlist_id,
            '_id' : self._id,
            'item_name' : self.item_name,
            'owner' : self.owner,
            'owner_id' : self.owner_id,
            'date' : self.date
        }

    def save_to_items(self):
        """this method saves data to the item list"""
        Data.add_data(self.item_data())
