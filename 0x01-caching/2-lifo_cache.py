#!/usr/bin/python3
"""
LIFOCache
"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ basic cache system using LIFO algorithm """
    def __init__(self):
        """ initialize LIFO cache """
        super().__init__()

    def put(self, key, item):
        """ add an item in cache """
        if key or item is not None:
            value = self.get(key)
            if value is None:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    discarded_key = list(self.cache_data.keys())
                    last_key = len(discarded_key) - 1
                    del self.cache_data[discarded_key[last_key]]
                    print("DISCARD: {}".format(discarded_key[last_key]))
            else:
                del self.cache_data[key]

            self.cache_data[key] = item

    def get(self, key):
        """ get an item by key """
        value = self.cache_data.get(key)
        return value
