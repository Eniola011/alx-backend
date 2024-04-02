#!/usr/bin/python3
"""
BasicCache
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ basic cache system without limit"""
    def put(self, key, item):
        """ add an item in cache """
        if key or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ get an item by key """
        value = self.cache_data.get(key)
        return value
