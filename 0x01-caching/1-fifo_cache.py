#!/usr/bin/python3
"""
BasicCache
"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ basic cache system using FIFO algorithm """
    def __init__(self):
        """ initialize FIFO cache """
        super().__init__()

    def put(self, key, item):
        """ add an item in cache """
        if key or item is not None:
            value = self.get(key)
            if value is None:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    discarded_key = list(self.cache_data.keys())[0]
                    del self.cache_data[discarded_key]
                    print("DISCARD: {}".format(discarded_key))

            self.cache_data[key] = item

    def get(self, key):
        """ get an item by key """
        value = self.cache_data.get(key)
        return value
