""" The data module where all none persistent data is stored """

class Data(object):
    """ main data class """
    users = []
    bucketlists = []
    items = []

    @staticmethod
    def add_data(arg):
        """method for appending items to their respective lists"""
        if 'email' in arg:
            Data.users.append(arg)
        elif 'title' in arg:
            Data.bucketlists.append(arg)
        elif 'item_name' in arg:
            Data.items.append(arg)

    @staticmethod
    def get_the_dictionary(_id, arg):
        """this method uses id attribute to get the dictionary"""
        data_ = [i for i in arg if _id == i['_id']\
         or _id == i['owner_id'] or _id == i['bucketlist_id']]
        if len(data_) == 1:
            data_ = data_[0]
            return data_
        elif len(data_) > 1:
            return data_
        else:
            return "id don't exist"

    @staticmethod
    def get_index(_id, arg):
        """gets the index of a dictionary in a list"""
        index_data = [i for i in arg if _id == i['_id']]
        _index = arg.index(index_data[0])
        return _index

    @staticmethod
    def delete_dictionary(_id, arg):
        """ deletes the dictionary in a list"""
        index_ = Data.get_index(_id, arg)
        del arg[index_]
