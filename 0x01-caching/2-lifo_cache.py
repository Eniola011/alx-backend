#!/usr/bin/python3
"""
    LIFOCache Module
"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Basic cache system using LIFO algorithm.
      - Inherits from BaseCaching and is a caching system.

      - Put function:
        >> Must assign to the dictionary self.cache_data the 'item'
           value for the key 'key'.
        >> If 'key' or 'item' is None, this method should not do anything.
        >> If the number of items in self.cache_data is higher that
           BaseCaching.MAX_ITEMS:
           > you must discard the last item put in cache (LIFO algorithm)
           > you must print DISCARD: with the key discarded and
             following by a new line.

      - Get function:
        >> Must return the value in self.cache_data linked to key.
        >> If 'key' is None or if the 'key' doesn’t exist in self.cache_data,
           return 'None'.
    """

    def __init__(self):
        """
            initialize LIFO cache
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
            value = self.get(key)
            if value is None:
                # If cache is full, discard the last item
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    # Find and remove the last item in cache_data (LIFO)
                    last_key = next(reversed(self.cache_data))
                    del self.cache_data[last_key]
                    print("DISCARD: {}".format(last_key))
            else:
                del self.cache_data[key]

        # Add the new item
        self.cache_data[key] = item

    def get(self, key):
        """
            Get an item by key.
            Args:
                key: of the dict.
            Return:
                value of the key.

        """
        if key in self.cache_data:
            return self.cache_data.get(key)
        return None
