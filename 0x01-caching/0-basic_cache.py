#!/usr/bin/python3
"""
    BasicCache Module
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Basic cache system without limit.
      - Inherits from BaseCaching and is a caching system.

      - Put function:
        >> Must assign to the dictionary self.cache_data the 'item'
           value for the key 'key'.
        >> If 'key' or 'item' is None, this method should not do anything.

      - Get function:
        >> Must return the value in self.cache_data linked to key.
        >> If 'key' is None or if the 'key' doesn’t exist in self.cache_data,
           return 'None'.
    """

    def put(self, key, item):
        """
            Add an item in cache.
            Args:
                key: of the dict.
                item: value of the key.

        """
        if key and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
            Get an item by key.
            Args:
                key: of the dict.
            Return:
                value of the key.

        """
        if key is not None and key in self.cache_data:
            return self.cache_data.get(key)
        return None
