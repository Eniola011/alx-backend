#!/usr/bin/python3
"""
    FIFOCache Module
"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Basic cache system using FIFO algorithm.
      - Inherits from BaseCaching and is a caching system.

      - Put function:
        >> Must assign to the dictionary self.cache_data the 'item'
           value for the key 'key'.
        >> If 'key' or 'item' is None, this method should not do anything.
        >> If the number of items in self.cache_data is higher that
           BaseCaching.MAX_ITEMS:
           > you must discard the first item put in cache (FIFO algorithm)
           > you must print DISCARD: with the key discarded and
             following by a new line.

      - Get function:
        >> Must return the value in self.cache_data linked to key.
        >> If 'key' is None or if the 'key' doesn’t exist in self.cache_data,
           return 'None'.
    """

    def __init__(self):
        """
            initialize FIFO cache
        """
        super().__init__()

    def put(self, key, item):
        """
            Add an item in cache.
            Args:
                key: of the dict.
                item: value of the key.

        """
        if key and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find and remove the first item in cache_data (FIFO)
                discarded_key = next(iter(self.cache_data))
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))
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
